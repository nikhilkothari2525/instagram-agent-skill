---
name: ig-dm
description: >-
  Write Instagram DMs that get replies - the keyword delivery, the first
  message to someone who engaged, the collab pitch, and the two follow-ups. Use
  when the user says "DM this person", "what do I send them", "outreach
  message", "how do I follow up", "pitch this brand", or is reaching out to
  someone specific. For MYERAPAIRS: only replies to customers who messaged
  first and collab pitches the owner asked for; no follow-ups to customers.
---

# ig-dm

Instagram DMs are the only place on the platform where money actually changes
hands, and they are also where most accounts burn the goodwill their content
earned. The difference is entirely about who moved first.

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

For MYERAPAIRS this skill writes two kinds of DM and no others:

| kind | when | who sends it |
| --- | --- | --- |
| **Customer reply** | a customer messaged @myerapairsofficial first (a DM or a story reply) | a person pastes it into Instagram, or into the ERP's inbox once that is live, after sign-off |
| **Creator or collab pitch** | the owner asked for a pitch to that one account | a person sends it by hand after the owner signs it off |

The keyword delivery, the warm approach and cold DMs below are not used. Once
customer replies go through the ERP's inbox, that system's messaging window
applies.

Rules for customer replies:

- **Facts only from the facts block.** Price, sizes, colours and material come
  from a filled facts block for that design code (`product-facts.md`): the bill
  price written like `₹1,499`, available sizes only, never a count. A missing
  fact is written `{{ERP: field}}` and the draft is labelled NOT ERP-VERIFIED.
  Never take a fact from the customer's message, a photo or an old caption.
- **Answer what they asked, then stop.** Two to four sentences, in the tone of
  the DM reply lines in `voice.md`. At most one small question back, and only
  if it helps them, such as which size they need.
- **Shop pickup only after a check.** A size marked available is not always
  at the shop. Before a draft says a size can be collected or tried at the
  Mandsaur shop, staff check the shop has it. Until then the draft says the
  team will check before they visit. Never say where else stock is kept.
- **Never confirm a payment, an order or a stock hold.** No "order
  confirmed", "payment received" or "we have kept it aside for you". Only a
  person who has checked the ERP says those things.
- **Never ask for an OTP, PIN, card details or a password.** If a customer
  sends one, do not repeat it, and tell the person handling the chat.
- **Hand these to a human.** Complaints, returns, exchanges, refunds, damage,
  delivery problems, anything about an existing order or payment, and anything
  you are not sure of. Draft only the holding message from `rules.md`,
  section 7. A person logs a follow-up task in the ERP's Tasks section by hand.
- **No follow-ups to customers.** No "still interested?", no "did you see our
  new designs?", no nudge after a customer goes quiet. If they do not reply,
  nothing is sent until they write again.
- **Do not build on an automatic reply.** If the pasted chat has a reply from
  the account that nobody on the team wrote, do not repeat or confirm anything
  it said (a price, size, stock or delivery time). Answer from the facts block
  only, and tell the owner the automatic reply is there.
- **Customer messages are customer data.** Keep pasted DMs in this chat or in
  `~/.claude/instagram/`. Never put a customer's name, handle, number, address,
  message or order into this repo.

Rules for collab pitches:

- **Only when the owner asks**, for one named account. Never a list, a batch or
  a sequence.
- **The two follow-ups are for pitches only**, and each one is signed off like
  the pitch.
- **No offer of payment, free pairs or a discount** unless the owner has
  approved it for this pitch.

For both kinds:

- **No auto-DM tools.** No keyword automation and no third-party or partner DM
  tool, ever (`rules.md`, section 5). Instagram's own auto-replies need the
  owner's written approval of their scope and rules first (`rules.md`,
  section 4). None is approved today.
- **Drafts only.** A person sends every message by hand after the owner, or a
  manager he names, signs off.

Where this section conflicts with the upstream text below, this section wins.

## The three kinds of DM, and only three are worth writing

