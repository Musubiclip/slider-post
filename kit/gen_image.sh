#!/bin/bash
# Generate one image with Codex's built-in image generation.
# usage: gen_image.sh "<prompt>" <out.png> [reference images...]
set -euo pipefail
prompt="$1"; out="$2"; shift 2
dir="$(cd "$(dirname "$out")" && pwd)"; name="$(basename "$out")"
refs=(); for r in "$@"; do refs+=(-i "$r"); done
codex exec -C "$dir" --skip-git-repo-check -s workspace-write "${refs[@]}" -- \
  "Use your image generation tool to make exactly one image from the prompt below, using the attached image(s) as the art style reference. Do not write code or draw it yourself. Then copy the generated PNG into the current directory as $name and stop. Prompt: $prompt" </dev/null >"$dir/$name.log" 2>&1
[ -s "$out" ] || { tail -20 "$dir/$name.log"; exit 1; }
echo "$out"
