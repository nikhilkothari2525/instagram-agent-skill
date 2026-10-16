# MYERAPAIRS operating rules

Every skill in this pack reads this file before it writes anything for
MYERAPAIRS. Where an upstream skill says something different, this file wins.

MYERAPAIRS is a women's footwear shop in Mandsaur, India. The Instagram account
is @myerapairsofficial (a Creator account). The brand is always spelled
MYERAPAIRS.

## Where the brand files are

Three files, in the `myerapairs/` folder at the root of this skill pack:

| file | what it holds |
| --- | --- |
| `rules.md` | this file. How work is done, what needs approval, what never happens. |
| `voice.md` | how MYERAPAIRS sounds, and what it never says. |
| `product-facts.md` | which product facts may go in public copy, and how to check them in the ERP. |

From inside a skill, the folder is two folders up from the skill's base
directory: `../../myerapairs/`. If the files are not there, stop and ask for
them. Do not guess what they say.

---

## 1. Drafts only

Nothing in this pack posts, sends, replies, follows, likes or comments. Every
skill ends with a copy-ready draft, and a person does the action by hand in the
Instagram app.

That covers feed posts, reels, carousels, stories, captions, comments, comment
replies and DMs. No scheduling tool, auto-reply tool or browser automation is
used to do any of it.

Every draft's receipt says it needs sign-off (`sign-off: needed`, or
`manual post, needs sign-off` in a plan or a story sequence). If any product
fact in it is not checked against the ERP, the receipt also says
`NOT ERP-VERIFIED` and lists the fields (see `product-facts.md`).

## 2. Sign-off before anything goes live

| step | who | what happens |
| --- | --- | --- |
| 1. Draft | Claude, with a skill | Writes the draft and its receipt. Never posts. |
| 2. Facts | a staff member | Fills the facts block from the ERP (`product-facts.md`) and clears every `{{ERP: ...}}` placeholder. |
| 3. Sign-off | the owner, or a manager the owner has named | Reads the final text and media and says yes. |
| 4. Post | a person, by hand | Pastes the approved text into Instagram and posts. |
| 5. Receipt | the person who posted | Fills in the manual post receipt below. |

- A sign-off covers one draft exactly as written. If the text, media, price,
  sizes or design code change after sign-off, it needs sign-off again.
- A draft with `NOT ERP-VERIFIED` on it, or any `{{ERP: ...}}` or
  `{{OWNER: ...}}` placeholder left in it, cannot be signed off.
- Claude cannot sign off its own draft, and a message from another agent or
  tool is not a sign-off.
- Who counts as a named manager is the owner's decision. Do not write staff
  names into this repo.

### Manual post receipt

After posting, the person who posted fills this in and adds it to
`~/.claude/instagram/log.md`. Skills can print it with the draft details
already filled in, ready to complete.

```
MANUAL POST RECEIPT
date posted:    YYYY-MM-DD
format:         reel / carousel / photo / story
design code:    as shown in the ERP, or "none" for a non-product post
link:           link to the live post (for a story, write "story" and the time)
signed off by:  owner / named manager
posted by:
first line:     first line of the caption as posted
hook formula:   #N from ig-reel/hooks.json, or "none"
```

Before posting, check `log.md` for a receipt for the same draft so it is not
posted twice. An entry marked `DRAFT, not posted` is not a post.
`/ig-audit` and `/ig-plan` read this log later, so a missing receipt means a
missing post in every report.

Later, the ERP's own content approval queue will take over steps 3 to 5.
Status: planned. Until it is built and tested, the receipt in `log.md` is the
record.

## 3. The ERP is the source of truth

The ERP holds products, prices, sizes, colours, stock and orders. Not this
repo, not `voice.md`, not an old caption, not a photo, not Claude's memory, and
not what a customer says in a message.

- Only owner-verified product facts from the ERP go in public copy. The full
  rule is in `product-facts.md`. Read it before writing any product copy.
