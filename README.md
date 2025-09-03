# langchain-math-agent-gemini
A LangChain-powered math agent that integrates custom arithmetic tools (addition, subtraction, multiplication, division) with Google Gemini (gemini-2.5-flash) using the langchain_google_genai wrapper. This project demonstrates how to bind custom tools in LangChain and let the LLM act as an intelligent math assistant.

# 🔢 LangChain Math Agent (Google Gemini)

An AI math assistant built with **LangChain** and **Google Gemini**.  
This project shows how to bind custom tools (add, subtract, multiply, divide) into a LangChain Agent and let Gemini (`gemini-2.5-flash`) handle natural language queries.

---

## 🚀 Features
- 🔧 Custom tools: `add`, `subtract`, `multiply`, `divide`
- 🤖 Powered by **Gemini LLM**
- 🛠️ Built with **LangChain Agents**
- 📝 Easy to extend with new tools

---

## 📂 Project Structure
├── main.py # Entry point for the agent
├── .env # Holds GEMINI_API_KEY
├── requirements.txt # Dependencies
└── README.md


---

## ⚙️ Setup

1. **Clone the repo**
   ```bash
   git clone https://github.com/your-username/langchain-math-agent-gemini.git
   cd langchain-math-agent-gemini

2. **Create virtual environment & activate**
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows

3. **Install dependencies**
pip install -r requirements.txt

4. **Set up environment variable**
Create a .env file:
GEMINI_API_KEY=your_api_key_here

**RUN AGENT**
python main.py


