import random
import datetime
def simple_chatbot():
    greetings = ["Hello there! How are you doing today?", 
                 "Hey! Nice to see you. How's your day going?", 
                 "Hi! Hope you're having a good time."]
    bot_name_responses = ["I am a simple rule-based chatbot created in Python.", 
                          "You can call me PyBot 🤖.", 
                          "I'm just a basic chatbot, but I'm learning!"]
    help_responses = ["I can answer simple questions based on rules.",
                      "You can ask me about my name, who created me, the current time, or just say hello!",
                      "I am still learning, but I can chat with you on basic topics."]
    mood_responses = ["I'm just a program, but I feel awesome when you talk to me! 😄", 
                      "I don't have feelings like humans, but I'm happy to chat with you.", 
                      "I'm doing great, thanks for asking!"]
    creator_responses = ["I was created using Python and simple if-else rules.", 
                         "My creator used Python programming language to build me.", 
                         "I am built with Python and lots of logic!"]
    thank_responses = ["You're welcome!", "No problem at all 😊", "Happy to help!"]
    joke_responses = ["Why don't programmers like nature? Because it has too many bugs 🐞.", 
                      "Why do Java developers wear glasses? Because they don't see sharp 👓.", 
                      "I told my computer a joke once... it didn't laugh, it just gave me a byte 😂."]
    print("Chatbot: Hello! I am PyBot, a simple chatbot. Type 'bye' to exit.")
    print("Chatbot: How can I help you today?")
    while True:
        user_input = input("You: ").lower()
        # Rule 1: Greeting
        if any(word in user_input for word in ["hello", "hi", "hey", "hii", "heyy"]):
            print("Chatbot:", random.choice(greetings))
        # Rule 2: Asking about the chatbot's name
        elif "your name" in user_input or "who are you" in user_input:
            print("Chatbot:", random.choice(bot_name_responses))
        # Rule 3: Asking for help
        elif "help" in user_input or "what can you do" in user_input:
            print("Chatbot:", random.choice(help_responses))
        # Rule 4: Asking about creation
        elif "how were you made" in user_input or "who created you" in user_input:
            print("Chatbot:", random.choice(creator_responses))
        # Rule 5: Mood / How are you
        elif "how are you" in user_input or "how do you feel" in user_input:
            print("Chatbot:", random.choice(mood_responses))
        # Rule 6: Current time
        elif "time" in user_input:
            now = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"Chatbot: The current time is {now} ⏰")
        # Rule 7: Current date
        elif "date" in user_input or "day" in user_input:
            today = datetime.datetime.now().strftime("%A, %d %B %Y")
            print(f"Chatbot: Today is {today} 📅")
        # Rule 8: Thank you
        elif "thank" in user_input:
            print("Chatbot:", random.choice(thank_responses))
        elif "joke" in user_input or "funny" in user_input:
            print("Chatbot:", random.choice(joke_responses))
        elif any(word in user_input for word in ["bye", "exit", "quit", "goodbye"]):
            print("Chatbot: Goodbye! Have a wonderful day. 👋")
            break
        else:
            print("Chatbot: I'm not sure I understand that 🤔. Could you try rephrasing?")
# Start the chatbot
if __name__ == "__main__":
    simple_chatbot()