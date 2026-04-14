"""
Unit Tests for Emotion Detection Module

This module contains comprehensive unit tests for the emotion_detector function,
testing all emotion types, edge cases, and output format requirements.
"""

import pytest
from EmotionDetection import emotion_detector


class TestEmotionDetection:
    """Test suite for emotion detection functionality."""

    def test_joy_emotion(self):
        """Test that 'I am glad this happened' detects joy as dominant emotion."""
        result = emotion_detector("I am glad this happened")
        assert result['dominant_emotion'] == 'joy'
        assert result['joy'] is not None
        assert result['joy'] > 0

    def test_anger_emotion(self):
        """Test that angry text detects anger as dominant emotion."""
        result = emotion_detector("I am really mad about this situation")
        assert result['dominant_emotion'] == 'anger'
        assert result['anger'] is not None
        assert result['anger'] > 0

    def test_disgust_emotion(self):
        """Test that disgusting text detects disgust as dominant emotion."""
        result = emotion_detector("I feel disgusted by this")
        assert result['dominant_emotion'] == 'disgust'
        assert result['disgust'] is not None
        assert result['disgust'] > 0

    def test_fear_emotion(self):
        """Test that fearful text detects fear as dominant emotion."""
        result = emotion_detector("I am terrified of what might happen")
        assert result['dominant_emotion'] == 'fear'
        assert result['fear'] is not None
        assert result['fear'] > 0

    def test_sadness_emotion(self):
        """Test that sad text detects sadness as dominant emotion."""
        result = emotion_detector("I am so sad about this news")
        assert result['dominant_emotion'] == 'sadness'
        assert result['sadness'] is not None
        assert result['sadness'] > 0

    def test_blank_input(self):
        """Test that blank input returns None values for all emotions."""
        result = emotion_detector("")
        assert result['anger'] is None
        assert result['disgust'] is None
        assert result['fear'] is None
        assert result['joy'] is None
        assert result['sadness'] is None
        assert result['dominant_emotion'] is None

    def test_whitespace_input(self):
        """Test that whitespace-only input returns None values."""
        result = emotion_detector("   ")
        assert result['anger'] is None
        assert result['disgust'] is None
        assert result['fear'] is None
        assert result['joy'] is None
        assert result['sadness'] is None
        assert result['dominant_emotion'] is None

    def test_none_input(self):
        """Test that None input returns None values."""
        result = emotion_detector(None)
        assert result['anger'] is None
        assert result['disgust'] is None
        assert result['fear'] is None
        assert result['joy'] is None
        assert result['sadness'] is None
        assert result['dominant_emotion'] is None

    def test_output_format(self):
        """Test that output contains all required keys."""
        result = emotion_detector("This is a test")
        required_keys = ['anger', 'disgust', 'fear', 'joy', 'sadness', 'dominant_emotion']
        assert all(key in result for key in required_keys)

    def test_emotion_scores_range(self):
        """Test that emotion scores are between 0 and 1."""
        result = emotion_detector("I feel happy and excited")
        if result['joy'] is not None:
            assert 0 <= result['joy'] <= 1
        if result['anger'] is not None:
            assert 0 <= result['anger'] <= 1
        if result['disgust'] is not None:
            assert 0 <= result['disgust'] <= 1
        if result['fear'] is not None:
            assert 0 <= result['fear'] <= 1
        if result['sadness'] is not None:
            assert 0 <= result['sadness'] <= 1

    def test_dominant_emotion_is_highest(self):
        """Test that dominant_emotion has the highest score."""
        result = emotion_detector("I am absolutely thrilled and delighted")
        emotions = {
            'anger': result['anger'],
            'disgust': result['disgust'],
            'fear': result['fear'],
            'joy': result['joy'],
            'sadness': result['sadness']
        }
        dominant = result['dominant_emotion']

        # Verify dominant emotion has the highest score
        if dominant and emotions[dominant] is not None:
            for emotion, score in emotions.items():
                if score is not None:
                    assert emotions[dominant] >= score


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
