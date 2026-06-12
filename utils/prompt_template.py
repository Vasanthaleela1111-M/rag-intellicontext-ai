from langchain_core.prompts import PromptTemplate

prompt = PromptTemplate(
    input_variables=[
        "context",
        "question"
    ],

    template = """
Context:
{context}

Question:
{question}

Instructions:
- Answer in 5-8 lines maximum.
- Do not repeat information.
- Do not copy large portions of the context.
- Summarize the information.
- If the answer is not found, say:
'I couldn't find that information in the uploaded documents.'

Answer:
""")
