import json

# Define the paths for input and output JSON files
input_json_file_path = 'alpaca_gpt4_data.json'
output_json_file_path = 'intents.json'

# Read the input data from the input JSON file
with open(input_json_file_path, 'r') as input_json_file:
    input_data = json.load(input_json_file)

# Process the input data and create the output data
output_data = []
for entry in input_data:
    instruction = entry['instruction']
    input_value = entry['input']
    # Your processing logic here to generate the output_value
    output_value = "Your processed output goes here"
    
    new_entry = {
        "tag": instruction.lower().replace(" ", "_"),
        "patterns": [instruction],
        "responses": [output_value],
        "context": [""]
    }
    output_data.append(new_entry)

# Save the output data to the output JSON file
with open(output_json_file_path, 'w') as output_json_file:
    json.dump(output_data, output_json_file, indent=4)
