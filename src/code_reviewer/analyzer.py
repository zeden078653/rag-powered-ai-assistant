"""
Code analysis and review system
"""
import ast
import re
from typing import Dict, List, Any
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate

class CodeAnalyzer:
    def __init__(self):
        self.llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash-exp", temperature=0.1)
        self.review_prompt = PromptTemplate(
            template="""You are an expert code reviewer and programming tutor. 
            Analyze the following {language} code and provide educational feedback.
            
            Code:
            ```{language}
            {code}
            ```
            
            Please provide:
            1. **Code Quality Assessment** (1-10 score)
            2. **Issues Found** (bugs, style problems, potential improvements)
            3. **Educational Explanations** (why each issue matters)
            4. **Suggested Improvements** (with code examples)
            5. **Learning Opportunities** (concepts the student should study)
            
            Focus on being educational and encouraging. Explain the 'why' behind each suggestion.
            
            Review:""",
            input_variables=["code", "language"]
        )
    
    def analyze_python_syntax(self, code: str) -> Dict[str, Any]:
        """Basic Python syntax analysis"""
        issues = []
        suggestions = []
        
        try:
            # Parse the code to check for syntax errors
            ast.parse(code)
            syntax_valid = True
        except SyntaxError as e:
            syntax_valid = False
            issues.append({
                "type": "syntax_error",
                "message": f"Syntax error at line {e.lineno}: {e.msg}",
                "line": e.lineno,
                "severity": "high"
            })
        
        # Basic style checks
        lines = code.split('\n')
        for i, line in enumerate(lines, 1):
            # Check for long lines
            if len(line) > 100:
                issues.append({
                    "type": "style",
                    "message": "Line too long (>100 characters)",
                    "line": i,
                    "severity": "low"
                })
            
            # Check for missing spaces around operators
            if re.search(r'\w[+\-*/=]\w', line):
                suggestions.append({
                    "type": "style",
                    "message": "Consider adding spaces around operators",
                    "line": i,
                    "severity": "low"
                })
        
        return {
            "syntax_valid": syntax_valid,
            "issues": issues,
            "suggestions": suggestions
        }
    
    def get_ai_review(self, code: str, language: str = "python") -> str:
        """Get AI-powered code review"""
        try:
            chain = self.review_prompt | self.llm
            result = chain.invoke({
                "code": code,
                "language": language
            })
            return result.content
        except Exception as e:
            return f"Error generating review: {str(e)}"
    
    def comprehensive_review(self, code: str, language: str = "python") -> Dict[str, Any]:
        """Comprehensive code review combining static analysis and AI"""
        review_result = {
            "language": language,
            "code_length": len(code),
            "line_count": len(code.split('\n'))
        }
        
        # Static analysis for Python
        if language.lower() == "python":
            static_analysis = self.analyze_python_syntax(code)
            review_result.update(static_analysis)
        
        # AI-powered review
        ai_review = self.get_ai_review(code, language)
        review_result["ai_review"] = ai_review
        
        return review_result