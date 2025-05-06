
# 🤖 AngelOne Support RAG Chatbot

[![Made with LangChain](https://img.shields.io/badge/Built%20With-LangChain-blue)](https://www.langchain.com/)
[![Powered by Gemini Flash](https://img.shields.io/badge/LLM-Gemini%201.5%20Flash-ffca28)](https://ai.google.dev/)
[![Deployed on Render](https://img.shields.io/badge/Deploy-Render-46a2f1)](https://render.com/)
[![Gradio UI](https://img.shields.io/badge/UI-Gradio-00b3a4)](https://gradio.app/)

> **A smart chatbot that answers AngelOne customer support queries using real FAQs + LLMs. Powered by LangChain, Gemini Flash, FAISS, and Gradio.**

🔗 **Live Demo:** [RAG_CHATBOT](https://rag-chatbot-v2-10.onrender.com/)

---

## 📌 Overview

This project showcases a Retrieval-Augmented Generation (RAG) chatbot built with:

- **Vector similarity search** using FAISS.
- **Context-aware answers** using Gemini 1.5 Flash (via Google Generative AI).
- **Interactive frontend** with Gradio.
- **Custom dataset** from AngelOne’s support knowledge base.

It's lightweight, serverless, and deployable for free with Render — great for customer support bots, internal Q&A, or as an AI portfolio piece.

---

## 🧠 Features

✅ Answer AngelOne support questions using real documentation  
✅ Handles ambiguous queries by searching similar questions  
✅ Gemini-powered LLM with natural conversational tone  
✅ CSV-based source, easy to update and expand  
✅ Clean Gradio UI with mobile responsiveness  
✅ Fully serverless + free deployment on Render

---

## 📂 Tech Stack

| Category       | Tools / Libraries                                           |
|----------------|-------------------------------------------------------------|
| Language Model | [Google Gemini Flash](https://ai.google.dev/)               |
| Framework      | [LangChain](https://www.langchain.com/)                    |
| Embeddings     | GoogleGenerativeAIEmbeddings                                |
| Vector Store   | FAISS                                                       |
| Frontend       | Gradio                                                      |
| Hosting        | Render (Free Plan)                                          |
| Dataset        | AngelOne FAQs (CSV format)                                  |

---

## 🖥️ Screenshots


![Output1](https://github.com/user-attachments/assets/ef5431f5-af87-4543-8de6-5932e191dafb)
![Output2](https://github.com/user-attachments/assets/1d2a698b-36e9-4344-9a1d-4b01276c0161)
![Output3](https://github.com/user-attachments/assets/34fb2f3e-b41a-4761-96c6-847c53d0cef5)


---

## 🚀 Quickstart

### 🧰 Local Setup

1. **Clone the repository**

   ```bash
   git clone https://github.com/vharishcse/RAG_Chatbot_V2.git
   ```

2. **Set up environment**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Create `.env` file**

   ```
   GOOGLE_API_KEY=your-google-api-key
   ```

4. **Build the vector DB**

   ```bash
   python rag_chatbot.py
   ```

5. **Run the app**

   ```bash
   python chat_ui.py
   ```

---

## 💬 How to Use

* Type your support query in the chat box.
* **Hit `Shift + Enter` to submit** the question.
* The bot retrieves relevant answers from AngelOne’s FAQ knowledge base.

💡 Example prompts:

* *Why is my trading balance not updated?*
* *How to close my account?*
* *What are AngelOne’s brokerage charges?*

---

## 🌍 Live Deployment (Render)

The app is deployed on [Render](https://rag-chatbot-v2-10.onrender.com/) using `render.yaml`.

```yaml
services:
  - type: web
    name: angelone-chatbot
    env: python
    buildCommand: pip install -r requirements.txt
    startCommand: python chat_ui.py
    envVars:
      - key: GOOGLE_API_KEY
        sync: false
    plan: free
```

---

## 🧾 File Structure

```
.
├── angelone_faqs.csv       # Dataset
├── chat_ui.py              # Gradio UI + chatbot logic
├── rag_chatbot.py          # Vector DB + chain setup
├── requirements.txt        # Python dependencies
├── .env                    # API key (not pushed)
├── .gitignore              # Git ignore rules
├── faiss_db/               # FAISS vector DB
└── render.yaml             # Render deployment config
```

---

## 📁 .gitignore

```bash
.env
__pycache__/
*.pyc
*.lock
venv/
```

---

## 👤 Author

**Harish** – Freelance Developer
🔗 [LinkedIn](https://www.linkedin.com/in/v-harish-yadav-b2bb52241/) • [GitHub](https://github.com/vharishcse)

---

## 🛑 Disclaimer

This project is for educational and demonstration purposes only. It is **not officially affiliated with AngelOne**.

