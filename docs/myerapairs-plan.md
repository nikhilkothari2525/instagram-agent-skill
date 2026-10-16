# MYERAPAIRS Instagram plan

How this skill pack fits into the way MYERAPAIRS runs its Instagram account,
@myerapairsofficial, and how that is meant to change over time.

This repo is public, so this plan describes the shop's ERP only in general
terms. It says what the ERP is for, not how it is built.

The brand rules this plan relies on are in
[`myerapairs/rules.md`](../myerapairs/rules.md). Where this plan and the rules
disagree, the rules win.

---

## Two parts, two jobs

| part | its job | what it holds |
| --- | --- | --- |
| This repo, the drafting desk | writes drafts for a person to check and post | skills, brand rules, voice, plans |
| The ERP | the source of truth, and the place where anything live happens | products, prices, sizes, colours, stock, orders, approvals, customer enquiries, tasks |

### This repo: the drafting desk

- Thirteen skills, from Jake Schincariol's upstream pack, with MYERAPAIRS
  sections added: reel scripts, captions, carousels, stories, profile review,
  the weekly plan, comments, comment replies, DMs, repurposing, audits,
  research notes and the humanizer.
- Every output is a draft. A person posts or sends it by hand, after the owner
  or a manager the owner has named signs it off.
- It runs only when someone opens Claude and asks for something. Nothing in it
  runs on a schedule, and nothing in it runs in the background.
- It has no connection to Instagram and no connection to the ERP.

### The ERP: the source of truth

- It holds products, prices, sizes, colours, stock and orders. Only
  owner-verified facts from the ERP go in public copy. A fact nobody has
  checked there stays a placeholder, `{{ERP: field}}`, and the draft is
  labelled `NOT ERP-VERIFIED`.
- It has a content approval queue, where drafts will be reviewed and signed
  off. Drafts from this repo do not reach it yet. That is phase 2.
- It has a customer inbox, where staff handle Instagram enquiries. Posts ask
  people to DM the design code, so staff can match a message to the right
  product.
- It has a tasks section, where staff log follow-ups for complaints, returns,
  damage, delivery problems and anything uncertain.

---

## The boundary

| stays in the ERP | stays in this repo |
| --- | --- |
| Anything that acts on the live Instagram account: publishing, comments, messages, insights | Skills, and the small tools that check a draft |
| Instagram and Meta access, and every credential | Brand rules, voice and the product-fact rules |
| Approvals, and the record of who signed off what | Plans and docs, like this one |
| Customer messages, orders, stock and their history | Made-up examples and tests |

- This repo never holds ERP or Instagram credentials, and it never calls the
  ERP or Instagram.
- ERP code, configuration and internal names are never copied into this repo.
- Customer data never comes into this repo. Working files and logs stay in
  `~/.claude/instagram/`, outside git.
- When a new feature needs to act on the live account or on business data, it
  is built in the ERP, not here.

---

## Phases

### Phase 1: rules and drafting (now)

Goal: every draft follows the MYERAPAIRS rules and is ready for a person to
check, sign off and post by hand.

- Brand files in [`myerapairs/`](../myerapairs/): `rules.md`, `voice.md` and
  `product-facts.md`. Every skill reads them before it writes anything.
- A person looks product facts up in the ERP and fills them in. Prices are the
  bill price including GST, written like ₹1,499. Sizes are only the ones the
  ERP marks available, with no counts.
- The owner, or a manager the owner has named, signs off each draft. A person
  posts it by hand and adds a manual post receipt to
  `~/.claude/instagram/log.md`.
- Complaints, returns, refunds, damage, delivery problems and anything
  uncertain go to a person, who logs a follow-up task in the ERP by hand.
- Research is paste-only, or uses a browser that is not logged in as the
  business account. See "Research" below.

Phase 2 starts when the owner says so.

### Phase 2: drafts flow into the ERP approval queue

Goal: one place to review, sign off and record every post, instead of a log
file on one computer.

- Skills write each draft in a fixed, documented format: the text, the format
  (reel, carousel, photo, story), the design code, the facts block and the
  status labels.
- The ERP takes these drafts into its content approval queue. How it takes them
  in is built and tested in the ERP project, not here.
- Sign-off happens in the ERP, by the owner or a named manager. The ERP checks
  the product facts against its own records before sign-off.
