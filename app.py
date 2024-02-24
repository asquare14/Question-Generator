import logging
import os

from flask import Flask, jsonify, render_template, request

from model.question_generator import QuestionGenerator
from utils import Utils

app = Flask(__name__)
questionGenerator = QuestionGenerator()
utils = Utils()


@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")


@app.route("/generate-question", methods=["POST"])
def generate_question_api():
    context = request.form.get("context", "")
    context = utils.cleanup_context(context)

    try:
        utils.validate_context(context)
        entities = questionGenerator.get_entities(context)
        utils.validate_entities(entities)
        logging.info(
            "Text Validation Passed, entitites generated successfully. Generating Question..."
        )
        question = questionGenerator.generate_question(context, entities[-1].text)
        return jsonify(question=question)
    except ValueError as error_message:
        return jsonify(error=str(error_message)), 400
    except Exception as error_message:
        return jsonify(error=str(error_message)), 500


if __name__ == "__main__":
    logging.basicConfig(
        filename="app.log",
        level=logging.INFO,
        format="%(asctime)s %(levelname)s: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    port = int(os.environ.get("PORT", 8000))
    app.run(host='0.0.0.0', port=port, debug=True)
