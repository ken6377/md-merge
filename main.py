#Recursively retrieve all markdown files in the subdirectories of the specified path
import sys
import os

def get_markdown_files(path):
    markdown_files = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(".md"):
                markdown_files.append(os.path.join(root, file))
    return markdown_files

#merge the retrieved markdown_files and write them to merged.md
def merge_markdown_files(markdown_files):
    with open("merged.md", "w", encoding="utf-8") as merged:
        for file in markdown_files:
            with open(file, "r", encoding="utf-8") as f:
                merged.write(f.read() + "\n")

#main function
def main():
    path = sys.argv[1]
    markdown_files = get_markdown_files(path)
    merge_markdown_files(markdown_files)

if __name__ == "__main__":
    main()