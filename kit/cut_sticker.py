"""Turn a ChatGPT character image (plain white background) into a Musubi sticker:
background removed, thick white rim, soft drop shadow. Output is a transparent PNG.

usage:  python cut_sticker.py input.png output.png [--loose]
        --loose  use when a white object touches the image edge (a white sign, a white car)
needs:  Pillow (pip install pillow) and numpy
"""
import sys
import numpy as np
from PIL import Image, ImageFilter

src, dst = sys.argv[1], sys.argv[2]
sat_max, val_min = (10, 240) if "--loose" in sys.argv else (14, 236)
RIM = 16

im = Image.open(src).convert("RGB"); rgb = np.asarray(im).astype(np.int16)
# background = near-white pixels connected to the image border (so white shirts inside the figure survive)
cand = ((rgb.max(2) - rgb.min(2)) <= sat_max) & (rgb.min(2) >= val_min)
bg = np.zeros_like(cand); bg[0] = cand[0]; bg[-1] = cand[-1]; bg[:, 0] = cand[:, 0]; bg[:, -1] = cand[:, -1]
while True:
    g = bg.copy(); g[1:] |= bg[:-1]; g[:-1] |= bg[1:]; g[:, 1:] |= bg[:, :-1]; g[:, :-1] |= bg[:, 1:]; g &= cand
    if (g == bg).all(): break
    bg = g

alpha = Image.fromarray(((~bg) * 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(0.8))
cut = im.convert("RGBA"); cut.putalpha(alpha)
rim = alpha.filter(ImageFilter.GaussianBlur(RIM * 0.55)).point(lambda v: 255 if v > 18 else 0).filter(ImageFilter.GaussianBlur(1.2))
pad = RIM * 3; W, H = im.size
can = Image.new("RGBA", (W + 2 * pad, H + 2 * pad), (0, 0, 0, 0))
sa = Image.new("L", can.size, 0); sa.paste(rim, (pad, pad + 14))
shadow = Image.new("RGBA", can.size, (0, 0, 0, 0)); shadow.putalpha(sa.filter(ImageFilter.GaussianBlur(16)).point(lambda v: int(v * .30)))
can.alpha_composite(shadow)
white = Image.new("RGBA", im.size, (255, 255, 255, 255)); white.putalpha(rim); can.alpha_composite(white, (pad, pad))
can.alpha_composite(cut, (pad, pad))
can = can.crop(can.getbbox()); can.save(dst)
print(dst, can.size, "background removed: %.0f%%" % (bg.mean() * 100))
