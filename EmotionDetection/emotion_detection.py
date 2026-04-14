"""
Emotion Detection Module

This module provides emotion detection functionality using IBM Watson's
Natural Language Understanding API. It analyzes text to determine emotional
content including anger, disgust, fear, joy, and sadness.
"""

from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_watson.natural_language_understanding_v1 import Features, EmotionOptions
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator


def emotion_detector(text_to_analyze):
    """
    Analyze text for emotions using IBM Watson NLP.

    This function takes a text string and analyzes it for emotional content.
    It returns scores for five emotions (anger, disgust, fear, joy, sadness)
    and identifies the dominant emotion.

    Args:
        text_to_analyze (str): The text to analyze for emotional content.

    Returns:
        dict: A dictionary containing:
            - anger (float): Score for anger emotion (0-1)
            - disgust (float): Score for disgust emotion (0-1)
            - fear (float): Score for fear emotion (0-1)
            - joy (float): Score for joy emotion (0-1)
            - sadness (float): Score for sadness emotion (0-1)
            - dominant_emotion (str): The emotion with the highest score

            If the input is blank or invalid, all values will be None.
    """
    # Handle blank or invalid input
    if not text_to_analyze or not isinstance(text_to_analyze, str) or text_to_analyze.strip() == "":
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    # Initialize Watson NLU service
    # Note: Replace these placeholders with your actual IBM Watson credentials
    authenticator = IAMAuthenticator('YOUR_WATSON_API_KEY_HERE')
    natural_language_understanding = NaturalLanguageUnderstandingV1(
        version='2022-04-07',
        authenticator=authenticator
    )
    natural_language_understanding.set_service_url('YOUR_WATSON_URL_HERE')

    try:
        # Analyze text for emotions
        response = natural_language_understanding.analyze(
            text=text_to_analyze,
            features=Features(emotion=EmotionOptions())
        ).get_result()

        # Extract emotion scores
        emotions = response['emotion']['document']['emotion']

        # Find dominant emotion (the one with highest score)
        dominant_emotion = max(emotions.items(), key=lambda x: x[1])[0]

        # Return formatted result
        return {
            'anger': emotions['anger'],
            'disgust': emotions['disgust'],
            'fear': emotions['fear'],
            'joy': emotions['joy'],
            'sadness': emotions['sadness'],
            'dominant_emotion': dominant_emotion
        }

    except Exception as e:
        # Handle API errors (including status_code 400 for invalid input)
        print(f"Error analyzing text: {e}")
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
