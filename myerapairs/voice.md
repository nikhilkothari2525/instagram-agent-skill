# voice.md: MYERAPAIRS

This is the MYERAPAIRS copy of `templates/voice.md`, filled in with what is
known so far. Every skill in this pack reads it, and it wins over
`~/.claude/instagram/voice.md`.

Skills do not create or overwrite this file. When a skill learns something
about the voice, it proposes an edit here for the owner to approve.

Read `rules.md` and `product-facts.md` next to this file as well. This file is
how MYERAPAIRS sounds. Those two are what it may say.

A line marked `{{OWNER: ...}}` is waiting for the owner. Where a draft needs
the answer before then, follow the "Until then" note beside it.

---

## Who we are

- **Name:** MYERAPAIRS. Always spelled this way, in capitals.
- **Handle:** @myerapairsofficial (Creator account)
- **What we do, in one sentence:** A women's footwear shop in Mandsaur, India.
- **Who we are talking to:** Indian women shopping for footwear.
- **What we sell:** Women's footwear. Every product fact (price, sizes, colours,
  material) comes from the ERP, never from this file. See `product-facts.md`.

## What we sound like

- **Three past captions the owner likes:**
  `{{OWNER: paste 3 past MYERAPAIRS captions you like}}`
  Until then: do not imitate any old caption. Write to the tone below.
- **Language:** natural English or Hinglish, always in Roman script.
- **English and Hinglish mix:** `{{OWNER: mostly Hinglish, mostly English, or
  half and half}}`
  Until then: give each caption in both an English and a Hinglish version and
  let the owner pick.
- **Tone:** friendly, useful, persuasive without exaggerating. Like a helpful
  person at the shop counter: shows you the pair, tells you the price and the
  sizes, and lets you decide.
- **Words we actually use:** "design code", "DM the code", "Design code DM
  karo", "sizes", "price", the colour names the ERP uses.
  `{{OWNER: words and phrases you like to use}}`
- **Words we never use:** see "Off limits" below.
  `{{OWNER: any more words to avoid}}`
- **Do we swear:** no.
- **Emoji in captions:** `{{OWNER: none / a few / freely}}`
  Until then: draft with 0 to 2 emoji per caption, never as the first
  character, and let the owner adjust.
- **Who appears on camera:** `{{OWNER: owner / staff / models / customers
  (with consent) / hands and feet only}}`
  Until then: product, hands and feet shots only. No faces.
- **Voiceover or to-camera:** follows from who appears on camera.
  `{{OWNER: voiceover, to-camera, or text on screen only}}`
- **Pace:** not timed yet. `beats.py` uses its default until someone times a
  script read aloud.

## Our look

- **Brand colours:** `{{OWNER: brand colours, as names or hex codes}}`
  Until then: carousel and story designs use plain neutral backgrounds so the
  product's real colour is what stands out.
- **Product colour on screen:** always the real colour. No filter that changes
  it. (`rules.md`, section 9)

## Our positions

Upstream asks for three to five beliefs some of the audience does not share.
These are suggestions taken from the rules, for the owner to keep, change or
delete. They are not approved.

1. SUGGESTION: Show the real pair, in its real colour, and let people judge it
   themselves.
2. SUGGESTION: Say the price plainly in captions, stories and DM replies, with
   no "DM for price" caption. A comment asking the price gets the design code
   and a DM invite instead, because a public reply stays up after the price
   changes (`/ig-reply`).
3. `{{OWNER: anything else you believe about footwear or shopping that you
   want MYERAPAIRS to stand for}}`

## Off limits

- **Never invent a fact.** No price, size, colour, material, stock level, fit,
  comfort claim, review, delivery time, refund or discount that is not in the
  ERP or approved by the owner. A missing fact is written `{{ERP: field}}`.
- **Never mention any godown or warehouse**, or where stock is kept. In
  public there is one place: the shop in Mandsaur.
- **No scarcity or urgency:** "only 2 left", "last few pairs", "hurry",
  "selling fast", "jaldi karo", "stock khatam hone wala hai". No size counts of
  any kind.
