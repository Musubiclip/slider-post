# Musubi slider post

A Claude Code skill. Type a movie or series name and get a 6 slide Instagram carousel in the Musubi house style, plus the caption.

## Install

```bash
npx skills add Musubiclip/slider-post
```

## Use

```
/musubi-slider-post Peaky Blinders
```

The finished post lands in `~/Desktop/<series-name>-slider-post/`: `slide-1.png` to `slide-6.png` and `caption.txt`.

## Needs

- [uv](https://docs.astral.sh/uv/)
- Google Chrome or Microsoft Edge
- [Codex CLI](https://github.com/openai/codex), logged in, for the character art. Without it the skill hands you prompts to run in ChatGPT.