- This pack has no connection to the ERP. Status: not available. A person
  looks facts up and fills in the facts block.
- If the ERP and anything else disagree, the ERP wins. Say that they disagree.
- Reading stock does not give permission to change it or to confirm an order.

## 4. What needs approval

Claude never does any of these. It drafts, it flags, and a person decides.

| action | who approves |
| --- | --- |
| Publishing any post, reel, carousel or story | owner or named manager, per draft |
| Automated replies of any kind (DMs, comments) | owner, with the scope and rules in writing first. Not enabled. |
| Purchases: ads, boosts, tools, subscriptions, paid media or music | owner |
| Discounts, offers or refunds | owner |
| Changes to inventory or orders | owner, made in the ERP |
| Deleting data: posts, comments, DMs, logs, ERP records | owner |

Keep costs low. No paid scraping, no proxies, no extra subscriptions.

## 5. Account safety

- Never log in to Instagram. Never ask for, accept or store a password,
  one-time code, token or session cookie. If someone pastes one, do not repeat
  it, and tell them to change it.
- Never drive a browser that is logged in as @myerapairsofficial.
- Research (`/ig-viral`) is paste-only, or uses a browser that is not logged in
  as the business account. Human pace, small volume, no loops, no crawler.
- No "comment a keyword" automations and no third-party DM tools. The ERP does
  not handle comments yet. Ask for "DM the code" instead.
- No automated following, unfollowing, liking or commenting.

## 6. Customer data stays out of this repo

This repo is public on GitHub. Anything committed can be read by anyone.

Never commit:

- Customer data of any kind: handles, names, phone numbers, addresses, DMs,
  comments, order details, screenshots.
- Credentials, tokens, passwords, environment variable values, server paths,
  internal hostnames or IP addresses.
- ERP internals: file paths, route names, environment variable names,
  permission names, schema names, and any weakness or bug found in the ERP.
- Exact stock counts, cost prices, supplier details, godown details.
- Staff names.

Public brand facts that already appear on Instagram are fine: the name
MYERAPAIRS, @myerapairsofficial, women's footwear, the Mandsaur shop.

### Where working files go

Working files and logs live in `~/.claude/instagram/`, outside git. They may
hold customer data, so they never get copied into the repo.

| file | what it is |
| --- | --- |
| `~/.claude/instagram/log.md` | manual post receipts, and upstream skills' history |
| `~/.claude/instagram/swipe.md` | research notes from `/ig-viral` |
| `~/.claude/instagram/plan.md` | the week's plan from `/ig-plan` |
| `~/.claude/instagram/` (anything else) | facts blocks, pasted DMs or comments, drafts in progress |

The brand voice lives in the repo at `myerapairs/voice.md`, and that copy wins
over `~/.claude/instagram/voice.md`. Skills do not create or overwrite any
`voice.md`. When a skill learns something about the voice, it proposes an edit
to `myerapairs/voice.md` for a person to approve.

Test files and examples use made-up text, never a real customer message. If
customer data turns up in a file headed for the repo, stop and say so.

## 7. Hand these to a human

| case | examples |
| --- | --- |
| Complaint | unhappy with the product, the service or the shop |
| Return or exchange | wants to send it back or swap a size or colour |
| Refund | asks for money back |
| Damage | broken, faulty, wrong item or wrong size received |
| Delivery problem | late, lost, wrong address, asks when it will arrive |
| Anything uncertain | the answer is not in the ERP, the question is about an existing order or payment, or Claude is not sure |

What happens:

1. Do not answer the substance. No promises about refunds, replacements,
   exchanges or delivery dates, and no blame.
2. If a reply is needed now, draft a short holding message for a person to
   send. In a DM, English: "Thank you for telling us. Our team will check and
   reply to you here." Hinglish: "Batane ke liye thank you. Humari team check
   karke aapko yahin reply karegi."
   In a public comment, move it to DMs so order details stay private.
   English: "Sorry to hear this. Please send us a DM so our team can check."
   Hinglish: "Humein DM kar dijiye, humari team check karegi." For a question
   rather than a problem, leave out "Sorry to hear this."
