---
name: ig-plan
description: >-
  Build the week on Instagram - what to post, which format, when, and who to
  engage with. Use when the user says "plan my week", "what should I post",
  "content calendar", "I have nothing to post about", or wants a posting
  schedule and an engagement list.
---

# ig-plan

The control room. Everything else in this pack executes; this decides what gets
executed. Run it once a week, on the same day.

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

- **Footwear post types, not creator types.** Plan with these:

  | type | job | usual format |
  | --- | --- | --- |
  | **New arrival** | a pair that just came in, shown clearly with its design code | Reel, photo or stories |
  | **Occasion styling** | one pair styled for a real occasion: office, college, daily wear, a wedding function | Reel or carousel |
  | **Size and fit help** | the sizes a design comes in, from the facts block. No fit claims; fit questions go to a person | carousel or stories |
  | **Colour options** | every colour the ERP lists for one design | carousel |
  | **How to order or pick up** | how to DM the code, and pickup terms only once the owner has approved them | stories or carousel |
  | **Shop behind-the-scenes** | the shop floor, unpacking, arranging the shelf. Never storage areas, never customers' faces | stories or Reel |
  | **Customer question answered** | a question customers really ask, answered from the facts block. No names, handles or screenshots | Reel, carousel or stories |

- **Cadence (DEFAULT, until the owner chooses):** 3 feed posts, 5 stories and
  1 Reel a week.
- **Only products with an ERP facts block.** Every product slot names a design
  code that has an ERP facts block (see `product-facts.md`). A product without
  one stays out of the plan and goes on a NEEDS FACTS line.
- **No festival or offer slots (DEFAULT).** No festival names, sale, discount or
  offer angles until the owner decides.
- **Every slot is labelled "manual post, needs sign-off".** Nothing in the plan
  is scheduled or posted by this pack. A person posts by hand after the owner,
  or a manager he names, signs off.
- **The engagement list is optional and manual.** Build it only if the owner
  wants one. A person works through it by hand. Nothing is followed, liked or
  commented automatically, and nobody is sent a DM first.

Where this section conflicts with the upstream text below, this section wins.

## Input

Read `../../myerapairs/voice.md` (see MYERAPAIRS above). If
`~/.claude/instagram/swipe.md` and `log.md` exist, read them.
The swipe file is the user's own evidence from `/ig-viral` about which formulas
are landing in their niche right now. It outranks the upstream advice in this
file, but never the MYERAPAIRS section or `rules.md`.
The log stops the plan repeating a theme from the last fortnight.

Then ask for these each week, and note them in the plan, not in a `voice.md`:

1. Which design codes have an ERP facts block this week, and which of them are
   new arrivals.
2. Which of the MYERAPAIRS post types the owner wants more or less of.
3. What actually happened this week: a new delivery, a question customers kept
   asking, a pair people kept asking about. This is where posts come from.
   Leave out customer names, handles and order details.
4. Optional: up to ten accounts for the manual engagement list.

## What to post

DEFAULT cadence, until the owner chooses: 3 feed posts, 5 stories and 1 Reel a
week. Reels are the format most likely to reach people who do not follow the
account. Carousels go deep with the people who already do. Stories are planned
separately with `/ig-story`.

Use the footwear post types in the MYERAPAIRS section. Mix across the week,
never two of the same type back to back.

For each slot give: the post type, the design code, the specific angle from
what actually happened this week, the format, and for a Reel the hook formula
number from `ig-reel/hooks.json`. Not a topic, an angle. "Heels" is not a plan.
"One pair, three outfits: kurta, jeans, saree" is a Reel.

## When to post

Post when the user's audience is awake and not at work. For most consumer
audiences that is early evening local time; for a business audience, early
morning.

But say this plainly: **the hour matters far less than the first two seconds.**
Instagram will keep showing a Reel for days if it performs, and will bury a
well-timed one that does not. If the user is optimising posting times before
their hooks work, they are polishing the wrong thing, and you should say so.

Anchor times to the audience's timezone, not the user's, if those differ.

## The engagement round (optional, manual)

Only if the owner wants it, and a person does it by hand. 20 minutes a day,
before posting, not after. Build a list of 10:

- **5 reach** - accounts with an audience the shop wants, where a good comment
  gets seen. Comment early, before the thread is 200 deep.
- **3 peers** - same size, same field. This is the group that reciprocates.
- **2 local** - Mandsaur pages and local businesses whose followers shop
  locally. Never pitch in a comment, and never send a DM first.

Hand the list to `/ig-comment` for drafts. A person posts any comment by hand.

## Output

```
WEEK OF <date>   DEFAULT cadence: 3 feed posts, 1 Reel, 5 stories

MON  7:30pm  PHOTO     NEW ARRIVAL        <design code>  first look, box to hand
             manual post, needs sign-off
WED  7:00pm  CAROUSEL  COLOUR OPTIONS     <design code>  every colour the ERP lists
             manual post, needs sign-off
THU  7:30pm  REEL      OCCASION STYLING   #18 Cold Open Demo  <design code>  kurta to jeans
             manual post, needs sign-off
SAT  6:00pm  CAROUSEL  CUSTOMER QUESTION  <design code>  the size question asked most
             manual post, needs sign-off

STORIES      5 this week, planned with /ig-story
             manual post, needs sign-off
NEEDS FACTS  design codes with no ERP facts block yet, left out of the plan
ENGAGE       optional, by hand, only if the owner wants a list

Say "write Thursday" and I will draft it.
```

Write the plan to `~/.claude/instagram/plan.md` so the other skills can read
it. Nothing is scheduled or posted anywhere. This is a plan, and a person posts
each item by hand after the owner signs off.
