"""
Emotion Detector Flask Server

This module provides a Flask web application for the Emotion Detector.
It serves a web interface where users can input text to analyze for emotions.
"""

from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

# Initialize Flask application
app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    """
    Render the home page with the emotion detection form.

    Returns:
        str: Rendered HTML template for the index page.
    """
    return render_template('index.html')


@app.route('/emotionDetector', methods=['POST'])
def emotion_detector_route():
    """
    Handle emotion detection requests from the web form.

    This route processes the text submitted through the web form,
    analyzes it for emotions, and returns the results.

    Returns:
        str: Rendered HTML template with emotion analysis results or error message.
    """
    # Get text from form
    text_to_analyze = request.form.get('textToAnalyze', '')

    # Validate input
    if not text_to_analyze or text_to_analyze.strip() == '':
        return render_template('index.html', error_text="Invalid text! Please try again!")

    # Analyze emotions
    result = emotion_detector(text_to_analyze)

    # Check if analysis was successful
    if result['dominant_emotion'] is None:
        return render_template('index.html', error_text="Invalid text! Please try again!")

    # Render results
    return render_template('index.html',
                          anger=result['anger'],
                          disgust=result['disgust'],
                          fear=result['fear'],
                          joy=result['joy'],
                          sadness=result['sadness'],
                          dominant_emotion=result['dominant_emotion'])


if __name__ == '__main__':
    """
    Run the Flask development server.

    The server runs on localhost:5000 in debug mode.
    """
    app.run(host='localhost', port=5000, debug=True)
