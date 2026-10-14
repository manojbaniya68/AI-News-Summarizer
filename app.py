from dotenv import load_dotenv
from langchain_tavily import TavilySearch
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

tool = TavilySearch(
    max_results=5,
    topic="news",
)

query = input("Enter the topic of news : ")

news_result = tool.invoke({"query" : query})

prompt = ChatPromptTemplate.from_template(
    """
    You are a news summarization assistant.

    Summarize the following news clearly and accurately.
    Preserve important facts, dates, names, and figures.
    Do not add information that is not present in the sources.

    News:
    {news}
"""
)

llm = ChatGoogleGenerativeAI(model = "gemini-3.8-flash")

chain = prompt | llm | StrOutputParser()


result = chain.invoke({"news" : news_result})
print(result)
