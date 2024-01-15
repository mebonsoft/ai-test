import openai
import pandas as pd
import numpy as np
import gradio as gr

OPENAI_API_KEY ="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"
data = pd.read_csv('finance_data.csv')
data = data.drop_duplicates().reset_index(drop=True)
data.head()
data['prompt'] = data['kor_sentence']
data['completion'] = data['labels']
data = data[['prompt', 'completion']]
data.loc[1]['prompt']
data.to_json('finance_data.jsonl', orient='records', force_ascii=False, lines=True)