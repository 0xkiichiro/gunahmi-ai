import os
from openai import OpenAI
import tiktoken


class OpenAIClient:
    def __init__(self):
        try:
            self.client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
        except Exception as e:
            print(f"Error: {e}")

    def load_data(self, wanted_token_count):
        try:
            with open("./sources/quran.txt", "r") as source:
                data = source.read()
            enc = tiktoken.get_encoding("cl100k_base")
            encoded_data = enc.encode(data)
            cropped_encoded_data = encoded_data[:int(wanted_token_count)]
            cropped_data = enc.decode(cropped_encoded_data)
            return cropped_data
        except Exception as e:
            print(f"Error: {e}")
            return ""


    def start_new_chat(self, pre_promt, user_promt):
        try:
            completion = self.client.chat.completions.create(
                model="gpt-4-0125-preview",
                messages=[
                    {"role": "system", "content": pre_promt},
                    {"role": "user", "content": user_promt}
                ]
                )
            print(completion.choices[0].message)
            return completion
        except Exception as e:
            print(f"Error: {e}")