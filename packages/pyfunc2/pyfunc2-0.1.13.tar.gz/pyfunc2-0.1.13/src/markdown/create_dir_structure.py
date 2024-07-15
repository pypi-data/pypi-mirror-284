import os
import mistune
from mistune import HTMLRenderer


def create_dir_structure(md_text, base_dir):
    # renderer = HeaderRenderer()
    # renderer = mistune.HTMLRenderer()
    renderer = mistune.HTMLRenderer()
    # markdown = mistune.Markdown(renderer, plugins=[strikethrough])
    markdown = mistune.Markdown(renderer)
    # markdown = mistune.Markdown(renderer=renderer)
    headers = markdown(md_text).split('\n')
    print(headers)

    for header in headers:
        if header:  # Exclude empty directories
            pathf = os.path.join(base_dir, header)
            print(pathf)
            os.makedirs(pathf, exist_ok=True)


def test(base_dir, filename):
    # Open and read markdown file
    with open(filename, "r") as md_file:
        md_text = md_file.read()

    create_dir_structure(md_text, base_dir)
