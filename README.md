# Emotion Detector

A web application that uses IBM Watson's Natural Language Understanding API to analyze text for emotional content. The application detects five emotions (anger, disgust, fear, joy, and sadness) and identifies the dominant emotion in the provided text.

## Features

- **Emotion Detection**: Analyzes text for five emotions: anger, disgust, fear, joy, and sadness
- **Dominant Emotion Identification**: Automatically identifies the strongest emotion detected
- **Web Interface**: Clean, responsive web interface built with Flask
- **Error Handling**: Graceful handling of invalid or blank input
- **Visual Results**: Displays emotion scores as percentages with visual progress bars

## Project Structure

```
Emotion Detector Project/
├── EmotionDetection/
│   ├── __init__.py              # Package initialization
│   └── emotion_detection.py     # Core emotion detection functionality
├── templates/
│   └── index.html               # Web interface template
├── static/
│   └── css/
│       └── style.css            # Styling for the web interface
├── tests/
│   ├── __init__.py              # Test package initialization
│   └── test_emotion_detection.py # Unit tests
├── server.py                    # Flask web server
├── requirements.txt             # Python dependencies
├── README.md                    # This file
├── .gitignore                   # Git ignore rules
└── .pylintrc                    # Pylint configuration
```

## Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- IBM Watson NLU API credentials (API key and service URL)

### Step 1: Clone or Download the Project

```bash
cd "/Users/mohamedkhalif/MK-Dev/Emotion Detector Project"
```

### Step 2: Create a Virtual Environment (Recommended)

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Configure IBM Watson Credentials

Edit `EmotionDetection/emotion_detection.py` and replace the placeholder credentials:

```python
authenticator = IAMAuthenticator('YOUR_WATSON_API_KEY_HERE')
natural_language_understanding.set_service_url('YOUR_WATSON_URL_HERE')
```

To get your IBM Watson credentials:
1. Sign up at [IBM Cloud](https://cloud.ibm.com/)
2. Create a Natural Language Understanding service instance
3. Generate an API key in the service credentials
4. Copy the API key and URL

## Usage

### Running the Web Application

```bash
python server.py
```

The application will start at `http://localhost:5000`

### Using the Web Interface

1. Open your browser and go to `http://localhost:5000`
2. Enter text you want to analyze in the text area
3. Click "Analyze Emotions"
4. View the emotion scores and dominant emotion

### Running Unit Tests

```bash
pytest tests/test_emotion_detection.py -v
```

### Running Pylint (Code Quality Check)

```bash
pylint server.py
```

Expected score: 10.00/10

## API Reference

### emotion_detector(text_to_analyze)

Analyzes text for emotional content using IBM Watson NLU.

**Parameters:**
- `text_to_analyze` (str): The text to analyze

**Returns:**
- Dictionary containing:
  - `anger` (float): Anger score (0-1)
  - `disgust` (float): Disgust score (0-1)
  - `fear` (float): Fear score (0-1)
  - `joy` (float): Joy score (0-1)
  - `sadness` (float): Sadness score (0-1)
  - `dominant_emotion` (str): The emotion with the highest score

**Example:**
```python
from EmotionDetection import emotion_detector

result = emotion_detector("I am so happy today!")
print(result)
# Output: {'anger': 0.02, 'disgust': 0.01, 'fear': 0.03, 'joy': 0.89, 'sadness': 0.05, 'dominant_emotion': 'joy'}
```

## Error Handling

The application handles two types of errors:

1. **Blank/Invalid Input**: When no text is provided, the function returns:
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

2. **Web Interface Error**: When blank input is submitted through the form, the user sees:
   - Error message: "Invalid text! Please try again!"

## Testing

The test suite includes:

1. **Emotion Detection Tests**:
   - Joy detection: "I am glad this happened"
   - Anger detection: "I am really mad about this"
   - Disgust detection: "I feel disgusted by this"
   - Fear detection: "I am terrified of what might happen"
   - Sadness detection: "I am so sad about this"

2. **Edge Case Tests**:
   - Blank input
   - Whitespace-only input
   - None input

3. **Output Format Tests**:
   - Verifies all required keys are present
   - Validates emotion score ranges (0-1)
   - Confirms dominant emotion has the highest score

## Requirements

The project requires the following Python packages:

- `ibm-watson==6.0.0` - IBM Watson SDK
- `Flask==3.0.0` - Web framework
- `pytest==7.4.3` - Testing framework
- `pylint==3.0.2` - Code quality tool
- `ibm-cloud-sdk-core==3.1.1` - IBM Cloud SDK core

## License

This project is created for educational purposes as part of a graded assignment.

## Author

Emotion Detector Project - IBM Watson NLP & Flask Application

## Acknowledgments

- IBM Watson Natural Language Understanding API
- Flask Web Framework
- pytest Testing Framework
