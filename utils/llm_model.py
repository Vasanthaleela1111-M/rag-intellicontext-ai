import streamlit as st
from langchain_groq import ChatGroq

def get_llm():
    return ChatGroq(
        model="mixtral-8x7b-32768",
        groq_api_key=st.secrets["GROQ_API_KEY"],
        temperature=0
    )
