import os

PUZZLE_FOLDER = "Puzzles"
ICON_FOLDER = "Icons"
OUTPUT_FILE = "index.html"

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
      overflow: hidden;
      text-decoration: none;
      color: inherit;
    }
    .card:hover {
      transform: translateY(-5px);
    }
    .icon-wrapper {
      width: 100%;
      aspect-ratio: 1 / 1;
      background: white;
      display: flex;
      align-items: center;
      justify-content: center;
    }
    .icon-wrapper img {
      max-width: 90%;
      max-height: 90%;
      object-fit: contain;
    }
    .card p {
      margin: 10px;
      font-weight: bold;
      color: #333;
    }
  </style>
</head>
<body>
  <header>
    <h1>My Crossword Collection</h1>
  </header>
  <div class="grid">
""")

    for file in puzzle_files:
        name = os.path.splitext(file)[0]
        cw_number = name.split("-")[0].strip()
        icon_path = f"{ICON_FOLDER}/{cw_number}_icon.png"
        puzzle_path = f"{PUZZLE_FOLDER}/{file}"

        f.write(f"""    <a href="{puzzle_path}" class="card">
      <div class="icon-wrapper">
        <img src="{icon_path}" alt="{cw_number} icon">
      </div>
      <p>{name}</p>
    </a>
""")

    f.write("""  </div>
</body>
</html>
""")
