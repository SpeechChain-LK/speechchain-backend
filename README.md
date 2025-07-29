# SpeechChain LK API

A FastAPI-based backend service for bidirectional speech translation between Tamil and Sinhala languages.

## Features

- **Tamil to Sinhala**: 
  - Transcribe Tamil audio files to text
  - Translate Tamil text to Sinhala
- **Sinhala to Tamil**: 
  - Transcribe Sinhala audio files to text  
  - Translate Sinhala text to Tamil
- **REST API**: Simple HTTP endpoints for easy integration
- **Interactive Documentation**: Built-in Swagger UI for testing

## Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- Virtual environment (recommended)

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd speechchain-backend
```

2. Create and activate a virtual environment:
```bash
# Create virtual environment
python -m venv speechchain-lk-env

# Activate virtual environment
# On Windows:
speechchain-lk-env\Scripts\activate
# On macOS/Linux:
source speechchain-lk-env/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Application

### Method 1: Using Virtual Environment (Recommended)

1. **Activate your virtual environment:**
```bash
# On Windows:
speechchain-lk-env\Scripts\activate
# On macOS/Linux:
source speechchain-lk-env/bin/activate
```

2. **Start the FastAPI server:**
```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

### Method 2: Direct Python Execution

```bash
python -m uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

The API will be available at: `http://localhost:8000`

**📌 Note:** Use `--reload` flag during development for auto-restart on code changes.

## API Endpoints

### 1. Tamil to Sinhala Speech Translation
- **URL**: `POST /speechchain/`
- **Description**: Upload Tamil audio file for transcription and Sinhala translation
- **Request**: Multipart form data with audio file (key: `file`)
- **Response**: JSON with Tamil transcription and Sinhala translation

Example Response:
```json
{
    "tamil_transcription": "வணக்கம், நான் தமிழ் பேசுகிறேன்",
    "sinhala_translation": "ආයුබෝවන්, මම දමිළ කතා කරමි"
}
```

### 2. Sinhala to Tamil Speech Translation
- **URL**: `POST /speechchain-reverse/`
- **Description**: Upload Sinhala audio file for transcription and Tamil translation
- **Request**: Multipart form data with audio file (key: `file`)
- **Response**: JSON with Sinhala transcription and Tamil translation

Example Response:
```json
{
    "sinhala_transcription": "ආයුබෝවන්, මම සිංහල කතා කරමි",
    "tamil_translation": "வணக்கம், நான் சிங்களம் பேசுகிறேன்"
}
```

### 3. Health Check
- **URL**: `GET /ping/`
- **Description**: Simple health check endpoint
- **Response**: `{"result": "pong"}`

## Testing Your API

### 🎯 Method 1: Interactive API Documentation (Easiest)

1. **Start your server** (see Running the Application section above)
2. **Open your browser** and go to: `http://localhost:8000/docs`
3. **Test endpoints interactively:**
   - Try `GET /ping/` first to verify server is working
   - Upload Tamil audio to `POST /speechchain/`
   - Upload Sinhala audio to `POST /speechchain-reverse/`

### 🎯 Method 2: Using the Test Script

We've included a Python test script for automated testing:

```bash
python test_api.py
```

This script will:
- Test the ping endpoint
- Allow you to test both speech translation endpoints
- Show detailed response information

### 🎯 Method 3: Using cURL Commands

**Test Health Check:**
```bash
curl -X GET "http://localhost:8000/ping/"
```

**Test Tamil to Sinhala:**
```bash
curl -X POST "http://localhost:8000/speechchain/" \
     -H "accept: application/json" \
     -H "Content-Type: multipart/form-data" \
     -F "file=@path/to/tamil_audio.wav"
```

**Test Sinhala to Tamil:**
```bash
curl -X POST "http://localhost:8000/speechchain-reverse/" \
     -H "accept: application/json" \
     -H "Content-Type: multipart/form-data" \
     -F "file=@path/to/sinhala_audio.wav"
```

### 🎯 Method 4: Using PowerShell (Windows)

**Test Health Check:**
```powershell
Invoke-RestMethod -Uri "http://localhost:8000/ping/" -Method GET
```

**Test with Audio File:**
```powershell
$form = @{file = Get-Item "path\to\audio.wav"}
Invoke-RestMethod -Uri "http://localhost:8000/speechchain/" -Method POST -Form $form
```

### 🎯 Method 5: Using Python Requests

```python
import requests

# Test health check
response = requests.get("http://localhost:8000/ping/")
print(response.json())

# Test Tamil to Sinhala
with open("tamil_audio.wav", "rb") as f:
    response = requests.post(
        "http://localhost:8000/speechchain/",
        files={"file": f}
    )
    print(response.json())

# Test Sinhala to Tamil  
with open("sinhala_audio.wav", "rb") as f:
    response = requests.post(
        "http://localhost:8000/speechchain-reverse/",
        files={"file": f}
    )
    print(response.json())
```

## Supported Audio Formats

- **WAV** (recommended)
- **MP3**
- **M4A**
- **FLAC**
- **OGG**

**📌 Note:** For best results, use mono audio files with 16kHz sample rate.

## Project Structure

