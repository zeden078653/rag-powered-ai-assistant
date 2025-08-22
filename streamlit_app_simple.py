"""
Simplified Streamlit web interface for AI Code Learning Assistant
"""
import streamlit as st
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# For Streamlit Cloud deployment, also check secrets
if hasattr(st, 'secrets') and 'GOOGLE_API_KEY' in st.secrets:
    os.environ['GOOGLE_API_KEY'] = st.secrets['GOOGLE_API_KEY']
    if 'LANGCHAIN_API_KEY' in st.secrets:
        os.environ['LANGCHAIN_API_KEY'] = st.secrets['LANGCHAIN_API_KEY']
    if 'LANGCHAIN_TRACING_V2' in st.secrets:
        os.environ['LANGCHAIN_TRACING_V2'] = st.secrets['LANGCHAIN_TRACING_V2']

# Page configuration
st.set_page_config(
    page_title="AI Code Learning Assistant",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Sidebar
st.sidebar.title("🤖 AI Code Learning Assistant")
st.sidebar.markdown("---")
st.sidebar.markdown("### About")
st.sidebar.info(
    "This AI assistant helps you learn programming through:\n"
    "- Interactive Q&A with Google Gemini\n"
    "- Intelligent code reviews\n"
    "- Educational guidance\n"
    "- Programming help"
)

# Main content
st.title("🤖 AI Code Learning Assistant")
st.markdown("*Your intelligent companion for mastering programming concepts*")

# Check API key
if not os.getenv("GOOGLE_API_KEY"):
    st.error("❌ Google Gemini API key not found!")
    st.info("Please add your GOOGLE_API_KEY to the app secrets.")
    st.info("Get your free API key from: https://makersuite.google.com/app/apikey")
    st.stop()

# Try to import and initialize the assistant
try:
    from langchain_google_genai import ChatGoogleGenerativeAI
    
    # Initialize the LLM
    llm = ChatGoogleGenerativeAI(
        model="gemini-2.0-flash-exp",
        temperature=0.1,
        google_api_key=os.getenv("GOOGLE_API_KEY")
    )
    
    st.success("✅ AI Assistant initialized successfully!")
    
    # Feature selection
    feature = st.selectbox(
        "Choose a feature:",
        ["💬 Ask Questions", "🔍 Code Review", "💡 Get Help"]
    )
    
    if feature == "💬 Ask Questions":
        st.header("Ask Programming Questions")
        st.markdown("Get instant answers to your coding questions using Google Gemini.")
        
        question = st.text_area(
            "Ask your programming question:",
            placeholder="How do I implement a binary search in Python?",
            height=100
        )
        
        if st.button("Ask Question", type="primary") and question:
            with st.spinner("Thinking..."):
                try:
                    response = llm.invoke(f"""You are an expert programming tutor. 
                    Answer this question clearly and educationally: {question}
                    
                    Provide:
                    - Clear explanation
                    - Code examples if helpful
                    - Best practices
                    - Learning tips""")
                    
                    st.markdown("### Answer:")
                    st.markdown(response.content)
                    
                except Exception as e:
                    st.error(f"Error: {str(e)}")
    
    elif feature == "🔍 Code Review":
        st.header("Code Review")
        st.markdown("Get feedback on your code with educational explanations.")
        
        language = st.selectbox("Programming Language:", ["python", "javascript", "java", "cpp"])
        
        code_input = st.text_area(
            "Paste your code here:",
            height=300,
            placeholder="def fibonacci(n):\n    if n <= 1:\n        return n\n    return fibonacci(n-1) + fibonacci(n-2)"
        )
        
        if st.button("Review Code", type="primary") and code_input:
            with st.spinner("Analyzing your code..."):
                try:
                    prompt = f"""You are an expert code reviewer and programming tutor. 
                    Analyze this {language} code and provide educational feedback:
                    
                    ```{language}
                    {code_input}
                    ```
                    
                    Please provide:
                    1. Code Quality Assessment (1-10 score)
                    2. Issues Found (bugs, style problems, improvements)
                    3. Educational Explanations (why each issue matters)
                    4. Suggested Improvements (with examples)
                    5. Learning Opportunities (concepts to study)
                    
                    Be educational and encouraging."""
                    
                    response = llm.invoke(prompt)
                    
                    st.markdown("### Code Review:")
                    st.markdown(response.content)
                    
                except Exception as e:
                    st.error(f"Error: {str(e)}")
    
    elif feature == "💡 Get Help":
        st.header("Programming Help")
        st.markdown("Get help with programming concepts and problems.")
        
        help_topic = st.selectbox(
            "What do you need help with?",
            [
                "Python Basics",
                "Data Structures",
                "Algorithms",
                "Object-Oriented Programming",
                "Web Development",
                "Debugging",
                "Best Practices",
                "Other"
            ]
        )
        
        specific_question = st.text_area(
            "Describe your specific question or problem:",
            placeholder="I'm having trouble understanding how recursion works...",
            height=100
        )
        
        if st.button("Get Help", type="primary") and specific_question:
            with st.spinner("Preparing help..."):
                try:
                    prompt = f"""You are a patient programming tutor helping with {help_topic}.
                    
                    Student's question: {specific_question}
                    
                    Provide:
                    - Clear, step-by-step explanation
                    - Simple examples
                    - Common mistakes to avoid
                    - Practice suggestions
                    - Additional resources if helpful
                    
                    Keep it educational and encouraging."""
                    
                    response = llm.invoke(prompt)
                    
                    st.markdown("### Help & Guidance:")
                    st.markdown(response.content)
                    
                except Exception as e:
                    st.error(f"Error: {str(e)}")

except ImportError as e:
    st.error(f"❌ Failed to import required libraries: {str(e)}")
    st.info("The app is still loading dependencies. Please wait a moment and refresh.")

except Exception as e:
    st.error(f"❌ Error initializing AI Assistant: {str(e)}")
    st.info("Please check your API key and try again.")

# Footer
st.markdown("---")
st.markdown(
    "Built with ❤️ using Google Gemini and Streamlit | "
    "Demonstrating practical AI applications in education"
)