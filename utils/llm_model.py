import streamlit as st
from langchain_groq import ChatGroq

def get_llm():
    return ChatGroq(
        model="openai/gpt-oss-20b",
        groq_api_key=st.secrets["GROQ_API_KEY"],
        temperature=0
    )
