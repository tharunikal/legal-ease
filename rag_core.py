import os
from typing import List
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.llms import Ollama
from langchain.chains import RetrievalQA

class LegalRAGSystem:
    def __init__(self, document_path: str):
        self.document_path = document_path
        self.qa_chain = self._initialize_rag()

    def _load_document(self) -> List:
        """Load and split a single PDF document"""
        if not os.path.exists(self.document_path):
            raise FileNotFoundError(f"Document not found at {self.document_path}")
        
        loader = PyPDFLoader(self.document_path)
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=400,
            chunk_overlap=50,
            separators=["\n\n", "\n", " ", ""]
        )
        return text_splitter.split_documents(loader.load())

    def _initialize_rag(self):
        """Initialize RAG components"""
        chunks = self._load_document()
        
        embeddings = HuggingFaceEmbeddings(
            model_name="all-MiniLM-L6-v2",
            encode_kwargs={'normalize_embeddings': False}
        )
        
        db = FAISS.from_documents(chunks, embeddings)
        
        llm = Ollama(
            model="phi3",
            temperature=0.3,
            num_thread=max(1, os.cpu_count() - 1)
        )
        
        return RetrievalQA.from_chain_type(
            llm=llm,
            retriever=db.as_retriever(search_kwargs={"k": 2}),
            chain_type="stuff"
        )

    def query(self, question: str) -> str:
        """Process a question and return answer"""
        return self.qa_chain.invoke({"query": question})["result"]