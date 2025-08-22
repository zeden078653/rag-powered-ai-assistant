# Deployment Guide

## Deploy to Streamlit Cloud

### Prerequisites
- GitHub account
- Google Gemini API key

### Steps

1. **Fork this repository** to your GitHub account

2. **Go to Streamlit Cloud**
   - Visit [share.streamlit.io](https://share.streamlit.io)
   - Sign in with your GitHub account

3. **Deploy the app**
   - Click "New app"
   - Select "From existing repo"
   - Choose your forked repository
   - Set main file: `streamlit_app.py`
   - Click "Deploy!"

4. **Add your API keys**
   - Go to app settings (☰ menu)
   - Click "Secrets"
   - Add your secrets in TOML format:
   ```toml
   GOOGLE_API_KEY = "your_google_gemini_api_key"
   LANGCHAIN_TRACING_V2 = "false"
   ```

5. **Get your Google Gemini API key**
   - Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
   - Create a free API key
   - Add it to your Streamlit secrets

### Your app will be available at:
`https://your-app-name.streamlit.app`

## Local Development

For local development, create a `.env` file:
```
GOOGLE_API_KEY=your_google_gemini_api_key
LANGCHAIN_TRACING_V2=false
LANGCHAIN_API_KEY=your_langchain_api_key_here
```

Then run:
```bash
pip install -r requirements.txt
streamlit run streamlit_app.py
```

## Features

- 💬 Interactive Q&A with RAG
- 🔍 Intelligent code reviews
- 🎯 Personalized practice problems
- 💡 Contextual hints and guidance