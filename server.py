from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotions Analyzer")

@app.route("/emotionDetector")
def sent_analyzer():
    text_to_analyze = request.args.get("textToAnalyze")
    response = emotion_detector(text_to_analyze)
    dominant_emotion = response['dominant_emotion']

    emotions_str = ""
    i = 0
    for key, value in response.items():
        if key != 'dominant_emotion':
            if i < 4:
                emotions_str += f"'{key}': {value}, "
            elif i == 4:
                emotions_str = emotions_str.rstrip(', ')
                emotions_str += f" and '{key}': {value}"
            i += 1

    return (
        f"For the given statement, the system response is {emotions_str}. "
        f"The dominant emotion is {dominant_emotion}."
    )

@app.route("/")
def render_index_page():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
