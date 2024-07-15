import re
import os
import sys
import string

sys.path.append('../')
from pyfunc.markdown.get_url_list import get_url_list
from pyfunc.markdown.get_dictionary_structure_from_headers_content import get_dictionary_structure_from_headers_content
from pyfunc.markdown.get_dictionary_structure_by_separator_list import get_dictionary_structure_by_separator_list
from pyfunc.markdown.get_code_extension_dict import get_code_extension_dict


# markdown_file
# source - path to source folder
# pattern - regular expression pattern for Markdown headers
def create_folders_files(markdown_file="",
                         path="",
                         pattern_list=[r'^#{1,6}\s+(.*)$', r'\[([^\]]+)\]\(([^)]+)\)'],
                         extension_list=['bash', 'php', 'js', 'javascript', 'shell', 'sh'],
                         extension_head_list={
                             'bash': '#!/bin/bash',
                             'shell': '#!/bin/shell',
                             'sh': '#!/bin/sh',
                             'php': '<?php'
                         }
                         ):
    markdown_data = get_dictionary_structure_from_headers_content(markdown_file)
    for section, content in markdown_data.items():
        # print(f"Section: {section}\nContent: {content}\n")
        # print(content.splitlines())
        # exit()
        # markdown_data = get_dictionary_structure_by_separator_list(content.splitlines())

        # print(markdown_data)
        # continue

        for url in get_url_list(section, pattern_list[1]):
            # print(path_folder)
            # exit()
            try:
                path_folder = os.path.join(path, str(url))

                if not os.path.exists(path_folder):
                    os.makedirs(path_folder)

                filename = 'README.md'
                path_file = os.path.join(path_folder, filename)
                # print(path_file)

                f = open(path_file, "w")
                f.write(content)
                f.close()

                result_list = get_code_extension_dict(content, extension_list, extension_head_list)
                # print(result_list)

                for item in result_list:
                    #print(item)
                    extension = item['extension']
                    filename = item['filename']
                    code = item['code']
                    print(extension, filename, code)
                    # print(item['code'])
                    path_file = os.path.join(path_folder, filename + '.' + extension)
                    f = open(path_file, "w")
                    f.write(code)
                    f.close()


            except Exception as e:
                print(e)
                continue


