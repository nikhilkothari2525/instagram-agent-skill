---
name: ig-reel
description: >-
  Write an Instagram Reel from a raw idea - hook options off 26 formulas, the
  spoken script, the on-screen text, and a timed beat sheet - in the user's own
  voice and scored before they shoot it. Use whenever the user wants a Reel, a
  short-form video script, a hook, a voiceover, "make a reel about X", "what
  should I say in this video", or is about to record and does not have the
  first line yet.
---

# ig-reel

Turns one raw idea into a Reel that somebody finishes.

Two tools live in this folder and they both actually run. Use them. Do not
eyeball the hook and do not guess at the length.

```bash
python3 hookscore.py hooks.txt              # rank your hook options
python3 hookscore.py --hook "one line"      # score a single one
python3 beats.py script.txt --target 30     # timed beat sheet before you shoot
```

## MYERAPAIRS

This pack is set up for MYERAPAIRS, a women's footwear shop in Mandsaur
(@myerapairsofficial). Before anything else, read these three files from the
`myerapairs/` folder at the root of this skill pack, two folders up from this
skill's base directory:

- `../../myerapairs/rules.md`
- `../../myerapairs/voice.md`
- `../../myerapairs/product-facts.md`

If any of them is missing, stop and ask for it. Do not guess the rules, the
voice or a product fact. The repo copy of `voice.md` wins over
`~/.claude/instagram/voice.md`.

Rules for this skill:

- **Hinglish or English, as `voice.md` says.** Hinglish is written in Roman
  script. Write the line the way the person on camera actually talks.
- **Real product footage only.** Shoot the actual pair: in hand, on the shelf,
  on foot. Never generated looks, generated models, AI try-ons or stock clips.
  Keep the real design, colours and details. Who appears on camera is the
  owner's call in `voice.md`. Audio is the shop's own or properly licensed,
  never a competitor's media or music.
- **Facts only from the facts block.** Price, sizes, colours and material come
  from the ERP facts block for that design code. A missing fact is written
  `{{ERP: field}}` and the script is labelled NOT ERP-VERIFIED. No comfort,
  durability or medical claims, no scarcity or urgency, no delivery promises, no
  festival names, offer wording or superlatives. So skip #19 The Deadline and
  #26 The Superlative, and use #23 The Statistic or #25 Someone Else's Result
  only when the claim is real and the owner has approved it.
- **End with the DM-the-code ask.** Spoken and on the last card:
  "DM the code {{ERP: design code}}", or in Hinglish "Design code DM karo" with
  the code on screen. Write the code exactly as the ERP has it, so the enquiry
  can be matched. This is the one ask.
- **The scoring tools are tuned on English.** `hookscore.py` and `beats.py`
  use English word lists and count money in dollars. On a Hinglish line, treat
  the score as rough: use it to compare length and timing, and judge the hook
  by reading it out loud. Do not turn a natural Hinglish line into English just
  to raise the score.
- **Do not create or overwrite `voice.md`.** Step 1 below reads the repo copy
  and proposes edits to it.
- **Drafts only.** Add `facts:` (verified, or NOT ERP-VERIFIED) and
  `sign-off: needed` lines to the REEL READY block. A person shoots and posts
  the Reel by hand after the owner signs off.
- **"yes" in step 7 only saves the draft.** It is not sign-off. Log it in
  `log.md` as `DRAFT, not posted, not signed off`, with the date, the design
  code, the hook formula and the first line, never in the post-receipt format.
  Only a MANUAL POST RECEIPT (`rules.md`, section 2) records a post, and its
  `hook formula:` line is what `/ig-audit` groups posts by.

Where this section conflicts with the upstream text below, this section wins.

## Before you write

1. Read `../../myerapairs/voice.md`. If it still has placeholders, ask the
   owner for **three past captions** he likes and propose edits to that file.
   Do not create or overwrite a `voice.md`. A script in the wrong voice is
   unusable, because someone has to say it out loud.
2. Read `hooks.json` in this folder. 26 formulas, each with a template, a filled
   example, the on-screen version, what it is for, and how it gets ruined.
   Four of them are in there because they kept turning up in real hooks, not
   because they completed a pattern.
3. If the idea is thin, do not pad it. Ask one batched question: what happened,
   to whom, and what did it cost or return. A Reel needs one specific true
   thing. Get it before writing.
4. If `~/.claude/instagram/swipe.md` exists, read it. `/ig-viral` writes that
   file, and it is the user's own evidence about which formulas are working in
   their niche right now. It beats the upstream hook and format advice in this
   file. It never overrides the MYERAPAIRS rules or the DEFAULTs in
   `rules.md`.

