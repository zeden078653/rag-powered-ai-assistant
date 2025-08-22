# AI Code Learning Assistant 🤖📚

An intelligent learning companion that helps students master programming concepts through personalized explanations, code reviews, and interactive Q&A using RAG (Retrieval-Augmented Generation).

## 🎯 Project Overview

This project demonstrates practical GenAI applications in education by building a comprehensive learning assistant that:
- Provides contextual programming help using RAG pipelines
- Reviews student code and offers improvement suggestions
- Creates personalized learning paths based on student progress
- Generates practice problems tailored to individual skill levels

## 🛠️ Tech Stack

- **Python 3.9+**
- **LangChain** - For LLM orchestration and chains
- **Google Gemini Pro** - Primary language model
- **ChromaDB** - Vector database for RAG
- **Streamlit** - Interactive web interface
- **Sentence Transformers** - For embeddings
- **FastAPI** - Backend API (optional)

## 🚀 Features

### 1. RAG-Powered Q&A System
- Ingests programming documentation, tutorials, and best practices
- Provides contextually relevant answers to coding questions
- Maintains conversation history for better context

### 2. Intelligent Code Review
- Analyzes student code for bugs, style issues, and improvements
- Provides educational explanations for suggested changes
- Tracks common mistakes and learning patterns

### 3. Personalized Learning Paths
- Assesses student skill level through interactive coding challenges
- Generates customized curriculum based on strengths/weaknesses
- Adapts difficulty based on performance

### 4. Practice Problem Generator
- Creates coding problems tailored to specific concepts
- Provides hints and step-by-step solutions
- Tracks progress and suggests next topics

## 📁 Project Structure

```
ai-code-learning-assistant/
├── src/
│   ├── rag_system/
│   │   ├── __init__.py
│   │   ├── document_loader.py
│   │   ├── vector_store.py
│   │   └── retrieval_chain.py
│   ├── code_reviewer/
│   │   ├── __init__.py
│   │   ├── analyzer.py
│   │   └── feedback_generator.py
│   ├── learning_path/
│   │   ├── __init__.py
│   │   ├── skill_assessor.py
│   │   └── curriculum_generator.py
│   ├── problem_generator/
│   │   ├── __init__.py
│   │   └── generator.py
│   └── main.py
├── data/
│   ├── programming_docs/
│   └── sample_code/
├── streamlit_app.py
├── requirements.txt
└── README.md
```

## 🎓 Educational Impact

This project showcases how GenAI can transform programming education by:
- Making learning more interactive and personalized
- Providing instant, contextual feedback
- Adapting to individual learning styles and pace
- Reducing barriers to getting help with coding problems

## 🔧 Installation & Setup

```bash
# Clone the repository
git clone <your-repo-url>
cd ai-code-learning-assistant

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env
# Add your Google Gemini API key to .env

# Run the application
streamlit run streamlit_app.py
```

## 💡 Why This Project Matters

This demonstrates practical GenAI applications in education - exactly what Coding Ninjas is building. It shows understanding of:
- RAG pipelines for knowledge retrieval
- LLM integration for educational content
- User-centric design for learners
- Scalable architecture for real-world deployment

---

*Built with curiosity, experimentation, and a passion for making coding education more accessible through AI.*