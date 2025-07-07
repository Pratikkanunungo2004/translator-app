from flask import Flask, request, jsonify, render_template
from googletrans import Translator

app = Flask(__name__)
translator = Translator()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/translate", methods=["POST"])
def translate():
    data = request.get_json()
    text = data.get("text")
    target = data.get("target", "hi")
    translated = translator.translate(text, dest=target)
    return jsonify({"translated_text": translated.text})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=10000)