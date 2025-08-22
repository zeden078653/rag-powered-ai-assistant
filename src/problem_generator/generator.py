"""
AI-powered coding problem generator
"""
from typing import Dict, List, Any
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate

class ProblemGenerator:
    def __init__(self):
        self.llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash-exp", temperature=0.7)
        
        self.problem_prompt = PromptTemplate(
            template="""You are an expert programming instructor creating practice problems.
            
            Generate a coding problem with the following specifications:
            - Topic: {topic}
            - Difficulty: {difficulty}
            - Language: {language}
            - Student Level: {student_level}
            
            Please provide:
            1. **Problem Title**
            2. **Problem Description** (clear and engaging)
            3. **Input/Output Examples** (at least 2 examples)
            4. **Constraints**
            5. **Hints** (3 progressive hints)
            6. **Solution Approach** (high-level strategy)
            7. **Sample Solution** (well-commented code)
            8. **Learning Objectives** (what concepts this teaches)
            
            Make the problem educational and appropriately challenging for the student level.
            
            Problem:""",
            input_variables=["topic", "difficulty", "language", "student_level"]
        )
        
        self.hint_prompt = PromptTemplate(
            template="""For the following coding problem, provide a helpful hint that guides the student without giving away the solution.
            
            Problem: {problem}
            Current attempt: {student_code}
            Hint level: {hint_level} (1=gentle nudge, 2=more specific, 3=detailed guidance)
            
            Provide an educational hint:""",
            input_variables=["problem", "student_code", "hint_level"]
        )
    
    def generate_problem(self, topic: str, difficulty: str = "medium", 
                        language: str = "python", student_level: str = "beginner") -> Dict[str, Any]:
        """Generate a coding problem"""
        try:
            chain = self.problem_prompt | self.llm
            result = chain.invoke({
                "topic": topic,
                "difficulty": difficulty,
                "language": language,
                "student_level": student_level
            })
            
            return {
                "topic": topic,
                "difficulty": difficulty,
                "language": language,
                "student_level": student_level,
                "problem_content": result.content,
                "generated": True
            }
        
        except Exception as e:
            return {
                "error": f"Failed to generate problem: {str(e)}",
                "generated": False
            }
    
    def get_hint(self, problem: str, student_code: str = "", hint_level: int = 1) -> str:
        """Generate a hint for the student"""
        try:
            chain = self.hint_prompt | self.llm
            result = chain.invoke({
                "problem": problem,
                "student_code": student_code,
                "hint_level": hint_level
            })
            return result.content
        
        except Exception as e:
            return f"Error generating hint: {str(e)}"
    
    def get_problem_topics(self) -> List[str]:
        """Get list of available problem topics"""
        return [
            "Arrays and Lists",
            "Strings and Text Processing",
            "Loops and Iteration",
            "Functions and Recursion",
            "Data Structures (Stack, Queue)",
            "Sorting and Searching",
            "Object-Oriented Programming",
            "File I/O",
            "Error Handling",
            "Algorithm Design",
            "Dynamic Programming",
            "Graph Algorithms",
            "Mathematical Problems",
            "Pattern Matching",
            "Database Operations"
        ]
    
    def generate_problem_set(self, topics: List[str], count: int = 5, 
                           difficulty: str = "medium", language: str = "python") -> List[Dict[str, Any]]:
        """Generate a set of problems"""
        problems = []
        
        for i in range(count):
            topic = topics[i % len(topics)]
            problem = self.generate_problem(topic, difficulty, language)
            if problem.get("generated"):
                problems.append(problem)
        
        return problems