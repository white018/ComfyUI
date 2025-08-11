import csv
import json
import os

name_idx = 0
prompt_idx = 1
negative_prompt_idx = 2

def convert_styles_to_json(input_path='styles.csv', output_path='styles.json'):
    """
    Converts a CSV file of styles to JSON format with specific keys.

    Args:
        input_path: Path to the input CSV file
        output_path: Path where the output JSON file will be saved
    """
    styles_list = []

    # Check if input file exists
    if not os.path.isfile(input_path):
        print(f"Error: Input file '{input_path}' not found.")
        return False

    try:
        # Read CSV file
        with open(input_path, 'r', encoding='utf-8') as csvfile:
            csv_reader = csv.reader(csvfile)

            # Read the header
            next(csv_reader, None)

            # Process rows
            for row in csv_reader:
                if not row or len(row) < 3:
                    continue
                if len(row) <= max(name_idx, prompt_idx, negative_prompt_idx):
                    print(f"Error: Row does not contain enough columns: {row}")
                    continue
                style = {
                    'name': row[name_idx],
                    'prompt': row[prompt_idx] + ", {prompt}",
                    'negative_prompt': row[negative_prompt_idx],
                }
                styles_list.append(style)

        # Write to JSON file
        with open(output_path, 'w', encoding='utf-8') as jsonfile:
            json.dump(styles_list, jsonfile, ensure_ascii=False, indent=4)

        print(f"Successfully converted '{input_path}' to '{output_path}'")
        print(f"Converted {len(styles_list)} styles")
        return True

    except Exception as e:
        print(f"Error converting CSV to JSON: {str(e)}")
        return False

if __name__ == "__main__":
    convert_styles_to_json()
