import json

# Define the replacement rules for tag values
replacement_rules = {
    "'": "",
    '"': "'",
    "\n": "",
    '<': "",
    '</': "",
    '>': "",
    '@': "at",
    '[': "",
    ']': "",
    '`': "",
    '%': " ",
    '^': "",
    '{': "",
    '}': "",
    ';': "",
    '#': "",
    '(': "",
    ')': "",
    '=': " equal ",
    '/': "",
    '?': "",
    '!': "",
    '-': "",
    '+': " plus ",
    ':': "",
    "'": "",
    "$": "",
    "&": "",
    "*": "",
    "_": "",
    "/": "",
    "\\": "",
    "|": "",
    "é": "e",
    ",": ""
}

# Read the original data from 'alpaca_gpt4_data.json'
with open('alpaca_gpt4_data.json', 'r', encoding="utf-8") as json_file:
    json_load = json.load(json_file)

# Modify and write the data to 'tags.json'
with open('tags.json', 'w', encoding="utf-8") as f:
    f.write('{"tags": [\n')
    
    for x in json_load:
        instruction = x['instruction']
        for old, new in replacement_rules.items():
            instruction = instruction.replace(old, new)
        f.write('{"tag": "' + instruction + '"},\n')

    f.write(']}\n')

# Truncate and format the resulting JSON file
MYFILE = "tags.json"

with open(MYFILE, 'r', encoding="utf-8") as file:
    lines = file.readlines()
    open(MYFILE, 'w', encoding="utf-8").writelines(lines[:11703])

with open(MYFILE, 'r', encoding="utf-8") as file:
    lines = file.readlines()
    last_line = lines[-1].rstrip().replace(',', ']\n}')
    lines[-1] = last_line
    open(MYFILE, 'w', encoding="utf-8").writelines(lines)