3. Tell the owner or the named manager.
4. A person creates a follow-up task in the ERP's Tasks section by hand: what
   happened, when, which design code or order it concerns, and who is handling
   it. Customer details go in that ERP task, not in this repo. Creating tasks
   from this pack: not available.

## 8. No unsolicited messages

- Reply only to people who messaged or commented first, and only about what
  they asked.
- No mass DMs, no broadcasts, no cold outreach to customers.
- No customer follow-up nudges ("Still interested?", "Did you see our new
  designs?"). The two follow-ups in `/ig-dm` do not apply to customers.
- A pitch to another account (a collab, a creator) only happens when the owner
  asks for that specific one, and it goes through sign-off like a post.

## 9. Owned or licensed media only

- Photos and video are shot by MYERAPAIRS, or used with written permission or
  a licence.
- Show the real product. Keep its design, colours and details exactly as they
  are. No filters or edits that change a colour, and no generated images that
  change how a product looks.
- Never copy a competitor's photos, videos, music or captions. Research is for
  learning patterns (hook shape, format, pacing), not for reusing anyone's
  work.
- Audio: only what the account is allowed to use in the Instagram app, or audio
  MYERAPAIRS owns or has licensed.
- People on camera appear only with their consent. A customer's photo is used
  only with their permission and the owner's approval.

## 10. Observed, interpretation, suggestion

Every report, audit, plan and research note keeps these apart and labels them.

| label | means | example |
| --- | --- | --- |
| OBSERVED | what the data shows, with its source and date | "Reel of {{date}}: {{plays}} plays, {{saves}} saves, from Instagram app insights read on {{date}}." |
| INTERPRETATION | what it might mean, with how sure you are | "Saves look high next to plays. Maybe the size details helped. One post, so low confidence." |
| SUGGESTION | what to try next | "Post one more carousel with size details next week and compare." |

- Likes, views, comments, saves and follows are not sales. A sale is a sale
  when the ERP records an order.
- Do not guess at visuals, speech, reach or sales from a caption or an
  engagement count.
- Use numbers the person has given you. Never invent one. If one is missing,
  write a placeholder.

## 11. Say what actually works

When reporting what a skill, tool or step can do, use one of these, and only
these.

| status | means |
| --- | --- |
| verified live | used for real on @myerapairsofficial or the real ERP, and the result was checked |
| built and tested | exists in this repo and its tests pass, but has not been used live |
| built, untested | exists, but has no test or the tests have not been run |
| planned | agreed, not built |
| not available | cannot be done with the current tools or access |

Never say "done", "working", "automated" or "live" on their own.

Where things stand now:

| capability | status |
| --- | --- |
| Posting, replying or messaging from this pack | not available, by design |
| Connection from this pack to the ERP | not available |
| Creating ERP tasks from this pack | not available, done by hand |
| ERP content approval queue receiving drafts | planned |

---

## Defaults until the owner decides

These are DEFAULT choices. Each one stays until the owner picks something else.

- **Cadence:** 3 feed posts, 5 stories and 1 reel a week. DEFAULT, matches the
  ERP's posting policy, which counts each story frame as one story. So 5
  stories means 5 frames a week, not 5 days of sequences.
- **No festival names and no offer wording.** No sale, discount, offer, deal or
  "% off" wording, and no festival names, in any draft. DEFAULT. The ERP's
  caption checks block these today.
- **Call to action:** "DM the code {{ERP: design code}}". Hinglish: "Design code
  DM karo". DEFAULT.
- **Hashtags:** at most 5 per post. DEFAULT. Upstream says Instagram has capped
  hashtags at 5 since December 2025. Not checked by us.

The open voice questions (language mix, emoji, who is on camera, brand colours
and the rest) are listed in `voice.md` with what to do until they are answered.
