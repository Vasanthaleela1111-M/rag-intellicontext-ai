import streamlit as st
from langchain_groq import ChatGroq

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    groq_api_key=st.secrets["GROQ_API_KEY"],
    temperature=0
)