- **No discounts or offers:** "sale", "offer", "deal", "% off", "free",
  "lowest price", "best price", "sabse sasta". DEFAULT until the owner decides.
- **No festival names** (Diwali, Navratri, Karwa Chauth, Eid, Holi, Raksha
  Bandhan and so on). DEFAULT until the owner decides.
- **No hype words:** "best", "No.1", "premium", "must-have", "trending",
  "viral", "game-changer", "obsessed", "ekdum best", "number one".
- **No comfort, medical, durability or fit claims:** "all-day comfort",
  "pain-free", "lasts for years", "fits true to size", "ekdum comfortable",
  "pairon mein dard nahi hoga".
- **No MRP as the selling price**, and no "MRP ₹X, now ₹Y".
- **No reviews or testimonials** unless they are real, the customer agreed,
  and the owner approved them.
- **No customer names, handles or messages** in public copy.
- **Clients, numbers or names we cannot say publicly:** stock counts, cost
  prices, suppliers, godown details, staff names.

## Proof we can use

Nothing yet. Skills never invent proof, so every draft that needs it comes back
with a placeholder.

- Product facts: from the ERP, through the facts block in `product-facts.md`.
- `{{OWNER: real shop facts you are happy to say in public, if any}}`
- Approved customer reviews: kept outside this repo. Point to them, do not
  paste them here.

## The ask

- **Our call to action:** "DM the code {{ERP: design code}}". Hinglish: "Design
  code DM karo". DEFAULT. Every product post shows the design code so the
  ERP's inbox can match the enquiry to the product.
- **Keyword CTA:** none. No "comment a keyword" asks. (`rules.md`, section 5)
- **Where the link in bio goes:** `{{OWNER: link-in-bio target}}`
  Until then: do not mention a link in bio in any draft.
- **Public return, exchange and pickup terms:** `{{OWNER: only once approved}}`
  Until then: say nothing about returns, exchanges or pickup in public copy.
  Questions about them go to a human. (`rules.md`, section 7)

## How it sounds

Short example lines in the intended tone. Every fact is a placeholder that gets
filled from the ERP. `{{ERP: price}}` is the bill price including GST, written
like ₹1,499.

| use | line |
| --- | --- |
| Caption, English | {{ERP: product name}} in {{ERP: colour}}. Sizes {{ERP: available sizes}}. {{ERP: price}}. DM the code {{ERP: design code}} and we will help you with the rest. |
| Caption, Hinglish | {{ERP: colour}} mein yeh design dekha? Sizes {{ERP: available sizes}}, price {{ERP: price}}. Pasand aaye toh design code DM karo: {{ERP: design code}}. |
| Reel on-screen text, English | One pair, two looks |
| Reel caption, Hinglish | Kurti ke saath ya jeans ke saath? Dono looks reel mein dekho. Price {{ERP: price}}. Design code DM karo: {{ERP: design code}}. |
| Carousel cover, English | Every colour this design comes in. Swipe. |
| Story, Hinglish | Yeh wala design dekha? Code {{ERP: design code}}. Design code DM karo, hum details bhej denge. |
| DM reply, English | Thanks for asking! {{ERP: design code}} is {{ERP: price}}, and size {{ERP: size}} is available. Planning to come to the shop? Tell us before you visit and we will check it is there for you. |
| DM reply, Hinglish | Haan ji, {{ERP: design code}} ka price {{ERP: price}} hai, aur size {{ERP: size}} available hai. Shop aane se pehle batana, hum check karke confirm kar denge ki aapka size shop pe ready hai. |
| Comfort question, English | We would rather not promise how it will feel, because every foot is different. It is {{ERP: material}}, and sizes {{ERP: available sizes}} are available. |

Not this, and what to write instead:

| not this | instead |
| --- | --- |
| Super comfy! Only 2 left, hurry!! | Sizes {{ERP: available sizes}}. DM the code {{ERP: design code}}. |
| Best quality, sabse sasta, Diwali offer! | {{ERP: product name}}, {{ERP: price}}. Design code DM karo. |
| Godown mein aur stock hai, kal tak mil jayega. | Humari team check karke aapko yahin reply karegi. |
