import os

PUZZLE_FOLDER = "Puzzles"
ICON_FOLDER = "Icons"
OUTPUT_FILE = "index.html"
DEFAULT_ICON = f"{ICON_FOLDER}/default_icon.png"

puzzle_files = sorted([f for f in os.listdir(PUZZLE_FOLDER) if f.endswith(".html")])

with open(OUTPUT_FILE, "w") as f:
    f.write("""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Crossword Collection</title>
  <style>
    body {
      font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
      margin: 0;
      padding: 0;
      background: #f9f9f9;
    }
    header {
      background-color: #333;
      color: #fff;
      padding: 20px;
      text-align: center;
    }
    h1 {
      margin: 0;
      font-size: 2em;
    }
    .grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
      gap: 20px;
      padding: 30px;
      max-width: 1000px;
      margin: auto;
    }
    .card {
      background: white;
      border-radius: 10px;
      box-shadow: 0 2px 8px rgba(0,0,0,0.1);
      transition: transform 0.2s;
      text-align: center;
      padding: 15px;
      position: relative;
    }
    .card:hover {
      transform: translateY(-5px);
    }
    .icon-wrapper {
      width: 100%;
      aspect-ratio: 1 / 1;
      background: #fff;
      display: flex;
      justify-content: center;
      align-items: center;
      overflow: hidden;
      border-radius: 8px;
    }
    .icon-wrapper img {
      max-width: 100%;
      max-height: 100%;
      object-fit: contain;
      background-color: white;
    }
    .card p {
      margin-top: 10px;
      font-weight: bold;
      color: #333;
    }
    a {
      text-decoration: none;
      color: inherit;
    }
    /* Floating button styles */
    .floating-btn {
      position: fixed;
      bottom: 20px;
      right: 20px;
      background-color: #333;
      color: #fff;
      padding: 10px 20px;
      border-radius: 50px;
      cursor: pointer;
      font-size: 1rem;
    }
  </style>
</head>
<body>
  <header>
    <h1>Moe's Mighty Crossword Collection</h1>
  </header>
  <div class="grid">
""")

    for file in puzzle_files:
        name = os.path.splitext(file)[0]  # e.g., "CW1 - Humblex"
        cw_number = name.split("-")[0].strip()  # Gets "CW1"
        icon_file = f"{cw_number}_icon.png"
        icon_path = f"{ICON_FOLDER}/{icon_file}"

        if not os.path.exists(icon_path):
            icon_path = DEFAULT_ICON

        puzzle_path = f"{PUZZLE_FOLDER}/{file}"

        f.write(f"""    <a href="{puzzle_path}" class="card">
      <div class="icon-wrapper">
        <img src="{icon_path}" alt="{name} icon">
      </div>
      <p>{name}</p>
    </a>
""")

    f.write("""  </div>

  <!-- Email signup form -->
  <div style="max-width: 500px; margin: 40px auto; background: #fff; padding: 20px; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1);">
    <form action="https://formspree.io/f/xvgapvlk" method="POST">
      <label style="display: block; margin-bottom: 10px; font-weight: bold;">
        Sign up for crossword updates:
        <input type="email" name="email" required placeholder="you@example.com" style="width: 100%; padding: 10px; margin-top: 5px; border: 1px solid #ccc; border-radius: 4px;" />
      </label>
      <button type="submit" style="padding: 10px 20px; background: #333; color: white; border: none; border-radius: 4px; cursor: pointer;">
        Subscribe
      </button>
    </form>
  </div>

  <!-- Floating button to pick random puzzle -->
  <button class="floating-btn" onclick="pickRandomPuzzle()">Pick a Random Puzzle</button>

  <script>
  function pickRandomPuzzle() {
    const puzzles = document.querySelectorAll('.grid a.card');

    if (puzzles.length === 0) {
      console.log("No puzzles found!");
      alert("No puzzles found!");
      return;
    }

    const randomPuzzle = puzzles[Math.floor(Math.random() * puzzles.length)];
    const randomPuzzleUrl = randomPuzzle.getAttribute('href');

    console.log("Redirecting to:", randomPuzzleUrl);
    if (randomPuzzleUrl) {
      window.location.href = randomPuzzleUrl;
    } else {
      alert("Invalid puzzle link!");
    }
  }
</script>

</body>
</html>
""")
