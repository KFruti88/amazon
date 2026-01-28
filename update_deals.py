import json
import os

# Coding Standard: Amazon Affiliate Automation
# Tracking ID: werewolf3788-20
# This script creates a separate data file so index.html remains untouched.

DATA_FILE = "amazon-deals.json"

def get_clearance_deals():
    """
    Returns the current list of Amazon Clearance items.
    Focus: High-Yield Targets & 24-hour cookie activation.
    """
    return [
        {
            "title": "13-Piece Professional Knife Set",
            "asin": "B09NVNCSR3",
            "desc": "60% Off Clearance. High-carbon stainless steel with built-in sharpener. Perfect for home chefs."
        },
        {
            "title": "Apple AirTag 4-Pack",
            "asin": "B0932QW2JZ",
            "desc": "Rare discount on the 4-pack. Track your keys, luggage, and gear with the Find My app."
        },
        {
            "title": "Under Desk Walking Pad",
            "asin": "B0C3M7Z9P5",
            "desc": "90% Price Drop. Slim portable treadmill for home office fitness. Stay active while you work."
        },
        {
            "title": "Portable Car Jump Starter",
            "asin": "B08P5FKGRX",
            "desc": "Winter Essential. 2500A Peak emergency power for dead batteries. Includes LED flashlight."
        }
    ]

def update_data_file():
    try:
        deals = get_clearance_deals()
        
        # Save as a clean JSON file
        # If this fails, it only affects the 'amazon-deals.json' file
        with open(DATA_FILE, 'w', encoding='utf-8') as f:
            json.dump(deals, f, indent=4)
        
        print(f"✅ Success: {DATA_FILE} has been updated with {len(deals)} items.")
        print("🛡️ Safety Check: index.html was not touched.")

    except Exception as e:
        print(f"❌ Error during update: {e}")

if __name__ == "__main__":
    update_data_file()