```
speechchain-backend/
├── app/
│   ├── main.py                           # FastAPI application with endpoints
│   ├── models/                           # ML model files
│   │   ├── mbart50/                      # Default mBART translation model
│   │   ├── whisper/                      # Default Whisper ASR model
│   │   ├── Tamil-To-Sinhala/             # Tamil→Sinhala models
│   │   │   ├── mbart50/                  # Tamil→Sinhala translation model
│   │   │   └── whisper/                  # Tamil ASR model
│   │   └── Sinhala-To-Tamil/             # Sinhala→Tamil models
│   │       ├── mbart50/                  # Sinhala→Tamil translation model
│   │       └── whisper/                  # Sinhala ASR model
│   ├── schemas/                          # Pydantic schemas
│   │   └── speech.py                     # Speech processing schemas
│   ├── services/                         # Business logic services
│   │   ├── asr_service.py                # Tamil speech recognition
│   │   ├── translation_service.py        # Tamil→Sinhala translation
│   │   ├── sinhala_asr_service.py        # Sinhala speech recognition
│   │   └── sinhala_translation_service.py # Sinhala→Tamil translation
│   └── __init__.py
├── speechchain-lk-env/                   # Virtual environment
├── requirements.txt                      # Python dependencies
├── test_api.py                          # Test script
├── test_commands.md                     # Testing documentation
└── README.md                            # This file
```

## API Documentation

Once the server is running, you can access:

- **Interactive API docs (Swagger UI)**: `http://localhost:8000/docs`
- **ReDoc documentation**: `http://localhost:8000/redoc`

## Usage Examples

### Using curl

```bash
# Health check
curl -X GET "http://localhost:8000/ping/"

# Tamil to Sinhala translation
curl -X POST "http://localhost:8000/speechchain/" \
     -H "accept: application/json" \
     -H "Content-Type: multipart/form-data" \
     -F "file=@your_tamil_audio.wav"

# Sinhala to Tamil translation  
curl -X POST "http://localhost:8000/speechchain-reverse/" \
     -H "accept: application/json" \
     -H "Content-Type: multipart/form-data" \
     -F "file=@your_sinhala_audio.wav"
```

### Using Python requests

```python
import requests

# Health check
response = requests.get("http://localhost:8000/ping/")
print(response.json())  # {"result": "pong"}

# Tamil to Sinhala
with open("tamil_audio.wav", "rb") as f:
    response = requests.post(
        "http://localhost:8000/speechchain/",
        files={"file": f}
    )
    result = response.json()
    print("Tamil:", result["tamil_transcription"])
    print("Sinhala:", result["sinhala_translation"])

# Sinhala to Tamil
with open("sinhala_audio.wav", "rb") as f:
    response = requests.post(
        "http://localhost:8000/speechchain-reverse/",
        files={"file": f}
    )
    result = response.json()
    print("Sinhala:", result["sinhala_transcription"])
    print("Tamil:", result["tamil_translation"])
```

## Error Handling

The API returns appropriate HTTP status codes and error messages:

### Success Response (200)
```json
{
    "tamil_transcription": "transcribed text",
    "sinhala_translation": "translated text"
}
```

### Error Responses

**400 Bad Request** - Empty audio file:
```json
{
    "detail": "Empty audio file"
}
```

**500 Internal Server Error** - Processing error:
```json
{
    "detail": "Processing error: [specific error message]"
}
```

## Troubleshooting

### Common Issues

1. **Server won't start:**
   - Make sure virtual environment is activated
   - Check if all dependencies are installed: `pip install -r requirements.txt`
   - Ensure models are present in the `app/models/` directory

2. **Import errors:**
   - Verify Python path includes the project root
   - Make sure all service files exist in `app/services/`

3. **Model loading errors:**
   - Check if model files are present in respective directories
   - Ensure sufficient RAM/VRAM for model loading

4. **Audio processing errors:**
   - Verify audio file format is supported
   - Check audio file is not corrupted
   - Ensure file size is reasonable (< 10MB recommended)

### Performance Tips

- Use **WAV files** with **16kHz sample rate** for best performance
- Keep audio files **under 30 seconds** for faster processing
- Use **mono audio** instead of stereo when possible

## Development

### Adding New Features

1. **Create new service modules** in `app/services/`
2. **Add corresponding schemas** in `app/schemas/` 
3. **Update `app/main.py`** with new endpoints
4. **Update tests** in `test_api.py`

### Code Structure Guidelines

- **Services**: Handle business logic and model interactions
- **Schemas**: Define request/response data structures  
- **Main**: Define API endpoints and routing
- **Models**: Store trained ML models

### Testing During Development

1. **Use `--reload` flag** when starting the server for auto-restart
2. **Test via Swagger UI** at `http://localhost:8000/docs`
3. **Run test script** with `python test_api.py`
4. **Check server logs** for debugging information

## Model Information

### Speech Recognition Models (Whisper)
- **Tamil ASR**: Fine-tuned Whisper model for Tamil speech recognition
- **Sinhala ASR**: Fine-tuned Whisper model for Sinhala speech recognition
- **Input**: Audio files (WAV, MP3, etc.)
- **Output**: Transcribed text in respective language

### Translation Models (mBART-50)
- **Tamil→Sinhala**: Fine-tuned mBART model for Tamil to Sinhala translation
- **Sinhala→Tamil**: Fine-tuned mBART model for Sinhala to Tamil translation  
- **Input**: Text in source language
- **Output**: Translated text in target language

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new functionality
5. Update documentation
6. Submit a pull request

## License

[Add your license information here]

## Support

For issues and questions:
- Create an issue on GitHub
- Contact the SpeechChain-LK development team

## Changelog

### v2.0.0 (Current)
- ✅ Added Sinhala to Tamil speech translation
- ✅ Bidirectional language support
- ✅ Enhanced testing framework
- ✅ Improved documentation

### v1.0.0
- ✅ Tamil to Sinhala speech translation
- ✅ Basic API endpoints
- ✅ FastAPI integration