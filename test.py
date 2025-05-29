from playwright.sync_api import sync_playwright

html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>don't render this part</title>
</head>
<body>
    <h1>did it work?</h1>
    <p> one more time! </p>
</body>
</html>
"""

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.set_content(html, wait_until="networkidle")
    page.pdf(path="./output/output.pdf", format="A4")
    browser.close()