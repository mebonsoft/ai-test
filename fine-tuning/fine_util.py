import json
import pandas as pd

def excel_to_jsonl(excel_file_path, jsonl_file_path, sheet_name='Sheet1'):
    # Read data from Excel file
    df = pd.read_excel(excel_file_path, sheet_name=sheet_name)

    with open(jsonl_file_path, 'w', encoding='utf-8') as jsonl_file:
     for index, row in df.iterrows():
            system_content = row.get('System', '')
            user_content = row.get('User', '')
            tag_data = {
                'response': row.get('Assistant', ''),
                'tag': row.get('Intention', '')
            }
            assistant_content = 'response' + ":" + row.get('Assistant', '') + "@@@" + "tag" + ":" + row.get('Intention', '')

            data = {
                'messages': [
                    {'role': 'system', 'content': system_content},
                    {'role': 'user', 'content': user_content},
                    {'role': 'assistant','content':assistant_content}
                ],                
            }

            # Write each JSON object to the JSONL file
            jsonl_file.write(json.dumps(data, ensure_ascii=False) + '\n')
            print(f"System: {system_content}")
            print(f"User: {user_content}")
            print(f"Assistant: {assistant_content}")
            print(",")

# Example usage:
excel_file_path = 'Prompt_Raw_0.1.xlsx'
jsonl_file_path = 'example.jsonl'
excel_to_jsonl(excel_file_path, jsonl_file_path)