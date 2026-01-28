import os
import re

TAG = "werewolf3788-20"
HTML_FILE = "index.html"

def get_deals():
    return [
        {"title": "13-Piece Knife Set", "asin": "B09NVNCSR3", "desc": "60% Off Clearance. High-carbon stainless steel."},
        {"title": "Apple AirTag 4-Pack", "asin": "B0932QW2JZ", "desc": "Never lose your gear again. Limited time discount."},
        {"title": "Under Desk Walking Pad", "asin": "B0C3M7Z9P5", "desc": "90% Price Drop. Stay active while working from home."},
        {"title": "Portable Car Jump Starter", "asin": "B08P5FKGRX", "desc": "Winter Essential. 2500A Peak emergency power."}
    ]

def update_html():
    if not os.path.exists(HTML_FILE):
        return

    with open(HTML_FILE, 'r', encoding='utf-8') as f:
        content = f.read()

    # Create Sideways/Glossy HTML
    deals = get_deals()
    new_html = "\n"
    for d in deals:
        new_html += f"""        <div class="deal-box">
            <div class="deal-info">
                <h3 class="deal-title">{d['title']}</h3>
                <p class="deal-desc">{d['desc']}</p>
            </div>
            <a href="https://www.amazon.com/dp/{d['asin']}?tag={TAG}" target="_blank" class="buy-btn">View on Amazon</a>
        </div>\n"""

    # Fail-safe check for anchors
    if "" not in content or "" not in content:
        print("ERROR: Anchors missing! File was not changed to prevent erasing data.")
        return

    pattern = re.compile(r'.*?', re.DOTALL)
    updated = pattern.sub(f'{new_html}        ', content)

    with open(HTML_FILE, 'w', encoding='utf-8') as f:
        f.write(updated)
    print("Grid updated successfully!")

if __name__ == "__main__":
    update_html()
