# Autonomous Data Analysis Agent

## Overview
This project is an autonomous agent for data analysis, leveraging LLMs and vector databases to automate exploratory data analysis (EDA), insight generation, and question answering on structured datasets and restaurant reviews.

## Features
- **Automated EDA**: Summarizes missing values, numeric distributions, and correlations for tabular datasets.
- **LLM-powered Insights**: Uses a local LLM (Ollama) to explain EDA findings and answer questions.
- **CSV Inspection**: Loads and inspects CSV files for quick data profiling.
- **Memory Store**: Saves and retrieves observations for session continuity.
- **Vector Search**: Embeds and retrieves restaurant reviews using LangChain and Chroma for semantic search.
- **Interactive Q&A**: Ask questions about restaurant reviews and get expert answers powered by LLM and vector search.

## Project Structure
- `agent.py`: Main agent logic for EDA, LLM calls, and explanations.
- `eda.py`: Functions for running EDA on pandas DataFrames.
- `llm.py`: Interface to the Ollama LLM API.
- `tools.py`: CSV inspection utilities.
- `memory.py`: In-memory store for observations.
- `vector.py`: Embedding and vector search setup for restaurant reviews.
- `main.py`: Interactive Q&A for restaurant reviews using LLM and vector search.
- `requirements.txt`: Python dependencies.
- `Exam_Score_Prediction.csv`, `sample_dataset.csv`: Example tabular datasets.
- `realistic_restaurant_reviews.csv`: Sample restaurant review data.

## Setup Instructions
1. **Install Python dependencies:**
	```sh
	pip install -r requirements.txt
	```
2. **Start Ollama LLM server:**
	- Ensure Ollama is running locally on port 11434.
	- Download the required model (e.g., llama3.2).
3. **Run the agent:**
	```sh
	python agent.py
	```
4. **Run the restaurant review Q&A:**
	```sh
	python main.py
	```

## Example Datasets
- `Exam_Score_Prediction.csv`: Student exam scores and related features.
- `realistic_restaurant_reviews.csv`: Pizza restaurant reviews with ratings and dates.
- `sample_dataset.csv`: Simple tabular data for testing.

## Technologies Used
- Python, Pandas, NumPy
- LangChain, LangChain-Ollama, LangChain-Chroma
- Ollama LLM (local API)
- Chroma vector database

## Usage
- Modify the CSV file paths in the scripts as needed.
- Use `agent.py` for EDA and insight generation.
- Use `main.py` for interactive restaurant review Q&A.

## License
MIT