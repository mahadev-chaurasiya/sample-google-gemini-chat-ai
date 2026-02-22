# Gemini AI ChatBot with Streamlit

A simple AI chatbot powered by Google's Gemini API that supports text, image, and audio inputs.

## Features

- 💬 Text-based chat
- 📷 Image upload and analysis
- 🎤 Audio upload and transcription
- 🚀 Clean and simple UI

## Prerequisites

- Python 3.8 or higher
- Google Gemini API Key

## Installation Steps

### 1. Clone or Download the Project

```bash
cd sample-gemini-chat-app
```

### 2. Install Required Packages

```bash
pip install streamlit google-generativeai python-dotenv pillow
```

### 3. Get Your Gemini API Key

1. Go to [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Sign in with your Google account
3. Click "Create API Key"
4. Copy your API key

### 4. Create `.env` File

Create a file named `.env` in the project directory:

```bash
GEMINI_API_KEY=your_api_key_here
```

Replace `your_api_key_here` with your actual Gemini API key.

### 5. Run the Application

```bash
streamlit run app.py
```

The app will automatically open in your browser at `http://localhost:8501`

## Usage

1. **Text Input**: Type your question in the text area
2. **Image Upload**: Click the 📷 icon to upload an image
3. **Audio Upload**: Click the 🎤 icon to upload audio
4. **Submit**: Press Enter or click outside the text area to get a response

## Example Queries

- "Who is Sardar Vallabhbhai Patel?"
- Upload an image and ask "What's in this image?"
- Upload audio and ask "Transcribe this audio"

## Project Structure

```
sample-gemini-chat-app/
├── app.py              # Main application file
├── .env                # API key configuration (create this)
└── README.md           # This file
```

## Troubleshooting

**Issue**: `ModuleNotFoundError: No module named 'streamlit'`
- **Solution**: Run `pip install streamlit`

**Issue**: API key not found
- **Solution**: Make sure `.env` file exists and contains `GEMINI_API_KEY=your_key`

**Issue**: Port already in use
- **Solution**: Run `streamlit run app.py --server.port 8502`

## Notes

- Keep your `.env` file secure and never commit it to version control
- Add `.env` to `.gitignore` if using Git
- The app uses Gemini 2.5 Flash model by default

## License

MIT
