'''
web deployment of the application using Flask 
'''
from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)


@app.route('/')
def index():
    '''index endpoint'''
    return render_template('index.html')


@app.route('/emotionDetector')
def get_emotion_detector():
    '''emotion detector endpoint'''

    text = request.args['textToAnalyze']
    analysis = emotion_detector(text)
    if analysis['dominant_emotion'] is None:
        return 'Invalid text! Please try again!.'
    response = 'For the given statement, the system response is'
    parts = []
    for emotion, score in analysis.items():
        parts.append(" '" + emotion + "': " + str(score))
    response += ', '.join(parts)
    dominant = analysis['dominant_emotion']
    response += f'. The dominant emotion is {dominant}.'
    return response


if __name__ == '__main__':
    app.run(debug=True)
