## 🧠 ChatGPT Flask Assistant

This is a web-based chatbot powered by OpenAI’s GPT model, deployed using Flask and Google Cloud Run.

### 🚀 Live Demo
👉 [Try it here](https://my-chatbot-636257024258.us-central1.run.app/)

### 🔧 Technologies Used
- Flask (Python)
- OpenAI API (`gpt-3.5-turbo`)
- Google Cloud Run (Docker deployment)
- HTML/CSS (with `fetch()`-based frontend)
- Secure .env-based API key management

### ⚙️ Running Locally

```bash
git clone https://github.com/your-username/chatgpt_flask_app.git
cd chatgpt_flask_app
python -m venv venv
venv\Scripts\activate  # or source venv/bin/activate on Linux/Mac
pip install -r requirements.txt
cp .env.example .env
# Add your OpenAI API key to .env
python app.py
