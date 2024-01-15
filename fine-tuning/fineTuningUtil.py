import json
import pandas as pd

def excel_to_jsonl(excel_file_path, jsonl_file_path, sheet_name='Sheet1'):
    # Read data from Excel file
    df = pd.read_excel(excel_file_path, sheet_name=sheet_name)

    with open(jsonl_file_path, 'w', encoding='utf-8') as jsonl_file:
     for index, row in df.iterrows():
            system = row.get('System', '')
            user_input = row.get('User', '')
            assistant_response = {
                'response': row.get('Assistant', ''),
                'tag': row.get('Intention', '')
            }

            data = {
                'system': system,
                'user': user_input,
                'assistant': assistant_response
            }

            # Write each JSON object to the JSONL file
            jsonl_file.write(json.dumps(data) + '\n')
            print(f"System: {system}")
            print(f"User Input: {user_input}")
            print(f"Assistant Response: {assistant_response}")
            print("\n")

# Example usage:
excel_file_path = 'Prompt_Raw_0.1.xlsx'
jsonl_file_path = 'example.jsonl'
excel_to_jsonl(excel_file_path, jsonl_file_path)