import os
import re

# Safely update index.html
def safe_update_html(new_content):
    with open('index.html', 'r', encoding='utf-8') as f:
        full_html = f.read()

    # Safety Check 1: Ensure anchors exist
    if "" not in full_html or "" not in full_html:
        print("Safety Triggered: Comment anchors missing. Skipping update.")
        return

    # Safety Check 2: Don't replace with nothing
    if not new_content.strip():
        print("Safety Triggered: New content is empty. Skipping update.")
        return

    pattern = re.compile(r'.*?', re.DOTALL)
    updated_html = pattern.sub(f'\n{new_content}\n', full_html)

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(updated_html)
