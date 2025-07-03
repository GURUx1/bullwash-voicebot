from flask import Flask, request, Response
from language_flow import get_twiml_response

app = Flask(__name__)

@app.route("/voice", methods=['POST'])
def voice():
    user_input = request.form.get("SpeechResult", "").lower()
    twiml_response = get_twiml_response(user_input)
    return Response(twiml_response, mimetype='text/xml')

@app.route("/")
def home():
    return "BullWash AI VoiceBot is Live ✅"

if __name__ == "__main__":
    app.run(debug=True)
