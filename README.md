# 🎈 Nex Edu Classes — Children's Day Games App (2026)

An interactive, 100% offline indoor game suite developed for **Nex Edu Classes** for their Children's Day celebration.

It features 6 games packed with content, dynamic randomization, offline audio synthesis, tablet-optimized responsive design, and a ready-to-install Android APK.

---

## 🎮 Included Games

1. **🏆 Quiz (157 Questions)**:
   - Covers Indian current affairs, sports (Cricket World Cup, ISL, Olympics, Badminton), Chandrayaan, science, and general knowledge.
   - Questions and options are shuffled each round.
   - Timed rounds with instant feedback and scoreboards.

2. **🎬 Guess The Movie (64 Bollywood & Blockbuster Movies)**:
   - Emoji puzzle solver (e.g. 🦁👑 for The Lion King, 🚂❤️ for DDLJ, 🤫🤫 for Chup Chup Ke).
   - Non-repeating deck and dynamic multiple-choice options.

3. **⚡ Rapid Fire (100 Questions)**:
   - Fast-paced 45-second True/False challenge.
   - Tricky questions spanning Indian records, world geography, history, and science.

4. **🎡 Spin The Wheel**:
   - Easy, fun prompts and dares tailored for students:
     - 🎤 *Sing a song*
     - 🎬 *Guess a movie name*
     - ❓ *Answer any fun question*
     - 😂 *Share your last funny moment*
     - 🌟 *Most memorable day of your life*
     - 🎁 *One thing from your wishlist*
   - Side-by-side tablet layout so the wheel and results remain in view simultaneously.

5. **🔠 Word Scramble (80+ Words)**:
   - Unscramble words across Animals, Science, and School topics with hints.

6. **🧠 Memory Match**:
   - 8 pairs (16 tiles) memory game with responsive touch cards and flip animations.

---

## 📱 Tablet & Android Optimizations

- **Universal Responsiveness**: Smoothly adapts from small mobile screens to 7", 8", 10", and 12"+ tablets in both **landscape and portrait** orientations.
- **Hardware-Accelerated Fullscreen**: Runs borderless and immersive on Android tablets without clipping or overflow.
- **100% Offline Audio**: Employs Web Audio API synthesis for victory fanfares, correct chimes, and buzzers — no external audio files required.
- **Branded Asset**: Official Nex Edu Classes high-resolution logo integrated across the app header and Android launcher mipmaps.

---

## 📂 Repository Contents

| File / Folder | Description |
| :--- | :--- |
| **`NexEdu_ChildrensDay_2026.apk`** | Ready-to-install Android application package (~465 KB). |
| **`NexEdu_ChildrensDay_Games.html`** | Standalone, single-file HTML5 web application. |
| **`build_apk.py`** | Automated build pipeline (compiles Java, links resources via AAPT2, converts to DEX via D8, zipaligns, and signs with apksigner). |
| **`generate_perfect_game.py`** | Master generator script that compiles the HTML with embedded assets and question banks. |
| **`update_banks.py`** | Source question banks (157 quiz questions, 64 movies, 100 rapid fire prompts). |
| **`logo.jpg`** | Official Nex Edu Classes logo asset. |

---

## 🚀 How to Run

### Option 1: Install APK on Android Tablet / Phone
1. Download `NexEdu_ChildrensDay_2026.apk` directly from this repository onto your Android device.
2. Tap the APK file to install (enable "Install from unknown sources" if prompted).
3. Open **Nex Edu Games** from your app drawer.

### Option 2: Run in Any Web Browser
Simply double-click or open `NexEdu_ChildrensDay_Games.html` in Chrome, Edge, Safari, or Firefox on any PC, laptop, projector, or tablet browser. No internet connection required!
