import streamlit as st
import os
import PyPDF2
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
from groq import Groq

groq_client = Groq(api_key=os.getenv("GROQ_API_KEY"))

@st.cache_resource
def load_embedding_model():
    return SentenceTransformer('all-MiniLM-L6-v2')

model = load_embedding_model()

st.set_page_config(
    page_title="DocTalk",
    page_icon="📄",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        text-align: center;
        padding: 2rem 0;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 15px;
        margin-bottom: 2rem;
        color: white;
    }
    .feature-card {
        background: #1e1e2e;
        border-radius: 10px;
        padding: 1rem;
        margin: 0.5rem 0;
        border-left: 4px solid #667eea;
    }
    .stat-box {
        background: #2d2d44;
        border-radius: 10px;
        padding: 1rem;
        text-align: center;
    }
    .stChatMessage {
        border-radius: 10px;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<div class="main-header">
    <h1>📄 DocTalk</h1>
    <p style="font-size: 1.2rem; opacity: 0.9;">Universal AI Document Intelligence Platform</p>
    <p style="font-size: 0.9rem; opacity: 0.7;">Upload any PDF • Ask Questions • Get Instant Answers</p>
</div>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.image("https://img.icons8.com/fluency/96/document.png", width=80)
    st.title("DocTalk")
    st.markdown("---")
    st.markdown("### ⚡ Features")
    st.markdown("✅ Multi-PDF Support")
    st.markdown("✅ Semantic Search")
    st.markdown("✅ LLaMA 3 Powered")
    st.markdown("✅ Source Citations")
    st.markdown("✅ One-Click Summary")
    st.markdown("✅ Chat History")
    st.markdown("---")
    st.markdown("### 📊 How it works")
    st.markdown("1. Upload your PDF(s)")
    st.markdown("2. AI indexes the content")
    st.markdown("3. Ask any question")
    st.markdown("4. Get accurate answers!")
    st.markdown("---")
    if st.button("🗑️ Clear Chat History"):
        st.session_state.chat_history = []
        st.rerun()

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Upload section
st.markdown("### 📁 Upload Your Documents")
uploaded_files = st.file_uploader(
    "Drag and drop your PDF files here",
    type="pdf",
    accept_multiple_files=True,
    help="You can upload multiple PDFs at once!"
)

if not uploaded_files:
    st.info("👆 Upload one or more PDF files to get started!")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""<div class="feature-card">
            <h4>📚 Research Papers</h4>
            <p>Extract insights from academic papers instantly</p>
        </div>""", unsafe_allow_html=True)
    with col2:
        st.markdown("""<div class="feature-card">
            <h4>📋 Legal Documents</h4>
            <p>Understand contracts and legal terms easily</p>
        </div>""", unsafe_allow_html=True)
    with col3:
        st.markdown("""<div class="feature-card">
            <h4>📖 Study Notes</h4>
            <p>Chat with your study material and notes</p>
        </div>""", unsafe_allow_html=True)

if uploaded_files:
    all_text = ""
    for uploaded_file in uploaded_files:
        reader = PyPDF2.PdfReader(uploaded_file)
        for page in reader.pages:
            all_text += page.extract_text()

    def split_text(text, chunk_size=500, overlap=50):
        chunks = []
        start = 0
        while start < len(text):
            end = start + chunk_size
            chunks.append(text[start:end])
            start = end - overlap
        return chunks

    chunks = split_text(all_text)

    @st.cache_data
    def build_index(chunks_tuple):
        chunks_list = list(chunks_tuple)
        embeddings = model.encode(chunks_list)
        embeddings = np.array(embeddings).astype('float32')
        dimension = embeddings.shape[1]
        index = faiss.IndexFlatL2(dimension)
        index.add(embeddings)
        return index, embeddings, chunks_list

    with st.spinner("🔄 Building AI knowledge base..."):
        index, embeddings, chunks_list = build_index(tuple(chunks))

    # Stats row
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("📄 PDFs Uploaded", len(uploaded_files))
    with col2:
        st.metric("📊 Characters Extracted", f"{len(all_text):,}")
    with col3:
        st.metric("🧩 Chunks Indexed", len(chunks))

    st.success("✅ AI Knowledge base ready! Ask me anything about your document.")

    def search_chunks(query, top_k=5):
        query_embedding = model.encode([query])
        query_embedding = np.array(query_embedding).astype('float32')
        distances, indices = index.search(query_embedding, top_k)
        return [chunks_list[i] for i in indices[0]]

    st.divider()

    if st.button("📝 Summarize this Document", use_container_width=True):
        with st.spinner("🤖 AI is summarizing your document..."):
            summary_prompt = f"""You are DocTalk, an intelligent document assistant.
Please provide a clear and concise summary of the following document in 5-7 bullet points.
Cover the main topics, key findings, and important details.

Document Content:
{all_text[:3000]}

Summary:"""
            summary_response = groq_client.chat.completions.create(
                model="gpt-oss-120b",
                messages=[{"role": "user", "content": summary_prompt}]
            )
            summary = summary_response.choices[0].message.content
            st.success("📝 Document Summary")
            st.write(summary)

    st.divider()
    st.subheader("💬 Ask your Document")

    for message in st.session_state.chat_history:
        with st.chat_message(message["role"]):
            st.write(message["content"])

    user_question = st.chat_input("Ask anything about your uploaded document...")

    if user_question:
        with st.chat_message("user"):
            st.write(user_question)

        relevant_chunks = search_chunks(user_question)
        context = "\n\n".join(relevant_chunks)

        prompt = f"""You are DocTalk, an intelligent document assistant.
Answer the user's question based ONLY on the document context provided below.
If the answer is not in the context, say "I couldn't find that information in the uploaded document."

Document Context:
{context}

User Question: {user_question}

Answer:"""

        with st.chat_message("assistant"):
            with st.spinner("🤖 Thinking..."):
                response = groq_client.chat.completions.create(
                    model="gpt-oss-120b",
                    messages=[{"role": "user", "content": prompt}]
                )
                answer = response.choices[0].message.content
                st.write(answer)

                with st.expander("📌 Source chunks used"):
                    for i, chunk in enumerate(relevant_chunks):
                        st.write(f"**Chunk {i+1}:** {chunk[:200]}...")

        st.session_state.chat_history.append({"role": "user", "content": user_question})
        st.session_state.chat_history.append({"role": "assistant", "content": answer})