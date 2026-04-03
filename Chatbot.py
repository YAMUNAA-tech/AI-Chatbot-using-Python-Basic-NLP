import random

def Chatbot():
    print("🤖 Bot: Hello! I am your AI assistant.")
    name = input("🤖 Bot: What's your name? \nYou: ")
    print(f"🤖 Bot: Nice to meet you, {name}! 😊")
    greetings = ["Hello!", "Hi there!", "Hey!", "Nice to see you!"]
    how_are_you_responses = [
        "I'm doing great! 😄",
        "All good here!",
        "Feeling awesome! 💯",
        "I'm fine, thanks for asking!"
    ]

    while True:
        user_input = input(f"{name}: ").lower()
        if user_input in ["hi", "hello", "hey"]:
            print("🤖 Bot:", random.choice(greetings))
        elif "how are you" in user_input:
            print("🤖 Bot:", random.choice(how_are_you_responses))
        elif "name" in user_input:
            print(f"🤖 Bot: Your name is {name}, right? 😄")
        elif "help" in user_input:
            print("🤖 Bot: I can chat with you! Try saying hi, ask my name, or say bye.")

        elif "bye" in user_input:
            print(f"🤖 Bot: Goodbye {name}! Have a great day! 👋")
            break
        else:
            print("🤖 Bot: Hmm... I didn't understand that. Try something else!")
Chatbot()