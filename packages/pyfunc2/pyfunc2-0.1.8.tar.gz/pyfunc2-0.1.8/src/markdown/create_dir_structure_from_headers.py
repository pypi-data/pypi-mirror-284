import re
import os
import sys

sys.path.append('../')
from pyfunc.markdown.get_url_list import get_url_list
from pyfunc.markdown.get_header_list import get_header_list


# markdown_file
# source - path to source folder
# pattern - regular expression pattern for Markdown headers
def create_dir_structure_from_headers(markdown_file="",
                                      path="",
                                      pattern_list=[r'^#{1,6}\s+(.*)$', r'\[([^\]]+)\]\(([^)]+)\)']):
    with open(markdown_file, 'r') as file:
        markdown = file.read()

    for header in get_header_list(markdown, pattern_list[0]):
        #print(header)
        #exit()
        for url in get_url_list(header, pattern_list[1]):
            path_folder = os.path.join(path, str(url))
            #print(path_folder)
            #exit()
            if not os.path.exists(path_folder):
                os.makedirs(path_folder)


