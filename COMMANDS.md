# Terminal Commands Reference

## Quick Start Commands

### 1. Install Dependencies
```bash
cd "/Users/mohamedkhalif/MK-Dev/Emotion Detector Project"
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 2. Configure IBM Watson Credentials
Edit this file:
```bash
open -a TextEdit "EmotionDetection/emotion_detection.py"
```

Replace:
- `YOUR_WATSON_API_KEY_HERE` → Your actual API key
- `YOUR_WATSON_URL_HERE` → Your actual service URL

### 3. Run Unit Tests
```bash
source venv/bin/activate
pytest tests/test_emotion_detection.py -v
```

Expected output: All tests pass (11 passed)

### 4. Run Pylint on server.py
```bash
source venv/bin/activate
pylint server.py
```

Expected output: `10.00/10`

### 5. Start the Flask Server
```bash
source venv/bin/activate
python server.py
```

Then open: http://localhost:5000

### 6. Stop the Server
Press `Ctrl+C` in the terminal

## Verification Commands

### Test Package Import
```bash
source venv/bin/activate
python3 -c "from EmotionDetection import emotion_detector; print('✓ Import successful')"
```

### Test File Structure
```bash
cd "/Users/mohamedkhalif/MK-Dev/Emotion Detector Project"
find . -type f \( -name "*.py" -o -name "*.html" -o -name "*.css" \) | grep -v __pycache__ | sort
```

### View All Files
```bash
cd "/Users/mohamedkhalif/MK-Dev/Emotion Detector Project"
ls -la
```

## Testing Individual Components

### Test Emotion Detection (Manual)
```bash
source venv/bin/activate
python3
>>> from EmotionDetection import emotion_detector
>>> result = emotion_detector("I am so happy today!")
>>> print(result)
>>> exit()
```

### Test Flask Server
```bash
source venv/bin/activate
python server.py
# Open browser to http://localhost:5000
# Enter text and submit
# Verify results display
```

## Troubleshooting

### Import Errors
```bash
# Ensure virtual environment is activated
source venv/bin/activate

# Reinstall dependencies
pip install -r requirements.txt --force-reinstall
```

### Port Already in Use
```bash
# Find process using port 5000
lsof -i :5000

# Kill the process
kill -9 <PID>
```

### Pylint Score Issues
```bash
# Check pylint configuration
cat .pylintrc

# Run with verbose output
pylint server.py --reports=y
```

## Screenshot Commands

### Take Screenshot of Working App
```bash
# After starting server and testing with text
screenshot -T 1 "6b_deployment_test.png"
```

### Take Screenshot of Error Handling
```bash
# After submitting blank form
screenshot -T 1 "7c_error_handling_interface.png"
```

## Complete Workflow

```bash
# 1. Navigate to project
cd "/Users/mohamedkhalif/MK-Dev/Emotion Detector Project"

# 2. Setup environment
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# 3. Configure credentials (edit file manually)
open -a TextEdit "EmotionDetection/emotion_detection.py"

# 4. Run tests
pytest tests/test_emotion_detection.py -v

# 5. Run pylint
pylint server.py

# 6. Start server
python server.py

# 7. Open browser
open http://localhost:5000
```
