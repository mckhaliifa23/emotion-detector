# Emotion Detector Project Plan

## Overview
Develop an "Emotion Detector" web application using IBM Watson NLP library and Flask.

## Project Structure
```
Emotion Detector Project/
├── EmotionDetection/
│   ├── __init__.py
│   └── emotion_detection.py
├── templates/
│   └── index.html
├── static/
│   └── css/
│       └── style.css
├── tests/
│   └── test_emotion_detection.py
├── server.py
├── requirements.txt
├── .gitignore
├── pylint.cfg
└── README.md
```

## Phase 1: Project Setup & Dependencies

### Task 1.1: Create Project Structure
- Create directory structure
- Set up virtual environment

### Task 1.2: Install Dependencies
- IBM Watson SDK
- Flask
- pytest
- pylint

## Phase 2: Core Emotion Detection Module

### Task 2.1: Create emotion_detection.py
- Import IBM Watson NLP library
- Create `emotion_detector` function
- Analyze text for: anger, disgust, fear, joy, sadness
- Return dictionary with all emotion scores
- Calculate and include `dominant_emotion` key (highest value)

### Task 2.2: Create Package Structure
- Create `EmotionDetection/` package
- Create `__init__.py` to expose the emotion_detector function

### Task 2.3: Error Handling
- Handle status_code 400 (blank inputs)
- Return None values for emotions
- Return "Invalid text! Please try again!" message

## Phase 3: Testing

### Task 3.1: Create test_emotion_detection.py
- Unit tests for specific phrases:
  - "I am glad this happened" → joy
  - "I am really mad about this" → anger
  - "I feel disgusted" → disgust
  - "I am terrified" → fear
  - "I am so sad" → sadness
- Test edge cases (empty text, None)

## Phase 4: Flask Web Server

### Task 4.1: Create server.py
- Flask application on localhost:5000
- Route for home page (GET)
- Route for emotion detection (POST)
- Render results to UI
- Error handling for invalid inputs

### Task 4.2: Frontend Templates
- Create `templates/index.html`
- Create form for text input
- Display emotion results
- Error message display

### Task 4.3: Static Assets
- Create `static/css/style.css`
- Style the web interface

## Phase 5: Quality Assurance

### Task 5.1: Pylint Optimization
- Configure pylint
- Ensure server.py scores 10/10
- Fix all warnings and errors

### Task 5.2: Testing
- Run all unit tests
- Verify manual testing scenarios

## Phase 6: Documentation & Deployment

### Task 6.1: Documentation
- Create README.md with setup instructions
- Document API usage
- Add contribution guidelines

### Task 6.2: Git Initialization
- Initialize git repository
- Create .gitignore
- Commit all files

### Task 6.3: GitHub Push
- Create GitHub repository
- Push code to remote

## Implementation Details

### Watson NLP Integration
```python
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson.natural_language_understanding_v1 import Features, EmotionOptions
```

### Expected Output Format
```python
{
    'anger': 0.1,
    'disgust': 0.05,
    'fear': 0.05,
    'joy': 0.8,
    'sadness': 0.0,
    'dominant_emotion': 'joy'
}
```

### Error Response Format
```python
{
    'anger': None,
    'disgust': None,
    'fear': None,
    'joy': None,
    'sadness': None,
    'dominant_emotion': None
}
```

## Terminal Output Expected

### Successful Test Run
```
============================= test session starts ==============================
collected 6 items

test_emotion_detection.py ......
============================== 6 passed in 2.34s ===============================
```

### Successful Server Launch
```
 * Serving Flask app 'server'
 * Debug mode: on
 * Running on http://127.0.0.1:5000
```

### Pylint Score
```
-------------------------------------------------------------------
Your code has been rated at 10.00/10
-------------------------------------------------------------------
```

## Notes
- Watson API key and URL will be needed from IBM Cloud
- Ensure proper environment variable setup for credentials
- The project will be developed incrementally with testing at each phase
