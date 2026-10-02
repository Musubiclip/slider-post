"""Export a Musubi slider post: screenshot the 6480x1350 strip in headless Chrome/Edge and slice it into six 1080x1350 PNGs.

usage:  python render_slides.py path/to/index.html  [out_dir]
needs:  Pillow (pip install pillow) and Google Chrome or Microsoft Edge
"""
import os, sys, shutil, subprocess, tempfile
from PIL import Image

W, H, N = 1080, 1350, 6
page = os.path.abspath(sys.argv[1])
out = os.path.abspath(sys.argv[2] if len(sys.argv) > 2 else os.path.join(os.path.dirname(page), "slides"))
os.makedirs(out, exist_ok=True)

BROWSERS = [r"C:\Program Files\Google\Chrome\Application\chrome.exe",
            r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
            r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
            "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
            shutil.which("google-chrome") or "", shutil.which("chromium") or ""]
browser = next((b for b in BROWSERS if b and os.path.exists(b)), None)
if not browser: sys.exit("Chrome or Edge not found. Edit BROWSERS in render_slides.py.")

# show the whole strip at once: widen the frame from one slide to all six
html = open(page, encoding="utf-8").read()
wide = "<style>html,body,#root{width:%dpx!important;height:%dpx!important}</style></head>" % (W * N, H)
tmp = os.path.join(os.path.dirname(page), "_strip_export.html")
open(tmp, "w", encoding="utf-8").write(html.replace("</head>", wide, 1))
shot = os.path.join(tempfile.gettempdir(), "musubi_strip.png")
try:
    subprocess.run([browser, "--headless=new", "--disable-gpu", "--hide-scrollbars", "--force-device-scale-factor=1",
                    "--allow-file-access-from-files", "--virtual-time-budget=4000", "--default-background-color=ffffffff",
                    "--window-size=%d,%d" % (W * N, H), "--screenshot=" + shot, "file:///" + tmp.replace("\\", "/")],
                   check=True, capture_output=True, timeout=120)
finally:
    os.remove(tmp)
strip = Image.open(shot).convert("RGB")
for i in range(N):
    strip.crop((i * W, 0, (i + 1) * W, H)).save(os.path.join(out, "slide-%d.png" % (i + 1)))
print("saved 6 slides to", out)
