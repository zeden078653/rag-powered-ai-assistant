# 🚀 Installation Guide

Follow these steps to set up the AI Code Learning Assistant on your system.

## Prerequisites

- Python 3.9 or higher
- Internet connection (for API calls and package installation)
- Google account (for free Gemini API key)

## Step 1: Clone or Download the Project

If you have the project files, navigate to the project directory:
```bash
cd ai-code-learning-assistant
```

## Step 2: Install Dependencies

### Option A: Using the Setup Script (Recommended)
```bash
python setup.py
```

### Option B: Manual Installation
```bash
pip install -r requirements.txt
```

## Step 3: Get Your Free Gemini API Key

1. Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Sign in with your Google account
3. Click "Create API Key"
4. Copy the generated API key

## Step 4: Configure Environment Variables

1. Copy the example environment file:
   ```bash
   cp .env.example .env
   ```

2. Open `.env` file in a text editor and replace the placeholder:
   ```
   GOOGLE_API_KEY=your_actual_api_key_here
   LANGCHAIN_TRACING_V2=true
   LANGCHAIN_API_KEY=your_langchain_api_key_here
   ```

   **Note:** Only the `GOOGLE_API_KEY` is required. The LangChain settings are optional.

## Step 5: Run the Application

### Web Interface (Recommended)
```bash
streamlit run streamlit_app.py
```

The application will open in your browser at `http://localhost:8501`

### Command Line Testing
```bash
python src/main.py
```

## Troubleshooting

### Common Issues

#### 1. "ModuleNotFoundError: No module named 'dotenv'"
**Solution:** Install the requirements first:
```bash
pip install -r requirements.txt
```

#### 2. "GOOGLE_API_KEY not found in environment variables"
**Solution:** 
- Make sure you created the `.env` file
- Check that your API key is correctly set in `.env`
- Verify the file is in the project root directory

#### 3. "Error initializing assistant"
**Solution:**
- Check your internet connection
- Verify your API key is valid
- Make sure you have sufficient API quota

#### 4. Streamlit not opening in browser
**Solution:**
- Check if port 8501 is available
- Try accessing manually: http://localhost:8501
- Use a different port: `streamlit run streamlit_app.py --server.port 8502`

### Package Installation Issues

#### On Windows:
```bash
# If you get SSL errors
pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org -r requirements.txt
```

#### On macOS/Linux:
```bash
# If you get permission errors
pip install --user -r requirements.txt
```

#### Using Virtual Environment (Recommended):
```bash
# Create virtual environment
python -m venv venv

# Activate it
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install requirements
pip install -r requirements.txt
```

## Verification

After installation, you should see:
1. ✅ All packages installed successfully
2. ✅ Environment file configured
3. ✅ Application starts without errors
4. ✅ Web interface loads properly

## Next Steps

1. **Test the features**: Try each tab in the web interface
2. **Review the demo guide**: Check `DEMO_GUIDE.md` for presentation tips
3. **Customize the content**: Add your own programming documentation to `data/programming_docs/`

## Getting Help

If you encounter issues:
1. Check this troubleshooting section
2. Verify all prerequisites are met
3. Ensure your API key is valid and has quota
4. Check the console output for specific error messages

## System Requirements

- **RAM**: 4GB minimum (8GB recommended)
- **Storage**: 2GB free space
- **Network**: Stable internet connection for API calls
- **Browser**: Modern browser (Chrome, Firefox, Safari, Edge)

The application is lightweight and should run smoothly on most modern systems!