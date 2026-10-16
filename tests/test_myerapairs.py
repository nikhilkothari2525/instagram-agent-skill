"""Checks that the skill scripts handle MYERAPAIRS captions.

MYERAPAIRS writes in English or in Hinglish (Hindi in Roman script). These
tests check that the scripts read Hinglish pronouns and calls to action, keep
prices, design codes and Hindi words intact, and still behave as upstream does
on English text.

Standard library only, no network. From the repo root:

    python3 -m unittest discover -s tests

The design code BH0001 and the price below are made-up test values, not real
product facts.
"""

import importlib.util
import json
import os
import re
import sys
import unittest

sys.dont_write_bytecode = True   # keep __pycache__ out of skills/

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKILLS = os.path.join(ROOT, "skills")


def load(name, *parts):
    """Import a skill script by its path, the way a skill would run it."""
    path = os.path.join(SKILLS, *parts)
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


detect = load("myerapairs_detect", "ig-human", "detect.py")
caption = load("myerapairs_caption", "ig-caption", "caption.py")
humanize = load("myerapairs_humanize", "ig-human", "humanize.py")

with open(os.path.join(SKILLS, "ig-human", "slop.json"), encoding="utf-8") as fh:
    LEX = json.load(fh)

# The pronoun pattern as upstream shipped it, before Hinglish was added.
UPSTREAM_PRONOUNS = re.compile(r"\b(i|me|my|mine|we|us|our|you|your)\b", re.IGNORECASE)

# A Hinglish product caption with no English pronoun in it, so every pronoun
# the VOICE check finds here is a Hindi one.
HINGLISH = (
    "Naya block heel aaya hai, design code BH0001.\n\n"
    "Main aapko bata doon, iska colour aur size humari shop ke system se "
    "confirm hota hai. Apna size check karke hi order karna.\n\n"
    "Bill price ₹1,499.\n\n"
    "Design code DM karo.\n\n"
    "#myerapairs #mandsaur"
)

# The caption from the README's caption.py example, rebuilt so the script
# prints the same result the README shows: 389 characters, a 133-character
# first line cut at "before I si", and one ask.
README_CAPTION = (
    "I lost $18,000 because of one missing clause in a contract, and the worst "
    "part is that I had read the thing twice before I signed it.\n\n"
    "The clause was about late payment. The client paid 94 days late, and I had "
    "nothing in writing that let me charge for it. So it changed my freelance "
    "pricing for good.\n\n"
    "Comment CLAUSE and I'll send you the exact wording.\n\n"
    "#freelance #contracts #agencyowner"
)

ENGLISH_PROSE = (
    "I lost a client last spring because I sent the proposal on a Friday night. "
    "The main reason was simple. You could not reach me until Monday, and by then "
    "they had signed with someone else. We changed one thing after that. "
    "Our proposals now go out before noon, and your reply gets an answer the "
    "same day. It is a mere habit, but it is mine."
)


class DetectPronouns(unittest.TestCase):

    def test_hinglish_caption_has_pronouns(self):
        self.assertEqual(len(UPSTREAM_PRONOUNS.findall(HINGLISH)), 0,
                         "the fixture should hold no English pronoun")
        found = [w.lower() for w in detect.PRONOUNS.findall(HINGLISH)]
        self.assertIn("main", found)
        self.assertIn("aapko", found)
        self.assertIn("humari", found)
        self.assertIn("apna", found)

    def test_hinglish_voice_detail_counts_pronouns(self):
        score, detail = detect.check_voice(HINGLISH, LEX)
        self.assertNotIn("too short", detail)
        rate = float(re.search(r"([\d.]+) personal pronouns", detail).group(1))
        self.assertGreater(rate, 0)

    def test_english_main_mere_hum_not_counted(self):
        for text in ("the main reason", "my main point", "a mere 5 minutes",
                     "the hum of the fan", "THE MAIN THING", "domain remain"):
            with self.subTest(text=text):
                found = {w.lower() for w in detect.PRONOUNS.findall(text)}
                self.assertFalse(found & {"main", "mere", "hum"}, found)

    def test_hindi_main_mere_hum_counted(self):
        cases = {
            "Main roz shop aati hoon": 1,
            "jab main aayi": 1,
            "mere liye": 1,
            "hum bhi wahi kehte hain": 1,
            "Humne dekha, aapne dekha?": 2,
            "Mujhe batao, hume pata hai.": 2,
        }
        for text, count in cases.items():
            with self.subTest(text=text):
                self.assertEqual(len(detect.PRONOUNS.findall(text)), count)

    def test_english_count_matches_upstream(self):
        self.assertEqual(len(detect.PRONOUNS.findall(ENGLISH_PROSE)),
                         len(UPSTREAM_PRONOUNS.findall(ENGLISH_PROSE)))

    def test_english_voice_and_verdict_match_upstream(self):
        new = detect.run(ENGLISH_PROSE, LEX)
        saved = detect.PRONOUNS
        try:
            detect.PRONOUNS = UPSTREAM_PRONOUNS
            old = detect.run(ENGLISH_PROSE, LEX)
        finally:
            detect.PRONOUNS = saved
        self.assertEqual(new, old)


