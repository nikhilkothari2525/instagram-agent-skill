---
name: ig-story
description: >-
  Write the day's Instagram Stories - the frame-by-frame sequence, which
  stickers to use where, and the one that moves people into the DMs. Use when
  the user says "stories", "what do I post on my story", "story sequence",
  "poll idea", "I have nothing to story about", or wants to sell something
  without making a post about it.
---

# ig-story

Stories are not a smaller feed. The feed is how strangers find you. Stories are
how the people who already follow you decide whether you are a person worth
buying from, and they are the only surface on Instagram where a tap turns into
a conversation in one move.

Nobody outside your followers sees these, so the job is completely different:
depth, not reach.

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

- **Cadence (DEFAULT, until the owner chooses):** 5 stories a week, as in
  `rules.md`, planned by `/ig-plan`. One story is one frame. The "three to
  seven frames a day" below is upstream advice, not the MYERAPAIRS cadence.
- **The design code is on every product frame**, written exactly as the ERP
  has it, with a "DM the code {{ERP: design code}}" line (Hinglish: "Design
  code DM karo") or a question sticker. The customer messages first.
- **No countdown or urgency stickers.** Nothing that implies scarcity or a
  deadline: no countdown, no "last few pairs", no "ending soon". No festival
  names or offer wording until the owner decides (DEFAULT).
- **Facts only from the ERP facts block.** Price written like `₹1,499`,
  available sizes only and never counts, material only if the ERP records it,
  no comfort or fit claims. A missing fact is written `{{ERP: field}}` and the
  sequence is labelled NOT ERP-VERIFIED.
- **Real footage of the actual pair.** Show the shop floor, never storage
  areas. Who appears on camera follows `voice.md`.
- **Reply only to people who wrote first:** a DM, or a question-box answer
  that asks something (price, sizes, the code), and only about what they
  asked. A plain answer like "with jeans" is not a question, and a poll vote is
  not a message, so neither gets a DM. A person writes and sends every reply.
  No follow-up nudges. Complaints, returns, refunds, damage, delivery problems
  and anything uncertain go to a person, who logs a follow-up task in the ERP
  by hand.
- **A link sticker** only points to a target the owner has approved.
- **Posted by hand.** A person posts the stories after the owner, or a manager
  he names, signs off.

Where this section conflicts with the upstream text below, this section wins.

## The daily shape

Three to seven frames a day. Beyond about seven, the tap-forward rate climbs
and the last frames play to nobody, which is exactly where people put the ask.

```
1       THE OPEN     something happening today, with a face or a hand in it.
2-3     THE MIDDLE   the actual content: the process, the result, the mistake.
4       THE ASK      one sticker. Poll, question box, quiz or link.
5       THE CLOSE    the answer, the outcome, or tomorrow's setup.
```

Put the ask at frame 4, not frame 7. Completion drops with every tap and the
ask should be seen by the people who are still there.

## The stickers, and what each is actually for

| sticker | job | use when |
| --- | --- | --- |
| **Poll** | the cheapest tap there is | you want volume of response, not information |
| **Question box** | harvesting the exact words people use | you need content ideas or objections, verbatim |
| **Quiz** | teaching by letting them be wrong | there is a common misconception in the niche |
| **Slider** | vibe check | nothing important. Fun, low value |
| **Link** | the only clickable surface besides the bio | there is somewhere real to go |
| **Countdown** | a deadline people can subscribe to | not for MYERAPAIRS: it implies a deadline or scarcity |
| **Add yours** | reach beyond your followers, occasionally | the prompt is one anyone in the niche can answer |

The question box is the most undervalued one in the list. Every answer is a
caption, a Reel hook or a DM opener written in the audience's own words. Feed
them to `/ig-reel` as formula #16. For MYERAPAIRS, use the answers as ideas
only. Do not quote a customer's answer in public copy, and never use one as a
DM opener.

## Rules

- **A face or a hand in the first frame.** Text on a coloured background gets
  tapped through, and the first frame decides whether the rest get watched.
- **One idea per frame.** Reading a paragraph on a story is not a thing anyone
  does.
- **Keep text inside the middle.** On 1080x1920, nothing above y=250 or below
  y=1600. The profile row sits on top and the reply bar sits underneath.
- **Talk to one person.** "You" singular. Stories are the closest thing to a
  DM that is not one.
- **Do not repost your own feed post to stories with no comment.** It is the
  single most ignored frame on the platform. If you are pointing at a post, say
  what happened in the comments and why it is worth going back for.
- **Sell on stories, not only in posts.** Three frames of context, one frame
  of the product with its design code, one frame that invites the DM. A
  customer photo or review goes in only if it is real and the owner has
  approved it. That sequence sells more than a feed post about the same thing
  and costs you no reach.

## The DM funnel, done honestly

The sequence that works: a story that names a problem, a question box or a
"DM the code" frame that lets people say "that's me" in their own words, and
then a reply to each person who wrote in. The conversation starts because they
spoke first.

Automated keyword DM replies exist for professional accounts, through
Instagram's own tools and approved partners. MYERAPAIRS does not use keyword
automations or partner tools at all (`rules.md`, section 5). A person writes
every reply. Only Instagram's own auto-replies could be considered, and only
after the owner approves their scope and rules in writing. Bulk DMing people
who did not interact is not allowed either, and it is what gets accounts
restricted. The rule is simple: **they message first, then
you reply.**

## Output

The frames in order, each with what is on screen, what is said, and which
sticker, plus what to do with the answers:

```
STORIES  ·  Tuesday  ·  5 frames  ·  manual post, needs sign-off

1  [hand lifting the pair off the shelf]  "New in."
2  [close-up, side view]                  code {{ERP: design code}} on screen
3  [the pair on foot, no face]            "{{ERP: colour}}. Sizes {{ERP: available sizes}}."
4  [question sticker]                     "Which outfit would you wear these with?"
5  [product photo + text]                 "{{ERP: price}}. DM the code {{ERP: design code}}."

After: reply by hand to each person who sent a DM, and to question-box answers
that ask something (price, sizes, the code), only about what they asked. A
plain answer like "with jeans" gets no DM. Nobody who did not write first gets
a message. That is the whole funnel.
```

Nothing is posted. A person posts it by hand after the owner signs off.
