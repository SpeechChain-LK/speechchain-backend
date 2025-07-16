# SpeechChain LK API

A FastAPI-based backend service for Tamil speech-to-text transcription and Tamil-to-Sinhala translation.

## Features

- **Speech-to-Text**: Transcribe Tamil audio files to text
- **Translation**: Translate Tamil text to Sinhala
- **REST API**: Simple HTTP endpoints for easy integration

## Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd speechchain-backend
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Application

Start the FastAPI server:

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

The API will be available at: `http://0.0.0.0:8000`

### Development Mode

For development with auto-reload:

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

## API Endpoints

### 1. Speech Processing
- **URL**: `POST /speechchain/`
- **Description**: Upload an audio file for Tamil transcription and Sinhala translation
- **Request**: Multipart form data with audio file
- **Response**: JSON with Tamil transcription and Sinhala translation

Example:
```json
{
    "tamil_transcription": "தமிழ் உரை",
    "sinhala_translation": "සිංහල පෙළ"
}
```

### 2. Health Check
- **URL**: `GET /ping/`
- **Description**: Simple health check endpoint
- **Response**: `{"result": "pong"}`

## API Documentation

Once the server is running, you can access:

- **Interactive API docs**: `http://0.0.0.0:8000/docs`
- **ReDoc documentation**: `http://0.0.0.0:8000/redoc`

## Project Structure

```
speechchain-backend/
├── app/
│   ├── main.py              # FastAPI application
│   ├── models/              # ML model files
│   │   ├── mbart50/         # Translation model
│   │   └── whisper/         # Speech recognition model
│   ├── schemas/             # Pydantic schemas
│   ├── services/            # Business logic
│   │   ├── asr_service.py   # Speech recognition service
│   │   └── translation_service.py  # Translation service
│   └── __init__.py
├── requirements.txt         # Python dependencies
└── README.md               # This file
```

## Usage Example

### Using curl

```bash
# Upload an audio file
curl -X POST "http://0.0.0.0:8000/speechchain/" \
     -H "accept: application/json" \
     -H "Content-Type: multipart/form-data" \
     -F "file=@your_audio_file.wav"

# Health check
curl -X GET "http://0.0.0.0:8000/ping/"
```

### Using Python requests

```python
import requests

# Upload audio file
with open("audio_file.wav", "rb") as f:
    response = requests.post(
        "http://0.0.0.0:8000/speechchain/",
        files={"file": f}
    )
    print(response.json())

# Health check
response = requests.get("http://0.0.0.0:8000/ping/")
print(response.json())
```

## Error Handling

The API returns appropriate HTTP status codes:
- `200`: Success
- `400`: Bad request (e.g., empty audio file)
- `500`: Internal server error

## Development

### Adding New Features

1. Create new service modules in `app/services/`
2. Add corresponding schemas in `app/schemas/`
3. Update `app/main.py` with new endpoints

### Testing

The API includes comprehensive error handling and logging for debugging purposes.

## Support

For issues and questions, please contact the SpeechChain-LK team.