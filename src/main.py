"""
Main application orchestrator for AI Code Learning Assistant
"""
import os
from dotenv import load_dotenv
from rag_system.document_loader import ProgrammingDocumentLoader
from rag_system.vector_store import CodeLearningVectorStore
from rag_system.retrieval_chain import CodeLearningRAGChain
from code_reviewer.analyzer import CodeAnalyzer
from problem_generator.generator import ProblemGenerator

# Load environment variables
load_dotenv()

class AICodeLearningAssistant:
    def __init__(self):
        self.vector_store = None
        self.rag_chain = None
        self.code_analyzer = None
        self.problem_generator = None
        self.initialized = False
    
    def initialize(self, docs_path: str = "./data/programming_docs"):
        """Initialize all components"""
        try:
            # Check for API key
            if not os.getenv("GOOGLE_API_KEY"):
                print("❌ GOOGLE_API_KEY not found in environment variables")
                print("Please set up your .env file with your Gemini API key")
                print("Get your free API key from: https://makersuite.google.com/app/apikey")
                self.initialized = False
                return
            
            # Initialize vector store
            self.vector_store = CodeLearningVectorStore()
            
            # Load documents if directory exists
            if os.path.exists(docs_path):
                doc_loader = ProgrammingDocumentLoader()
                documents = doc_loader.load_documents(docs_path)
                
                if documents:
                    self.vector_store.add_documents(documents)
                    print(f"Loaded {len(documents)} documents into vector store")
            
            # Initialize RAG chain
            self.rag_chain = CodeLearningRAGChain(self.vector_store)
            
            # Initialize other components
            self.code_analyzer = CodeAnalyzer()
            self.problem_generator = ProblemGenerator()
            
            self.initialized = True
            print("AI Code Learning Assistant initialized successfully!")
            print("Using Google Gemini 2.0 Flash API")
            
        except Exception as e:
            print(f"Error initializing assistant: {e}")
            print("Make sure your GOOGLE_API_KEY is valid and you have internet connection")
            self.initialized = False
    
    def ask_question(self, question: str, use_conversation: bool = True):
        """Ask a programming question"""
        if not self.initialized:
            return {"error": "Assistant not initialized"}
        
        return self.rag_chain.ask_question(question, use_conversation)
    
    def review_code(self, code: str, language: str = "python"):
        """Review student code"""
        if not self.initialized:
            return {"error": "Assistant not initialized"}
        
        return self.code_analyzer.comprehensive_review(code, language)
    
    def generate_problem(self, topic: str, difficulty: str = "medium", language: str = "python"):
        """Generate a coding problem"""
        if not self.initialized:
            return {"error": "Assistant not initialized"}
        
        return self.problem_generator.generate_problem(topic, difficulty, language)
    
    def get_hint(self, problem: str, student_code: str = "", hint_level: int = 1):
        """Get a hint for a problem"""
        if not self.initialized:
            return {"error": "Assistant not initialized"}
        
        return self.problem_generator.get_hint(problem, student_code, hint_level)

# Global instance
assistant = AICodeLearningAssistant()

if __name__ == "__main__":
    # Initialize the assistant
    assistant.initialize()
    
    # Example usage
    if assistant.initialized:
        # Test Q&A
        result = assistant.ask_question("How do I create a list in Python?")
        print("Q&A Result:", result["answer"])
        
        # Test code review
        sample_code = """
def add_numbers(a,b):
    return a+b
        """
        review = assistant.review_code(sample_code)
        print("Code Review:", review["ai_review"])
        
        # Test problem generation
        problem = assistant.generate_problem("Arrays and Lists", "beginner")
        if problem.get("generated"):
            print("Generated Problem:", problem["problem_content"][:200] + "...")
        else:
            print("Problem generation failed:", problem.get("error", "Unknown error"))