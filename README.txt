Ideas:
- Difficulty rating system? Have users rate out of 5 or just mark it myself. If added, implement search.sort by difficulty on main page
- A way to check how many times each puzzle has been solved?

# 🧩 My Crossword Collection

This repository auto-generates both individual puzzle pages and a beautiful homepage for all your embedded PuzzleMe crosswords. Everything is managed cleanly using GitHub Actions, with automatic updates and hosting via GitHub Pages or Netlify.

---

## ✍️ How to Add a New Puzzle

1. **Create your puzzle on PuzzleMe**  
   Go to https://puzzleme.com/ and create your crossword.

2. **Copy the embed iframe**  
   In PuzzleMe, go to **Share > Embed**, and copy the `<iframe>` snippet.

3. **Add it to the puzzle CSV**  
   Open `Puzzles/puzzle_data.csv` and add a new line in this format:  
   ```
   CWX|Custom Puzzle Name|<iframe ...>|Y
   ```
   - Replace `CWX` with your puzzle number (e.g. CW10)
   - Replace the iframe with your copied embed
   - Set the last column to `Y` if you want the puzzle page to be (re)generated

4. **Download the puzzle icon**  
   From the **Print** section in PuzzleMe, download the crossword grid image.

5. **Save the icon**  
   Save it in the `/Icons` folder using the format:  
   ```
   CWX_icon.png
   ```
   Example: `Icons/CW10_icon.png`

6. **Commit your changes**  
   Push your update with the CSV and icon — everything else will happen automatically!

---

## ⚙️ What Happens Next?

Two GitHub Actions automatically run whenever you push:

- **Puzzle HTML Generator**  
  - Reads `puzzle_data.csv`
  - Generates or updates HTML puzzle pages for all rows marked `Y`
  - Saves them to `/Puzzles`

- **Homepage Index Builder**  
  - Scans all `.html` files in `/Puzzles`
  - Extracts puzzle numbers and titles
  - Matches icons from `/Icons`
  - Generates a polished `index.html` with:
    - Square puzzle icons
    - Puzzle titles below icons
    - Clickable links to each puzzle

💡 If no custom icon is found, it uses `Icons/default_icon.png`.

✅ No manual edits to HTML files needed — it's all handled automatically!

---

## 🧪 Manual HTML Template (Optional)

Want to hand-code a puzzle page? Here's a simple template (OR use the possibly outdated puzzle HTML generator.html):

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>CWX - Custom Puzzle Name</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      text-align: center;
      margin: 0;
      padding: 0;
    }
    iframe {
      border: none;
      width: 100%;
      max-width: 800px;
      height: 700px;
    }
  </style>
</head>
<body>
  <h1>CWX - Custom Puzzle Name</h1>
  <div style="margin: 20px;">
    <iframe src="https://puzzleme.amuselabs.com/pmm/..." allow="fullscreen" aria-label="Puzzle Me Game"></iframe>
  </div>
</body>
</html>
```

---

## 🚀 Deployment

Your site is automatically deployed via **Netlify** (or **GitHub Pages**, depending on your setup).

Any time you:
- Add or update puzzles via the CSV
- Add or update icons
- Manually commit puzzle pages

✅ The homepage (`index.html`) is auto-regenerated and published.

---

## 📂 Folder Structure

```
/Puzzles            → Auto-generated HTML pages for each puzzle  
/Icons              → Puzzle icon images (e.g. CW10_icon.png)  
Puzzles/puzzle_data.csv → Data source for puzzles to generate  
generate_index.py   → Script to build index.html  
generate_puzzle_html.py → Script to create individual puzzle HTMLs  
index.html          → Auto-generated homepage with puzzle grid
```

---

Happy puzzling! 🧠🖤
