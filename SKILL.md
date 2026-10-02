---
name: musubi-slider-post
description: Make a Musubi Instagram slider post (6 slide carousel) that teaches a business or marketing lesson through a movie or series, with the researched script, ChatGPT image prompts, the built 1080x1350 slides and an SEO caption in the Musubi house style. Use this whenever someone names a movie, series, show or anime and wants a slider post, carousel, Instagram post, "next series is X", or just types a title after invoking the skill, even if they never say "carousel".
---

# Musubi slider post

**What this makes:** a 6 slide Instagram carousel that teaches a business or marketing lesson through a movie or series, ending on a Musubi campaign CTA, plus the caption to post it with.

The user gives only a title ("Peaky Blinders"). Everything else is yours. If the title is already in the series log (section 6), say so and ask before repeating it.

`<skill dir>` below is this skill's base directory. There are two folders, and they are kept apart on purpose. The **work folder** is `~/MusubiSliderPosts/<series-name>/` (lowercase, hyphens): script, prompts, raw images, stickers, `index.html`, build files and exports all live there. The **delivery folder** is `~/Desktop/<series-name>-slider-post/`, for example `~/Desktop/gangs-of-wasseypur-slider-post/`. It holds only what gets posted: `slide-1.png` to `slide-6.png` and `caption.txt`, nothing else. Create it last, by copying those seven files out of the work folder once the slides pass QA, and copy again after any later fix. The user opens only the delivery folder, so never leave working files in it.

## The flow

One turn, from the title alone, without stopping to ask:

1. Research the show and write the 6 slide script and the 6 image prompts (section 3). Save to `script.txt` in the work folder.
2. Write the SEO caption (section 5). Save to `caption.txt`.
3. Generate the six images with Codex (section 3d). No pause for the user: Codex's image generation is the same model as ChatGPT's.
4. Cut the stickers, build the strip, export `slides/slide-1.png` to `slide-6.png`, look at the slides yourself against the QA list in 4c and fix what fails (section 4).
5. Copy the six slides and `caption.txt` into the delivery folder on the Desktop.
6. Reply with the delivery folder path, the six headlines, the caption, and anything in the FACTS section you could not confirm. Add the show's row to the series log in section 6 of this file.

If `codex` is not installed or not logged in, fall back to two turns: give the user the six prompts in copy ready code blocks to run in ChatGPT, and build the slides when they send the images back.

---

## 1. Musubi facts (use these, nothing else)

| Fact | Use |
|---|---|
| What Musubi is | India-only creator clipping platform: brands post a campaign, creators clip it into Reels and Shorts, and the brand **pays only per verified view** |
| Creators | **5,000+ creators** across India |
| Views delivered | **810.1K views delivered** |
| Website | **musubiclip.com** |

- Never use the old numbers (870 creators, 7.18 lakh views).
- Never invent stats, clients or results. If a lesson needs a number, it must come from the show, not from Musubi.

---

## 2. The one rule that makes these posts work

**The lessons come from what the character DOES on screen. Not from the show's real-world history.**

