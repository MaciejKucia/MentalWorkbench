import os
import re
import sys

def dokuwiki_to_markdown(text):
    # Headings
    text = re.sub(r'======\s*(.*?)\s*======', r'# \1', text)
    text = re.sub(r'=====\s*(.*?)\s*=====', r'## \1', text)
    text = re.sub(r'====\s*(.*?)\s*====', r'### \1', text)
    text = re.sub(r'===\s*(.*?)\s*===', r'#### \1', text)

    # Bold/Italic
    text = re.sub(r"'''(.*?)'''", r'**\1**', text)
    text = re.sub(r"''(.*?)''", r'*\1*', text)

    # Unordered lists
    text = re.sub(r'^\s*\*\s+', r'* ', text, flags=re.MULTILINE)

    # Ordered lists
    text = re.sub(r'^\s*-\s+', r'1. ', text, flags=re.MULTILINE)

    # Links
    text = re.sub(r'\[\[(https?://[^\|\]]+)\|([^\]]+)\]\]', r'[\2](\1)', text)
    text = re.sub(r'\[\[(https?://[^\]]+)\]\]', r'<\1>', text)

    # Images
    text = re.sub(r'\{\{(.*?)(\|.*?)?\}\}', r'![alt](\1)', text)

    # Code blocks (with <code> tags)
    text = re.sub(r'<code(?: [^>]*)?>', '```', text)
    text = re.sub(r'</code>', '```', text)

    return text

def convert(filename):
    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()

    md_content = dokuwiki_to_markdown(content)

    output_path = filename.replace(".txt", ".md")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(md_content)

    print(f"Converted {filename} -> {os.path.basename(output_path)}")

convert(sys.argv[1])
