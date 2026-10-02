"""Builds index.html for this post from the kit's example strip. Run from this folder: python3 build.py <skill kit dir>"""
import re, sys, os

t = open(os.path.join(sys.argv[1], "example", "index.html"), encoding="utf-8").read()
css = '''
  .ph { background:#f26a1b; color:#fff; }
  .chalk { border-color:#f26a1b; background:#161616; }
  .tix { background:#ffe9c7; border:5px solid #111111; border-left:6px dashed #111111; padding:18px 26px 20px; box-shadow:8px 8px 0 #111111; font:400 34px/1.2 Marker; z-index:7; }
  .tix small { display:block; font:700 18px/1 SG; letter-spacing:.18em; color:#f26a1b; margin-bottom:10px; }
  .tix s { text-decoration-color:#d81f26; text-decoration-thickness:6px; }
  .tix em { display:block; font:500 24px/1.3 SG; font-style:normal; margin-top:10px; }
</style>'''
t = t.replace("</style>", css, 1).replace("Better Call Saul x Musubi", "Gangs of Wasseypur x Musubi")
a = t.index('      <div class="hd" style="left:60px">')
b = t.index('    </div>\n  </section>')
old = t[a:b]
hd0 = re.search(r'      <div class="hd" style="left:60px">.*?</div>\n', old, re.S).group(0)
card = re.search(r'      <div class="card".*?Launch campaign &rarr;</div></div>\n', old, re.S).group(0)
url = re.search(r'      <div class="url".*?</div>\n', old, re.S).group(0)


def hd(i):
    o = 1080 * i
    s = hd0.replace("left:60px", f"left:{o+60}px").replace("kh0-", f"kh{i}-")
    s += f'      <div class="pg" style="left:{o+860}px">0{i+1}<span>/06</span></div>\n'
    if i < 5:
        s += f'      <div class="sw" style="left:{o+790}px">SWIPE &rarr;</div>\n'
    return s


def el(i, cls, x, y, inner, style=""):
    return f'      <div class="{cls}" style="left:{1080*i+x}px;top:{y}px;{style}">{inner}</div>\n'


def img(i, name, x, y, w, h, z=3):
    return f'      <img class="art" src="assets/cut/{name}.png" alt="" style="left:{1080*i+x}px;top:{y}px;width:{w}px;height:{h}px;z-index:{z}">\n'


def h1(i, y, size, html, w=940):
    return f'      <h1 style="left:{1080*i+72}px;top:{y}px;width:{w}px;font-size:{size}px">{html}</h1>\n'


def lesson(i, n):
    return el(i, "ph", 72, 150, f"REEL {n}") + f'      <div class="ghost" style="left:{1080*i+560}px">0{n}</div>\n'


