import os
import pandas as pd
from dotenv import load_dotenv
from langchain_community.vectorstores import FAISS
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_core.documents import Document
from langchain.chains.question_answering import load_qa_chain
from langchain_core.prompts import PromptTemplate

load_dotenv()

# 1. Load API key
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    raise ValueError("Google API key not found in .env file")

# 2. Load CSV
def load_faq_csv(path):
    df = pd.read_csv(path)
    docs = []
    for _, row in df.iterrows():
        content = f"Q: {row['Question']}\nA: {row['Answer']}"
        docs.append(Document(page_content=content))
    return docs

docs = load_faq_csv("angelone_faqs.csv")

# 3. Split text into chunks
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=512,
    chunk_overlap=50
)
chunks = text_splitter.split_documents(docs)

# 4. Create embeddings
embedding = GoogleGenerativeAIEmbeddings(model="models/embedding-001", google_api_key=api_key)

# 5. Build and save vector store
db = FAISS.from_documents(chunks, embedding)
db.save_local("faiss_db")
print("✅ Vector database created and saved to /faiss_db")

# 6. Load the saved vector DB (needed for query time)
db = FAISS.load_local("faiss_db", embedding, allow_dangerous_deserialization=True)

# 7. Setup LLM and QA chain
llm = ChatGoogleGenerativeAI(model="gemini-pro", google_api_key=api_key)

prompt = PromptTemplate(
    input_variables=["context", "question"],
    template="""
You are a helpful assistant. Use the context below to answer the user's question.
If the answer isn't found in the context, say "Sorry, I couldn't find an answer."

Context:
{context}

Question:
{question}
"""
)

qa_chain = load_qa_chain(llm=llm, chain_type="stuff", prompt=prompt)

# 8. Generate response function
def generate_response(user_query):
    relevant_docs = db.similarity_search(user_query, k=3)
    response = qa_chain.run(input_documents=relevant_docs, question=user_query)
    return response
