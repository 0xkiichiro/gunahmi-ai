from flask import Flask, jsonify, request
from flask_cors import CORS
from gunah_client import OpenAIClient
import logging

logging.basicConfig(filename='app.log', level=logging.ERROR, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

app = Flask(__name__, template_folder='.')
CORS(app)

client = OpenAIClient()
data = client.load_data("15000")
prepromt = f"You are a religious counselour that responds questions asked to him in a holy and formal manner. Always start with a comment to your answer, then cite the related part of quran if there is one if there isn't mention there isn't also, finally provide a yes - no answer as well. As a source of your comments you will use the holy book of quran whichs contents are: {data}"

@app.route("/ask_question>", methods=["POST"])
def ask_question():
    if request.is_json:
        prompt = request.get_json()
        answer = client.start_new_chat(prepromt, prompt)
        return answer


def run_app():
    try:
        app.run(debug=True, host='0.0.0.0', port=5001)
    except Exception as e:
        logging.error(f"Flask app crashed: {e}")
        run_app()

if __name__ == '__main__':
    run_app()