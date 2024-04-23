import os
import logging

from gunah_client import OpenAIClient
from dotenv import load_dotenv
from flask import Flask, jsonify, request
from flask_cors import CORS

logging.basicConfig(filename='app.log', level=logging.ERROR, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

app = Flask(__name__, template_folder='.')
CORS(app)

load_dotenv()
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

client = OpenAIClient(api_key=OPENAI_API_KEY)
data = client.load_data("15000")

preprompt = f"You are a religious counselor that responds questions asked to him in a holy and formal manner. Always start with a comment to your answer, then cite the related part of Quran if there is one if there isn't mention there isn't also, finally provide a yes - no answer as well. As a source of your comments you will use the holy book of Quran which's contents are: {data}"

@app.route("/ask_question", methods=["POST"])
def ask_question():
    print("hit endpoint")
    if request.is_json:
        data = request.get_json()
        print(data["prompt"])
        prompt = data["prompt"]
        answer = client.start_new_chat(preprompt, prompt)
        return answer
    else:
        return jsonify({"error": "Request must be JSON"}), 400

def run_app():
    try:
        app.run(debug=True, host='0.0.0.0', port=5001)
    except Exception as e:
        logging.error(f"Flask app crashed: {e}")
        run_app()

if __name__ == '__main__':
    run_app()
