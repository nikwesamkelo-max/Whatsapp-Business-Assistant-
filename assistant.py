def process_message(message: str) -> str:

    message = message.lower()

    # Basic business logic (you can expand this late.)
    if "hello" in message or "hi" in message:
        return "Hi 👋 Welcome to our business! How can I help you today?"

    if "price" in message or "prices" in message:
        return "Our prices start from R500 depending on the service."

    if "book" in message or "booking" in message:
        return "To book an appointment, please share your preferred date and time."

    if "hours" in message:
        return "We operate Monday to Saturday, 9am - 5pm."

    return "Sorry, I didn't understand that. Please ask about prices, booking, or business info."