- Posting is still by hand. The ERP records the post, and the manual receipt in
  `log.md` is no longer needed.
- This repo still has no credentials and no connection to the ERP. A person
  moves each draft across.

### Phase 3: official Instagram API features, in the ERP, one at a time

Goal: less manual work, using only Instagram's official API for professional
accounts. No browser automation, no third-party posting or reply tools, no
unofficial access.

Features are added one at a time, in this order unless the owner picks
another:

| feature | what it would do | what stays with a person |
| --- | --- | --- |
| Publishing | posts a signed-off draft from the approval queue | sign-off of every post |
| Comments | shows comments on MYERAPAIRS posts in the ERP, with draft replies | sending replies, unless the owner approves written rules for routine ones |
| Insights | reads the account's own post numbers for audits and plans | deciding what the numbers mean. Likes and views are not sales. |

Before any one of them starts:

1. The owner approves its scope and rules in writing.
2. Someone checks what the official API actually supports for this account
   type, one format at a time (photo, carousel, reel, story), and writes the
   result down with a status word.
3. It is built and tested in the ERP, behind the approval queue.
4. It has duplicate-post protection, a way to pause it, a limited number of
   retries, clear errors when access expires or a post fails, and a log of
   what it did.

A feature is called verified live only after it has been used for real on
@myerapairsofficial and the result was checked.

---

## Research

Research is for learning patterns (hook shapes, formats, pacing), never for
copying anyone's photos, video, music or captions.

- **Own account:** numbers a person reads from the Instagram app, and later
  official insights (phase 3).
- **Other accounts:** public professional accounts only. Paste-in, or a browser
  that is not logged in as the business account, at human pace and small
  volume.
- **Approved sources only.** No paid scraping, no proxies, no logging in as
  anyone, and no crawler in this repo. Any automated research tool runs outside
  this repo, only with the owner's approval, only on public data, and inside a
  fixed limit on how much it collects. When it hits that limit it stops. Nobody
  resets or works around a limit to get more.
- **Reports keep three things apart:** what was observed (with source and
  date), what it might mean, and what to try next.

---

## Where things stand

Status words are the ones in [`myerapairs/rules.md`](../myerapairs/rules.md),
section 11.

| capability | status |
| --- | --- |
| Posting, replying or messaging from this repo | not available, by design |
| Connection from this repo to the ERP | not available, by design |
| Creating ERP tasks from this repo | not available, done by hand |
| Drafts flowing into the ERP approval queue | planned (phase 2) |
| Publishing through the official API, in the ERP | planned (phase 3), needs owner approval |
| Comment handling through the official API, in the ERP | planned (phase 3), needs owner approval |
| Insights through the official API, in the ERP | planned (phase 3), needs owner approval |

---

## Open owner decisions

Each of these waits for the owner. Where drafts need an answer first, they
follow the DEFAULT or the "until then" note.

### Voice and look

| decision | until then |
| --- | --- |
| Three past captions the owner likes | do not imitate old captions. Write to the tone in `voice.md`. |
| English and Hinglish mix | give each caption in both, and the owner picks |
| Emoji level | 0 to 2 per caption, never the first character |
| Who appears on camera | product, hands and feet only. No faces. |
| Brand colours | plain neutral backgrounds, so the real product colour stands out |
| Words to use, and more words to avoid | follow the "Off limits" list in `voice.md` |
| Where the link in bio goes | no mention of a link in bio |
| Public return, exchange and pickup terms | say nothing about them in public. Questions go to a person. |

### Posting rules

| decision | until then |
| --- | --- |
| How often to post | 3 feed posts, 5 stories and 1 reel a week. DEFAULT. |
| Festival names and offer wording | none in any draft. DEFAULT. |
| Call to action | "DM the code {{ERP: design code}}", or "Design code DM karo". DEFAULT. |
| Hashtags | at most 5 per post. DEFAULT. The cap is not checked by us. |
| Who besides the owner can sign off | only the owner. Names are kept out of this repo. |

### Phases

| decision | until then |
| --- | --- |
| When to start phase 2, and how drafts should move into the queue | phase 1 carries on |
| Whether to start each phase 3 feature, and its scope and rules | nothing in phase 3 is built |
| Whether any reply, to a comment or a message, may ever go out without a person sending it | every reply is sent by a person |
| Which research sources and tools are approved | paste-in and a not-logged-in browser only |
