from flask import Flask, request, jsonify, render_template, session
import os
import uuid
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", os.urandom(24).hex())

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get("message")
    conversation_id = request.json.get("conversation_id")
    
    # Initialize or get existing conversation
    if not conversation_id:
        conversation_id = str(uuid.uuid4())
        session[conversation_id] = [
            {"role": "system", "content": "You are a helpful assistant."}
        ]
    elif conversation_id not in session:
        session[conversation_id] = [
            {"role": "system", "content": "You are a helpful assistant."}
        ]
    
    # Add user message to conversation history
    session[conversation_id].append({"role": "user", "content": user_input})
    
    try:
        # Send the entire conversation history to the API
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=session[conversation_id]
        )
        
        reply = response.choices[0].message.content
        
        # Add assistant response to conversation history
        session[conversation_id].append({"role": "assistant", "content": reply})
        
        # Save the updated conversation
        session.modified = True
        
        return jsonify({
            "response": reply,
            "conversation_id": conversation_id
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))

