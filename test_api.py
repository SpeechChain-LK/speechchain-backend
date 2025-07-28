#!/usr/bin/env python3
"""
Test script for SpeechChain API endpoints
"""

import requests
import os
from pathlib import Path

# API Base URL
BASE_URL = "http://localhost:8000"

def test_ping():
    """Test the ping endpoint"""
    print("🔍 Testing ping endpoint...")
    try:
        response = requests.get(f"{BASE_URL}/ping/")
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.json()}")
        return response.status_code == 200
    except Exception as e:
        print(f"❌ Ping test failed: {e}")
        return False

def test_tamil_to_sinhala(audio_file_path):
    """Test Tamil to Sinhala endpoint"""
    print("🔍 Testing Tamil to Sinhala endpoint...")
    
    if not os.path.exists(audio_file_path):
        print(f"❌ Audio file not found: {audio_file_path}")
        return False
    
    try:
        with open(audio_file_path, 'rb') as audio_file:
            files = {'file': audio_file}
            response = requests.post(f"{BASE_URL}/speechchain/", files=files)
        
        print(f"Status Code: {response.status_code}")
        if response.status_code == 200:
            result = response.json()
            print(f"✅ Tamil Transcription: {result.get('tamil_transcription', 'N/A')}")
            print(f"✅ Sinhala Translation: {result.get('sinhala_translation', 'N/A')}")
            return True
        else:
            print(f"❌ Error: {response.text}")
            return False
    except Exception as e:
        print(f"❌ Test failed: {e}")
        return False

def test_sinhala_to_tamil(audio_file_path):
    """Test Sinhala to Tamil endpoint"""
    print("🔍 Testing Sinhala to Tamil endpoint...")
    
    if not os.path.exists(audio_file_path):
        print(f"❌ Audio file not found: {audio_file_path}")
        return False
    
    try:
        with open(audio_file_path, 'rb') as audio_file:
            files = {'file': audio_file}
            response = requests.post(f"{BASE_URL}/speechchain-reverse/", files=files)
        
        print(f"Status Code: {response.status_code}")
        if response.status_code == 200:
            result = response.json()
            print(f"✅ Sinhala Transcription: {result.get('sinhala_transcription', 'N/A')}")
            print(f"✅ Tamil Translation: {result.get('tamil_translation', 'N/A')}")
            return True
        else:
            print(f"❌ Error: {response.text}")
            return False
    except Exception as e:
        print(f"❌ Test failed: {e}")
        return False

def main():
    print("🚀 Starting SpeechChain API Tests\n")
    
    # Test ping first
    ping_success = test_ping()
    print("-" * 50)
    
    if not ping_success:
        print("❌ Server is not responding. Make sure it's running on http://localhost:8000")
        return
    
    # Test Tamil to Sinhala (replace with your actual Tamil audio file path)
    tamil_audio_path = input("Enter path to Tamil audio file (or press Enter to skip): ").strip()
    if tamil_audio_path:
        test_tamil_to_sinhala(tamil_audio_path)
        print("-" * 50)
    
    # Test Sinhala to Tamil (replace with your actual Sinhala audio file path)
    sinhala_audio_path = input("Enter path to Sinhala audio file (or press Enter to skip): ").strip()
    if sinhala_audio_path:
        test_sinhala_to_tamil(sinhala_audio_path)
        print("-" * 50)
    
    print("✅ Testing complete!")

if __name__ == "__main__":
    main()
