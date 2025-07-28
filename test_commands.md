# Testing SpeechChain API

## Test Commands

### 1. Test Ping Endpoint
```bash
curl -X GET "http://localhost:8000/ping/"
```

### 2. Test Tamil to Sinhala (upload audio file)
```bash
curl -X POST "http://localhost:8000/speechchain/" \
  -H "accept: application/json" \
  -H "Content-Type: multipart/form-data" \
  -F "file=@path/to/your/tamil_audio.wav"
```

### 3. Test Sinhala to Tamil (upload audio file)
```bash
curl -X POST "http://localhost:8000/speechchain-reverse/" \
  -H "accept: application/json" \
  -H "Content-Type: multipart/form-data" \
  -F "file=@path/to/your/sinhala_audio.wav"
```

## PowerShell Commands (Windows)

### 1. Test Ping
```powershell
Invoke-RestMethod -Uri "http://localhost:8000/ping/" -Method GET
```

### 2. Test Tamil to Sinhala
```powershell
$headers = @{
    "accept" = "application/json"
}
$form = @{
    file = Get-Item "path\to\your\tamil_audio.wav"
}
Invoke-RestMethod -Uri "http://localhost:8000/speechchain/" -Method POST -Headers $headers -Form $form
```

### 3. Test Sinhala to Tamil
```powershell
$headers = @{
    "accept" = "application/json"
}
$form = @{
    file = Get-Item "path\to\your\sinhala_audio.wav"
}
Invoke-RestMethod -Uri "http://localhost:8000/speechchain-reverse/" -Method POST -Headers $headers -Form $form
```

## Expected Responses

### Tamil to Sinhala Response:
```json
{
  "tamil_transcription": "தமிழ் உரை",
  "sinhala_translation": "සිංහල පරිවර්තනය"
}
```

### Sinhala to Tamil Response:
```json
{
  "sinhala_transcription": "සිංහල පාඨය",
  "tamil_translation": "தமிழ் மொழிபெயர்ப்பு"
}
```

### Error Response:
```json
{
  "detail": "Processing error: [error message]"
}
```
