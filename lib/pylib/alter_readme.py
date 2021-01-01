import os
import re


BASE_DIR = os.path.split(os.path.abspath(__file__))[0]
BASE_DIR = os.path.join(BASE_DIR.split('JD_LeetCode')[0], 'JD_LeetCode')
assert os.path.isdir(BASE_DIR), f'[Error]: {BASE_DIR} not recognized as directory'

EASY = "#### Difficulty: ![#c5f015](https://via.placeholder.com/15/c5f015/000000?text=+) ```Easy```"
MEDIUM = "#### Difficulty: ![#1589F0](https://via.placeholder.com/15/1589F0/000000?text=+) ```Medium```"
HARD = "#### Difficulty: ![#f03c15](https://via.placeholder.com/15/f03c15/000000?text=+) ```Hard```"


def find_replace_difficulty_lines(_file, dry_run=False):
    """
    Locates all directories containing LeetCode challenge problems
    Overwrites 'Difficulty' line of sub-dir README file, adding color coding for difficulty level

    Args:
        dry_run: (bool) - Set to True for verbose output of changes to be made
                          (with no actual file overwriting taking place)

    Notes:
        Use cautiously - script will overwrite existing files if dry_run == False
    """
    with open(_file, 'r') as f:
        readme_lines = [line for line in f.readlines()]
    difficulty_line = [line for line in readme_lines if line.startswith('#### Difficulty')][0]
    difficulty_index = readme_lines.index(difficulty_line)
    if 'Easy' in difficulty_line:
        swap_line = EASY
    elif 'Medium' in difficulty_line:
        swap_line = MEDIUM
    else:
        swap_line = HARD
    if dry_run: print(f'Lines pre-swap -> {readme_lines}')
    readme_lines.remove(difficulty_line)
    readme_lines.insert(difficulty_index, swap_line + '\n')
    if dry_run: print(f'Lines post-swap -> {readme_lines}')
    if not dry_run:
        with open(_file, 'w+') as f:
            for line in readme_lines:
                f.write(line)

read_me = [os.path.join(os.path.join(BASE_DIR, dir), 'README.md')
           for dir in os.listdir(BASE_DIR)
           if re.match(r'^[A-Z]', os.path.split(dir)[-1])
           and os.path.isdir(os.path.join(BASE_DIR, dir))]

for _file in read_me[:]:
    print(_file)
    #find_replace_difficulty_lines(_file, dry_run=True)
