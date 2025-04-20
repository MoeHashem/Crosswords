import os
import random

PUZZLE_FOLDER = "Puzzles"
ICON_FOLDER = "Icons"
AD_FOLDER = "Ads"
OUTPUT_FILE = "index.html"
DEFAULT_ICON = f"{ICON_FOLDER}/default_icon.png"

puzzle_files = sorted([f for f in os.listdir(PUZZLE_FOLDER) if f.endswith(".html")])

# Pick a random ad from the Ads folder
ad_images = [f for f in os.listdir(AD_FOLDER) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]

with open(OUTPUT_FILE, "w") as f:
    # --- Start of HTML ---
    f.write(f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Crossword Collection</title>
  <style>
    body {{
      font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
      margin: 0;
      padding: 0;
      background: #f9f9f9;
    }}
    header {{
      background-color: #333;
      color: #fff;
      padding: 20px;
      text-align: center;
    }}
    h1 {{
      margin: 0;
      font-size: 2em;
    }}
    .container {{
      display: flex;
      justify-content: center;
      align-items: flex-start;
      padding: 30px;
      gap: 30px;
      flex-wrap: wrap;
    }}
    .grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
      gap: 20px;
      max-width: 1000px;
      flex: 1 1 600px;
    }}
    .ad {{
  width: 200px;
  max-width: 90vw;
  flex-shrink: 0;
  margin-top: 20px;
  min-height: 200px; /* NEW: ensures there's always space for the ad */
  border: 2px dashed #ccc; /* Optional: helps you see if the ad container is rendering */
  display: flex;
  align-items: center;
  justify-content: center;
}}
    .card {{
      background: white;
      border-radius: 10px;
      box-shadow: 0 2px 8px rgba(0,0,0,0.1);
      transition: transform 0.2s;
      text-align: center;
      padding: 15px;
      position: relative;
    }}
    .card:hover {{
      transform: translateY(-5px);
    }}
    .icon-wrapper {{
      width: 100%;
      aspect-ratio: 1 / 1;
      background: #fff;
      display: flex;
      justify-content: center;
      align-items: center;
      overflow: hidden;
      border-radius: 8px;
    }}
    .icon-wrapper img {{
      max-width: 100%;
      max-height: 100%;
      object-fit: contain;
      background-color: white;
    }}
    .card p {{
      margin-top: 10px;
      font-weight: bold;
      color: #333;
    }}
    a {{
      text-decoration: none;
      color: inherit;
    }}
    .floating-btn {{
      position: fixed;
      bottom: 20px;
      right: 20px;
      background-color: #333;
      color: #fff;
      padding: 10px 20px;
      border-radius: 50px;
      cursor: pointer;
      font-size: 1rem;
    }}
  </style>
</head>
<body>
  <header>
    <h1>Moe's Mighty Crossword Collection</h1>
  </header>

  <div class="container">
    <div class="grid">
""")

    # --- Puzzle grid cards ---
    for file in puzzle_files:
        name = os.path.splitext(file)[0]  # e.g., "CW1 - Humblex"
        cw_number = name.split("-")[0].strip()
        icon_file = f"{cw_number}_icon.png"
        icon_path = f"{ICON_FOLDER}/{icon_file}"

        if not os.path.exists(icon_path):
            icon_path = DEFAULT_ICON

        puzzle_path = f"{PUZZLE_FOLDER}/{file}"

        f.write(f"""      <a href="{puzzle_path}" class="card">
        <div class="icon-wrapper">
          <img src="{icon_path}" alt="{name} icon">
        </div>
        <p>{name}</p>
      </a>
""")

    # --- Ad slot and floating button ---
    f.write("""    </div> <!-- .grid -->
  </div> <!-- .container -->

  <!-- Floating button to pick random puzzle -->
  <button class="floating-btn" onclick="pickRandomPuzzle()">Pick a Random Puzzle</button>

  <!-- Ad Slot -->
  <div class="ad" id="ad-slot">
    <!-- Ad will be inserted here by JS -->
  </div>

  <script>
    function pickRandomPuzzle() {
      const puzzles = document.querySelectorAll('.grid a.card');
      if (puzzles.length === 0) {
        alert("No puzzles found!");
        return;
      }
      const randomPuzzle = puzzles[Math.floor(Math.random() * puzzles.length)];
      window.location.href = randomPuzzle.getAttribute('href');
    }

    window.onload = function() {
      console.log('Page loaded');
""")

    # --- Write JS ad array using Python ---
    js_ad_array = ",\n      ".join([f'"{AD_FOLDER}/{ad}"' for ad in ad_images])
    f.write(f"""
      const ads = [
        {js_ad_array}
      ];
""")

    # --- Static JS for ad display ---
    f.write("""
      if (ads.length > 0) {
        console.log('Random ad selected');
        const randomAd = ads[Math.floor(Math.random() * ads.length)];
        const adHTML = `
          <a href="https://www.youtube.com/watch?v=o-YBDTqX_ZU&ab_channel=MusRest" target="_blank">
            <img src="${randomAd}" alt="Sponsored Ad" style="width:100%; border-radius:8px;">
          </a>`;
        document.getElementById('ad-slot').innerHTML = adHTML;
      } else {
        console.log('No ads found');
      }
    };  // End of window.onload
  </script>
</body>
</html>
""")
