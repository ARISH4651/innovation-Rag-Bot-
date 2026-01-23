# Innovation RAG Bot

A Python-based Retrieval-Augmented Generation (RAG) chatbot that uses Google's Gemini model to answer questions based on a custom knowledge base.

## Project Overview

This application serves as an educational example of building a RAG chatbot. It utilizes a "naive RAG" approach where knowledge is loaded from a local CSV file and injected directly into the Large Language Model's (LLM) context window to provide accurate, domain-specific answers.

## Architecture

The bot operates using a straightforward context-injection pattern:
1.  **Data Loading**: Loads Q&A pairs from a CSV file (`qa_data (1).csv`) using Pandas.
2.  **Context Construction**: Aggregates the knowledge base into a single text block.
3.  **Query Processing**: Captures user input via a Command Line Interface (CLI).
4.  **Inference**: Sends the user query along with the full context to Google's Gemini-2.5-Flash model.
5.  **Response**: The model generates an answer based strictly on the provided context.

## Features

-   **Custom Knowledge Base**: Answers questions derived from a local CSV dataset.
-   **Gemini Integration**: Powered by Google's `gemini-2.5-flash` model.
-   **Interactive CLI**: Simple command-line interface for continuous conversation.
-   **Fallback Handling**: Explicitly handles out-of-domain queries with a standard "I don't know" response.

## Tech Stack

-   **Language**: Python 3.x
-   **LLM Provider**: Google Generative AI (Gemini)
-   **Data Manipulation**: Pandas
-   **Environment Management**: python-dotenv

## Installation

1.  **Clone the repository**
    ```bash
    git clone https://github.com/ARISH4651/innovation-Rag-Bot-.git
    cd innovation-Rag-Bot-
    ```

2.  **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Configure Environment**
    Create a `.env` file in the root directory and add your Google API key:
    ```env
    GOOGLE_API_KEY=your_api_key_here
    ```

## Usage

1.  **Start the Bot**
    Run the application script:
    ```bash
    python app.py
    ```

2.  **Interact**
    -   The bot will initialize and display `Rag-Bot is started`.
    -   Type your question at the `You :` prompt.
    -   Type `exit` to terminate the session.

## Folder Structure

```
innovation-Rag-Bot-/
├── app.py              # Main application entry point and logic
├── qa_data (1).csv     # Knowledge base CSV file
├── requirements.txt    # Python dependencies
├── .env                # Environment variables (not committed)
└── README.md           # Project documentation
```
