"""
RAG chain for answering programming questions
"""
import os
from typing import Dict, Any
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain

class CodeLearningRAGChain:
    def __init__(self, vector_store, model_name: str = "gemini-2.0-flash-exp"):
        self.vector_store = vector_store
        self.llm = ChatGoogleGenerativeAI(
            model=model_name,
            temperature=0.1,
            google_api_key=os.getenv("GOOGLE_API_KEY")
        )
        self.memory = ConversationBufferMemory(
            memory_key="chat_history",
            return_messages=True
        )
        self._setup_chains()
    
    def _setup_chains(self):
        """Setup different types of chains for various use cases"""
        
        # Q&A Chain with custom prompt
        qa_prompt = PromptTemplate(
            template="""You are an expert programming tutor helping students learn to code. 
            Use the following context to answer the student's question in a clear, educational way.
            
            Context: {context}
            
            Question: {question}
            
            Instructions:
            - Provide clear, step-by-step explanations
            - Include code examples when helpful
            - Explain the reasoning behind your answer
            - If the context doesn't contain enough information, say so and provide general guidance
            - Keep your tone encouraging and supportive
            
            Answer:""",
            input_variables=["context", "question"]
        )
        
        retriever = self.vector_store.get_retriever(
            search_kwargs={"k": 5}
        )
        
        self.qa_chain = RetrievalQA.from_chain_type(
            llm=self.llm,
            chain_type="stuff",
            retriever=retriever,
            chain_type_kwargs={"prompt": qa_prompt},
            return_source_documents=True
        )
        
        # Conversational chain for follow-up questions
        conversational_prompt = PromptTemplate(
            template="""You are an expert programming tutor. Use the context and chat history to provide helpful, educational responses.
            
            Context: {context}
            Chat History: {chat_history}
            Question: {question}
            
            Provide a clear, educational response that builds on the conversation:""",
            input_variables=["context", "chat_history", "question"]
        )
        
        self.conversational_chain = ConversationalRetrievalChain.from_llm(
            llm=self.llm,
            retriever=retriever,
            memory=self.memory,
            combine_docs_chain_kwargs={"prompt": conversational_prompt}
        )
    
    def ask_question(self, question: str, use_conversation: bool = False) -> Dict[str, Any]:
        """Ask a programming question and get an answer"""
        try:
            if use_conversation:
                result = self.conversational_chain({"question": question})
                return {
                    "answer": result["answer"],
                    "source_documents": result.get("source_documents", []),
                    "chat_history": self.memory.chat_memory.messages
                }
            else:
                result = self.qa_chain({"query": question})
                return {
                    "answer": result["result"],
                    "source_documents": result["source_documents"]
                }
        
        except Exception as e:
            return {
                "answer": f"Sorry, I encountered an error: {str(e)}",
                "source_documents": []
            }
    
    def get_code_explanation(self, code: str, language: str = "python") -> str:
        """Get explanation for a piece of code"""
        question = f"Please explain this {language} code step by step:\n\n```{language}\n{code}\n```"
        result = self.ask_question(question)
        return result["answer"]
    
    def clear_memory(self):
        """Clear conversation memory"""
        self.memory.clear()