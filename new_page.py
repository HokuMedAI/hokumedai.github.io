#!/usr/bin/env python3
import subprocess
import sys
from datetime import datetime
import re

def main():
    # Select page type
    print("\nSelect page type:")
    print("1. Article")
    print("2. Seminar")
    print("3. Mokumoku")
    print("4. Meeting")
    print("5. Other (default)")
    
    page_type = input("\nEnter number (1-5): ")
    
    # Set page type
    type_map = {
        "1": "article",
        "2": "seminar",
        "3": "mokumoku",
        "4": "meeting",
        "5": "default"
    }
    
    if page_type in type_map:
        page_kind = type_map[page_type]
    else:
        print("Invalid selection. Using default.")
        page_kind = "default"
    
    # Build path based on type
    if page_kind == "article":
        print("\nEnter path for article (e.g., new_series/new_page)")
        print("Example: new_series/new_page/index.md")
        article_path = input("\nEnter path: ")
        path = f"content/articles/{article_path}/index.md"
        date = None
    else:
        # Get date input for non-article types
        today = datetime.now().strftime("%Y-%m-%d")
        date_input = input(f"\nEnter date (YYYY-MM-DD) [default: {today}]: ")
        date = today if date_input == "" else date_input
        path = f"content/activities/{page_kind}/{date}/index.md"
    
    # Execute Hugo command
    print(f"\nWill execute the following command:")
    print(f"hugo new {path} --kind {page_kind}")
    confirm = input("\nProceed? (y/n): ")
    
    if confirm.lower() == "y":
        try:
            # Create new page
            subprocess.run(["hugo", "new", path, "--kind", page_kind], check=True)
            
            # Update date in front matter if it's not an article
            if page_kind != "article" and date:
                try:
                    with open(path, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    # Replace the date line
                    content = re.sub(r'date: .*', f'date: {date}', content)
                    
                    with open(path, 'w', encoding='utf-8') as f:
                        f.write(content)
                except FileNotFoundError:
                    print(f"Warning: Could not update date in {path}")
            
            print(f"\nPage created: {path}")
            
        except subprocess.CalledProcessError as e:
            print(f"Error executing hugo command: {e}")
            sys.exit(1)
        except Exception as e:
            print(f"Error: {e}")
            sys.exit(1)
    else:
        print("\nOperation cancelled.")

if __name__ == "__main__":
    main()