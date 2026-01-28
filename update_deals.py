import os
import re

TAG = "werewolf3788-20"
HTML_FILE = "index.html"

def get_deals():
    # These are your active January 2026 Clearance items
    return [
        {"title": "13-Piece Knife Set", "asin": "B09NVNCSR3", "desc": "60% Off Clearance. Professional high-carbon steel."},
        {"title": "Apple AirTag 4-Pack", "asin": "B0932QW2JZ", "desc": "Never lose your gear. Limited time price drop."},
        {"title": "Under Desk Walking Pad", "asin": "B0C3M7Z9P5", "desc": "90% Price Drop. Portable treadmill for home office."},
        {"title": "Portable Car Jump Starter", "asin": "B08P5FKGRX", "desc": "Winter Essential. 2500A Peak emergency power."}
    ]

def update_site():
    if not os.path.exists(HTML_FILE):
        print(f"Error: {HTML_FILE} not found!")
        return

    with open(HTML_FILE, 'r', encoding='utf-8') as f:
        content = f.read()

    # SAFETY CHECK: If anchors aren't found, stop immediately.
    if "" not in content or "" not in content:
        print("CRITICAL ERROR: Comment anchors missing in index.html! Aborting update.")
        return

    deals = get_deals()
    grid_html = ""
    for d in deals:
        grid_html += f"""
        <div class="deal-box">
            <div class="deal-info">
                <h3 class="deal-title">{d['title']}</h3>
                <p class="deal-desc">{d['desc']}</p>
            </div>
            <a href="https://www.amazon.com/dp/{d['asin']}?tag={TAG}" target="_blank" class="buy-btn">View on Amazon</a>
        </div>"""

    # Use re.DOTALL to ensure it matches across multiple lines
    pattern = re.compile(r'.*?', re.DOTALL)
    new_content = pattern.sub(f'{grid_html}\n', content)

    with open(HTML_FILE, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Update successful! Items added to the grid.")

if __name__ == "__main__":
    update_site()
