"""
Document loader for programming documentation and tutorials
"""
import os
from typing import List
from langchain_community.document_loaders import TextLoader, DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document

class ProgrammingDocumentLoader:
    def __init__(self, chunk_size: int = 1000, chunk_overlap: int = 200):
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
            separators=["\n\n", "\n", " ", ""]
        )
    
    def load_documents(self, directory_path: str) -> List[Document]:
        """Load and split documents from directory"""
        try:
            loader = DirectoryLoader(
                directory_path,
                glob="**/*.txt",
                loader_cls=TextLoader,
                loader_kwargs={'encoding': 'utf-8'}
            )
            documents = loader.load()
            
            # Split documents into chunks
            split_docs = self.text_splitter.split_documents(documents)
            
            # Add metadata for better retrieval
            for doc in split_docs:
                doc.metadata['source_type'] = 'programming_doc'
                doc.metadata['chunk_size'] = len(doc.page_content)
            
            return split_docs
        
        except Exception as e:
            print(f"Error loading documents: {e}")
            return []
    
    def load_code_examples(self, examples_path: str) -> List[Document]:
        """Load code examples with special handling"""
        code_docs = []
        
        for root, dirs, files in os.walk(examples_path):
            for file in files:
                if file.endswith(('.py', '.js', '.java', '.cpp')):
                    file_path = os.path.join(root, file)
                    try:
                        with open(file_path, 'r', encoding='utf-8') as f:
                            content = f.read()
                        
                        # Create document with code-specific metadata
                        doc = Document(
                            page_content=content,
                            metadata={
                                'source': file_path,
                                'language': file.split('.')[-1],
                                'source_type': 'code_example',
                                'filename': file
                            }
                        )
                        code_docs.append(doc)
                    
                    except Exception as e:
                        print(f"Error loading {file_path}: {e}")
        
        return code_docs