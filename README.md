# 🤖 Satya AI Agent

Satya AI Agent is a web-based AI chatbot built using FastAPI, AWS EC2, and OpenRouter. Users can chat with an AI model directly from their browser through a simple and responsive web interface.

## 🚀 Features

- Real-time AI chat
- FastAPI backend
- Web-based frontend
- OpenRouter API integration
- Secure API key management using `.env`
- AWS EC2 deployment
- Easy to customize and extend

## 🏗️ Architecture

User Browser
↓
Frontend (HTML/CSS/JavaScript)
↓
FastAPI Backend
↓
OpenRouter API
↓
AI Model
↓
Response to User

## 🛠️ Tech Stack

- Python
- FastAPI
- HTML
- CSS
- JavaScript
- OpenRouter
- AWS EC2
- Ubuntu Linux

## 📂 Project Structure

```text
project/
│
├── app.py
├── index.html
├── requirements.txt
├── .gitignore
├── .env
└── venv/
```

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/satyaprakash196/satya-ai-agent.git
cd satya-ai-agent
```

### Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Environment Variables

Create a `.env` file:

```env
OPENROUTER_API_KEY=your_api_key_here
```

### Run Application

```bash
uvicorn app:app --host 0.0.0.0 --port 8000
```

Open browser:

```text
http://YOUR_SERVER_IP:8000
<img width="1258" height="725" alt="image" src="https://github.com/user-attachments/assets/6e42f4f7-a67d-4d8e-9c0e-a942a717bef4" />


## 📸 Demo

Satya AI Agent provides a simple browser-based chat interface where users can interact with AI in real time.

## 🔒 Security

- API keys stored in `.env`
- `.env` excluded using `.gitignore`
- Secrets are not committed to GitHub

## 🔮 Future Enhancements

- User Authentication
- Chat History
- WhatsApp Integration
- Voice Assistant
- PDF Knowledge Base
- Custom Domain & HTTPS

## 👨‍💻 Author

**Satya Prakash**

GitHub:
https://github.com/satyaprakash196



