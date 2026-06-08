# Rule-Based Chatbot

print("Softchat: Hello! Type 'bye' to exit.")

while True:
    user = input("You: ").lower()

    if user == "hello" or user == "hi" or user == "hey":
        print("Softchat: Hello! How can I help you?")

    elif user == "how are you" or user == "How are you ":
        print("Softchat: I am fine. Thank you for asking!")

    elif user == "what is your name" or user == "what should I call you":
        print("Softchat: I am a simple Rule-Based ChatBot.")

    elif "help" in user:
        print("Softchat: I can answer simple questions like greetings, name, and time.")

    elif "time" in user:
        from datetime import datetime
        current_time = datetime.now().strftime("%H:%M:%S")
        print("Softchat: Current time is", current_time)

    elif "thank you" in user or "thanks" in user:
        print("Softchat: You're welcome!")

    elif user == "bye":
        print("Softchat: Goodbye! Have a nice day.")
        break

    else:
        print("Softchat: Sorry, I don't understand that.")