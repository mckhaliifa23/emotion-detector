# Emotion Detector - Architecture Overview

## System Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                         USER BROWSER                             │
│                      (Web Interface)                             │
└──────────────────────────────┬──────────────────────────────────┘
                               │ HTTP Request
                               ▼
┌─────────────────────────────────────────────────────────────────┐
│                      Flask Server (server.py)                    │
│                    localhost:5000                                │
├─────────────────────────────────────────────────────────────────┤
│  Routes:                                                         │
│  - GET  /        → Serve index.html                              │
│  - POST /emotion → Process text, return emotions                 │
└──────────────────────────────┬──────────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────────┐
│              EmotionDetection Package                            │
├─────────────────────────────────────────────────────────────────┤
│  emotion_detector(text) → {emotion_scores, dominant_emotion}     │
└──────────────────────────────┬──────────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────────┐
│            IBM Watson NLP API                                    │
│         (Natural Language Understanding)                         │
├─────────────────────────────────────────────────────────────────┤
│  Features: Emotion Detection                                     │
│  - Anger, Disgust, Fear, Joy, Sadness                           │
└─────────────────────────────────────────────────────────────────┘
```

## Data Flow

### Happy Path
```
User Input → Flask Route → emotion_detector() → Watson API
    ↓
JSON Response ← Flask Route ← emotion_detector() ← Watson API
```

### Error Path
```
Empty Input → Flask Route → emotion_detector() → Returns None
    ↓
Error Message ← Flask Route ← "Invalid text! Please try again!"
```

## File Dependencies

```
server.py
    ├── imports → EmotionDetection.emotion_detection
    ├── renders → templates/index.html
    └── serves  → static/css/style.css

emotion_detection.py
    ├── imports → ibm_watson NLU library
    └── exports → emotion_detector function

test_emotion_detection.py
    └── imports → EmotionDetection.emotion_detection
```

## Environment Variables Required

```
WATSON_API_KEY=<your-ibm-cloud-api-key>
WATSON_URL=<your-watson-service-url>
```
