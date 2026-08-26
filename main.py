import tkinter as tk
from datetime import datetime
from tkinter import scrolledtext

from chatbot import get_response


def send_message():
    send_button.config(bg="#9b6aa0")
    window.after(150, lambda: send_button.config(bg="#c99acb"))
    
    user_message = entry.get()

    if user_message.strip() == "":
        chat_box.insert(
            tk.END,
            "\nBot: Please type a message first.\n\n",
            "bot"
        )
        entry.focus_set()
        return

    current_time = datetime.now().strftime("%I:%M %p")

    chat_box.insert(
        tk.END,
        f"\n[{current_time}]\nYou: {user_message}\n",
        "user"
    )

    response = get_response(user_message)

    chat_box.insert(
        tk.END,
        f"Bot: {response}\n\n",
        "bot"
    )

    entry.delete(0, tk.END)
    chat_box.see(tk.END)

    entry.focus_set()


def clear_chat():
    chat_box.delete(1.0, tk.END)

    chat_box.insert(
        tk.END,
        "Welcome to CodSoft AI Chatbot\n"
        "──────────────────────────────────\n"
        "Type your message to begin.\n\n"
    )

    entry.focus_set()


window = tk.Tk()
window.title("CodSoft AI Chatbot")
window.geometry("720x720")
window.configure(bg="#f7eef8")


# Header
header = tk.Label(
    window,
    text="CodSoft AI Chatbot",
    font=("Arial", 21, "bold"),
    bg="#ead7f0",
    fg="#684a72",
    pady=15
)
header.pack(fill=tk.X)


subtitle = tk.Label(
    window,
    text="Your little AI conversation space",
    font=("Arial", 10),
    bg="#ead7f0",
    fg="#92799a",
    pady=3
)
subtitle.pack(fill=tk.X)


# Chat box
chat_box = scrolledtext.ScrolledText(
    window,
    wrap=tk.WORD,
    font=("Arial", 12),
    bg="#fffafd",
    fg="#514653",
    insertbackground="#8d6b91",
    selectbackground="#ead7f0",
    selectforeground="#514653",
    relief=tk.FLAT,
    borderwidth=0
)

chat_box.tag_config(
    "user",
    foreground="#8a5c83",
    font=("Arial", 12, "bold")
)

chat_box.tag_config(
    "bot",
    foreground="#63758c",
    font=("Arial", 12)
)

chat_box.pack(
    padx=18,
    pady=18,
    fill=tk.BOTH,
    expand=True
)


# Input
entry = tk.Entry(
    window,
    font=("Arial", 13),
    bg="white",
    fg="#4A3B52",
    insertbackground="#7B4B8A",
    relief=tk.SOLID,
    bd=1
)

entry.pack(
    fill=tk.X,
    padx=18,
    pady=10,
    ipady=10
)

# Press Enter to send
entry.bind("<Return>", lambda event: send_message())


# Buttons
button_frame = tk.Frame(
    window,
    bg="#f7eef8"
)

button_frame.pack(pady=12)


send_button = tk.Button(
    button_frame,
    text="Send",
    command=send_message,
    bg="#c99acb",
    fg="white",
    activebackground="#9b6aa0",
    activeforeground="white",
    font=("Arial", 11, "bold"),
    width=14,
    relief=tk.FLAT,
    bd=0,
    cursor="hand2"
)

send_button.pack(side=tk.LEFT, padx=6)

clear_button = tk.Button(
    button_frame,
    text="Clear Chat",
    command=clear_chat,
    bg="#ded1e2",
    fg="#5d4563",
    activebackground="#cfc0d4",
    activeforeground="#5d4563",
    font=("Arial", 11),
    width=14,
    relief=tk.FLAT,
    bd=0,
    cursor="hand2"
)

clear_button.pack(side=tk.LEFT, padx=6)


# Welcome message
chat_box.insert(
    tk.END,
    "Welcome to CodSoft AI Chatbot\n"
    "──────────────────────────────────\n"
    "Type your message to begin.\n\n"
    "Commands:\n"
    "hi\n"
    "good morning\n"
    "good night\n"
    "name\n"
    "who are you\n"
    "thank you\n"
    "how are you\n"
    "help\n"
    "time\n"
    "date\n"
    "joke\n"
    "motivate\n"
    "course\n"
    "bye\n"
)


# Automatically place cursor in typing box
entry.focus_set()


window.mainloop()