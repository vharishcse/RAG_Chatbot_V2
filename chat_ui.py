import os
import gradio as gr
from rag_chatbot import generate_response
from dotenv import load_dotenv
from langchain_core.documents import Document
from langchain_community.vectorstores import FAISS
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings

# Load environment variables
load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
assert GOOGLE_API_KEY is not None, "❌ GOOGLE_API_KEY not found in .env"

# Load FAISS DB
vector_db = FAISS.load_local("faiss_db", GoogleGenerativeAIEmbeddings(model="models/embedding-001"), allow_dangerous_deserialization=True)

# Set up LLM
llm = ChatGoogleGenerativeAI(model="models/gemini-1.5-flash-latest", google_api_key=GOOGLE_API_KEY)

# Chatbot function
def chatbot(query, history):
    if not query.strip():
        return "❗ Please enter a valid question."
    
    docs = vector_db.similarity_search(query, k=4)
    context = "\n\n".join([doc.page_content for doc in docs])
    prompt = f"Answer the question using the below context:\n\n{context}\n\nQuestion: {query}\n\nIf the answer is not in the context, say 'I don't know.'"

    response = llm.invoke(prompt)
    return response.content

# Launch Gradio ChatInterface using correct Render settings
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 7860))
    gr.ChatInterface(
        fn=chatbot,
        title="📘 AngelOne Support Chatbot",
        chatbot=gr.Chatbot(label="Chat with AngelOne Docs", type="messages"),
        textbox=gr.Textbox(placeholder="Ask a question about AngelOne support...", lines=2),
        theme="soft",
        examples=[
            "Why is my trading balance not updated even after adding funds successfully?",
            "How do I close my account?",
            "What are brokerage charges?"
        ]
    ).launch(server_name="0.0.0.0", server_port=port)
