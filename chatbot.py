from datetime import datetime

def get_response(user):

    user = user.lower().strip()

    words = user.replace(",", "").replace("?", "").replace("!", "").split()

    if any(word in words for word in ["hi", "hello", "hey"]):
        return "Hello! How can I help you?"

    elif any(word in words for word in ["name"]):
        return "My name is CodBot."

    elif any(word in words for word in ["thank", "thanks"]):
        return "You're welcome! I'm happy to help."

    elif "how are you" in user:
        return "I am doing great. Thanks for asking!"

    elif any(word in words for word in ["help"]):
        return (
            "I can help you with:\n"
            "• Greetings\n"
            "• Date and time\n"
            "• Jokes\n"
            "• Motivation\n"
            "• AI, Python and Machine Learning\n"
            "• Basic conversation"
        )

    elif any(word in words for word in ["course", "courses", "study"]):
        return "I can help you with AI, Python and Machine Learning."

    elif any(word in words for word in ["time", "clock"]):
        return datetime.now().strftime("%I:%M %p")

    elif any(word in words for word in ["date", "day", "today"]):
        return datetime.now().strftime("%d-%m-%Y")

    elif any(word in words for word in ["joke", "funny"]):
        return "Why do programmers prefer dark mode? Because light attracts bugs!"

    elif any(word in words for word in ["motivate", "inspire", "motivation"]):
        return "Success comes from learning something every day."

    elif any(word in words for word in ["bye", "exit"]):
        return "Goodbye! Have a nice day."

    elif "good morning" in user:
        return "Good morning! Have a great day."

    elif "good night" in user:
        return "Good night! Take care."

    elif "who are you" in user:
        return "I am a simple AI chatbot created using Python."

    else:
        return "Sorry, I didn't understand that."