import os
import streamlit as st
from streamlit_option_menu import option_menu

from utils.document_loader import load_documents
from utils.vector_db import build_vector_db, load_vector_db
from utils.rag_chain import ask_question
from utils.memory import ChatMemory

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------
st.set_page_config(
    page_title="Intellicontext AI",
    page_icon="⚡",
    layout="wide"
)

# --------------------------------------------------
# SESSION STATE
# --------------------------------------------------
if "chat_sessions" not in st.session_state:
    st.session_state.chat_sessions = {
        "Chat 1": [
            {
                "role": "assistant",
                "content": "Hello! Welcome to the AI Knowledge Assistant."
            }
        ]
    }

if "current_chat" not in st.session_state:
    st.session_state.current_chat = "Chat 1"
if "memory" not in st.session_state:
    st.session_state.memory = ChatMemory()

if "last_sources" not in st.session_state:
    st.session_state.last_sources = []

# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------
with st.sidebar:

    st.title("🤖 AI Assistant")

    selected = option_menu(
        menu_title=None,
        options=[
            "🚀 Project Introduction",
            "🤖 AI Studio",
            "👨‍💻 Developer"
        ],
        icons=[
            "rocket",
            "robot",
            "person-badge"
        ],
        default_index=0
    )

    # ==========================================
    # AI STUDIO SIDEBAR FEATURES
    # ==========================================
    if selected == "🤖 AI Studio":

        st.divider()

        # New Chat
        if st.button("➕ New Chat", use_container_width=True):

            chat_number = len(
                st.session_state.chat_sessions
            ) + 1

            new_chat_name = f"Chat {chat_number}"

            st.session_state.chat_sessions[
                new_chat_name
            ] = [
                {
                    "role": "assistant",
                    "content": "Hello! Welcome to the AI Knowledge Assistant."
                }
            ]

            st.session_state.current_chat = (
                new_chat_name
            )

            st.rerun()

        st.divider()

        # Upload Documents
        uploaded_files = st.file_uploader(
            "📂 Upload Documents",
            type=["pdf", "docx", "txt","csv","ppt","pptx"],
            accept_multiple_files=True
        )

        if uploaded_files:

            if st.button("⚙️ Process Documents"):

                all_docs = []

                os.makedirs(
                    "data",
                    exist_ok=True
                )

                for file in uploaded_files:

                    file_path = os.path.join(
                        "data",
                        file.name
                    )

                    with open(
                        file_path,
                        "wb"
                    ) as f:

                        f.write(
                            file.getbuffer()
                        )

                    docs = load_documents(
                        file_path
                    )

                    all_docs.extend(
                        docs
                    )

                build_vector_db(
                    all_docs
                )

                st.success(
                    "✅ Documents Processed Successfully"
                )

        st.divider()

        st.markdown("### 🕘 Chat History")

        chat_names = list(
            st.session_state.chat_sessions.keys()
        )

        chat_names.reverse()

        for chat_name in chat_names:

            col1, col2 = st.columns([4, 1])

            with col1:

                if st.button(
                    chat_name,
                    key=f"open_{chat_name}",
                    use_container_width=True
                ):
                    st.session_state.current_chat = (
                        chat_name
                    )
                    st.rerun()

            with col2:

                if (
                    len(
                        st.session_state.chat_sessions
                    ) > 1
                ):

                    if st.button(
                        "🗑",
                        key=f"delete_{chat_name}"
                    ):

                        del st.session_state.chat_sessions[
                            chat_name
                        ]

                        if (
                            st.session_state.current_chat
                            == chat_name
                        ):
                            st.session_state.current_chat = list(
                                st.session_state.chat_sessions.keys()
                            )[0]

                        st.rerun()

    st.divider()