## The shape

A Reel is decided in the first two seconds and kept by the next five.

```
0:00 - 0:02   HOOK        the claim. Spoken line and on-screen line, written
                          separately. Motion in the first frame, not a static face.
0:02 - 0:07   THE STAKE   why this matters to the person watching. One line.
0:07 - ...    THE BODY    one idea per beat, and the frame changes every beat.
LAST 3s       THE PAYOFF  deliver what the hook promised, then the single ask.
LAST LINE     THE LOOP    echo one word from the hook so the replay lands clean.
```

Length: 15 to 45 seconds is the working range. Reels run to 3 minutes and
almost nobody should use it. Under 7 seconds the loop counts inflate and
nothing else does.

## The loop

**1. Pick three hooks, not one.** Run the idea through `hooks.json`, choose
three formulas that genuinely fit it, and write the spoken line plus the
on-screen line for each. Different formulas, not three rewrites of one.

**2. Score them.** Put the three spoken lines in a file, one per line, and run
`hookscore.py`. Show the user the ranking. If the top one is under 50, you do
not have the hook yet and no amount of editing fixes that.

**3. Write the script** on the winning hook. Plain spoken language, the way the
user actually talks. Contractions. Short lines. No sentence they would have to
rehearse.

**4. Time it.** Run `beats.py script.txt --target {length}`. Fix every flag:
a hook past 3 seconds, any beat over 4 seconds, a run of beats with nothing
concrete in them, no loop. Re-run until it is clean.

**5. Humanize it.** Run the script through `/ig-human` before showing it. A
written-sounding line is obvious the moment someone says it out loud.

**6. Print the block.** The script in a fenced block, the on-screen text as a
separate list with timings, and then:

```
REEL READY
hook:       #3 Nobody Tells You, scored 86 STRONG
length:     28.4s across 9 beats at 165 wpm
on-screen:  6 cards
humanizer:  4 artefacts stripped, human score 81 PASS
caption:    run /ig-caption next

Reply "yes" to log it, or tell me what to change.
```

**7. Never publish.** This skill produces a script. The user shoots it and
posts it. On "yes", append to `~/.claude/instagram/log.md` with the date, the
hook formula used and the first line, so `/ig-audit` has a history later.

## On-screen text is a separate script

Write it separately, every time. It is read before it is heard.

- **Six words or fewer per card.** It is being read at arm's length by someone
  who is not listening yet.
- **The hook card is up at frame 1**, not after a beat of silence.
- **Keep it inside the safe zone.** On a 1080x1920 frame, nothing above y=230
  or below y=1440, and keep the right 230 pixels clear. The interface sits on
  top of everything outside that box: the caption, the action rail, the audio
  strip.
- **Never put the hook where the caption sits.** That is the bottom of the
  frame and it is covered.
- **Burn in captions for the body.** Most people watch muted first.

## Rules that make the difference

- **One idea per Reel.** If the script has two, you have two Reels. Say so.
- **Numbers over adjectives.** "₹1,499" beats "affordable", but only a number
  from the ERP facts block. If it is not there, write `{{ERP: field}}` rather
  than writing around the hole.
- **Cut the intro.** No greeting, no "in this video", no name, no logo sting.
  The video starts at the sentence you would normally reach at second six.
- **Change the frame every beat.** A static shot for 8 seconds is where people
  leave, and `beats.py` will flag it.
- **One ask at the end.** DM the code. One.
- **Never fabricate.** No invented prices, sizes, stock, materials, reviews,
  metrics or outcomes under the shop's name, even as a placeholder. If a fact is
  needed and unknown, leave `{{ERP: field}}` in the script and label it NOT
  ERP-VERIFIED.
- **Do not write a script around a trending audio the user cannot use.** If the
  idea needs the user's own voice, say so.

## Example

```
/ig-reel we cut proposal time from 5 hours to 20 minutes with one template
```

```
HOOKS  (scored)
  86  STRONG  #5  Time Collapse   "Proposals used to take me five hours. Twenty minutes now."
                                  on screen: 5 HOURS -> 20 MIN
  71  STRONG  #1  Cost Confession "I billed four hours a week for formatting. For two years."
                                  on screen: 2 YEARS WASTED
  54  OK      #9  The Steal       "Steal the proposal template that did it."
                                  on screen: STEAL THIS

Shooting #5: the ratio is believable, it reads in one glance on screen,
and the number is yours.
```
