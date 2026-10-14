# AI News Summarizer

A lightweight AI-powered news summarization app that searches current news topics using Tavily and generates concise, reliable summaries with Google Gemini through LangChain.

This project includes both a polished Streamlit web app and a simple command-line version, making it easy to use for quick news research or as a starter project for LangChain-based AI workflows.

## Overview

The application works in three steps:

1. Accept a news topic from the user.
2. Search the web for recent results using Tavily.
3. Pass the retrieved article snippets to Gemini for a clear summary.

The result is a concise summary that preserves important facts, names, dates, and figures while avoiding unsupported claims.

## Features

- Search for any topic using live web results
- Retrieve the latest news from Tavily
- Summarize results using Google Generative AI
- Clean and simple Streamlit interface
- Command-line version for quick terminal usage

## Tech Stack

- Python
- Streamlit
- LangChain
- Tavily Search API
- Google Gemini via `langchain-google-genai`

## Project Structure

```text
.
├── app.py          # Command-line interface version
├── GUI.py          # Streamlit web application
├── .env            # Local environment variables (not committed)
├── .gitignore      # Ignores .env
├── Readme.md       # Project documentation
└── .git            # Git repository metadata
```

## Prerequisites

Before running the project, make sure you have:

- Python 3.9 or newer
- A Tavily API key
- A Google AI API key
- Internet access for live news search and LLM requests

## Installation

Clone the repository:

```bash
git clone https://github.com/manojbaniya68/AI-News-Summarizer.git
cd AI-News-Summarizer
```

Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

On Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
pip install streamlit python-dotenv langchain langchain-core langchain-tavily langchain-google-genai
```

## Configuration

Create a `.env` file in the project root with your API keys:

```env
TAVILY_API_KEY=your_tavily_api_key_here
GOOGLE_API_KEY=your_google_api_key_here
```

The application loads these values automatically using `python-dotenv`.

## Running the App

### Web app (recommended)

```bash
streamlit run GUI.py
```

Then open the local URL printed in the terminal, usually:

```text
http://localhost:8501
```

### Command-line version

```bash
python app.py
```

Enter the news topic when prompted and the script will fetch and summarize the results.

## Example Usage

```text
Enter a news topic: Latest AI news around the world
```

The app searches recent coverage, gathers relevant sources, and returns a concise summary in plain English.

## How It Works

- `TavilySearch` retrieves recent web results for the user query.
- The retrieved articles are passed into a LangChain prompt template.
- `ChatGoogleGenerativeAI` summarizes the news with a guided instruction:
  - preserve facts and figures
  - avoid fabricating unsupported details
  - mention uncertainty when the sources are unclear or conflicting
- The final summary is displayed in the UI or printed in the terminal.

