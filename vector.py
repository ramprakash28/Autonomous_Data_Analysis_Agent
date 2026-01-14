from langchain_ollama import OllamaEmbeddings  # For generating vector embeddings
from langchain_chroma import Chroma  # Chroma vector database
from langchain_core.documents import Document  # Document structure for LangChain
import os  # For file system operations
import pandas as pd  # For reading CSV files

df = pd.read_csv("realistic_restaurant_reviews.csv")  # Load restaurant reviews from CSV

# Instantiate the embedding model (Ollama)
embeddings = OllamaEmbeddings(model='mxbai-embed-large')

# Set the location for the Chroma vector database
db_location = "./chrome_langchain_db"
# Flag to determine if documents need to be added (True if DB doesn't exist)
add_documents = not os.path.exists(db_location)

# If the database doesn't exist, create documents from the CSV
if add_documents:
    documents = []
    ids = []

    for i, row in df.iterrows():
        # Create a LangChain Document for each review
        document = Document(
            page_content=row["Title"] + " " + row["Review"],  # Combine title and review text
            meta_data={"rating": row["Rating"], "date": row["Date"]},  # Add metadata
            id=str(i)  # Unique ID for each document
        )
        ids.append(str(i))
        documents.append(document)

# Initialize the Chroma vector store (persisted on disk)
vector_store = Chroma(
    collection_name="restaurant_reviews",
    persist_directory=db_location,
    embedding_function=embeddings
)

# Add documents to the vector store if it's a new database
if add_documents:
    vector_store.add_documents(documents=documents, ids=ids)

# Create a retriever to search for the top 2 most similar reviews
retriever = vector_store.as_retriever(
    search_kwargs={"k": 2}
)