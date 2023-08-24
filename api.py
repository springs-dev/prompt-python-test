import os
from flask import Flask, request, jsonify
import openai
from dotenv import load_dotenv

from main import split_text_into_actions, write_actions_to_csv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)


@app.route("/split-text", methods=["POST"])
def split_text():
    data = request.get_json()
    input_text = data.get("input_text", "")

    if not input_text:
        return jsonify({"error": "Input text missing"}), 400

    actions = split_text_into_actions(input_text)
    output_file = "actions.csv"
    write_actions_to_csv(actions, output_file)

    return jsonify({"message": f"Actions extracted and saved to {output_file}"}), 200


if __name__ == '__main__':
    app.run()
