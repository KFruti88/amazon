import os
import re
import sys

# Coding Standard: Amazon Affiliate
TAG = "werewolf3788-20"
HTML_FILE = "index.html"

def get_deals():
    return [
        {"title": "13-Piece Knife Set", "asin": "B09NVNCSR3", "desc": "60% Off Clearance. Professional carbon steel."},
        {"title": "Apple AirTag 4-Pack", "asin": "B0932QW2JZ", "desc": "Rare discount. Track your luggage and keys."},
        {"title": "Under Desk Walking Pad", "asin": "B0C3M7Z9P5", "desc": "90% Price Drop. Portable home office treadmill."},
        {"title": "Portable Car Jump Starter", "asin": "B08P5FKGRX", "desc": "2500A Peak emergency power. Car safety must-have."}
    ]

def update_site():
    # 1. Check if file even exists
    if not os.path.exists(HTML_FILE):
        print(f"Error: {HTML_FILE} not found. Check your file paths.")
        sys.exit(1)

    # 2. Read the file into memory
    with open(HTML_FILE, 'r', encoding='utf-8') as f:
        original_content = f.read()

    # 3. SAFETY CHECK: If anchors are missing, STOP IMMEDIATELY
    if "<!-- DEALS_START -->" not in original_content or "<!-- DEALS_END -->" not in original_content:
        print("CRITICAL ERROR: Comment anchors missing. Aborting to prevent file erasure!")
        # This exit code 1 tells GitHub the job failed, so it won't push a broken file
        sys.exit(1)

    # 4. Build the new HTML string
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

    # 5. Perform the swap in memory
    pattern = re.compile(r'([ \t]*)<!-- DEALS_START -->.*?<!-- DEALS_END -->', re.DOTALL)
    updated_content = pattern.sub(lambda m: f'{m.group(1)}<!-- DEALS_START -->{grid_html}\n{m.group(1)}<!-- DEALS_END -->', original_content)

    # 6. FINAL PROTECTION: Verify the new content is valid
    if len(updated_content) < (len(original_content) * 0.5):
        print("Safety check failed: Resulting file is too small. Something went wrong.")
        sys.exit(1)

    # 7. ONLY NOW do we open the file for writing
    with open(HTML_FILE, 'w', encoding='utf-8') as f:
        f.write(updated_content)
    
    print("Success: Amazon deals updated safely.")

if __name__ == "__main__":
    update_site()
