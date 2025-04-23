Ideas:
- Difficulty rating system? Have users rate out of 5 or just mark it myself. If added, implement search.sort by difficulty on main page
- User sign up for new uploads
- A way to check how many times each puzzle has been solved?



🧩 My Crossword Collection

This repository auto-generates a homepage for all your embedded PuzzleMe crosswords. It’s perfect for managing and sharing your puzzle collection in a clean and beautiful layout — all hosted via GitHub Pages and auto-updated with GitHub Actions.

---

✍️ How to Add a New Puzzle

1. Create your puzzle on PuzzleMe  
   Go to https://puzzleme.com/ and create your crossword.

2. Copy the embed iframe  
   In PuzzleMe, go to Share > Embed and copy the <iframe> snippet.

3. Use the HTML generator  
   Paste your iframe into your HTML puzzle generator page (or use the provided template below), give it a custom title, and copy the generated HTML.

4. Save the puzzle HTML  
   Save the HTML file into the /Puzzles folder using the format:  
   CWX - Custom Name.html  
   Example: Puzzles/CW5 - Coffee Craze.html

5. Download the puzzle icon  
   From the Print section in PuzzleMe, download the crossword grid image.

6. Save the icon  
   Save it into the /Icons folder using this format:  
   CWX_icon.png  
   Example: Icons/CW5_icon.png

---

⚙️ What Happens Next?

A GitHub Action automatically runs whenever:
- A new puzzle is added
- A new icon is added
- You push changes to the Puzzles/ or Icons/ folders

✅ The Python script does the following:
- Scans all .html files in the /Puzzles folder.
- Extracts the puzzle number from each filename.
- Looks for a matching icon in /Icons using the format CWX_icon.png.
- Falls back to Icons/default_icon.png if none is found.
- Generates a responsive index.html homepage grid with:
  - Square icons (resized and padded if needed)
  - Puzzle title below each icon
  - Clickable links to each puzzle

No manual edits to index.html are ever needed!

---

🧪 HTML Puzzle Template

Here’s a quick template you can copy to manually generate your puzzle HTML (after grabbing the iframe):

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
    <!-- Paste your iframe below -->
    <iframe src="https://puzzleme.amuselabs.com/pmm/..." allow="fullscreen" aria-label="Puzzle Me Game"></iframe>
  </div>
</body>
</html>

---

🚀 Deployment

Your site is automatically deployed via Netlify (or GitHub Pages, depending on setup). The index.html is re-generated and pushed whenever new puzzles are added.

---

📂 Folder Structure

/Puzzles        → Contains all puzzle HTML files  
/Icons          → Contains puzzle icons (named CWX_icon.png)  
generate_index.py → Python script that builds index.html  
index.html      → Auto-generated homepage showing all puzzles

---

Happy puzzling! 🧠🖤
