# -*- coding: utf-8 -*-
import json
import os

import base64

with open("logo.jpg", "rb") as f:
    logo_base64 = base64.b64encode(f.read()).decode("ascii")

# Import the data banks from update_banks.py
from update_banks import qbank, ebank, rbank

# Word Scramble Bank
sbank = {
  "animals": [
    {"w": "ELEPHANT", "h": "Largest living land mammal on Earth"},
    {"w": "PENGUIN", "h": "Flightless aquatic bird that swims gracefully"},
    {"w": "GIRAFFE", "h": "Tallest living animal with a long neck"},
    {"w": "DOLPHIN", "h": "Highly intelligent marine mammal"},
    {"w": "BUTTERFLY", "h": "Colourful winged insect undergoing metamorphosis"},
    {"w": "KANGAROO", "h": "Australian marsupial that hops with a pouch"},
    {"w": "CROCODILE", "h": "Ancient predatory aquatic reptile"},
    {"w": "CHAMELEON", "h": "Reptile known for colour camouflage"}
  ],
  "countries": [
    {"w": "AUSTRALIA", "h": "Island continent down under"},
    {"w": "BRAZIL", "h": "Famous for Samba, carnival, and football"},
    {"w": "CANADA", "h": "North American country with maple leaf flag"},
    {"w": "JAPAN", "h": "Asian island nation called Land of Rising Sun"},
    {"w": "ICELAND", "h": "Nordic island nation of geysers and volcanoes"},
    {"w": "MEXICO", "h": "Land of tacos, pyramids, and mariachi"},
    {"w": "EGYPT", "h": "Home to ancient Giza Pyramids and the Nile"},
    {"w": "GERMANY", "h": "European country famous for Autobahn & engineering"}
  ],
  "food": [
    {"w": "CHOCOLATE", "h": "Sweet confectionery made from roasted cacao"},
    {"w": "SPAGHETTI", "h": "Long, thin cylindrical Italian pasta"},
    {"w": "PINEAPPLE", "h": "Tropical fruit with spiky tough skin"},
    {"w": "SANDWICH", "h": "Food typically consisting of fillings between bread"},
    {"w": "MUSHROOM", "h": "Edible fleshy fruiting body of a fungus"},
    {"w": "BROCCOLI", "h": "Edible green plant in cabbage family with tree-like heads"},
    {"w": "PANCAKES", "h": "Flat circular batter cake fried on a griddle"},
    {"w": "AVOCADO", "h": "Creamy green fruit used in guacamole"}
  ],
  "science": [
    {"w": "GRAVITY", "h": "Invisible force attracting bodies toward center of Earth"},
    {"w": "OXYGEN", "h": "Vital chemical element gas humans breathe"},
    {"w": "MOLECULE", "h": "Group of atoms bonded together"},
    {"w": "TELESCOPE", "h": "Optical instrument used to view distant space objects"},
    {"w": "VOLCANO", "h": "Rupture in planetary crust allowing molten lava to escape"},
    {"w": "DINOSAUR", "h": "Extinct prehistoric giant reptiles"},
    {"w": "MAGNET", "h": "Material generating a magnetic field attracting iron"},
    {"w": "CRYSTAL", "h": "Solid material whose constituents form a lattice pattern"}
  ]
}

# Spin Wheel Segments
wsegs = [
  {"t": "🎵 Sing a Song!", "c": "#ef5350"},
  {"t": "🎬 Guess the Movie!", "c": "#42a5f5"},
  {"t": "😂 Funniest Moment!", "c": "#66bb6a"},
  {"t": "🌟 Memorable Day!", "c": "#fdd835"},
  {"t": "🎁 One Wish!", "c": "#ab47bc"},
  {"t": "❓ Any Question!", "c": "#ff6f00"},
  {"t": "🤩 Best Teacher Story!", "c": "#00bcd4"},
  {"t": "🍕 Fav Food & Why!", "c": "#e91e63"},
  {"t": "💭 Dream Job!", "c": "#8bc34a"},
  {"t": "🦸 Your Superpower!", "c": "#ff7043"}
]

qbank_json = json.dumps(qbank, ensure_ascii=False)
ebank_json = json.dumps(ebank, ensure_ascii=False)
rbank_json = json.dumps(rbank, ensure_ascii=False)
sbank_json = json.dumps(sbank, ensure_ascii=False)
wsegs_json = json.dumps(wsegs, ensure_ascii=False)

