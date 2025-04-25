import csv
import os
import re

CSV_FILE = os.path.join("Puzzles", "puzzle_data.csv")  # adjust if your file is named differently
OUTPUT_FOLDER = "Puzzles"

# Make sure the output directory exists
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

with open(CSV_FILE, newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile, delimiter='|')
    for row in reader:
        puzzle_num, title, iframe_input, should_generate = row

        if should_generate.strip().upper() != 'Y':
            continue

        # Extract iframe src URL
        match = re.search(r'src="([^"]+)"', iframe_input)
        iframe_src = match.group(1) if match else (iframe_input if iframe_input.startswith("http") else "")

        if not iframe_src:
            print(f"Skipping {puzzle_num}: Invalid iframe input")
            continue

        full_title = f"{puzzle_num} – {title}"
        filename = os.path.join(OUTPUT_FOLDER, f"{puzzle_num}.html")

        html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{full_title}</title>
  <link rel="icon" href="../favicon.png" type="image/png">
  <style>
    body {{
      font-family: Arial, sans-serif;
      margin: 0;
      text-align: center;
      background: #f9f9f9;
    }}
    iframe {{
      border: none;
      width: 100%;
      height: 700px;
      max-width: 900px;
      margin: 20px auto;
      display: block;
    }}
    .signup-form-container {{
      max-width: 500px;
      margin: 40px auto;
      background: #fff;
      padding: 20px;
      border-radius: 8px;
      box-shadow: 0 2px 8px rgba(0,0,0,0.1);
    }}
    #thank-you-message {{
      display: none;
      margin-top: 20px;
      color: #28a745;
      font-weight: bold;
      opacity: 0;
      transition: opacity 0.5s ease;
    }}
  </style>
</head>
<body>
  <a href="../index.html" style="position: absolute; top: 10px; left: 10px; font-size: 1.2rem; text-decoration: none; background: #eee; padding: 8px 12px; border-radius: 4px; color: #333;">← Home</a>
  <h1>{full_title}</h1>
  <iframe 
    src="{iframe_src}" 
    allow="web-share; fullscreen"
    aria-label="Puzzle Me Game">
  </iframe>

  <div class="signup-form-container">
  <form id="signup-form" action="https://formspree.io/f/xvgapvlk" method="POST">
    <label style="display: block; margin-bottom: 10px; font-weight: bold;">
      Notify me for new crosswords?
      <input type="email" name="email" required placeholder="you@example.com" style="width: 90%; padding: 10px; margin-top: 5px; border: 1px solid #ccc; border-radius: 4px; box-sizing: border-box;" />
    </label>
    <button type="submit" style="padding: 10px 20px; background: #333; color: white; border: none; border-radius: 4px; cursor: pointer;">
      Subscribe
    </button>
    <div id="thank-you-message" style="display: none; margin-top: 20px; color: #28a745; font-weight: bold; opacity: 0; transition: opacity 0.4s ease;">
      Thank you for signing up! You'll be notified about new crosswords.
    </div>
  </form>
</div>

<script>
  document.getElementById('signup-form').addEventListener('submit', async function (event) {
    event.preventDefault();

    const form = event.target;
    const data = new FormData(form);
    const thankYouMessage = document.getElementById('thank-you-message');

    try {
      const response = await fetch(form.action, {
        method: form.method,
        body: data,
        headers: { 'Accept': 'application/json' }
      });

      if (response.ok) {
        thankYouMessage.style.display = 'block';
        setTimeout(() => {
          thankYouMessage.style.opacity = '1';
        }, 10);
        form.reset();
      } else {
        alert('Oops! Something went wrong. Please try again.');
      }
    } catch (error) {
      alert('Network error. Please try again later.');
    }
  });
</script>

  <script>
    function handleFormSubmit(event) {{
      event.preventDefault();
      const successMessage = document.getElementById('thank-you-message');
      successMessage.style.display = 'block';
      setTimeout(() => {{
        successMessage.style.opacity = '1';
      }}, 10);
      document.getElementById('signup-form').reset();
    }}
  </script>
</body>
</html>
"""
        with open(filename, "w", encoding="utf-8") as f:
            f.write(html_content)
            print(f"✅ Created {filename}")
