import os

# Tracking ID: werewolf3788-20
# THIS SCRIPT ONLY TOUCHES amazon.html. IT CANNOT SEE index.html.
DEALS_FILE = "amazon.html"

def get_deals():
    return [
        {"title": "13-Piece Professional Knife Set", "asin": "B09NVNCSR3", "desc": "60% Off Clearance. High-carbon stainless steel."},
        {"title": "Apple AirTag 4-Pack", "asin": "B0932QW2JZ", "desc": "Rare discount. Track your gear with ease."},
        {"title": "Under Desk Walking Pad", "asin": "B0C3M7Z9P5", "desc": "90% Price Drop. Portable treadmill."},
        {"title": "Portable Car Jump Starter", "asin": "B08P5FKGRX", "desc": "2500A Peak emergency power. Essential gear."}
    ]

def create_snippet():
    deals = get_deals()
    html_content = ""
    
    for d in deals:
        html_content += f"""
<div class="deal-box">
    <div class="deal-info">
        <h3 class="deal-title">{d['title']}</h3>
        <p class="deal-desc">{d['desc']}</p>
    </div>
    <a href="https://www.amazon.com/dp/{d['asin']}?tag=werewolf3788-20" target="_blank" class="buy-btn">View Details</a>
</div>\n"""

    with open(DEALS_FILE, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print(f"✅ Success: {DEALS_FILE} updated. index.html remains untouched.")

if __name__ == "__main__":
    create_snippet()
