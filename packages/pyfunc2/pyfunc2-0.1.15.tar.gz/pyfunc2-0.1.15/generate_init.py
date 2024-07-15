import os
import toml
import argparse
import re
from typing import List, Tuple
from path import Path


def bypyproject():
    # Load the pyproject.toml file
    with open("pyproject.toml", "r") as f:
        pyproject_data = toml.load(f)

    # Extract project information
    project_info = pyproject_data.get("project", {})
    version = project_info.get("version", "0.1.0")

    # Define the content of __init__.py
    init_content = f"""\
# Auto-generated __init__.py

# Version of the pyfunc2 package
__version__ = "{version}"

# Import necessary modules and functions here
"""

    # Create the __init__.py file in the appropriate directory
    package_dir = os.path.join("src", project_info["name"])
    os.makedirs(package_dir, exist_ok=True)

    # with open(os.path.join(package_dir, "__init__.py"), "w") as f:
    #    f.write(init_content)

    print(f"__init__.py generated at {os.path.join(package_dir, '__init__.py')}")
    return init_content


class_function_regex = re.compile(r'(?<!\s )(?:class|def)\s+(?P<name>\w+)')

local_import_regex = re.compile(r'(?<!\s )from \.\w+ import (?P<name>\w+)')


def find_importable_elements_from_files(root: Path) -> List[Tuple[str, str]]:
    result = []
    for file in root.files('*.py'):
        with open(file) as f:
            content = f.read()
        for match in class_function_regex.finditer(content):
            name = match.group('name')
            if name is not None:
                result.append((file.basename().replace('.py', ''), name))
    return result


def find_importable_elements_from_subfolders(root: Path) -> List[Tuple[str, str]]:
    result = []
    for subdir in root.dirs():
        if not (subdir / '__init__.py').exists():
            continue
        with open(subdir / '__init__.py') as f:
            content = f.read()
        for match in local_import_regex.finditer(content):
            name = match.group('name')
            if name is not None:
                result.append((subdir.basename(), name))
    return result


def template_initpy(imports: List[Tuple[str, str]]):
    template = bypyproject()
    for fname, elname in imports:
        template += f'from .{fname} import {elname}\n'

    template += '\n# Public API of the package'
    template += '\n__all__ = [' + ', '.join([elname for _, elname in imports]) + ']'
    return template


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--path', '-p', type=Path, required=False, dest='path', default=None)

    args = parser.parse_args()

    if args.path is None:
        args.path = Path('./').abspath()

    imports = find_importable_elements_from_files(args.path) + \
              find_importable_elements_from_subfolders(args.path)
    print('imports found:', '\n'.join([f'\t{a} - {b}' for a, b in imports]), sep='\n')
    init_content = template_initpy(imports)

    with open(args.path / '__init__.py', 'w') as f:
        f.write(init_content)


if __name__ == "__main__":
    main()