# ==================================================
# PAGE 1 : LAUNCHPAD
# ==================================================
if selected == "🚀 Project Introduction":

    # ==================================================
    # HERO SECTION
    # ==================================================

    # st.title("🧠 Personal AI Knowledge Assistant")

    # st.caption(
    #     "Next-Generation Document Intelligence Platform"
    # )

    # st.write("""
    # Upload documents, build a knowledge base,
    # and interact with your information through
    # natural language conversations powered by AI.
    # """)

    st.info("""
# 🧠 Personal AI Knowledge Assistant

### Next-Generation Document Intelligence Platform

Upload documents, build a knowledge base,
and interact with your information through
natural language conversations powered by AI.
""")

    st.divider()

    # ==================================================
    # PLATFORM SNAPSHOT
    # ==================================================

    st.subheader("📊 Platform Snapshot")

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric(
            "Documents",
            "PDF • DOCX • PPT"
        )

    with c2:
        st.metric(
            "Retrieval",
            "FAISS"
        )

    with c3:
        st.metric(
            "Embeddings",
            "Vector AI"
        )

    with c4:
        st.metric(
            "Responses",
            "Real-Time"
        )

    st.write("")

    # ==================================================
    # KNOWLEDGE HUB
    # ==================================================

    with st.container(border=True):

        st.subheader("🏛️ Knowledge Intelligence Hub")

        st.write("""
        The platform transforms static documents into an
        intelligent conversational knowledge system.

        Instead of manually searching through reports,
        notes, presentations, or research papers, users
        can simply ask questions and receive accurate,
        context-aware responses generated from uploaded
        documents.

        The assistant combines semantic retrieval,
        vector databases, embeddings, and large language
        models to provide reliable answers grounded in
        document knowledge.
        """)

    st.write("")

    # ==================================================
    # AI PROCESSING FLOW
    # ==================================================

    st.subheader("🔄 AI Processing Flow")

    flow1, flow2, flow3, flow4 = st.columns(4)

    with flow1:
        with st.container(border=True):
            st.markdown("""
            ### 📂 Ingest

            Import documents from
            multiple formats into
            the knowledge workspace.
            """)

    with flow2:
        with st.container(border=True):
            st.markdown("""
            ### 🧬 Understand

            Convert document content
            into semantic vector
            representations.
            """)

    with flow3:
        with st.container(border=True):
            st.markdown("""
            ### 🔍 Discover

            Retrieve the most
            relevant knowledge
            using similarity search.
            """)

    with flow4:
        with st.container(border=True):
            st.markdown("""
            ### 🤖 Respond

            Generate intelligent
            answers grounded in
            retrieved context.
            """)

    st.write("")

    # ==================================================
    # BUSINESS IMPACT
    # ==================================================

    st.subheader("🌟 Business Impact")

    impact1, impact2 = st.columns(2)

    with impact1:

        st.success("""
        ### 🔍 Knowledge Discovery

        Instantly retrieve critical
        information from large
        document collections.
        """)

        st.success("""
        ### 🎯 Decision Support

        Generate accurate,
        context-aware answers for
        faster decision making.
        """)

    with impact2:

        st.success("""
        ### ⚡ Research Acceleration

        Reduce hours of manual
        document searching into
        seconds.
        """)

        st.success("""
        ### 🚀 Productivity Enhancement

        Interact conversationally
        with documents instead of
        reading entire files.
        """)

    st.write("")

    # ==================================================
    # PLATFORM ARCHITECTURE
    # ==================================================

    st.subheader("⚙️ Platform Architecture")

    col1, col2 = st.columns(2)

    with col1:

        with st.container(border=True):

            st.markdown("""
            ### 📄 Knowledge Processing

            • Multi-format document ingestion

            • Intelligent text extraction

            • Context chunk generation

            • Metadata preservation
            """)

        with st.container(border=True):

            st.markdown("""
            ### 🔍 Retrieval System

            • Vector similarity search

            • FAISS indexing

            • Context ranking

            • Semantic matching
            """)

    with col2:

        with st.container(border=True):

            st.markdown("""
            ### 🧬 Embedding Engine

            • Text vectorization

            • Semantic representation

            • Document understanding

            • Query encoding
            """)

        with st.container(border=True):

            st.markdown("""
            ### 🤖 Response Generation

            • Prompt orchestration

            • Context-aware reasoning

            • Conversational responses

            • Source-grounded answers
            """)

    st.write("")

    st.success(
        "🎯 Goal: Transform static documents into an intelligent conversational knowledge system."
    )

# ==================================================
# PAGE 2 : AI STUDIO
# ==================================================
elif selected == "🤖 AI Studio":

    current_chat = (
        st.session_state.current_chat
    )

    st.success(f"💬 Active Workspace : {current_chat}")

    current_messages = (
        st.session_state.chat_sessions[
            current_chat
        ]
    )

    for msg in current_messages:

        with st.chat_message(
            msg["role"]
        ):
            st.write(
                msg["content"]
            )

    prompt = st.chat_input(
        "Ask anything..."
    )

    if prompt:

        st.session_state.chat_sessions[
            current_chat
        ].append(
            {
                "role": "user",
                "content": prompt
            }
        )

        # Replace with RAG response
        try:

            db = load_vector_db()

            chat_history = (
                st.session_state.memory.get_history()
            )

            answer, docs = ask_question(
                db,
                prompt,
                chat_history
            )

            st.session_state.memory.add_message(
                prompt,
                answer
            )

            response = answer

            st.session_state.last_sources = docs

        except Exception as e:

            response = f"❌ Error: {str(e)}"

        st.session_state.chat_sessions[
            current_chat
        ].append(
            {
                "role": "assistant",
                "content": response
            }
        )

        st.rerun()

# ==================================================
# PAGE 3 : DEVELOPER
# ==================================================
elif selected == "👨‍💻 Developer":
    st.title("👨‍💻 Creator Info")

    with st.container(border=True):

        st.markdown("""
        ## Vasantha Leela MB

        **Computer Science & Engineering**

        Karpagam Academy of Higher Education

        Passionate about building intelligent systems that
        combine Artificial Intelligence, Machine Learning,
        and modern software technologies to solve real-world
        problems.
        """)

        st.write("")

        col1, col2 = st.columns(2)

    with col1:

        st.info("""
        ### 🛠 Technical Stack

        Python

        Machine Learning

        Deep Learning

        Computer Vision

        Streamlit
        """)

    with col2:

        st.info("""
        ### 🎯 Current Interests

        Retrieval-Augmented Generation

        Conversational AI

        Knowledge Systems

        NLP Applications

        Intelligent Automation
        """)

        st.write("")

    with st.container(border=True):

        st.markdown("""
        ### 🚀 Vision

        To create AI-powered solutions that make information
        more accessible, improve decision-making, and deliver
        meaningful user experiences through innovation and
        continuous learning.
        """)