# 🔑 Google Gemini API Setup Guide

This project uses Google's Gemini Pro API, which is free and powerful. Here's how to set it up:

## Step 1: Get Your API Key

1. Go to [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Sign in with your Google account
3. Click "Create API Key"
4. Copy the generated API key

## Step 2: Set Up Environment Variables

1. Copy the example environment file:
   ```bash
   cp .env.example .env
   ```

2. Open `.env` file and add your API key:
   ```
   GOOGLE_API_KEY=your_actual_api_key_here
   ```

## Step 3: Test the Setup

Run the setup script to verify everything works:
```bash
python setup.py
```

Then test the application:
```bash
streamlit run streamlit_app.py
```

## Why Gemini Pro?

✅ **Free to use** - No credit card required  
✅ **Powerful performance** - Comparable to GPT-3.5/4  
✅ **Good for education** - Excellent at explanations  
✅ **Fast responses** - Low latency  
✅ **Large context window** - Can handle long documents  

## API Limits

- **Free tier**: 60 requests per minute
- **Rate limit**: Sufficient for development and demos
- **Context length**: Up to 30,720 tokens

## Troubleshooting

### Error: "API key not found"
- Make sure your `.env` file is in the project root
- Check that `GOOGLE_API_KEY` is spelled correctly
- Verify your API key is valid

### Error: "Rate limit exceeded"
- Wait a minute and try again
- The free tier has generous limits for development

### Error: "Model not found"
- Make sure you're using `gemini-pro` (not `gemini-pro-vision`)
- Check your internet connection

## Alternative Models

You can also use other Gemini models by changing the model name in the code:

- `gemini-pro` - Best for text generation (recommended)
- `gemini-pro-vision` - For image + text (not used in this project)

## Cost Comparison

| Provider | Model | Cost | Our Choice |
|----------|-------|------|------------|
| Google | Gemini Pro | **FREE** | ✅ |
| OpenAI | GPT-3.5-turbo | $0.002/1K tokens | ❌ |
| OpenAI | GPT-4 | $0.03/1K tokens | ❌ |

Using Gemini Pro makes this project completely free to run and demo!