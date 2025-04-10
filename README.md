# RAG Syllabus Q&A System

This project implements a Retrieval-Augmented Generation (RAG) system to answer questions based on your syllabus, notes, books, and presentations. It supports PDF, TXT, PPT/PPTX, and DOCX file formats and uses a local Large Language Model (LLM) via Ollama.

## Setup

### Prerequisites

* **Python 3.x** installed on your system.
* **Ollama** installed and running. Follow the installation instructions on the [Ollama website](https://ollama.ai/).
* **Llama 2** model downloaded via Ollama. Run `ollama pull llama2` in your terminal.
* **VS Code** (or your preferred code editor).

### Installation

1.  **Clone or create the project directory:**

    ```bash
    mkdir rag-syllabus-project
    cd rag-syllabus-project
    mkdir documents
    ```

2.  **Install Python dependencies:**

    ```bash
    pip install langchain sentence-transformers chromadb pypdf python-pptx docx tiktoken streamlit
    ```

3.  **Place your documents:**

    Copy your syllabus files (PDF, TXT, DOCX, PPT/PPTX) into the `documents/` folder.

4.  **Create `rag_app.py`:**

    Create a file named `rag_app.py` in the root of your project directory and paste the Python code provided in the previous responses into it. **Ensure the `file_paths` list in the code correctly points to your files within the `documents/` folder.**

## Running the Application

1.  **Open your project directory in VS Code.**
2.  **Open the VS Code terminal** (Terminal -> New Terminal).
3.  **Run the Streamlit application:**

    ```bash
    streamlit run rag_app.py
    ```

    This command will open a new tab in your web browser with the RAG Syllabus Q&A interface.

## Usage

1.  **Ask a question:** Enter your question related to your syllabus or study materials in the text input box.
2.  **Question Bank Mode:**
    * **Checked:** The system will prioritize answers found within your uploaded documents. If no relevant information is found, it will fall back on the LLM's general knowledge and indicate this in the answer. It will also provide a warning if the answer seems significantly different from the retrieved content.
    * **Unchecked:** The system will provide answers based on the retrieved information and the LLM's general knowledge without explicitly prioritizing the documents or providing the "general knowledge" disclaimer.
3.  **View the answer:** The generated answer will be displayed below the input box.


rag-syllabus-project/
├── rag_app.py           # The main Python application code
├── documents/          # Folder to store your syllabus, notes, books, etc.
│   ├── syllabus.pdf
│   ├── notes.txt
│   ├── book.docx
│   └── presentation.pptx
└── README.md           # This README file

## Further Enhancements

* **More sophisticated verification:** Implement semantic similarity checks or keyword analysis for better answer verification.
* **Source citation:** Add functionality to cite the specific documents or sections used to generate the answer.
* **Multi-turn conversations:** Allow for follow-up questions and maintain conversation history.
* **More advanced chunking strategies:** Experiment with different chunking methods for better retrieval.
* **Integration with other local LLMs:** Allow the user to choose from different models available in Ollama.
* **User interface improvements:** Enhance the Streamlit UI for better user experience.
## Project Structure
