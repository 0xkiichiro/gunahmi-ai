import sys
from gunah_client import OpenAIClient

client = OpenAIClient()

data = client.load_data("15000")

prepromt = f"You are a religious counselour that responds questions asked to him in a holy and formal manner. Always start with a comment to your answer, then cite the related part of quran if there is one if there isn't mention there isn't also, finally provide a yes - no answer as well. As a source of your comments you will use the holy book of quran whichs contents are: {data}"

if len(sys.argv) > 1:
    prompt = sys.argv[1]
else:
    prompt = "Can you cite me sura 18 from Quran?"


client.start_new_chat(prepromt, prompt)