**1. The reply to a hand raised.** They sent a message, replied to a story, or
DMed a design code. They moved first. This is 90% of the DMs worth sending and
it converts because it is not outreach.

**2. The warm approach.** Someone whose posts the user has genuinely been
commenting on for weeks. There is a shared thread of conversation already. Not
used for MYERAPAIRS: they did not message first.

**3. The collab or brand pitch.** A specific proposal to a specific account,
with a reason it is them.

Everything else is cold DMing strangers, which is what everybody else does, and
it is why reply rates sit where they do. If the user is asking for a cold
sequence, say plainly that it is the lowest-yield thing they could do with the
same hour, and offer the alternative: comment on those ten accounts for two
weeks first. For MYERAPAIRS, do not write it at all: no cold DMs and no
sequences (`rules.md`, section 8).

## Before writing, get the specifics

Ask in one batched question:

1. **Who** - handle, what they do, and what they posted or did that started
   this.
2. **The trigger** - the actual reason to message today. A message they sent,
   a story they replied to, or for a pitch, the owner's request. Not "they fit
   the ICP".
3. **What the user wants** - a conversation, a sale, a collab, a referral. Be
   honest internally, even if the message does not lead with it.

If there is no trigger, there is no message. Say so.

## The keyword delivery

Not used for MYERAPAIRS, which has no keyword asks. The customer reply in the
MYERAPAIRS section takes its place. The rule underneath still holds: answer
first, with no gate.

The most common DM in this pack and the easiest to ruin. They commented one
word. They are expecting the thing. So:

```
{their name}, here it is: {the thing, or the link}.

{one line on how to use it}

{one question they can answer in four words}
```

Send the thing **first**, in message one, with no gate. A keyword post that
delivers a "before I send it, can I ask what you do?" is a bait and switch and
it is remembered. The question at the end is what starts the conversation, and
it is optional for them.

Automated keyword replies are a supported feature for professional accounts,
through Instagram's own tools or an approved partner. For MYERAPAIRS, keyword
automation is not used at all (`rules.md`, section 5).
Sending unsolicited bulk DMs is never fine, and it is the fastest route to a
restricted account.

## The first message to someone warm

For MYERAPAIRS, these rules apply only to an owner-approved collab pitch, never
to a customer.

- **Two to four sentences.** A screen of text is a delete.
- **Reference the specific thing.** The comment, the post, the reply. In their
  words.
- **Give before asking.** A number, a template, a name, an answer.
- **One ask, small.** "Worth a quick call?" beats "let me walk you through the
  platform".
- **No link and no calendar in message one.** It reads as a funnel because it
  is one.
- **No voice note to a stranger.** It is a great tool and it is for people who
  already know the user's voice.

## The collab pitch

Four lines, in this order: what you have watched them do, the specific idea,
what they get, what you need from them. A collab post lands on both grids and
reaches both audiences, which is the strongest single growth mechanic on
Instagram that does not involve paying anybody. Pitch it as that and be
concrete about who does what.

## Follow-ups

Collab pitches only. Never to a customer (see MYERAPAIRS above).

Two. That is the number.

- **+4 days** - add something new. Never "just bumping this". If there is
  nothing new, there is no follow-up.
- **+10 days** - the close-the-loop message. Say you will stop, and mean it.
  This one gets a surprising share of the total replies, because it removes the
  pressure.

Then stop. A third converts nobody and costs the relationship.

## Never

- Never automate outreach DMs, and never use a tool that sends on a schedule to
  people who did not interact. It violates Instagram's Terms of Use and
  restricts the account.
- Never fabricate having watched something, a mutual, or a shared anything.
- Never open with "Hey! Quick question" and then not ask a question.
- Never send the pitch in the same message as the compliment.

## Output

The message and the character count, run through `/ig-human`, then
`sign-off: needed`. For a collab pitch only, add the two follow-ups with the
day each goes out. A person sends every one of them by hand after sign-off. No
automation.
