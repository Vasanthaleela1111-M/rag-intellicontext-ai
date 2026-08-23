from utils.prompt_template import prompt
from utils.llm_model import get_llm


def ask_question(
    vector_store,
    question,
    chat_history=""
):

    docs = vector_store.similarity_search(
        question,
        k=3
    )

    # DEBUGGING
    print("\nQUESTION:")
    print(question)

    print("\nRETRIEVED CHUNKS:")
    for i, doc in enumerate(docs):
        print(f"\nChunk {i+1}")
        print(doc.page_content)

    context = "\n".join(
        [doc.page_content for doc in docs]
    )

    print("\nCONTEXT SENT TO LLM:")
    print(context)

    final_prompt = prompt.format(
        context=context,
        question=question,
        chat_history=chat_history
    )

    print("\nFINAL PROMPT:")
    print(final_prompt)

    response = llm.invoke(final_prompt)
    answer=response.content
    return answer, docs