o = ""
# slide 1
o += hd(0)
o += el(0, "say", 72, 160, "Gangs of Musubi", "font-size:54px")
o += h1(0, 246, 90, "REVENGE TOOK 3 GENERATIONS. YOU GET <mark>30 SECONDS.</mark>", 600)
o += el(0, "body", 72, 668, "Wasseypur is a three generation grudge. It is also the best marketing class Dhanbad ever gave. <b>4 reels from Wasseypur for your brand.</b>", "width:440px;font-size:28px")
o += el(0, "chalk", 72, 876, '<div class="ct" style="font-size:38px;white-space:nowrap">NOW SHOWING</div><div class="cl"><i>1</i>Don&rsquo;t fake it</div><div class="cl"><i>2</i>One line</div><div class="cl"><i>3</i>Be on screen</div><div class="cl"><i>4</i>Build a gang</div>', "width:430px;transform:rotate(-2deg);padding:18px 26px 16px")
o += el(0, "spot", 560, 500, "", "width:500px;height:500px")
o += img(0, "faizal", 640, 330, 370, 861)
# slide 2
o += hd(1) + lesson(1, 1)
o += h1(1, 226, 108, "DON&rsquo;T FAKE IT. <mark>GET VERIFIED.</mark>")
o += el(1, "body", 72, 486, "Shahid Khan robs British trains by pretending to be Sultana Daku, a bandit everyone already fears. It works for a while. Then the people who own that name find out, and he is thrown out of Wasseypur. <b>Fake reach gets caught. Pay only for views that are real.</b>", "width:936px;font-size:29px")
o += el(1, "tix", 72, 760, '<small>NAME ON THE TICKET</small><s>SULTANA DAKU</s><em>Robbery? Don&rsquo;t copy that part. Copy the lesson.</em>', "width:440px;transform:rotate(-2deg)")
o += img(1, "train", 530, 767, 1100, 433, 5)
# slide 3
o += hd(2) + lesson(2, 2)
o += h1(2, 226, 104, "SAY IT ONCE. MAKE THEM <mark>REPEAT IT.</mark>")
o += el(2, "body", 72, 470, "Sardar Khan shaves his head and swears he will not grow his hair back until his father is avenged. Then he says it in three words. Now all of Wasseypur knows what he stands for. <b>Give people one line they can repeat for you.</b>", "width:620px;font-size:28px")
o += el(2, "tix", 90, 690, '<small>ADMIT ONE</small>&ldquo;Keh ke lunga.&rdquo;', "width:400px;transform:rotate(3deg);font-size:48px")
o += el(2, "spot", 690, 640, "", "width:380px;height:380px")
o += img(2, "sardar", 690, 560, 334, 630)
# slide 4
o += hd(3) + lesson(3, 3)
o += h1(3, 226, 96, "GO WHERE EVERYONE IS <mark>ALREADY WATCHING.</mark>")
o += el(3, "body", 410, 466, "Ramadhir Singh outlives every rival, and he says why: he is the only one who does not watch films. Everyone around him copies the screen. As long as India has cinema, he says, people will follow it. Today that screen is Reels and Shorts. <b>Put your brand where India is already looking.</b>", "width:600px;font-size:28px")
o += el(3, "chalk", 430, 890, '<div class="ct">NOW SHOWING</div><div class="cl">Your brand.</div><div class="cf">Reels and Shorts, every city.</div>', "width:560px;transform:rotate(2deg)")
o += el(3, "spot", 40, 720, "", "width:360px;height:360px")
o += img(3, "ramadhir", 70, 500, 292, 690)
# slide 5
o += hd(4) + lesson(4, 4)
o += h1(4, 226, 104, "ONE HERO CAN&rsquo;T DO IT. <mark>BUILD A GANG.</mark>")
o += el(4, "body", 72, 480, "Faizal Khan does not run Wasseypur alone. He has Definite, Perpendicular and Tangent. Young, local, and names nobody forgets. Each one covers a street he can&rsquo;t. <b>One big ad is one man. 5,000+ creators is a gang.</b>", "width:936px;font-size:29px")
o += el(4, "spot", 60, 790, "", "width:340px;height:340px")
o += img(4, "gang", 50, 700, 341, 490)
for k, (n, y, r) in enumerate([("DEFINITE", 700, -3), ("PERPENDICULAR", 800, 2), ("TANGENT", 900, -2)]):
    o += el(4, "tix", 430, y, f'<small>GANG MEMBER 0{k+1}</small>{n}', f"width:330px;transform:rotate({r}deg);font-size:30px;padding:12px 20px 14px;z-index:4")
o += img(4, "scooter", 770, 723, 620, 477, 6)
# slide 6
o += hd(5)
o += el(5, "say", 72, 150, "Baap ka, dada ka, sabka view lega tera Musubi.", "font-size:38px;width:960px")
o += h1(5, 236, 96, "DON&rsquo;T WAIT THREE GENERATIONS. <mark>CALL MUSUBI.</mark>")
o += el(5, "body", 72, 570, "Put your brand&rsquo;s best 30 seconds on Musubi. 5,000+ creators across India turn it into clips on Reels and Shorts, right where your customers already are. <b>Your budget only pays out for verified views.</b>", "width:930px;font-size:30px")
o += card.replace("left:5880px;top:720px", "left:5890px;top:730px") + url

open("index.html", "w", encoding="utf-8").write(t[:a] + o + t[b:])
