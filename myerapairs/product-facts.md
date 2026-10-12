# MYERAPAIRS product facts

The rule for every product fact that goes into a caption, reel, carousel,
story or DM draft. Read `rules.md` first.

A product post sells a real pair. A wrong price, a size that is not there or a
colour that does not match costs a customer's trust, and a posted mistake is
seen before it can be fixed. So product copy uses only facts the ERP holds and
the owner has verified, and nothing else.

## How the ERP fits in

The ERP is the business system that holds products, prices, sizes, colours,
stock and orders. It is the source of truth.

This skill pack has no connection to the ERP (status: not available). A person
looks the product up in the ERP and fills in the facts block below. The draft
is written from that block and nothing else.

Never take a product fact from memory, an old caption, a photo, a price tag in
a photo, a competitor's page or a customer's message.

## Allowed facts

| fact | from the ERP | how to write it | rules |
| --- | --- | --- | --- |
| Design code | the product's design or style code | exactly as the ERP shows it, same letters, numbers and hyphens | Every product post shows it, with "DM the code". |
| Product name | the product's name | as recorded | Do not add words the ERP does not have, like "premium" or "designer". |
| Price | the bill price, including GST | rupee sign and Indian commas, like ₹1,499 | Never MRP as the selling price. Never two prices side by side. |
| Colours | the colour names recorded | the ERP's colour name | The photo must show that colour. Do not invent colour names. |
| Available sizes | the sizes the ERP marks available | the ERP's size labels, in order | Sizes only, never counts. |
| Material | only if the ERP records it | the ERP's wording | If it is not recorded, leave it out. No claims built on it ("leather, so it lasts"). |
| Photos to use | owned shots of this exact design and colour | file names or a short description | Must match the design code and colour. See `rules.md`, section 9. |

Stock levels are never a public fact. "Available" is the only stock word that
goes in copy, and only for sizes the ERP marks available.

Sizes change. If the draft was written on an earlier day, check the sizes in
the ERP again on the day it is posted.

## The facts block

Fill this in from the ERP before drafting. One block per design code. Keep
filled blocks in `~/.claude/instagram/`, not in this repo.

```
FACTS BLOCK
design code:
product name:
bill price:       ₹          (bill price including GST, not MRP)
colours:
available sizes:
material:                    (only if the ERP records it, else "not recorded")
photos to use:               (owned shots of this exact design and colour)
checked on:                  (date and time the ERP was read)
checked by:                  (role: owner, manager, staff)
verified:         yes / no   (yes only when the owner has verified these facts)
```

- `verified: yes` means every field above was read from the ERP and the facts
  are owner-verified. Anything less is `no`.
- A blank field stays a placeholder in the draft. It is never filled with a
  guess.

## The NOT ERP-VERIFIED placeholder

When a fact is not in a verified facts block, the draft writes a placeholder
in its place:

```
{{ERP: design code}}   {{ERP: product name}}   {{ERP: price}}
{{ERP: colour}}        {{ERP: available sizes}} {{ERP: size}}
{{ERP: material}}
```

`{{ERP: price}}` is replaced with the full price, rupee sign included, like
₹1,499. If the ERP records no material, the material line comes out of the
draft altogether rather than staying as `{{ERP: material}}`.

The draft's receipt then starts with a label that names every missing field:

```
NOT ERP-VERIFIED: price, available sizes
```

A draft with that label, or with any `{{ERP: ...}}` left in it, cannot be
signed off or posted. A person fills the facts block, the draft is updated, and
the label comes off.

## Claims that are never allowed

| type | not this (English) | not this (Hinglish) | instead |
| --- | --- | --- | --- |
| Comfort | "All-day comfort", "so soft you forget you are wearing them" | "Ekdum comfortable, pura din pehno" | Show it worn in the video and let people judge. |
| Medical or health | "Good for back pain", "no more blisters", "orthopaedic" | "Pairon ke dard mein aaram" | Nothing. |
| Durability | "Lasts for years", "waterproof", "unbreakable" | "Saalon saal chalegi" | Nothing. |
| Fit | "Fits true to size", "perfect for wide feet" | "Har pair perfect fit" | The ERP's available sizes. Fit questions go to a human. |
| Scarcity or urgency | "Only 2 left!", "last few pairs", "hurry", "selling fast" | "Sirf 2 pair bache hain", "jaldi karo" | "Sizes {{ERP: available sizes}}." |
| Discount, offer or sale | "Flat 20% off", "sale", "best price", "MRP ₹X, now ₹Y" | "Offer chal raha hai", "sabse sasta" | The bill price only. DEFAULT until the owner decides. |
| Festival names | "Diwali collection", "Eid special" | "Navratri special design" | Nothing. DEFAULT until the owner decides. |
| Delivery time | "Delivered in 2 days", "same-day delivery" | "Kal tak mil jayega" | Nothing. Delivery questions go to a human. |
| Returns, exchanges, refunds | "Easy returns", "exchange anytime" | "Pasand na aaye toh wapas" | Nothing until the owner approves public terms. |
| Reviews or testimonials | "Customers love it", "5-star rated", a made-up quote | "Sab customers ko pasand aaya" | Only real ones, with the customer's consent and the owner's approval. |
| Superlatives | "Best footwear in Mandsaur", "No.1 shop" | "Mandsaur ki sabse best dukaan" | Nothing. |
| Stock location | "More stock at our godown", "coming from the warehouse" | "Godown mein hai" | Nothing. Never mention any godown or warehouse in public. |
| Material beyond the ERP | "Genuine leather" when the ERP says "leather" | "Pure leather" | The ERP's exact wording. |

## Check the shop before promising pickup

A size marked available in the facts block is not always at the shop.

- Before anyone tells a customer they can collect a pair, or come in and buy
  or try a size, a staff member checks that the shop has that design, colour
  and size.
- Until that check is done, a DM draft says the team will check before the
  customer visits. It never says the size is waiting at the shop.
- A post can invite people to the shop. It cannot promise a size will be
  there.
- If the size is not at the shop, hand it to a human. Do not promise when it
  will arrive, and do not say where else stock is kept.

## Before sign-off

Run this on every product draft before it goes to the owner or the named
manager.

```
[ ] Facts block filled from the ERP, verified: yes
[ ] Sizes checked again today if the draft is from an earlier day
[ ] No {{ERP: ...}} or {{OWNER: ...}} placeholders and no NOT ERP-VERIFIED label
[ ] Design code is shown, matches the ERP and matches the photos
[ ] Price is the bill price including GST, written like ₹1,499, not MRP
[ ] Sizes are only ERP-available sizes, with no counts
[ ] Material only if the ERP records it, in the ERP's words
[ ] Photos and video show this exact design and colour, owned or licensed,
    with no filter that changes the colour
[ ] No comfort, medical, durability, fit, scarcity, urgency, delivery,
    return or refund claims
[ ] No festival names and no sale, offer or discount wording (DEFAULT)
[ ] No godown or warehouse, stock location, stock counts, cost prices or
    suppliers
[ ] No reviews or testimonials unless real and approved
[ ] Call to action is "DM the code ..." or "Design code DM karo", with no
    "comment a keyword" ask
[ ] At most 5 hashtags (DEFAULT)
[ ] No customer names, handles or messages
[ ] Shop pickup is not promised unless staff checked the shop has the size
[ ] MYERAPAIRS spelled correctly
```

Then follow the sign-off steps in `rules.md`, section 2.
