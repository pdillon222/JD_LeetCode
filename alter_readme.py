import os
import re

EASY = "#### Difficulty: ![#c5f015](https://via.placeholder.com/15/c5f015/000000?text=+) ```Easy```"
MEDIUM = "#### Difficulty: ![#1589F0](https://via.placeholder.com/15/1589F0/000000?text=+) ```Medium```"
HARD = "#### Difficulty: ![#f03c15](https://via.placeholder.com/15/f03c15/000000?text=+) ```Hard```"

def find_replace_difficulty_lines(_file):
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
    #print(f'Lines pre-swap -> {readme_lines}')
    readme_lines.remove(difficulty_line)
    readme_lines.insert(difficulty_index, swap_line)
    #print(f'Lines post-swap -> {readme_lines}')
    with open(_file, 'w+') as f:
        for line in readme_lines:
            f.write(line)

read_me = [os.path.join(dir, 'README.md')
           for dir in os.listdir()
           if re.match(r'^[A-Z]', dir)
           and os.path.isdir(dir)]

for _file in read_me[:1]:
    print(_file)
    find_replace_difficulty_lines(_file)
