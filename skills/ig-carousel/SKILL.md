---
name: ig-carousel
description: >-
  Build an Instagram carousel - the cover that earns the swipe, slide-by-slide
  copy, and the 1080x1350 files to upload. Use when the user says "carousel",
  "slides", "swipe post", "turn this into a carousel", or has a list-shaped or
  step-shaped idea that would die as a single image.
---

# ig-carousel

Carousels are the highest-dwell format on the grid, because a swipe is an
interaction and a scroll is not. They also get a second chance: Instagram can
show a carousel again starting from a later slide to someone who did not engage
the first time, so slide two has to stand on its own as well.

The format rewards one idea broken into steps. It punishes a caption cut into
pieces.

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

- **Only real photos.** Every product image is a real photo of the actual pair,
  from the ERP or from the owner. No generated images, stock photos or
  competitor media. Keep the real design, colours and details, and no filter
  that changes a colour.
- **Fact-check every slide against the facts block.** Price (the bill price
  including GST, written like `₹1,499`), available sizes (never counts),
  colours, and material only if the ERP records it. No comfort or fit claims,
  scarcity, festival names or offer wording. A missing fact is written
  `{{ERP: field}}` and the carousel is labelled NOT ERP-VERIFIED.
- **The design code is on every product slide**, and the CTA slide is
  "DM the code {{ERP: design code}}" (Hinglish: "Design code DM karo").
- **Brand colours come from `voice.md`.** While it still has a placeholder for
  them, follow its "Until then" note and ask the owner. Do not invent a
  palette.
- **Rendering the files is optional.** The copy and the photo order are the
  deliverable. Rendering 1080x1350 files needs a headless browser, and only one
  the owner has approved. Without it, hand over the copy and the photos for
  whoever designs the slides.
- **Posted by hand.** Nothing is uploaded. A person posts it after the owner,
  or a manager he names, signs off.
- Carousel-shaped footwear posts: colour options, occasion styling, size and
  fit help (available sizes only, fit questions go to a person), a customer
  question answered.

Where this section conflicts with the upstream text below, this section wins.

## When to use it instead of a Reel

Use a carousel when the idea has **sequence and needs to be re-read**: steps, a
framework with parts, a before and after, a list worth screenshotting. Use a
Reel when the idea has motion, a face, or a payoff that has to be seen
happening.

If the idea is one claim, it is neither. Hand it to `/ig-reel` and say so.

## Structure

6 to 10 slides. The cap is 20 and 20 is almost always a book nobody finishes.
Under 5 and the swipe never starts.

```
1         COVER     the hook. 6 words or fewer, at a size that is legible in
                    the grid at thumbnail. One line of promise under it.
2         THE STAKE why this matters, in one sentence. This slide is also a
                    second cover, so it cannot be setup.
3 to N    ONE IDEA PER SLIDE. A headline of 3 to 7 words, at most 25 words
                    under it. If a slide needs a paragraph, it is two slides.
N+1       RECAP     the whole thing as a list. This is the screenshot slide.
LAST      CTA       one action: DM the code {{ERP: design code}}. One.
```

## Slide copy rules

- **The cover is 80% of the result.** Six words. Big. Nothing on the deck saves
  a cover nobody swipes.
- **Design for the grid crop.** The profile grid crops to a portrait rectangle
  that is taller than it is wide, and the exact ratio has moved more than once.
  Build at 1080x1350 and keep the cover text well inside the middle, clear of
  the outer 120 pixels on every side, and the crop stops mattering.
- **Number the slides** (3/8). Completion goes up when people can see the end.
- **No slide is a paragraph.** If it cannot be said in 25 words, split it.
- **The recap slide is the one people screenshot and send.** Sends are the
  strongest signal you can earn. Make it standalone and readable with no
  context.
- **The handle on every slide**, small, bottom corner. Screenshots travel
  without you.
- **Alt text on the cover at minimum.** It is read by screen readers and by
  Instagram.

## Building the files

Optional, and only with a headless browser the owner has approved. Instagram
wants 1080x1350 (4:5), JPEG or PNG, up to 20 items. Build it as HTML and print
each slide:

```bash
# one <section> per slide, 1080x1350, page-break-after: always
# then Chrome headless --print-to-pdf, or any HTML-to-image you already use
```

Write the HTML with `width:1080px; height:1350px`, a single accent colour from
`../../myerapairs/voice.md`, and type no smaller than 32px, because this is
read on a phone at a third of its real size. Do not invent a palette.

## Output

The slide-by-slide copy first, as a numbered list the user can read in ten
seconds and edit before anything is rendered. Then the **caption**, which for a
carousel is Job B in `/ig-caption`: the caption is doing work here, because the
cover has already used its six words.

Run both through `/ig-human`. Build the files only after the user approves the
copy.

```
CAROUSEL  ·  6 slides  ·  code {{ERP: design code}} on every product slide

1  COVER   ONE PAIR, TWO LOOKS
           How to wear this pair all week.         [owner photo]
2  STAKE   Kurta on Monday, jeans on Saturday.     [owner photo]
3          WITH A KURTA                            [owner photo]
4          WITH JEANS                              [owner photo]
5  RECAP   Colours: {{ERP: colour}}
           Sizes: {{ERP: available sizes}}
           Price: {{ERP: price}}
6  CTA     DM the code {{ERP: design code}}.

Caption: Job B, hook in line 1, one ask, 3 tags.
NOT ERP-VERIFIED: design code, colour, available sizes, price
sign-off: needed
```

Nothing is uploaded. A person posts it by hand after the owner signs off.
