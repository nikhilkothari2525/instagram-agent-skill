---
name: ig-reply
description: >-
  Handle the comments under the user's own reels and posts - draft replies to
  the ones worth answering, sorted by which ones are. Use when the user pastes
  their comments, says "reply to these", "handle my comments", "someone said X
  on my reel", or is dealing with a critic, a hater or a lead in the comments.
---

# ig-reply

The comment thread under your own post is where reach is decided. Every reply
is another interaction on the post, replies arriving in the first hour do most
of the work, and on Instagram a reply can also be a Reel, which is the single
most underused move on the platform.

But the value is not equal across comments, so this skill sorts before it
writes.

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

- **Pasted comments are customer data.** Keep them, and the names and handles
  in them, in this chat or in `~/.claude/instagram/`. Never write them into
  this repo, a test or an example.
- **No prices in public replies.** A question about a pair (price, size,
  colour, "available?") gets the design code and an invitation to DM, not a
  price and not a size promise. The DM reply is then drafted with `/ig-dm`
  from the facts block.

  | language | reply |
  | --- | --- |
  | English | Thank you for asking! DM us the code {{ERP: design code}} and we will send you the details. |
  | Hinglish | Design code {{ERP: design code}} DM karo, hum aapko details bhej denge. |

  Take the design code from the post's caption or its facts block, exactly as
  written there. Vary the wording a little so the replies do not read as
  copy-paste.
- **Hand these to a human.** A complaint, return, exchange, refund, damage, a
  wrong item or a delivery problem, a question about delivery, payment or an
  existing order, or anything uncertain goes in the HANDOVER bucket, first. Do
  not answer the substance and do not promise anything. Draft only the comment
  holding reply from `rules.md`, section 7, which moves the conversation to
  DMs so order details stay out of public comments. English: "Sorry to hear
  this. Please send us a DM so our team can check." Hinglish: "Humein DM kar
  dijiye, humari team check karegi." For a question rather than a problem,
  leave out "Sorry to hear this." Tell the owner or the named manager, and
  remind them that a person logs a follow-up task in the ERP's Tasks section
  by hand.
- **No keyword asks and no keyword tools.** MYERAPAIRS posts ask people to DM
  the code, so there is no KEYWORD bucket. Never set up or suggest an auto-DM
  for comments, through Instagram's own tools or a partner, and never DM
  someone who did not message first.
- **Same claims rules as a caption.** No comfort, fit, durability, stock,
  delivery or offer claims in a reply (`product-facts.md`). A comfort or fit
  question gets the DM invitation, never a promise of how it feels.
- **No reply-with-Reel.** It puts the person's comment and handle on a public
  video (`voice.md`, Off limits). Turn a common question into an ordinary
  `/ig-reel` draft that paraphrases it and does not show or name the person
  (the "Customer question answered" type in `/ig-plan`).
- **Drafts only.** A person pastes each reply into Instagram by hand after the
  owner, or a manager he names, signs off. This skill does not like, hide or
  delete anything.

Where this section conflicts with the upstream text below, this section wins.

## Input

The user pastes the comments, ideally with handles. Screenshots are fine. Do
not scrape the thread with a browser tool.

## Triage first

Sort every comment into one of six buckets and say the counts out loud:

| bucket | what it is | what it gets |
| --- | --- | --- |
| **HANDOVER** | a complaint, return, refund, damage or delivery problem, a question about delivery, payment or an existing order, or anything uncertain | the comment holding reply from `rules.md`, section 7, then a person |
| **LEAD** | someone asking about a pair: price, size, colour, "available?" | the design code and an invitation to DM, no price |
| **SUBSTANCE** | adds data, disagrees, extends | the longest reply on the thread |
| **QUESTION** | a question a lot of people have | this one becomes a Reel, not just a reply |
| **SUPPORT** | "🔥", "great post", a tag | a like, and 3 to 8 words at most |
| **NOISE** | pitch, spam, bad faith, bait | nothing, or one line and out |

Write in that order and stop when the value stops.

## The move most people miss

If a question in the comments is one that thirty other people also have,
**reply to it with a Reel**. Instagram will attach the comment to the new video
as a sticker, the person who asked gets notified, and a question with real
demand behind it becomes a post with the hook already written for you. Flag
every QUESTION that qualifies and hand it to `/ig-reel` as formula #16.

For MYERAPAIRS: an ordinary Reel, not a reply-with-Reel. Paraphrase the
question, with no comment sticker and no handle (see MYERAPAIRS above).

## How to reply

- **Answer the actual question**, except price and anything about a specific
  pair, which go to DM with the design code. If someone asks how, tell them
  how, in the reply.
- **Use their name once**, at the start, without an exclamation mark.
- **Match their length.** A four-word comment does not get a four-line reply.
- **To a critic:** concede the true part first, in their words, then hold the
  line. Never delete, never get defensive, never reply twice on the same
  thread.
- **To a hater:** nothing. A reply is reach, and reach is what they came for.
  Hide the comment if it is abusive. Instagram's comment controls exist and
  using them is not losing.
- **To a lead:** thank them, give the design code and invite a DM, in one or
  two sentences. No price in public, and no pitch.

## Keyword comments

Not used for MYERAPAIRS: posts ask people to DM the code, not to comment a
keyword. If someone comments a design code or "price?", it is a LEAD. Never set
up an auto-DM for comments, and never bulk-DM people who did not message first.

## Output

One block, grouped by bucket, each reply copy-ready and already humanized:

```
REPLIES  ·  31 comments  ·  1 HANDOVER, 9 LEAD, 1 SUBSTANCE, 1 QUESTION, 17 SUPPORT, 2 NOISE
sign-off: needed

HANDOVER  (1)  for a person. Comment holding reply only, then an ERP task by hand.
@handle - says the wrong size arrived
> Sorry to hear this. Please send us a DM so our team can check.

LEAD  (9)  design code and a DM invite, no price. Same warmth, not copy-paste.
@handle - "price?"
> Thank you for asking! DM us the code {{ERP: design code}} and we will send
> you the details.

QUESTION -> REEL
@handle - "does this come in other colours?"
  12 likes on this comment. Could be a Reel, not a reply. Formula #16,
  owner approval first. For MYERAPAIRS: an ordinary Reel, not a
  reply-with-Reel.

NOISE  (2)  skipped. Replying gives them reach.
```

Then the gate: nothing is posted until the owner, or a manager he names, says
yes. A person pastes the replies by hand.
