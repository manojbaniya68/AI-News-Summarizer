from dotenv import load_dotenv
import streamlit as st
from langchain_tavily import TavilySearch
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

st.set_page_config(
    page_title="AI News Summarizer",
    page_icon="\U0001F4F0",
    layout="centered",
)

st.title("📰 AI News Summarizer")
st.write("Search for a news topic and get a clear summary of the latest results.")

query = st.text_input(
    "Enter a news topic",
    placeholder="e.g. Latest AI news around the world",
)

if st.button("Search and summarize", type="primary", use_container_width=True):
    if not query.strip():
        st.warning("Please enter a news topic.")
    else:
        try:
            with st.spinner("Searching for news..."):
                tool = TavilySearch(
                    max_results=5,
                    topic="news",
                )
                news_result = tool.invoke({"query": query.strip()})

            with st.spinner("Summarizing the results..."):
                prompt = ChatPromptTemplate.from_template(
                    """
                    You are a news summarization assistant.

                    Summarize the following news clearly and accurately.
                    Preserve important facts, dates, names, and figures.
                    Do not add information that is not present in the sources.
                    If the sources conflict or provide limited detail, mention that.

                    News:
                    {news}
                    """
                )

                llm = ChatGoogleGenerativeAI(model="gemini-3.8-flash")
                chain = prompt | llm | StrOutputParser()
                result = chain.invoke({"news": str(news_result)})

            st.subheader("Summary")
            st.write(result)

        except Exception as exc:
            st.error("Something went wrong while searching or summarizing the news.")
            st.caption("Check that your API keys are configured and that your installed packages support the selected model.")
            st.exception(exc)
