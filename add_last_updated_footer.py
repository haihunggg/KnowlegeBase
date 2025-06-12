import subprocess
import os
from datetime import datetime

def get_last_editor_and_date(filepath):
    try:
        author = subprocess.check_output(
            ["git", "log", "-1", "--pretty=format:%an", filepath],
            encoding="utf-8"
        ).strip()

        date_str = subprocess.check_output(
            ["git", "log", "-1", "--pretty=format:%ad", "--date=short", filepath],
            encoding="utf-8"
        ).strip()

        date_obj = datetime.strptime(date_str, "%Y-%m-%d")
        date = date_obj.strftime("%b %d, %Y").replace(" 0", " ")
        return author, date
    except subprocess.CalledProcessError:
        return None, None

def add_footer(filepath, author, date):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read().strip()

    footer_html = (
        f'<div class="last-updated">'
        f'Last updated on <strong>{date}</strong> by <strong>{author}</strong>'
        f'</div>'
    )

    # Remove old footer if exists
    if "Last updated on" in content:
        content = "\n".join([
            line for line in content.splitlines()
            if "Last updated on" not in line
        ])

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content + "\n\n" + footer_html + "\n")

def main():
    for root, _, files in os.walk("docs"):
        for file in files:
            if file.endswith(".md"):
                filepath = os.path.join(root, file)
                author, date = get_last_editor_and_date(filepath)
                if author and date:
                    print(f"✔ {filepath} → {author}, {date}")
                    add_footer(filepath, author, date)

if __name__ == "__main__":
    main()
