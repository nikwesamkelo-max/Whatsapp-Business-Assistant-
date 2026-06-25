from fastapi import FastAPI
from assistant import process_message
from database import init_db, save_message, get_all_messages

app = FastAPI()

# Initialize database when server starts
init_db()


@app.get("/")
def home():
    return {"message": "WhatsApp Business Assistant is running 🚀"}


@app.get("/message")
def message(text: str):

    # 1. Process message through assistant brain
    response = process_message(text)

    # 2. Save to SQLite database
    save_message(text, response)

    # 3. Return response (simulating WhatsApp reply)
    return {
        "user_message": text,
        "bot_response": response
    }


@app.get("/history")
def history():

    # View saved conversations
    data = get_all_messages()

    return {
        "total_messages": len(data),
        "messages": data
    }