| Bad (the audience doesn't care) | Good (the post teaches something) |
|---|---|
| "Money Heist became Netflix's most-watched non-English show." | "The Professor recruited a crew and named them after cities, so get a creator in every city." |
| "Shinchan has been on air since 1992." | "Shinchan's butt dance grabs attention in 3 seconds, and that's your hook." |

Every lesson must map onto something Musubi actually does:

- **Many creators beat one ad** (crew, army, ravens, gang).
- **Go where your audience already is** (Reels and Shorts, every Indian city).
- **Real verified views, not fake reach** (quality, trust, getting caught).
- **Your best 30 seconds** (the scene or song or moment everyone replays).
- **A name or line people repeat** (brand identity, sigil, catchphrase).
- **Small budget, right crowd** (pay per view, no big production).

---

## 3. Round 1: research, script and prompts

### 3a. Research (always check facts)

- Search the web for the show's key scenes. Name the season and episode for every scene you use, and list sources at the bottom of the script.
- Find 4 scenes where a character does something smart or bold that maps to a Musubi lesson (section 2).
- Find the show's **signature device**, a visual object that can hold each lesson. Past examples:
  - Breaking Bad: periodic table tiles.
  - The Mentalist: case-file polaroids.
  - Game of Thrones: parchment scrolls with wax seals.
  - Money Heist: the Professor's chalkboard.
  - Better Call Saul: a yellow legal pad and "Exhibits".
- Find 2 **scroll-effect props**: big things that can cross from one slide into the next when you swipe. Past examples:
  - Breaking Bad: the RV.
  - The Mentalist: the car.
  - Game of Thrones: ravens and the dragon.
  - Money Heist: the airship and the masked crew.
  - Better Call Saul: the billboard and the yellow car.
- If a scene is dark (crime, violence), take the harmless idea from it and say so on the slide. Example: "Staged? Don't copy that part. Copy the idea."
- Avoid gore, drugs used as a joke, and real actors' names.

### 3b. The 6-slide structure (always the same)

| Slide | Job | Parts |
|---|---|---|
| 1 | **Hook** | Kicker line in the handwritten font (a pun on the show plus Musubi). Big headline with the key words in a green highlight box. 1 to 2 sentence sub. A small device card listing the 4 lessons. The main character sticker. |
| 2 | **Lesson 1** | Label chip ("EXHIBIT A", "PHASE 1", etc.). Headline. Body of 3 to 5 sentences: what the character does, then what it means for your brand. A device card. A character sticker. **Scroll prop 1 starts here.** |
| 3 | **Lesson 2** | Same parts. **Scroll prop 1 lands here.** |
| 4 | **Lesson 3** | Same parts. |
| 5 | **Lesson 4** | Same parts. **Scroll prop 2 starts here.** |
| 6 | **The ask** | Kicker (the show's catchphrase, twisted). Headline "Don't X. Call/Do Musubi." Body: put your best 30 seconds on Musubi, 5,000+ creators clip it on Reels and Shorts, your budget only pays out for verified views. The Musubi campaign card. musubiclip.com. **Scroll prop 2 lands next to the card.** |

**Writing rules:**
- Headlines: 4 to 8 words, all caps, and the punchline in the green highlight.
- Body: short sentences, simple English, and the last sentence is the lesson in **bold**.
- Lesson headlines are commands: "PICK A NAME PEOPLE CAN'T FORGET." / "GO WHERE YOUR PEOPLE ALREADY ARE."
- Hinglish kickers are welcome for Indian shows (Mirzapur used "bhaukaal").

### 3c. ChatGPT image prompts (6 images)

- 4 character images for slides 1, 2 (or 3), 4 and 5, plus 2 scroll-effect props.
- Tell the team to **attach one image from the last post** to every prompt so the art style matches.
- **Make the main character first**, then attach that image too so the face stays the same.
- **Never name the actors.** Describe hair, face, age, outfit and pose. Naming the character is fine.
- Ask for a **plain pure white background, no text, no ground shadow**. Text on props must be blank (blank billboard, blank card): Claude adds the text later so it stays sharp.
- Characters: **portrait 2:3**, full body. Scroll props: **landscape 16:9**, seen from the side, moving toward the right.

**Character prompt template:**
```
Use the exact same art style as the attached image. Full-body caricature illustration of <age, build, hair, face, expression>. He/She wears <exact outfit, colours, shoes, accessories>. <One clear pose with a prop>. Thick black outlines, soft cel shading, detailed premium caricature illustration. Plain pure white background, no text, no ground shadow. Portrait 2:3.
```

**Scroll prop template:**
```
Use the exact same art style as the attached images. <The object> seen exactly from the side, moving toward the right, <details, who is in it, what it carries>. <Any sign or card must be completely blank>. Thick black outlines, soft cel shading, detailed premium illustration. Plain pure white background, no text, no ground shadow. Landscape 16:9.
```

- If ChatGPT refuses, resend the same prompt.
- End the script file with a "FACTS" section: every show fact with its episode, the sources, and the Musubi facts used.

---

### 3d. Generate the images with Codex

```bash
<skill dir>/kit/gen_image.sh "<prompt>" <work folder>/raw/1-main.png <skill dir>/kit/style-ref.png
```

It runs `codex exec` with its built in image generation, attaches the reference images, and saves one PNG (about a minute each). `kit/style-ref.png` is the house style reference, so every prompt gets it.

- Make the main character first and look at it. Then run the other five in parallel (background `&` then `wait`), each with `style-ref.png` and the main character attached so the style and faces stay consistent.
- Look at every image before cutting. Regenerate one that has text on it, a coloured background, a cropped figure, or a prop facing left.
- If a run fails, the reason is in `<out>.log` next to the image.

---

## 4. Round 2: build the slides

### 4a. The house style (don't change it)

| Token | Value |
|---|---|
| Canvas | 6 slides of **1080x1350**, built as one continuous strip **6480x1350**, then sliced |
| Background | White `#ffffff` with a light blue grid (135px squares, `rgba(67,136,255,.13)`) |
| Road | Green `#00e751` band from **y=1172** to the bottom, 7px black top border, dashed centre line. It runs through all 6 slides. |
| Ink | `#111111` |
| Musubi blue | `#4388ff` (shapes only; for blue text use `#2563d6`) |
| Musubi green | `#00e751` |
| Accent | One colour from the show: Money Heist red `#d81f26`, Better Call Saul mustard `#f5b700`, etc. Used for the label chip and small marks. |
| Headline font | **Anton**, line-height .98, 6px blue text-shadow. Key words go in `<mark>`: green box, 5px ink border, hard 6px shadow, rotated -1.5deg. |
| Body font | **Space Grotesk** 500/700, 27 to 33px |
| Handwritten | **Permanent Marker** (kickers, device cards) |
| Logo | White pill top-left at (60,44): Musubi knot and "Musubi" in Inter 900. Page number "01/06" top-right. |
| Swipe pill | Black pill "SWIPE →" bottom-right on slides 1 to 5 |
| Characters | Stickers with a thick white rim and soft shadow, feet standing on the road (bottom around y=1190). Usually a blue circle "spot" with an ink border sits behind them. |
| Ghost letter | Big outlined letter or number top-right on lesson slides (A/B/C/D or 01..04) |
| CTA card | White rounded card: Musubi header, "Your best 30 seconds", "Budget pays out for / Verified views", "Your crowd / 5,000+ creators", green "Launch campaign →" button. musubiclip.com bottom-left on slide 6, as text only with no logo beside it. |

**Layout grid, per slide (x relative to the slide's left edge):**

| Element | Position |
|---|---|
| Kicker or label chip | x=72, y≈150 |
| Headline | x=72, y≈226, width 940, 96 to 112px |
| Body | x=72, y≈470 to 500, width 936 (or 420 to 480 when a character stands on the right) |
| Device card | lower left or lower right, y≈740 to 1080 |
| Character | opposite side from the device card, 470 to 860px tall |

**Scroll effect:** place the prop so its centre sits on a slide seam (x = 1080 × k). Half is on each slide, so it "drives" across when you swipe. Give it a higher z-index than the device cards.

### 4b. Files in the kit

```
<skill dir>/kit/
  gen_image.sh         prompt + reference images -> one PNG, via Codex image generation
  example-build.py     a working build.py (Gangs of Wasseypur) to copy into the work folder
  style-ref.png        house style reference to attach to every prompt
  cut_sticker.py       generated image -> sticker PNG (white rim + shadow)
  render_slides.py     index.html -> slide-1.png ... slide-6.png
  example/             the finished Better Call Saul post, as the working template
    index.html         all 6 slides in one strip; copy this and edit it
    assets/fonts/      Anton, Space Grotesk, Permanent Marker, Inter
    assets/cut/        the Saul stickers (replace with the new show's)
    assets/vendor/     gsap (only used by the HyperFrames preview; export doesn't need it)
```

### 4c. Steps

1. Copy `<skill dir>/kit/example/.` into the work folder, then delete the Saul stickers from `assets/cut/` once you have replaced them.
2. Cut each ChatGPT image into a sticker:
   ```bash
   uv run --with pillow --with numpy <skill dir>/kit/cut_sticker.py image1.png <work folder>/assets/cut/tommy.png
   ```
   Add `--loose` when a white object (a sign, a card) touches the image edge.

   Check each sticker on a coloured background. If a white area near the edge got eaten (like a blank billboard running off the top of the image), rebuild it: pad the image, fill the missing panel, redraw its frame line, then cut.
3. Build `index.html`. Do not hand edit 180 lines of absolute positions: write a short `build.py` in the work folder that takes the kit's example strip, keeps the CSS, header, card and url blocks, and emits the elements per slide from a list, so a layout fix is a one line change and a rerun. `<skill dir>/kit/example-build.py` is a working one (the Gangs of Wasseypur post) to copy and edit. Every element inside `<div id="strip">` is absolutely positioned on the 6480px strip, so slide N starts at x = 1080 × (N−1). Replace the text, the device cards and the `<img class="art">` stickers. Keep the header, road, grid, swipe pills and CTA card.
4. Export:
   ```bash
   uv run --with pillow <skill dir>/kit/render_slides.py <work folder>/index.html <work folder>/slides
   ```
   It needs Chrome or Edge. If `uv` is missing, `brew install uv` (ask first).
5. **QA each slide before sending.** Paste slides 1 to 3 and 4 to 6 into two contact sheets and Read those, which is cheaper than six full reads; open a single slide only when something looks off. An all white export means the HTML is broken, not the renderer.
   - No text overlaps a sticker, and nothing is cut at the slide edge except the scroll props.
   - Headlines are at most 3 lines, and lists on device cards don't wrap awkwardly.
   - The scroll props line up across the seams (slide 2 right edge meets slide 3 left edge).
   - Every number matches the FACTS section. The Musubi numbers are exactly 5,000+ and verified views.
   - Text you add onto props (card names, signs) sits inside the prop.

---

## 5. SEO caption (written in turn 1)

Write it for Instagram, **with no dashes of any kind** (no hyphens used as dashes, no en or em dashes):

1. A first line that hooks, using the show name and the lesson ("Saul Goodman never had an ad budget. He had something better.").
2. 3 to 5 short lines, one per lesson.
3. The CTA: "Put your best 30 seconds on Musubi. 5,000+ creators across India. You only pay for verified views. musubiclip.com".
4. "Save this for your next launch" plus a follow line with your Instagram handle.
5. 15 to 25 hashtags mixing the show (#BetterCallSaul #SaulGoodman), marketing (#MarketingTips #BrandBuilding #ContentMarketing #D2CIndia) and creators (#CreatorEconomy #UGC #InstagramReels #IndianCreators).

---

## 6. Series log (don't repeat, keep the style consistent; add a row after every finished post)

| Show | Idea | Device | Scroll effects |
|---|---|---|---|
| Breaking Bad | What Walter White can teach your business | Periodic table tiles | RV |
| Mirzapur | "Bhaukaal": Hinglish hooks for an Indian audience | (see the posted slides) | continuous road |
| Shinchan (script only) | "Shinchan Sir ki marketing class" | Crayon scribbles | crayon line |
| The Mentalist | He never read minds. He read people. | CBI case-file polaroids | car 5→6 |
| Game of Thrones | The Iron Throne wasn't won by the biggest army | Parchment and wax seals | ravens 4→5, dragon 5→6 |
| Money Heist | The real heist was attention | Professor's chalkboard, 4 phases | airship 3→4, masked crew 5→6 |
| Better Call Saul | He couldn't afford ads. So he became the story. | Yellow legal pad, 4 exhibits | billboard 2→3, yellow car 5→6 |
| Gangs of Wasseypur | Revenge took 3 generations. You get 30 seconds. | "Now Showing" cinema board and ticket stubs, 4 reels | coal train 2→3, scooter 5→6 |

Ideas not done yet: Peaky Blinders, Sacred Games, Scam 1992, Panchayat, Suits, The Office, Shark Tank India, Kota Factory, 3 Idiots.

---

## 7. Worked example: Better Call Saul (the script, condensed)

- **Slide 1:**
  - Kicker "Better Call Musubi".
  - Headline "HE COULDN'T AFFORD ADS. SO HE BECAME **THE STORY.**"
  - Sub: "The best marketer on TV wasn't in advertising. He was a lawyer with an office in a nail salon."
  - Device: "The Case File" legal pad listing A to D.
- **Slide 2, Exhibit A:** "PICK A NAME PEOPLE **CAN'T FORGET.**" Jimmy McGill becomes Saul Goodman, which sounds like "S'all good, man." Saul holds a card; I lettered it "SAUL GOODMAN". The billboard starts here.
- **Slide 3, Exhibit B:** "DON'T BUY THE AD. **BE THE NEWS.**"
  - The staged billboard rescue (S1E4 "Hero").
  - Front page prop: "LOCAL LAWYER SAVES WORKER".
  - Note: "Staged? Don't copy that part."
- **Slide 4, Exhibit C:** "GO WHERE YOUR PEOPLE **ALREADY ARE.**" Bingo at the retirement home, plus gelatin cups printed "Need a Will, Call McGill!" (S1E5).
- **Slide 5, Exhibit D:** "SMALL BUDGET. **RIGHT CROWD.**" A homemade TV ad aired in one small market, and 100+ clients in a day (S2E3 "Amarillo"). The yellow car starts here.
- **Slide 6:**
  - Kicker "S'all good, man."
  - Headline "DON'T CALL SAUL. **CALL MUSUBI.**"
  - CTA card and musubiclip.com.
  - The yellow car parks beside the card.
