from langchain_community.vectorstores import FAISS

from utils.embeddings import get_embeddings
from utils.text_splitter import split_documents


def build_vector_db(documents):

    print("Documents:", len(documents))

    chunks = split_documents(documents)

    print("Chunks:", len(chunks))

    if len(chunks) > 0:
        print("First chunk:")
        print(chunks[0].page_content[:300])
    else:
        print("NO CHUNKS CREATED")
        return None

    embeddings = get_embeddings()

    db = FAISS.from_documents(
        chunks,
        embeddings
    )

    db.save_local("vector_store")

    return db


def load_vector_db():

    embeddings = get_embeddings()

    db = FAISS.load_local(
        "vector_store",
        embeddings,
        allow_dangerous_deserialization=True
    )

    return db
