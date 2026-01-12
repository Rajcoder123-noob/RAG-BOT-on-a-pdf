#RAG System for Mathematics for Machine Learning

This project implements a Retrieval-Augmented Generation (RAG) pipeline that enables intelligent question answering over the PDF Mathematics for Machine Learning.
The system extracts text from the PDF, generates vector embeddings using the OpenAI API, stores them in Qdrant, and retrieves relevant context at query time to generate accurate, grounded answers.

The entire vector database setup is containerized using Docker.

🚀 Features

📄 PDF ingestion and text chunking

🧠 Semantic embeddings using OpenAI models

📦 Vector storage and similarity search with Qdrant

🐳 Dockerized vector database for easy deployment

💬 Context-aware Q&A using Retrieval-Augmented Generation

📐 Domain-specific focus on Machine Learning mathematics

🏗️ Architecture Overview

PDF Loader
Loads Mathematics for Machine Learning and extracts raw text.

Text Chunking
Splits text into overlapping chunks to preserve mathematical context.

Embedding Generation
Each chunk is converted into a dense vector using OpenAI Embedding models.

Vector Storage (Qdrant)
Embeddings are stored and indexed inside Qdrant running in Docker.

Retriever
Relevant chunks are retrieved via cosine similarity.

LLM Response Generation
Retrieved context + user query → OpenAI LLM → final answer.

📂 Project Structure
rag-math-ml/
│
├── data/
│   └── mathematics_for_machine_learning.pdf
│
├── embeddings/
│   └── ingest.py          # PDF parsing & embedding pipeline
│
├── rag/
│   ├── retriever.py       # Qdrant similarity search
│   └── qa.py              # RAG-based question answering
│
├── docker/
│   └── docker-compose.yml # Qdrant container setup
│
├── .env                   # OpenAI API key
├── requirements.txt
└── README.md

🔑 Prerequisites

Python 3.9+

Docker & Docker Compose

OpenAI API Key

Basic understanding of RAG and vector databases

⚙️ Setup Instructions
1️⃣ Clone the Repository
git clone https://github.com/your-username/rag-math-ml.git
cd rag-math-ml

2️⃣ Set Environment Variables

Create a .env file:

OPENAI_API_KEY=your_openai_api_key_here

3️⃣ Start Qdrant Using Docker
docker-compose up -d


Qdrant will be available at:

http://localhost:6333

4️⃣ Install Python Dependencies
pip install -r requirements.txt

5️⃣ Ingest the PDF and Create Embeddings
python embeddings/ingest.py


This step:

Loads the PDF

Splits text into chunks

Generates embeddings

Stores them in Qdrant

6️⃣ Ask Questions
python rag/qa.py


Example questions:

What is eigenvalue decomposition?

Explain gradient descent mathematically.

What role does linear algebra play in machine learning?

🧠 Why RAG for Mathematics?

Mathematical content:

Requires high factual accuracy

Has symbol-dense explanations

Benefits from exact source grounding

RAG ensures responses are:

Based on original textbook context

Less prone to hallucinations

More reliable for technical learning

🧪 Tech Stack
Component	Technology
LLM & Embeddings	OpenAI API
Vector Database	Qdrant
Containerization	Docker
Language	Python
Document Type	PDF
🔮 Future Improvements

📊 Add citation highlighting from PDF pages

🌐 Web-based UI (Streamlit / React)

➗ LaTeX rendering for equations

🧮 Support for multiple ML textbooks

📜 License

This project is for educational and research purposes only.
Ensure you have the legal right to use the Mathematics for Machine Learning PDF.

🙌 Acknowledgements

OpenAI for embedding and LLM APIs

Qdrant for high-performance vector search

Authors of Mathematics for Machine Learning for foundational knowledge
