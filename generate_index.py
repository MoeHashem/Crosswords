import os

PUZZLE_FOLDER = "Puzzles"
ICON_SUFFIX = "_icon.PNG"
OUTPUT_FILE = "index.html"

puzzle_files = sorted([f for f in os.listdir(PUZZLE_FOLDER) if f.endswith(".html")])

with open(OUTPUT_FILE, "w") as f:
    f.write("""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>All My Crossword Puzzles</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            text-align: center;
            margin: 0;
            padding: 0;
        }
        .puzzle-list {
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
            margin-top: 20px;
        }
        .puzzle-item {
            margin: 10px;
            width: 150px;
        }
        .puzzle-item a {
            text-decoration: none;
            color: black;
            display: block;
            text-align: center;
        }
        .puzzle-item img {
            width: 100%;
            height: auto;
        }
    </style>
</head>
<body>
    <h1>All My Crossword Puzzles</h1>
    <div class="puzzle-list">
""")

    for file in puzzle_files:
        name = os.path.splitext(file)[0]
        icon = f"{name}_icon.PNG"
        path = f"{PUZZLE_FOLDER}/{file}"
        f.write(f"""        <div class="puzzle-item">
            <a href="{path}">
                <img src="{icon}" alt="{name}">
                <p>{name}</p>
            </a>
        </div>
""")

    f.write("""    </div>
</body>
</html>""")