html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no, viewport-fit=cover">
  <meta name="mobile-web-app-capable" content="yes">
  <meta name="apple-mobile-web-app-capable" content="yes">
  <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
  <meta name="theme-color" content="#1a237e">
  <title>🎉 Nex Edu Classes — Children's Day Games 2026</title>
  <style>
    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
      -webkit-tap-highlight-color: transparent;
    }}

    :root {{
      --bg: #0f0e17;
      --card: #1a1a2e;
      --accent: #ff6f00;
      --pink: #e91e63;
      --cyan: #00e5ff;
      --green: #00e676;
      --gold: #ffd700;
      --text: #eee;
    }}

    html, body {{
      font-family: 'Segoe UI', system-ui, -apple-system, Roboto, sans-serif;
      background: var(--bg);
      color: var(--text);
      min-height: 100vh;
      min-height: -webkit-fill-available;
      overflow-x: hidden;
      user-select: none;
      -webkit-user-select: none;
      touch-action: manipulation;
    }}

    body {{
      padding-top: env(safe-area-inset-top, 0);
      padding-bottom: env(safe-area-inset-bottom, 0);
      padding-left: env(safe-area-inset-left, 0);
      padding-right: env(safe-area-inset-right, 0);
    }}

    body::before {{
      content: '';
      position: fixed;
      inset: 0;
      background: radial-gradient(circle at 20% 30%, rgba(255, 111, 0, .12), transparent 50%), radial-gradient(circle at 80% 70%, rgba(0, 229, 255, .08), transparent 50%);
      z-index: -1;
      pointer-events: none;
    }}

    #confetti {{
      position: fixed;
      inset: 0;
      pointer-events: none;
      z-index: 9999;
    }}

    /* HEADER */
    .hdr {{
      background: linear-gradient(135deg, #1a237e, #283593);
      padding: clamp(.5rem, 2vw, .8rem) clamp(.8rem, 3vw, 1.5rem);
      display: flex;
      align-items: center;
      gap: clamp(.6rem, 2vw, 1rem);
      box-shadow: 0 4px 20px #0005;
      position: sticky;
      top: 0;
      z-index: 100;
    }}

    .hdr img {{
      width: clamp(44px, 10vw, 56px);
      height: clamp(44px, 10vw, 56px);
      border-radius: 50%;
      border: 2px solid var(--accent);
      object-fit: cover;
      flex-shrink: 0;
    }}

    .hdr h1 {{
      font-size: clamp(.92rem, 3.8vw, 1.3rem);
      line-height: 1.25;
      background: linear-gradient(90deg, var(--gold), var(--accent), var(--pink));
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      background-clip: text;
      background-size: 200%;
      animation: shimmer 3s linear infinite;
    }}

    .hdr p {{
      font-size: clamp(.7rem, 2.6vw, .85rem);
      color: var(--cyan);
      margin-top: 2px;
    }}

    @keyframes shimmer {{
      0% {{ background-position: 200%; }}
      100% {{ background-position: -200%; }}
    }}

    /* NAV */
    .nav {{
      display: flex;
      gap: .4rem;
      padding: .5rem .8rem;
      overflow-x: auto;
      -webkit-overflow-scrolling: touch;
      white-space: nowrap;
      scrollbar-width: none;
      background: #1a1a2ecc;
      backdrop-filter: blur(10px);
      position: sticky;
      top: 60px;
      z-index: 99;
    }}

    .nav::-webkit-scrollbar {{
      display: none;
    }}

    .nav button {{
      flex-shrink: 0;
      padding: .45rem .85rem;
      border: 2px solid transparent;
      border-radius: 12px;
      background: var(--card);
      color: var(--text);
      cursor: pointer;
      font-size: clamp(.75rem, 2.5vw, .84rem);
      font-weight: 600;
      min-height: 38px;
      transition: .2s;
      touch-action: manipulation;
    }}

    .nav button:hover, .nav button:active {{
      border-color: var(--accent);
    }}

    .nav button.on {{
      background: linear-gradient(135deg, var(--accent), #e65100);
      color: #fff;
      border-color: var(--accent);
      box-shadow: 0 2px 10px rgba(255,111,0,.35);
    }}

    @media(min-width: 768px) {{
      .nav {{
        justify-content: center;
      }}
    }}

    /* PAGES */
    .pg {{
      display: none;
      padding: clamp(.7rem, 2.5vw, 1.6rem);
      max-width: 1050px;
      margin: auto;
      animation: fadeUp .3s ease;
    }}

    .pg.show {{
      display: block;
    }}

    @keyframes fadeUp {{
      from {{ opacity: 0; transform: translateY(12px); }}
      to {{ opacity: 1; transform: translateY(0); }}
    }}

    /* CARDS */
    .card {{
      background: var(--card);
      border-radius: 18px;
      padding: clamp(1rem, 3.5vw, 2rem);
      margin-bottom: 1.2rem;
      border: 1px solid #fff1;
      box-shadow: 0 4px 25px #0004;
    }}

    .card h2 {{
      font-size: clamp(1.1rem, 3vw, 1.45rem);
      margin-bottom: 1rem;
      display: flex;
      align-items: center;
      gap: .6rem;
    }}

    /* BUTTONS */
    .btn {{
      padding: .65rem 1.4rem;
      border: none;
      border-radius: 14px;
      font-size: clamp(.88rem, 2.2vw, 1.05rem);
      font-weight: 700;
      cursor: pointer;
      min-height: 48px;
      transition: transform .15s, box-shadow .15s;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: .5rem;
      touch-action: manipulation;
    }}

    .btn:active {{
      transform: scale(.97);
    }}

    .btn:disabled {{
      opacity: .4;
      cursor: default;
      transform: none;
    }}

    .btn-o {{ background: linear-gradient(135deg, var(--accent), #e65100); color: #fff; }}
    .btn-g {{ background: linear-gradient(135deg, var(--green), #00c853); color: #fff; }}
    .btn-p {{ background: linear-gradient(135deg, var(--pink), #c2185b); color: #fff; }}
    .btn-c {{ background: linear-gradient(135deg, var(--cyan), #00838f); color: #fff; }}
    .btn-gold {{ background: linear-gradient(135deg, var(--gold), #ff8f00); color: #111; }}

    /* QUIZ & OPTIONS */
    .q-text {{
      font-size: clamp(1.1rem, 3vw, 1.45rem);
      font-weight: 600;
      line-height: 1.5;
      margin-bottom: 1.2rem;
    }}

    .opts {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: clamp(.55rem, 2vw, .95rem);
    }}

    @media(max-width: 620px) {{
      .opts {{
        grid-template-columns: 1fr;
      }}
    }}

    .opt {{
      padding: clamp(.8rem, 2.5vw, 1.15rem) clamp(.9rem, 3vw, 1.4rem);
      border: 2px solid #fff2;
      border-radius: 14px;
      background: #0003;
      color: var(--text);
      font-size: clamp(.92rem, 2.5vw, 1.1rem);
      cursor: pointer;
      min-height: 52px;
      transition: background .2s, border-color .2s;
      text-align: left;
      font-weight: 500;
      touch-action: manipulation;
      display: flex;
      align-items: center;
    }}

    .opt:active, .opt:hover {{
      border-color: var(--accent);
      background: rgba(255, 111, 0, .12);
    }}

    .opt.ok {{
      border-color: var(--green);
      background: rgba(0, 230, 118, .2);
    }}

    .opt.no {{
      border-color: var(--pink);
      background: rgba(233, 30, 99, .2);
      animation: shake .4s;
    }}

    .opt.off {{
      pointer-events: none;
      opacity: .55;
    }}

    @keyframes shake {{
      25% {{ transform: translateX(-6px); }}
      75% {{ transform: translateX(6px); }}
    }}

    /* TIMER BAR */
    .tbar {{
      width: 100%;
      height: 8px;
      background: #fff1;
      border-radius: 4px;
      margin: .8rem 0;
      overflow: hidden;
    }}

    .tfill {{
      height: 100%;
      border-radius: 4px;
      transition: width .1s linear;
      background: linear-gradient(90deg, var(--green), var(--accent));
    }}

    .tfill.warn {{ background: linear-gradient(90deg, var(--accent), var(--pink)); }}
    .tfill.crit {{ background: var(--pink); }}

    .ttext {{
      font-size: clamp(1.5rem, 4.5vw, 2.2rem);
      font-weight: 900;
      text-align: center;
      font-variant-numeric: tabular-nums;
    }}

    /* MEMORY MATCH */
    .mem-grid {{
      display: grid;
      gap: clamp(.45rem, 2vw, .9rem);
      justify-content: center;
      margin: 1rem auto;
      max-width: 650px;
      width: 100%;
    }}

    .mc {{
      aspect-ratio: 1;
      border-radius: 12px;
      cursor: pointer;
      perspective: 600px;
      min-width: 0;
      width: 100%;
      touch-action: manipulation;
    }}

    .mc-in {{
      width: 100%;
      height: 100%;
      position: relative;
      transition: transform .45s;
      transform-style: preserve-3d;
    }}

    .mc.flip .mc-in {{ transform: rotateY(180deg); }}

    .mc-f, .mc-b {{
      position: absolute;
      inset: 0;
      border-radius: 12px;
      display: flex;
      align-items: center;
      justify-content: center;
      backface-visibility: hidden;
      font-size: clamp(1.6rem, 5vw, 2.6rem);
    }}

    .mc-f {{
      background: linear-gradient(135deg, #1a237e, #283593);
      border: 2px solid #fff1;
    }}

    .mc-b {{
      background: var(--card);
      border: 2px solid var(--accent);
      transform: rotateY(180deg);
    }}

    .mc.done .mc-b {{
      border-color: var(--green);
      background: rgba(0, 230, 118, .15);
    }}

    /* SCRAMBLE */
    .scr-word {{
      font-size: clamp(1.8rem, 6vw, 3.2rem);
      font-weight: 900;
      text-align: center;
      letter-spacing: clamp(.25rem, 1.2vw, .6rem);
      color: var(--accent);
      margin: 1rem 0;
      word-break: break-all;
    }}

    /* WHEEL */
    .wheel-wrap {{
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 1.2rem;
      width: 100%;
    }}

    .wheel-ptr {{
      font-size: clamp(2.2rem, 5vw, 2.8rem);
      margin-bottom: -.4rem;
      filter: drop-shadow(0 2px 4px #0008);
    }}

    #wheelCanvas {{
      border-radius: 50%;
      box-shadow: 0 0 35px rgba(255, 111, 0, .28);
      max-width: min(380px, 86vw);
      max-height: min(380px, 86vw);
      width: 100%;
      height: auto;
      aspect-ratio: 1;
    }}

    /* TABLET SPECIFIC LAYOUT FOR WHEEL */
    @media(min-width: 800px) {{
      .wheel-wrap {{
        flex-direction: row;
        justify-content: center;
        align-items: center;
        gap: 3rem;
      }}
      .wheel-side-controls {{
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 1.5rem;
        flex: 1;
        max-width: 420px;
      }}
    }}

    /* EMOJI GUESS */
    .emoji-clue {{
      font-size: clamp(2.2rem, 6.5vw, 3.5rem);
      text-align: center;
      margin: 1rem 0;
      letter-spacing: .35rem;
      line-height: 1.35;
    }}

    /* HOME GRID - TABLET ADAPTIVE */
    .home-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(135px, 1fr));
      gap: clamp(.65rem, 2vw, 1.2rem);
      margin-top: 1.5rem;
    }}

    @media(min-width: 640px) {{
      .home-grid {{
        grid-template-columns: repeat(3, 1fr);
      }}
    }}

    @media(min-width: 960px) {{
      .home-grid {{
        grid-template-columns: repeat(6, 1fr);
      }}
    }}

    .home-tile {{
      background: var(--card);
      border-radius: 16px;
      padding: clamp(1rem, 2.5vw, 1.6rem) .8rem;
      text-align: center;
      cursor: pointer;
      border: 1px solid #fff1;
      transition: transform .2s, border-color .2s;
      touch-action: manipulation;
    }}

    .home-tile:active, .home-tile:hover {{
      transform: translateY(-4px);
      border-color: var(--accent);
      box-shadow: 0 10px 30px #0005;
    }}

    .home-tile .icon {{
      font-size: clamp(2rem, 5vw, 3rem);
      margin-bottom: .4rem;
    }}

    .home-tile h3 {{
      font-size: clamp(.88rem, 2.2vw, 1.05rem);
    }}

    .home-tile p {{
      font-size: clamp(.68rem, 1.8vw, .78rem);
      color: #fff8;
      margin-top: .2rem;
    }}

    /* RAPID FIRE BUTTONS */
    .rapid-btns {{
      display: flex;
      gap: clamp(.8rem, 3vw, 1.8rem);
      justify-content: center;
      width: 100%;
      max-width: 600px;
      margin: .8rem auto;
    }}

    .rapid-btn {{
      flex: 1;
      min-height: clamp(54px, 8vw, 72px);
      font-size: clamp(1.15rem, 3.5vw, 1.55rem) !important;
      border-radius: 16px !important;
    }}

    #rText {{
      min-height: clamp(4.2rem, 10vw, 6rem);
      font-size: clamp(1.15rem, 3.2vw, 1.6rem) !important;
    }}

    /* FOOTER */
    .ftr {{
      text-align: center;
      padding: 1.2rem 1rem;
      color: #fff4;
      font-size: clamp(.68rem, 2.2vw, .78rem);
      margin-top: 1.5rem;
    }}

    .ftr img {{
      width: 28px;
      height: 28px;
      border-radius: 50%;
      vertical-align: middle;
      margin-right: .4rem;
    }}
  </style>
</head>
<body>

<canvas id="confetti"></canvas>

<!-- HEADER -->
<header class="hdr">
  <img src="data:image/jpeg;base64,{logo_base64}" alt="Nex Edu">
  <div>
    <h1>🎉 Nex Edu Classes — Children's Day 2026</h1>
    <p>Happy Children's Day! Let the fun begin! 🎈</p>
  </div>
</header>

<!-- NAVIGATION -->
<nav class="nav" id="nav">
  <button class="on" onclick="go('home')">🏠 Home</button>
  <button onclick="go('quiz')">🧠 Quiz</button>
  <button onclick="go('emoji')">🎬 Guess Movie</button>
  <button onclick="go('scramble')">🔤 Word Scramble</button>
  <button onclick="go('memory')">🃏 Memory Match</button>
  <button onclick="go('rapid')">⚡ Rapid Fire</button>
  <button onclick="go('wheel')">🎡 Spin Wheel</button>
</nav>

<!-- ============ HOME ============ -->
<div class="pg show" id="p-home">
  <div class="card" style="text-align:center;padding:2.5rem 1.5rem">
    <img src="data:image/jpeg;base64,{logo_base64}" alt="" style="width:100px;height:100px;border-radius:50%;border:3px solid var(--accent);margin-bottom:1rem">
    <h1 style="font-size:1.8rem;margin-bottom:.3rem;background:linear-gradient(90deg,var(--gold),var(--accent),var(--pink));-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text">🎊 Happy Children's Day! 🎊</h1>
    <p style="color:var(--cyan)">Pick a game below and have fun!</p>
    <div class="home-grid">
      <div class="home-tile" onclick="go('quiz')"><div class="icon">🧠</div><h3>Quiz</h3><p>India, Science, GK & Fun</p></div>
      <div class="home-tile" onclick="go('emoji')"><div class="icon">🎬</div><h3>Guess Movie</h3><p>Bollywood & Blockbusters</p></div>
      <div class="home-tile" onclick="go('scramble')"><div class="icon">🔤</div><h3>Word Scramble</h3><p>Unscramble letters</p></div>
      <div class="home-tile" onclick="go('memory')"><div class="icon">🃏</div><h3>Memory Match</h3><p>Find the pairs</p></div>
      <div class="home-tile" onclick="go('rapid')"><div class="icon">⚡</div><h3>Rapid Fire</h3><p>True or False blitz!</p></div>
      <div class="home-tile" onclick="go('wheel')"><div class="icon">🎡</div><h3>Spin Wheel</h3><p>Dares & fun sharing</p></div>
    </div>
  </div>
</div>

<!-- ============ QUIZ ============ -->
<div class="pg" id="p-quiz">
  <div class="card">
    <h2>🧠 Quiz Time!</h2>
    <div id="qSetup">
      <p style="margin-bottom:1rem;color:#fffa">Pick a category and test your knowledge!</p>
      <div style="display:flex;gap:.6rem;flex-wrap:wrap;margin-bottom:1rem">
        <select id="qCat" style="padding:.5rem 1rem;border-radius:8px;background:#0005;color:var(--text);border:2px solid #fff2;font-size:.9rem">
          <option value="all">🎲 All (150+ Questions)</option>
          <option value="science">🔬 Science</option>
          <option value="math">📐 Math</option>
          <option value="gk">🌍 GK</option>
          <option value="sports">⚽ Sports</option>
          <option value="india">🇮🇳 India & Current Affairs</option>
          <option value="trend">🔥 Trending & Tech</option>
          <option value="fun">🎉 Fun & Entertainment</option>
        </select>
        <button class="btn btn-o" onclick="startQuiz()">▶ Start Quiz</button>
      </div>
    </div>
    <div id="qGame" style="display:none">
      <div style="display:flex;justify-content:space-between;font-size:.85rem;font-weight:700;margin-bottom:.3rem">
        <span id="qProg"></span>
        <span id="qScore"></span>
      </div>
      <div class="tbar"><div class="tfill" id="qBar"></div></div>
      <div id="qTimer" class="ttext"></div>
      <div id="qCatBadge" style="display:inline-block;padding:.2rem .7rem;border-radius:15px;font-size:.7rem;font-weight:700;margin-bottom:.6rem"></div>
      <div id="qText" class="q-text"></div>
      <div class="opts" id="qOpts"></div>
      <div style="text-align:center;margin-top:.8rem">
        <button class="btn btn-o" id="qNext" onclick="nextQ()" style="display:none">Next ➡️</button>
      </div>
    </div>
    <div id="qEnd" style="display:none;text-align:center;padding:2rem">
      <div style="font-size:3.5rem" id="qEndIcon"></div>
      <h2 id="qEndTitle" style="margin:.5rem 0"></h2>
      <p id="qEndMsg" style="color:var(--accent);font-size:1.1rem;margin-bottom:1.5rem"></p>
      <button class="btn btn-o" onclick="resetQuiz()">🔄 Play Again</button>
    </div>
  </div>
</div>

<!-- ============ EMOJI GUESS ============ -->
<div class="pg" id="p-emoji">
  <div class="card">
    <h2>🎬 Guess the Movie from Emojis!</h2>
    <div id="eSetup">
      <p style="margin-bottom:1rem;color:#fffa">Can you guess the Bollywood & famous blockbuster movie from emoji clues?</p>
      <button class="btn btn-o" onclick="startEmoji()">▶ Start Game</button>
    </div>
    <div id="eGame" style="display:none">
      <div style="display:flex;justify-content:space-between;font-size:.85rem;font-weight:700;margin-bottom:.3rem">
        <span id="eProg"></span>
        <span id="eScore"></span>
      </div>
      <div class="tbar"><div class="tfill" id="eBar"></div></div>
      <div class="emoji-clue" id="eClue"></div>
      <p style="text-align:center;color:#fffa;margin-bottom:.8rem" id="eHintText">Guess the movie title from the emojis above!</p>
      <div class="opts" id="eOpts"></div>
      <div style="text-align:center;margin-top:.8rem">
        <button class="btn btn-o" id="eNext" onclick="nextE()" style="display:none">Next ➡️</button>
      </div>
    </div>
    <div id="eEnd" style="display:none;text-align:center;padding:2rem">
      <div style="font-size:3.5rem">🎬</div>
      <h2 id="eEndTitle" style="margin:.5rem 0"></h2>
      <p id="eEndMsg" style="color:var(--accent);margin-bottom:1.5rem"></p>
      <button class="btn btn-o" onclick="resetEmoji()">🔄 Play Again</button>
    </div>
  </div>
</div>

<!-- ============ WORD SCRAMBLE ============ -->
<div class="pg" id="p-scramble">
  <div class="card">
    <h2>🔤 Word Scramble</h2>
    <div id="sSetup">
      <select id="sCat" style="padding:.5rem 1rem;border-radius:8px;background:#0005;color:var(--text);border:2px solid #fff2;font-size:.9rem;margin-bottom:.8rem">
        <option value="animals">🐾 Animals</option>
        <option value="countries">🌍 Countries</option>
        <option value="food">🍕 Food</option>
        <option value="science">🔬 Science</option>
      </select><br>
      <button class="btn btn-o" onclick="startScramble()">▶ Start</button>
    </div>
    <div id="sGame" style="display:none">
      <div style="display:flex;justify-content:space-between;font-size:.85rem;font-weight:700;margin-bottom:.3rem">
        <span id="sProg"></span>
        <span id="sScore"></span>
      </div>
      <div class="tbar"><div class="tfill" id="sBar"></div></div>
      <div id="sTimer" class="ttext"></div>
      <p id="sHint" style="text-align:center;color:var(--cyan);font-style:italic;margin-bottom:.3rem"></p>
      <div id="sWord" class="scr-word"></div>
      <div style="text-align:center;margin:.8rem 0">
        <input type="text" id="sAns" placeholder="Type your answer..." style="font-size:1.1rem;text-align:center;width:260px;padding:.5rem 1rem;border-radius:10px;background:#0005;color:var(--text);border:2px solid #fff2" onkeydown="if(event.key==='Enter')checkScramble()">
      </div>
      <div style="text-align:center;display:flex;gap:.5rem;justify-content:center;flex-wrap:wrap">
        <button class="btn btn-g" onclick="checkScramble()">✅ Submit</button>
        <button class="btn btn-c" onclick="scrambleHint()">💡 Hint</button>
        <button class="btn btn-o" id="sNext" onclick="nextScramble()" style="display:none">Next ➡️</button>
      </div>
    </div>
  </div>
</div>

<!-- ============ MEMORY MATCH ============ -->
<div class="pg" id="p-memory">
  <div class="card">
    <h2>🃏 Memory Match</h2>
    <div id="mSetup">
      <select id="mSize" style="padding:.5rem 1rem;border-radius:8px;background:#0005;color:var(--text);border:2px solid #fff2;font-size:.9rem;margin-bottom:.8rem">
        <option value="4">4×3 Easy (6 pairs)</option>
        <option value="6" selected>4×4 Medium (8 pairs)</option>
        <option value="8">4×5 Hard (10 pairs)</option>
      </select><br>
      <button class="btn btn-o" onclick="startMemory()">▶ Start</button>
    </div>
    <div id="mGame" style="display:none">
      <div style="display:flex;justify-content:space-between;font-size:.9rem;font-weight:700;margin-bottom:.3rem">
        <span id="mMoves">Moves: 0</span>
        <span id="mTime">⏱ 0s</span>
        <span id="mPairs">Pairs: 0/0</span>
      </div>
      <div class="mem-grid" id="mGrid"></div>
    </div>
  </div>
</div>

<!-- ============ RAPID FIRE ============ -->
<div class="pg" id="p-rapid">
  <div class="card">
    <h2>⚡ Rapid Fire — True or False?</h2>
    <div id="rSetup">
      <p style="margin-bottom:1rem;color:#fffa">60 seconds! Test your speed on 100 challenging questions!</p>
      <button class="btn btn-o" onclick="startRapid()">⚡ GO!</button>
    </div>
    <div id="rGame" style="display:none">
      <div id="rTimer" class="ttext" style="font-size:2.5rem;color:var(--pink)"></div>
      <div class="tbar"><div class="tfill" id="rBar"></div></div>
      <div style="display:flex;justify-content:center;gap:1.5rem;font-size:1.05rem;font-weight:700;margin:.4rem 0">
        <span id="rRight" style="color:var(--green)">✅ 0</span>
        <span id="rWrong" style="color:var(--pink)">❌ 0</span>
      </div>
      <div id="rCatTag" style="text-align:center;font-size:.78rem;font-weight:700;color:var(--cyan);letter-spacing:1px;text-transform:uppercase;margin-top:.4rem"></div>
      <div id="rText" class="q-text" style="text-align:center;margin:.8rem 0;min-height:4.2rem;display:flex;align-items:center;justify-content:center"></div>
      <div class="rapid-btns">
        <button class="btn btn-g rapid-btn" onclick="rapidAns(true)">👍 TRUE</button>
        <button class="btn btn-p rapid-btn" onclick="rapidAns(false)">👎 FALSE</button>
      </div>
    </div>
    <div id="rEnd" style="display:none;text-align:center;padding:2rem">
      <div style="font-size:3.5rem">⚡</div>
      <h2 id="rEndTitle" style="margin:.5rem 0"></h2>
      <p id="rEndMsg" style="color:var(--accent);margin-bottom:1.5rem"></p>
      <button class="btn btn-o" onclick="resetRapid()">🔄 Play Again</button>
    </div>
  </div>
</div>

<!-- ============ SPIN WHEEL ============ -->
<div class="pg" id="p-wheel">
  <div class="card">
    <h2>🎡 Spin the Wheel!</h2>
    <div class="wheel-wrap">
      <div style="display:flex;flex-direction:column;align-items:center">
        <div class="wheel-ptr">⬇️</div>
        <canvas id="wheelCanvas" width="360" height="360"></canvas>
      </div>
      <div class="wheel-side-controls">
        <button class="btn btn-gold" onclick="spin()" id="spinBtn" style="font-size:1.25rem;padding:.9rem 2.5rem;min-height:56px">🎡 SPIN NOW!</button>
        <div id="wheelRes" style="font-size:1.35rem;font-weight:700;min-height:3.5rem;text-align:center;width:100%;line-height:1.5;padding:.8rem;border-radius:14px;background:#0003;border:1px solid #fff1"></div>
      </div>
    </div>
  </div>
</div>

<!-- FOOTER -->
<div class="ftr">
  <img src="data:image/jpeg;base64,{logo_base64}" alt="">
  Powered by <strong>Nex Edu Classes</strong> · Children's Day 2026 · Made with ❤️
</div>

<script>
// ==========================================
// STATE VARIABLES (Declared at top of script)
// ==========================================
var actx = null;
var qs = {{ pool: [], i: 0, sc: 0, timer: null }};
var es = {{ pool: [], i: 0, sc: 0, timer: null }};
var ss = {{ pool: [], i: 0, sc: 0, timer: null, hinted: false }};
var ms = {{ cards: [], flipped: [], matched: [], moves: 0, pairs: 0, cols: 4, t0: 0, ti: null }};
var rs = {{ pool: [], i: 0, ok: 0, no: 0, timer: null }};
var wAngle = 0;
var wSpin = false;

// ==========================================
// DATA BANKS (Embedded JSON)
// ==========================================
const QBank = {qbank_json};
const EBank = {ebank_json};
const RBank = {rbank_json};
const SBank = {sbank_json};
const WSegs = {wsegs_json};

const catC = {{
  science: '#00e5ff',
  math: '#ff6f00',
  gk: '#00e676',
  sports: '#ef5350',
  fun: '#ab47bc',
  india: '#ff9933',
  trend: '#e040fb'
}};

const catN = {{
  science: '🔬 Science',
  math: '📐 Math',
  gk: '🌍 GK',
  sports: '⚽ Sports',
  fun: '🎉 Fun',
  india: '🇮🇳 India',
  trend: '🔥 Trending'
}};

const MEmoji = ['🍎', '🍌', '🍇', '🍓', '🍒', '🥝', '🍍', '🥭', '🍊', '🍋'];

// ==========================================
// AUDIO ENGINE (Web Audio API - 100% offline)
// ==========================================
function tone(f, d = .12, t = 'sine', v = .25) {{
  try {{
    if (!actx) actx = new (window.AudioContext || window.webkitAudioContext)();
    const o = actx.createOscillator();
    const g = actx.createGain();
    o.type = t;
    o.frequency.value = f;
    g.gain.setValueAtTime(v, actx.currentTime);
    g.gain.exponentialRampToValueAtTime(.001, actx.currentTime + d);
    o.connect(g);
    g.connect(actx.destination);
    o.start();
    o.stop(actx.currentTime + d);
  }} catch (e) {{}}
}}

function sfxOk() {{
  tone(523, .08);
  setTimeout(() => tone(659, .08), 80);
  setTimeout(() => tone(784, .15), 160);
}}

function sfxNo() {{
  tone(200, .25, 'sawtooth', .18);
}}

function sfxWin() {{
  [523, 659, 784, 1047].forEach((f, i) => setTimeout(() => tone(f, .18), i * 120));
}}

function sfxTick() {{
  tone(900, .04, 'sine', .08);
}}

// ==========================================
// CONFETTI ENGINE
// ==========================================
const CC = document.getElementById('confetti');
const cx = CC.getContext('2d');
let cps = [];
let cRun = false;

function rsz() {{
  CC.width = window.innerWidth;
  CC.height = window.innerHeight;
}}
window.addEventListener('resize', rsz);
rsz();

function boom(dur = 3000) {{
  cps = [];
  const cl = ['#ffd700', '#ff6f00', '#e91e63', '#00e676', '#42a5f5', '#ab47bc', '#00e5ff'];
  for (let i = 0; i < 120; i++) {{
    cps.push({{
      x: Math.random() * CC.width,
      y: Math.random() * CC.height - CC.height,
      w: Math.random() * 9 + 4,
      h: Math.random() * 5 + 2,
      c: cl[~~(Math.random() * cl.length)],
      vx: (Math.random() - .5) * 4,
      vy: Math.random() * 3 + 2,
      r: Math.random() * 360,
      vr: (Math.random() - .5) * 10
    }});
  }}
  if (!cRun) {{
    cRun = true;
    cfAnim();
  }}
  setTimeout(() => {{
    cRun = false;
    cps = [];
    cx.clearRect(0, 0, CC.width, CC.height);
  }}, dur);
}}

function cfAnim() {{
  if (!cRun) return;
  cx.clearRect(0, 0, CC.width, CC.height);
  cps.forEach(p => {{
    cx.save();
    cx.translate(p.x, p.y);
    cx.rotate(p.r * Math.PI / 180);
    cx.fillStyle = p.c;
    cx.fillRect(-p.w / 2, -p.h / 2, p.w, p.h);
    cx.restore();
    p.x += p.vx;
    p.y += p.vy;
    p.r += p.vr;
    if (p.y > CC.height) {{
      p.y = -10;
      p.x = Math.random() * CC.width;
    }}
  }});
  requestAnimationFrame(cfAnim);
}}

// ==========================================
// NAVIGATION
// ==========================================
const pages = ['home', 'quiz', 'emoji', 'scramble', 'memory', 'rapid', 'wheel'];

function go(id) {{
  document.querySelectorAll('.pg').forEach(p => p.classList.remove('show'));
  const target = document.getElementById('p-' + id);
  if (target) target.classList.add('show');
  const bs = [...document.querySelectorAll('.nav button')];
  bs.forEach(b => b.classList.remove('on'));
  const idx = pages.indexOf(id);
  if (idx >= 0 && bs[idx]) bs[idx].classList.add('on');
  if (id === 'wheel') drawWheel();
}}

// ==========================================
// RANDOM SHUFFLE (Fisher-Yates)
// ==========================================
function shuf(a) {{
  const b = [...a];
  for (let i = b.length - 1; i > 0; i--) {{
    const j = Math.floor(Math.random() * (i + 1));
    const tmp = b[i];
    b[i] = b[j];
    b[j] = tmp;
  }}
  return b;
}}

// ==========================================
// SMART NON-REPEATING DECK ENGINE
// ==========================================
const Decks = {{
  quiz: {{}},
  emoji: [],
  rapid: []
}};

function getQuizSlice(cat, count = 10) {{
  const full = cat === 'all' ? [...QBank] : QBank.filter(q => q.c === cat);
  if (!Decks.quiz[cat] || Decks.quiz[cat].length < count) {{
    Decks.quiz[cat] = shuf(full);
  }}
  const picked = Decks.quiz[cat].splice(0, count);
  return picked.map(q => {{
    const cor = q.o[q.a];
    const so = shuf([...q.o]);
    return {{ ...q, o: so, a: so.indexOf(cor) }};
  }});
}}

function getEmojiSlice(count = 10) {{
  if (!Decks.emoji || Decks.emoji.length < count) {{
    Decks.emoji = shuf([...EBank]);
  }}
  const picked = Decks.emoji.splice(0, count);
  return picked.map(q => {{
    const so = shuf([...q.opts]);
    return {{ ...q, opts: so }};
  }});
}}

function getRapidDeck() {{
  if (!Decks.rapid || Decks.rapid.length < 35) {{
    Decks.rapid = shuf([...RBank]);
  }}
  const sliceCount = Math.min(40, Decks.rapid.length);
  return Decks.rapid.splice(0, sliceCount);
}}

// ==========================================
// GAME 1: QUIZ
// ==========================================
function startQuiz() {{
  const cat = document.getElementById('qCat').value;
  const pool = getQuizSlice(cat, 10);
  qs = {{ pool: pool, i: 0, sc: 0, timer: null }};
  document.getElementById('qSetup').style.display = 'none';
  document.getElementById('qGame').style.display = 'block';
  document.getElementById('qEnd').style.display = 'none';
  showQ();
}}

function showQ() {{
  if (qs.i >= qs.pool.length) {{
    endQuiz();
    return;
  }}
  const q = qs.pool[qs.i];
  document.getElementById('qProg').textContent = (qs.i + 1) + ' / ' + qs.pool.length;
  document.getElementById('qScore').textContent = '⭐ ' + qs.sc;
  document.getElementById('qCatBadge').textContent = catN[q.c] || 'QUIZ';
  document.getElementById('qCatBadge').style.background = (catC[q.c] || '#00e5ff') + '33';
  document.getElementById('qCatBadge').style.color = catC[q.c] || '#00e5ff';
  document.getElementById('qText').textContent = q.q;
  document.getElementById('qNext').style.display = 'none';
  document.getElementById('qOpts').innerHTML = q.o.map((o, idx) =>
    `<button class="opt" onclick="ansQ(${{idx}})">${{String.fromCharCode(65 + idx)}}. ${{o}}</button>`
  ).join('');

  let tl = 20;
  const bar = document.getElementById('qBar');
  const txt = document.getElementById('qTimer');
  bar.style.width = '100%';
  bar.className = 'tfill';
  txt.textContent = '20s';
  clearInterval(qs.timer);
  qs.timer = setInterval(() => {{
    tl -= 0.1;
    if (tl <= 0) {{
      tl = 0;
      clearInterval(qs.timer);
      ansQ(-1);
    }}
    bar.style.width = (tl / 20 * 100) + '%';
    txt.textContent = Math.ceil(tl) + 's';
    if (tl < 4) bar.className = 'tfill crit';
    else if (tl < 10) bar.className = 'tfill warn';
    if (Math.ceil(tl) <= 3 && Math.ceil(tl) > 0) sfxTick();
  }}, 100);
}}

function ansQ(idx) {{
  clearInterval(qs.timer);
  const q = qs.pool[qs.i];
  const bs = document.querySelectorAll('#qOpts .opt');
  bs.forEach(b => b.classList.add('off'));
  if (bs[q.a]) bs[q.a].classList.add('ok');

  if (idx === q.a) {{
    qs.sc += 10;
    sfxOk();
  }} else {{
    if (idx >= 0 && bs[idx]) bs[idx].classList.add('no');
    sfxNo();
  }}
  document.getElementById('qScore').textContent = '⭐ ' + qs.sc;
  document.getElementById('qNext').style.display = 'inline-flex';
}}

function nextQ() {{
  qs.i++;
  showQ();
}}

function endQuiz() {{
  clearInterval(qs.timer);
  const pct = Math.round((qs.sc / (qs.pool.length * 10)) * 100);
  document.getElementById('qGame').style.display = 'none';
  document.getElementById('qEnd').style.display = 'block';
  document.getElementById('qEndIcon').textContent = pct >= 70 ? '🏆' : (pct >= 40 ? '👏' : '💪');
  document.getElementById('qEndTitle').textContent = pct >= 70 ? 'Amazing!' : (pct >= 40 ? 'Good Job!' : 'Keep Learning!');
  document.getElementById('qEndMsg').textContent = `You scored ${{qs.sc}} out of ${{qs.pool.length * 10}} (${{pct}}%)`;
  if (pct >= 70) {{
    boom(3000);
    sfxWin();
  }}
}}

function resetQuiz() {{
  document.getElementById('qSetup').style.display = 'block';
  document.getElementById('qGame').style.display = 'none';
  document.getElementById('qEnd').style.display = 'none';
}}

// ==========================================
// GAME 2: EMOJI MOVIE GUESS
// ==========================================
function startEmoji() {{
  const pool = getEmojiSlice(10);
  es = {{ pool: pool, i: 0, sc: 0, timer: null }};
  document.getElementById('eSetup').style.display = 'none';
  document.getElementById('eGame').style.display = 'block';
  document.getElementById('eEnd').style.display = 'none';
  showE();
}}

function showE() {{
  if (es.i >= es.pool.length) {{
    endEmoji();
    return;
  }}
  const q = es.pool[es.i];
  document.getElementById('eProg').textContent = (es.i + 1) + ' / ' + es.pool.length;
  document.getElementById('eScore').textContent = '⭐ ' + es.sc;
  document.getElementById('eClue').textContent = q.e;
  document.getElementById('eNext').style.display = 'none';

  let tl = 15;
  const bar = document.getElementById('eBar');
  bar.style.width = '100%';
  bar.className = 'tfill';
  clearInterval(es.timer);
  es.timer = setInterval(() => {{
    tl -= 0.1;
    if (tl <= 0) {{
      tl = 0;
      clearInterval(es.timer);
      ansE(-1);
    }}
    bar.style.width = (tl / 15 * 100) + '%';
    if (tl < 3) bar.className = 'tfill crit';
    else if (tl < 7) bar.className = 'tfill warn';
  }}, 100);

  document.getElementById('eOpts').innerHTML = q.opts.map((o, idx) =>
    `<button class="opt" onclick="ansE(${{idx}})">${{o}}</button>`
  ).join('');
}}

function ansE(idx) {{
  clearInterval(es.timer);
  const q = es.pool[es.i];
  const ci = q.opts.indexOf(q.ans);
  const bs = document.querySelectorAll('#eOpts .opt');
  bs.forEach(b => b.classList.add('off'));
  if (bs[ci]) bs[ci].classList.add('ok');

  if (idx === ci) {{
    es.sc += 10;
    sfxOk();
  }} else {{
    if (idx >= 0 && bs[idx]) bs[idx].classList.add('no');
    sfxNo();
  }}
  document.getElementById('eScore').textContent = '⭐ ' + es.sc;
  document.getElementById('eNext').style.display = 'inline-flex';
}}

function nextE() {{
  es.i++;
  showE();
}}

function endEmoji() {{
  const pct = Math.round((es.sc / (es.pool.length * 10)) * 100);
  document.getElementById('eGame').style.display = 'none';
  document.getElementById('eEnd').style.display = 'block';
  document.getElementById('eEndTitle').textContent = pct >= 70 ? '🎉 Movie Master!' : (pct >= 40 ? '👍 Nice Try!' : '💪 Keep Watching!');
  document.getElementById('eEndMsg').textContent = `Score: ${{es.sc}} / ${{es.pool.length * 10}} (${{pct}}%)`;
  if (pct >= 70) {{
    boom(3000);
    sfxWin();
  }}
}}

function resetEmoji() {{
  document.getElementById('eSetup').style.display = 'block';
  document.getElementById('eGame').style.display = 'none';
  document.getElementById('eEnd').style.display = 'none';
}}

// ==========================================
// GAME 3: WORD SCRAMBLE
// ==========================================
function scrambleStr(w) {{
  const a = w.split('');
  for (let i = a.length - 1; i > 0; i--) {{
    const j = Math.floor(Math.random() * (i + 1));
    const tmp = a[i];
    a[i] = a[j];
    a[j] = tmp;
  }}
  return a.join('') === w ? scrambleStr(w) : a.join('');
}}

function startScramble() {{
  const cat = document.getElementById('sCat').value;
  const pool = shuf(SBank[cat] || SBank.animals).slice(0, 6);
  ss = {{ pool: pool, i: 0, sc: 0, timer: null, hinted: false }};
  document.getElementById('sSetup').style.display = 'none';
  document.getElementById('sGame').style.display = 'block';
  showS();
}}

function showS() {{
  if (ss.i >= ss.pool.length) {{
    endScramble();
    return;
  }}
  const w = ss.pool[ss.i];
  ss.hinted = false;
  document.getElementById('sProg').textContent = (ss.i + 1) + ' / ' + ss.pool.length;
  document.getElementById('sScore').textContent = '⭐ ' + ss.sc;
  document.getElementById('sHint').textContent = '💡 ' + w.h;
  document.getElementById('sWord').textContent = scrambleStr(w.w);
  document.getElementById('sWord').style.color = 'var(--accent)';
  document.getElementById('sAns').value = '';
  document.getElementById('sAns').focus();
  document.getElementById('sNext').style.display = 'none';

  let tl = 30;
  const bar = document.getElementById('sBar');
  const txt = document.getElementById('sTimer');
  bar.style.width = '100%';
  txt.textContent = '30s';
  clearInterval(ss.timer);
  ss.timer = setInterval(() => {{
    tl -= 0.1;
    if (tl <= 0) {{
      tl = 0;
      clearInterval(ss.timer);
      checkScramble(true);
    }}
    bar.style.width = (tl / 30 * 100) + '%';
    txt.textContent = Math.ceil(tl) + 's';
  }}, 100);
}}

function scrambleHint() {{
  if (!ss.pool || !ss.pool[ss.i]) return;
  const w = ss.pool[ss.i].w;
  document.getElementById('sHint').textContent = `First: ${{w[0]}}  Last: ${{w[w.length - 1]}}`;
  ss.hinted = true;
}}

function checkScramble(timeout = false) {{
  clearInterval(ss.timer);
  if (!ss.pool || !ss.pool[ss.i]) return;
  const w = ss.pool[ss.i].w;
  const ans = document.getElementById('sAns').value.trim().toUpperCase();
  if (!timeout && ans === w) {{
    ss.sc += ss.hinted ? 8 : 10;
    sfxOk();
    document.getElementById('sWord').textContent = '✅ ' + w;
    document.getElementById('sWord').style.color = 'var(--green)';
  }} else {{
    sfxNo();
    document.getElementById('sWord').textContent = '❌ ' + w;
    document.getElementById('sWord').style.color = 'var(--pink)';
  }}
  document.getElementById('sScore').textContent = '⭐ ' + ss.sc;
  document.getElementById('sNext').style.display = 'inline-flex';
}}

function nextScramble() {{
  ss.i++;
  showS();
}}

function endScramble() {{
  clearInterval(ss.timer);
  alert(`🎉 Word Scramble complete! Score: ${{ss.sc}}`);
  if (ss.sc >= 40) {{
    boom(2000);
    sfxWin();
  }}
  document.getElementById('sSetup').style.display = 'block';
  document.getElementById('sGame').style.display = 'none';
}}

// ==========================================
// GAME 4: MEMORY MATCH
// ==========================================
function startMemory() {{
  const sz = parseInt(document.getElementById('mSize').value);
  const pairs = sz === 4 ? 6 : (sz === 6 ? 8 : 10);
  const cols = 4;
  const em = MEmoji.slice(0, pairs);
  const cards = shuf([...em, ...em]);
  ms = {{
    cards: cards,
    flipped: [],
    matched: [],
    moves: 0,
    pairs: pairs,
    cols: cols,
    t0: Date.now(),
    ti: null
  }};
  document.getElementById('mSetup').style.display = 'none';
  document.getElementById('mGame').style.display = 'block';
  document.getElementById('mMoves').textContent = 'Moves: 0';
  document.getElementById('mPairs').textContent = 'Pairs: 0/' + pairs;

  const g = document.getElementById('mGrid');
  g.style.gridTemplateColumns = `repeat(${{cols}}, 1fr)`;
  g.innerHTML = cards.map((_, i) =>
    `<div class="mc" onclick="flip(${{i}})" id="mc${{i}}">
      <div class="mc-in">
        <div class="mc-f">❓</div>
        <div class="mc-b">${{cards[i]}}</div>
      </div>
    </div>`
  ).join('');

  clearInterval(ms.ti);
  ms.ti = setInterval(() => {{
    document.getElementById('mTime').textContent = '⏱ ' + Math.floor((Date.now() - ms.t0) / 1000) + 's';
  }}, 500);
}}

function flip(i) {{
  if (ms.flipped.length >= 2 || ms.matched.includes(i) || ms.flipped.includes(i)) return;
  const el = document.getElementById('mc' + i);
  if (el) el.classList.add('flip');
  ms.flipped.push(i);
  sfxTick();

  if (ms.flipped.length === 2) {{
    ms.moves++;
    document.getElementById('mMoves').textContent = 'Moves: ' + ms.moves;
    const [a, b] = ms.flipped;
    if (ms.cards[a] === ms.cards[b]) {{
      setTimeout(() => {{
        const elA = document.getElementById('mc' + a);
        const elB = document.getElementById('mc' + b);
        if (elA) elA.classList.add('done');
        if (elB) elB.classList.add('done');
        ms.matched.push(a, b);
        ms.flipped = [];
        sfxOk();
        document.getElementById('mPairs').textContent = 'Pairs: ' + (ms.matched.length / 2) + '/' + ms.pairs;
        if (ms.matched.length === ms.cards.length) {{
          clearInterval(ms.ti);
          const t = Math.floor((Date.now() - ms.t0) / 1000);
          boom(3000);
          sfxWin();
          setTimeout(() => alert(`🏆 All matched!\nMoves: ${{ms.moves}} | Time: ${{t}}s`), 400);
          document.getElementById('mSetup').style.display = 'block';
          document.getElementById('mGame').style.display = 'none';
        }}
      }}, 350);
    }} else {{
      setTimeout(() => {{
        const elA = document.getElementById('mc' + a);
        const elB = document.getElementById('mc' + b);
        if (elA) elA.classList.remove('flip');
        if (elB) elB.classList.remove('flip');
        ms.flipped = [];
        sfxNo();
      }}, 700);
    }}
  }}
}}

// ==========================================
// GAME 5: RAPID FIRE
// ==========================================
function startRapid() {{
  const pool = getRapidDeck();
  rs = {{ pool: pool, i: 0, ok: 0, no: 0, timer: null }};
  document.getElementById('rSetup').style.display = 'none';
  document.getElementById('rGame').style.display = 'block';
  document.getElementById('rEnd').style.display = 'none';

  let tl = 60;
  document.getElementById('rTimer').textContent = '60';
  document.getElementById('rBar').style.width = '100%';
  document.getElementById('rTimer').style.color = 'var(--pink)';
  clearInterval(rs.timer);
  rs.timer = setInterval(() => {{
    tl -= 0.1;
    if (tl <= 0) {{
      clearInterval(rs.timer);
      endRapid();
      return;
    }}
    document.getElementById('rTimer').textContent = Math.ceil(tl);
    document.getElementById('rBar').style.width = (tl / 60 * 100) + '%';
  }}, 100);
  showR();
}}

function showR() {{
  if (rs.i >= rs.pool.length) rs.i = 0;
  const cur = rs.pool[rs.i];
  document.getElementById('rCatTag').textContent = cur.tag || '⚡ TRIVIA';
  document.getElementById('rText').textContent = cur.q;
  document.getElementById('rRight').textContent = '✅ ' + rs.ok;
  document.getElementById('rWrong').textContent = '❌ ' + rs.no;
}}

function rapidAns(v) {{
  if (!rs.pool || !rs.pool[rs.i]) return;
  if (v === rs.pool[rs.i].a) {{
    rs.ok++;
    sfxOk();
  }} else {{
    rs.no++;
    sfxNo();
  }}
  rs.i++;
  showR();
}}

function endRapid() {{
  clearInterval(rs.timer);
  document.getElementById('rGame').style.display = 'none';
  document.getElementById('rEnd').style.display = 'block';
  document.getElementById('rEndTitle').textContent = rs.ok >= 14 ? '🔥 Mastermind!' : (rs.ok >= 8 ? '⚡ Great Reflexes!' : '💪 Good Attempt!');
  document.getElementById('rEndMsg').textContent = `${{rs.ok}} correct, ${{rs.no}} wrong out of 60 seconds!`;
  if (rs.ok >= 10) {{
    boom(3000);
    sfxWin();
  }}
}}

function resetRapid() {{
  document.getElementById('rSetup').style.display = 'block';
  document.getElementById('rGame').style.display = 'none';
  document.getElementById('rEnd').style.display = 'none';
}}

// ==========================================
// GAME 6: SPIN THE WHEEL
// ==========================================
function drawWheel() {{
  const cv = document.getElementById('wheelCanvas');
  if (!cv) return;
  const c = cv.getContext('2d');
  const cx = 180, cy = 180, r = 170;
  const sa = Math.PI * 2 / WSegs.length;
  c.clearRect(0, 0, 360, 360);

  WSegs.forEach((s, i) => {{
    const a1 = wAngle + i * sa;
    const a2 = a1 + sa;
    c.beginPath();
    c.moveTo(cx, cy);
    c.arc(cx, cy, r, a1, a2);
    c.closePath();
    c.fillStyle = s.c;
    c.fill();
    c.strokeStyle = '#1a1a2e';
    c.lineWidth = 2.5;
    c.stroke();

    c.save();
    c.translate(cx, cy);
    c.rotate(a1 + sa / 2);
    c.fillStyle = '#fff';
    c.font = 'bold 11px Segoe UI, sans-serif';
    c.textAlign = 'center';
    c.fillText(s.t, r * .58, 4);
    c.restore();
  }});

  c.beginPath();
  c.arc(cx, cy, 22, 0, Math.PI * 2);
  c.fillStyle = '#1a237e';
  c.fill();
  c.strokeStyle = '#ffd700';
  c.lineWidth = 2.5;
  c.stroke();
  c.fillStyle = '#ffd700';
  c.font = 'bold 12px Segoe UI, sans-serif';
  c.textAlign = 'center';
  c.textBaseline = 'middle';
  c.fillText('NEX', cx, cy);
}}

function spin() {{
  if (wSpin) return;
  wSpin = true;
  document.getElementById('spinBtn').disabled = true;
  document.getElementById('wheelRes').textContent = '';
  const target = wAngle + (5 + Math.random() * 5) * Math.PI * 2;
  const dur = 4000;
  const t0 = Date.now();
  const a0 = wAngle;

  (function anim() {{
    const p = Math.min((Date.now() - t0) / dur, 1);
    const e = 1 - Math.pow(1 - p, 3);
    wAngle = a0 + (target - a0) * e;
    drawWheel();
    if (p < 1) {{
      requestAnimationFrame(anim);
    }} else {{
      wSpin = false;
      document.getElementById('spinBtn').disabled = false;
      const sa = Math.PI * 2 / WSegs.length;
      const na = (((-wAngle - Math.PI / 2) % (Math.PI * 2)) + Math.PI * 2) % (Math.PI * 2);
      const wi = Math.floor(na / sa) % WSegs.length;
      sfxWin();
      boom(2000);
      document.getElementById('wheelRes').innerHTML = `<span style="color:${{WSegs[wi].c}}">${{WSegs[wi].t}}</span>`;
    }}
  }})();
}}

// ==========================================
// INITIALIZATION
// ==========================================
drawWheel();
setTimeout(() => boom(2000), 500);
</script>
</body>
</html>
"""

with open("NexEdu_ChildrensDay_Games.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"Generated NexEdu_ChildrensDay_Games.html successfully! Size: {len(html_content)} bytes")
