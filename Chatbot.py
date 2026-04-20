import random

def bot(msg):
    print("🤖 Bot:", msg)

def load_data():
    data = {}
    try:
        with open("data.txt") as f:
            for line in f:
                if ":" in line:
                    key, value = line.strip().split(":", 1)
                    data[key.lower()] = value
    except FileNotFoundError:
        pass
    return data

def Chatbot():
    bot("Hello! I am your AI assistant.")
    name = input("🤖 Bot: What's your name?\nYou: ")
    bot(f"Nice to meet you, {name}! 😊")
    greetings = ["Hello!", "Hi there!", "Hey!", "Nice to see you!"]
    how_are_you_responses = [
        "I'm doing great! 😄",
        "All good here!",
        "Feeling awesome! 💯",
        "I'm fine, thanks for asking!"
    ]
    sad_responses = [
        "I'm here for you ❤️",
        "Don't worry, things will get better",
        "Talk to me, what happened?"
    ]
    unknown_responses = [
        "Hmm, I didn’t get that 🤔",
        "Can you say that differently?",
        "I'm still learning 😅"
    ]
    data = load_data()   
    last_topic = ""      
    while True:
        user_input = input(f"{name}: ").lower().strip()
        if user_input in data:
            bot(data[user_input])
        elif any(word in user_input for word in ["hi", "hello", "hey"]):
            bot(random.choice(greetings))
        elif any(word in user_input for word in ["how are you", "how r u", "how are u"]):
            bot(random.choice(how_are_you_responses))
        elif "name" in user_input:
            bot(f"Your name is {name}, right? 😄")
        elif any(word in user_input for word in ["sad", "upset", "tired"]):
            bot(random.choice(sad_responses))
            last_topic = "sad"
        elif "again" in user_input and last_topic == "sad":
            bot("Still feeling sad? I'm here for you ❤️")
        elif "help" in user_input:
            bot("You can say hi, ask how I am, tell me you're sad, or say bye.")
        elif "bye" in user_input:
            bot(f"Goodbye {name}! Have a great day! 👋")
            break
        else:
            bot(random.choice(unknown_responses))
Chatbot()
