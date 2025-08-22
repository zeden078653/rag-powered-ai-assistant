"""
Streamlit web interface for AI Code Learning Assistant
"""
import streamlit as st
import os
import sys
from dotenv import load_dotenv

# Add src to path
sys.path.append('src')

from main import AICodeLearningAssistant

# Load environment variables
load_dotenv()

# For Streamlit Cloud deployment, also check secrets
import streamlit as st
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

# Initialize session state
if 'assistant' not in st.session_state:
    st.session_state.assistant = AICodeLearningAssistant()
    st.session_state.assistant.initialize()

if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

# Sidebar
st.sidebar.title("🤖 AI Code Learning Assistant")
st.sidebar.markdown("---")

# Feature selection
feature = st.sidebar.selectbox(
    "Choose a feature:",
    ["💬 Ask Questions", "🔍 Code Review", "🎯 Practice Problems", "💡 Get Hints"]
)

st.sidebar.markdown("---")
st.sidebar.markdown("### About")
st.sidebar.info(
    "This AI assistant helps you learn programming through:\n"
    "- Interactive Q&A with RAG\n"
    "- Intelligent code reviews\n"
    "- Personalized practice problems\n"
    "- Contextual hints and guidance"
)

# Main content
st.title("🤖 AI Code Learning Assistant")
st.markdown("*Your intelligent companion for mastering programming concepts*")

if not st.session_state.assistant.initialized:
    st.error("❌ Assistant not initialized. Please check your Google Gemini API key in .env file.")
    st.info("Get your free API key from: https://makersuite.google.com/app/apikey")
    st.stop()

# Feature implementations
if feature == "💬 Ask Questions":
    st.header("Ask Programming Questions")
    st.markdown("Get instant, contextual answers to your coding questions using RAG technology.")
    
    # Chat interface
    question = st.text_input("Ask your programming question:", placeholder="How do I implement a binary search in Python?")
    
    col1, col2 = st.columns([1, 4])
    with col1:
        ask_button = st.button("Ask Question", type="primary")
    with col2:
        clear_chat = st.button("Clear Chat History")
    
    if clear_chat:
        st.session_state.chat_history = []
        st.session_state.assistant.rag_chain.clear_memory()
        st.success("Chat history cleared!")
    
    if ask_button and question:
        with st.spinner("Thinking..."):
            result = st.session_state.assistant.ask_question(question, use_conversation=True)
            
            # Add to chat history
            st.session_state.chat_history.append({"question": question, "answer": result["answer"]})
    
    # Display chat history
    if st.session_state.chat_history:
        st.markdown("### Conversation History")
        for i, chat in enumerate(reversed(st.session_state.chat_history[-5:])):  # Show last 5
            with st.expander(f"Q: {chat['question'][:50]}...", expanded=(i==0)):
                st.markdown(f"**Question:** {chat['question']}")
                st.markdown(f"**Answer:** {chat['answer']}")

elif feature == "🔍 Code Review":
    st.header("Intelligent Code Review")
    st.markdown("Get detailed feedback on your code with educational explanations.")
    
    col1, col2 = st.columns([3, 1])
    with col1:
        language = st.selectbox("Programming Language:", ["python", "javascript", "java", "cpp"])
    with col2:
        review_button = st.button("Review Code", type="primary")
    
    code_input = st.text_area(
        "Paste your code here:",
        height=300,
        placeholder="def fibonacci(n):\n    if n <= 1:\n        return n\n    return fibonacci(n-1) + fibonacci(n-2)"
    )
    
    if review_button and code_input:
        with st.spinner("Analyzing your code..."):
            review = st.session_state.assistant.review_code(code_input, language)
            
            if "error" not in review:
                st.success("✅ Code analysis complete!")
                
                # Display results
                col1, col2 = st.columns(2)
                
                with col1:
                    st.subheader("📊 Quick Stats")
                    st.metric("Lines of Code", review["line_count"])
                    st.metric("Characters", review["code_length"])
                    
                    if "syntax_valid" in review:
                        status = "✅ Valid" if review["syntax_valid"] else "❌ Invalid"
                        st.metric("Syntax", status)
                
                with col2:
                    if "issues" in review and review["issues"]:
                        st.subheader("⚠️ Issues Found")
                        for issue in review["issues"]:
                            st.warning(f"Line {issue['line']}: {issue['message']}")
                
                # AI Review
                st.subheader("🤖 AI Code Review")
                st.markdown(review["ai_review"])
            else:
                st.error(f"Error: {review['error']}")

elif feature == "🎯 Practice Problems":
    st.header("Personalized Practice Problems")
    st.markdown("Generate coding challenges tailored to your learning needs.")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        topic = st.selectbox("Topic:", st.session_state.assistant.problem_generator.get_problem_topics())
    with col2:
        difficulty = st.selectbox("Difficulty:", ["beginner", "intermediate", "advanced"])
    with col3:
        language = st.selectbox("Language:", ["python", "javascript", "java", "cpp"])
    
    generate_button = st.button("Generate Problem", type="primary")
    
    if generate_button:
        with st.spinner("Creating your personalized problem..."):
            problem = st.session_state.assistant.generate_problem(topic, difficulty, language)
            
            if problem.get("generated"):
                st.success("🎯 Problem generated successfully!")
                
                # Store in session state for hints
                st.session_state.current_problem = problem["problem_content"]
                
                # Display problem
                st.markdown("### Your Challenge")
                st.markdown(problem["problem_content"])
                
                # Code editor for solution
                st.markdown("### Your Solution")
                solution_code = st.text_area(
                    "Write your solution here:",
                    height=200,
                    key="solution_code"
                )
                
                if solution_code:
                    col1, col2 = st.columns(2)
                    with col1:
                        if st.button("Get Hint"):
                            hint = st.session_state.assistant.get_hint(
                                st.session_state.current_problem, 
                                solution_code, 
                                1
                            )
                            st.info(f"💡 Hint: {hint}")
                    
                    with col2:
                        if st.button("Review My Solution"):
                            review = st.session_state.assistant.review_code(solution_code, language)
                            st.markdown("### Code Review")
                            st.markdown(review["ai_review"])
            else:
                st.error(f"Failed to generate problem: {problem.get('error', 'Unknown error')}")

elif feature == "💡 Get Hints":
    st.header("Smart Hints System")
    st.markdown("Get progressive hints for any coding problem you're working on.")
    
    problem_text = st.text_area(
        "Describe the problem you're working on:",
        height=150,
        placeholder="Write a function that finds the maximum element in an array..."
    )
    
    current_code = st.text_area(
        "Your current attempt (optional):",
        height=200,
        placeholder="def find_max(arr):\n    # Your code here"
    )
    
    hint_level = st.slider("Hint Level:", 1, 3, 1, help="1=Gentle nudge, 2=More specific, 3=Detailed guidance")
    
    if st.button("Get Hint", type="primary") and problem_text:
        with st.spinner("Generating hint..."):
            hint = st.session_state.assistant.get_hint(problem_text, current_code, hint_level)
            
            st.success("💡 Here's your hint:")
            st.info(hint)

# Footer
st.markdown("---")
st.markdown(
    "Built with ❤️ using LangChain, Google Gemini, ChromaDB, and Streamlit | "
    "Demonstrating practical GenAI applications in education"
)