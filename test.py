from client import OpenAIClient

client = OpenAIClient()

data = client.load_data("15000")

prepromt = f"You are a religious counselour that responds questions asked to him in a holy and formal manner. As a source of your comments you will use the holy book of quran whichs contents are: {data}"
promt = "can you cite me sura 18 from quran?"
client.start_new_chat(prepromt, promt)