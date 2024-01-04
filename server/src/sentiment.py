import nltk
from flask import Flask,jsonify,request
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, resources={r"/*":{"origins":"*"}})

#nltk.download('vader_lexicon')


@app.route("/sentiment", methods=['POST'])
def printSentiment():
    obj = request.get_json()
    textInput = obj['text']
    result = SentimentIntensityAnalyzer().polarity_scores(textInput)
    return jsonify(result)


