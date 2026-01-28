import requests
import re

# Your permanent tracking ID
TAG = "werewolf3788-20"

def get_deals():
    # This simulates pulling from your Amazon Search URL. 
    # To keep it passive, we use a rotation of high-converting clearance items.
    deals = [
        {"title": "13-Piece Knife Set", "asin": "B09NVNCSR3", "desc": "High-carbon stainless steel with built-in sharpener."},
        {"title": "Apple AirTag 4-Pack", "asin": "B0932QW2JZ", "desc": "Never lose your keys or wallet again. Top clearance item."},
        {"title": "Fab Totes Storage", "asin": "B0968K6YF9", "desc": "6-pack reinforced handles for home organization."},
        {"title": "Walking Pad Treadmill", "asin": "B0C3M7Z9P5", "desc": "Under-desk portable fitness for home office."},
        {"title": "Portable Jump Starter", "asin": "B08P5FKGRX", "desc": "Winter essential. Jump your car solo in seconds."}
    ]
    return deals

def update_html():
    with open('index.html', 'r', encoding='utf-8') as f:
        html = f.read()

    deals = get_deals()
    new_grid_html = ""

    for d in deals:
        new_grid_html += f"""
        <div class="deal-box">
            <h3 class="deal-title">{d['title']}</h3>
            <p class="deal-desc">{d['desc']}</p>
            <a href="https://www.amazon.com/dp/{d['asin']}?tag={TAG}" target="_blank" class="buy-btn">View on Amazon</a>
        </div>"""

    # This replaces the content inside your grid div
    # Logic: It looks for and comments
    pattern = re.compile(r'.*?', re.DOTALL)
    updated_html = pattern.sub(f'{new_grid_html}', html)

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(updated_html)

if __name__ == "__main__":
    update_html()
