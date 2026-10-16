---
name: ig-audit
description: >-
  Post-mortem on what the user has already posted - which reels actually
  worked, why, and what to stop making. Use when the user pastes their
  Instagram insights or past posts and asks "what's working", "why did this
  flop", "read my analytics", "audit my content", or wants to know what to do
  more of.
---

# ig-audit

The only honest source of what works for an account is that account. Every
rule in every Instagram guide, including the ones in this pack, is a prior.
The user's own last 30 posts are the evidence.

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
`~/.claude/instagram/voice.md`. Never create or overwrite a `voice.md`; propose
edits to `../../myerapairs/voice.md` instead.

Rules for this skill:

- **Two inputs, both from a person.** Screenshots from Instagram's Professional
  Dashboard (account and per-post insights), taken by the owner or staff in
  the app, and sales or order numbers the owner pastes from the ERP for the
  same dates, such as orders per design code per week. Totals only: no
  customer names, numbers, addresses or order details. This skill has no
  connection to Instagram or the ERP and reads neither directly.
- **Likes and views are not sales.** A sale is an order the ERP records.
  Views, likes, comments, saves, shares, sends and follows are attention.
  Report them apart from the ERP numbers, and never write "this post sold" or
  "drove sales" from engagement alone.
- **Match posts to design codes.** Use the manual post receipts in
  `~/.claude/instagram/log.md` to find each post's design code, then put the
  ERP numbers for that code beside it. A post with no receipt cannot be
  matched. Say so rather than guessing.
- **Label every finding.** OBSERVED is what the screenshots or the ERP numbers
  show, with source and date. INTERPRETATION is what it might mean, and how
  sure you are. SUGGESTION is what to try next. The labels go in the output
  (`rules.md`, section 10).
- **Correlation is not proof.** Orders for a design code rising in the week it
  was posted is a correlation. Walk-ins, word of mouth, the time of year and
  what was in stock move orders too. Write "went up in the same week", not
  "the post caused it". A handful of posts means low confidence. Say that.
- **Never invent a number.** If a metric is not in the screenshots or the
  pasted numbers, write a placeholder and leave that post out of the ranking
  for that metric. Do not estimate hold at 3 seconds from views.
- **Keep it out of the repo.** Screenshots, ERP numbers and the audit stay in
  this chat or in `~/.claude/instagram/`.

For the WHAT THE DATA SAYS part of the output, use this shape, and add a SALES
block when the owner has pasted ERP numbers:

```
WHAT THE DATA SAYS
1. OBSERVED        Hold at 3s: top five average {{x}}%, bottom five {{y}}%.
                   Professional Dashboard, read {{date}}.
   INTERPRETATION  The opening seconds look like the main difference.
                   {{n}} posts, so {{low / medium / high}} confidence.
   SUGGESTION      Test two openings on the next product Reel.

SALES  (ERP numbers pasted by the owner, {{dates}})
   OBSERVED        {{design code}}: {{n}} orders the week it was posted,
                   {{n}} the week before.
   INTERPRETATION  Went up in the same week. One post. Not proof.
```

Where this section conflicts with the upstream text below, this section wins.

## Input

Ask for whichever the user has:

- Insights per post: views, reach, interactions, watch time, saves, shares,
  follows, and the non-follower share of reach. Screenshots are fine.
- Or the retention graph for their best and worst recent reels. This one
  screenshot is worth more than the rest combined.
- Or just the posts and their view counts, which is enough for a first pass.

Also read `~/.claude/instagram/log.md` if it exists, since it records which
hook formula each post used.

## What to actually measure

Raw views is the least useful number on the page, because it is mostly a
function of how many people already follow the account. Compute these instead
and show the working:

| metric | how | what it tells you |
| --- | --- | --- |
| **Outlier multiple** | views / the account's own median views | whether this was a real hit or a normal day |
| **Non-follower reach** | % of reach from people who do not follow | whether it travelled at all |
| **Hold at 3s** | viewers still there at 3s / viewers who started | whether the hook worked. This is the hook's grade. |
| **Average watch time** | straight from insights | whether the middle worked |
| **Sends per reach** | shares / reach | the strongest single signal you can earn. A send is a person putting their name on it. |
| **Follows per reach** | follows / reach | whether the profile converted the attention |

Rank by outlier multiple and sends per reach, not views. A reel with 4,000
views and 90 sends beat the one with 60,000 views and 11.

## Then find the pattern

With the top five and bottom five side by side, look for what separates them,
and be willing to conclude something the user will not like:

- **Hold at 3 seconds.** If the top and bottom differ here, it is the hook and
  nothing else, and everything downstream is a distraction.
- **Hook formula.** Which ids from `ig-reel/hooks.json` are in the top five?
- **Format.** Reel, carousel, single image.
- **Length.** Group into under 15s, 15 to 30s, 30 to 60s, over 60s.
- **Theme.**
- **Whether the user replied to comments in the first hour.**
- **Day and time.** Check this **last** and only if the others show nothing.
  It is almost never the cause and it is where people want it to be.

State the finding as a claim with the evidence attached, and say how confident
it is. With 30 posts you can see a pattern. With 6 you cannot, and saying so is
better than inventing one.

## The distinction that saves people months

**A reel that gets views and no follows is not a failed reel, it is a profile
problem.** A reel that gets no views is a hook problem. Separate the two before
recommending anything. If non-follower reach is high and follows per reach is
low, stop rewriting hooks and go to `/ig-profile`.

## Output

```
AUDIT  ·  31 posts  ·  Jun 12 - Sep 5  ·  median views 4,100

TOP 5 BY OUTLIER MULTIPLE
  18.2x  #3  Nobody Tells You   74,600 views  62% non-follower  hold@3s 71%  128 sends
   6.4x  #1  Cost Confession    26,300 views  48% non-follower  hold@3s 64%   71 sends
  ...

BOTTOM 5
   0.3x  #11 Numbered            1,200 views  9% non-follower   hold@3s 31%    2 sends
  ...

WHAT THE DATA SAYS
1. Hold at 3 seconds is the whole story. Top five average 66%, bottom five 33%.
   Everything else you are worried about is downstream of the first two seconds.
2. The posts where you were the one who looked bad: mean 8.1x vs 0.9x for
   everything else. n=5. Strongest signal here and it is not close.
3. Tool listicles get views and nothing else. High reach, no sends, no follows.
   Three of your bottom five.
4. Day of week shows nothing. Your Tuesday and Friday means are inside the
   noise. Stop optimising it.

STOP: listicles.
DO MORE: the ones with a cost you paid and a number attached.
```

For MYERAPAIRS, write WHAT THE DATA SAYS and SALES in the labelled shape from
the MYERAPAIRS section, and turn STOP and DO MORE into SUGGESTION lines.

Then hand the conclusions to `/ig-plan` so next week is built on the user's own
evidence rather than on defaults, and to `/ig-viral` so the swipe file gets
filtered to the formulas that work for this account specifically. The DEFAULTs
in `rules.md` (cadence, no festival or offer wording, the call to action, the
hashtag cap) stay until the owner changes them, whatever the evidence shows.