class CaptionAsks(unittest.TestCase):

    def check(self, result, name):
        return next(c for c in result["checks"] if c["check"] == name)

    def test_hinglish_caption_has_one_recognised_ask(self):
        result = caption.analyse(HINGLISH)
        self.assertEqual(result["asks"], ["DM the code"])
        self.assertEqual(self.check(result, "ONE ASK")["status"], "PASS")

    def test_new_calls_to_action(self):
        cases = {
            "DM the code BH0001 for sizes.": "DM the code",
            "DM code BH0001.": "DM the code",
            "Design code DM karo.": "DM the code",
            "Style code message karein.": "DM the code",
            "DM the design code BH0001.": "DM the code",
            "DM us the code BH0001 and we will send you the details.": "DM the code",
            "DM the style code.": "DM the code",
            "Design code BH0001 DM karo, hum aapko details bhej denge.": "DM the code",
            "Code BH0001 DM karo.": "DM the code",
            "Design code {{ERP: design code}} DM karo.": "DM the code",
            "Sizes ke liye DM karo.": "DM me",
            "DM karein, hum batayenge.": "DM me",
            "DM kijiye.": "DM me",
            "Ek baar DM kare.": "DM me",
            "Message karo.": "DM me",
            "Message karein.": "DM me",
            "Visit the shop this week.": "visit the shop",
            "Visit our Mandsaur shop.": "visit the shop",
            "Shop pe aao.": "visit the shop",
            "Shop par aaiye.": "visit the shop",
            "Shop pe aayein.": "visit the shop",
        }
        for text, name in cases.items():
            with self.subTest(text=text):
                self.assertEqual(caption.analyse(text)["asks"], [name])

    def test_dm_karo_and_dm_me_is_one_ask(self):
        for text in ("Design code DM karo. Koi sawaal ho toh DM me.",
                     "DM karo ya message me.",
                     "DM the code BH0001, or DM me for help."):
            with self.subTest(text=text):
                result = caption.analyse(text)
                self.assertEqual(len(result["asks"]), 1, result["asks"])
                self.assertEqual(self.check(result, "ONE ASK")["status"], "PASS")

    def test_different_asks_still_count_twice(self):
        result = caption.analyse("Design code DM karo ya humari shop pe aaiye.")
        self.assertEqual(result["asks"], ["DM the code", "visit the shop"])
        self.assertEqual(self.check(result, "ONE ASK")["status"], "WARN")

    def test_readme_english_example_unchanged(self):
        result = caption.analyse(README_CAPTION,
                                 keywords=["client contracts", "freelance pricing"])
        self.assertEqual(result["characters"], 389)
        self.assertTrue(result["visible"].endswith("before I si"))
        self.assertEqual(result["hashtags"], ["#freelance", "#contracts", "#agencyowner"])
        self.assertEqual(result["asks"], ["comment a keyword"])
        statuses = {c["check"]: c["status"] for c in result["checks"]}
        self.assertEqual(statuses, {
            "LENGTH": "PASS",
            "FIRST LINE": "WARN",
            "HOOK IS CONCRETE": "PASS",
            "HASHTAGS": "PASS",
            "TAG PLACEMENT": "PASS",
            "LINKS": "PASS",
            "ONE ASK": "PASS",
            "EMOJI": "PASS",
            "SEARCH TERMS": "WARN",
        })
        self.assertIn("Missing: client contracts", self.check(result, "SEARCH TERMS")["detail"])

    def test_english_dm_me_unchanged(self):
        result = caption.analyse("Want the template? DM me and I'll send it.")
        self.assertEqual(result["asks"], ["DM me"])

    def test_english_code_words_are_not_an_ask(self):
        for text in ("I kept getting the same error code message for a week. "
                     "Save this for the fix.",
                     "Shipping the code DM bot next week. Save this."):
            with self.subTest(text=text):
                result = caption.analyse(text)
                self.assertEqual(result["asks"], ["save this"])
                self.assertEqual(self.check(result, "ONE ASK")["status"], "PASS")


class Humanize(unittest.TestCase):

    def test_keeps_price_code_and_hinglish(self):
        draft = ("Naya pair aaya hai \u2014 design code BH0001, bill price ₹1,499.\n"
                 "Design code DM karo ya humari Mandsaur shop pe aaiye.\n")
        clean, report = humanize.humanize(draft, humanize.load_lexicon())
        self.assertNotIn("\u2014", clean)
        self.assertIn("aaya hai, design code BH0001", clean)
        self.assertIn("₹1,499", clean)
        for word in ("Naya", "pair", "aaya", "hai", "karo", "humari",
                     "Mandsaur", "shop", "pe", "aaiye"):
            with self.subTest(word=word):
                self.assertRegex(clean, r"\b" + word + r"\b")
        names = [h["name"] for h in report["typographic"]]
        self.assertTrue(any("EM DASH" in n for n in names), names)
        self.assertEqual(report["lexical"], [])


class OtherScriptsImport(unittest.TestCase):

    def test_hookscore_imports_and_runs(self):
        hookscore = load("myerapairs_hookscore", "ig-reel", "hookscore.py")
        results, overall, verdict, flags = hookscore.run("Ye block heel ₹1,499 ka hai.")
        self.assertIn(verdict, ("STRONG", "OK", "WEAK"))
        self.assertTrue(0 <= overall <= 100)

    def test_swipe_imports(self):
        swipe = load("myerapairs_swipe", "ig-viral", "swipe.py")
        self.assertTrue(callable(swipe.analyse))
        self.assertIsNotNone(swipe.score_hook, "swipe.py could not load hookscore.py")


if __name__ == "__main__":
    unittest.main()
