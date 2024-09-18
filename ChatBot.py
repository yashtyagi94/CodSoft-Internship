import datetime

def chatbot_user_input(user_input):
    user_input = user_input.lower()

    # Greeting handling
    if any(greeting in user_input for greeting in ["hey", "hello", "hii"]):
        return "Hello! How can I assist you today?"
    
    # "How are you?" handling
    elif "how are you?" in user_input:
        return "I'm good! Tell me something about you."
        
    # "Nothing" handling
    elif "nothing" in user_input:
        return "Fine! Enjoy your day."
   
    # Time handling
    elif "time" in user_input:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        return f"The current time is: {current_time}."
    
    # Emotion handling
    elif any(emotion in user_input for emotion in ["sad", "happy"]):
        if "sad" in user_input:
            return "I'm here for you!"
        elif "happy" in user_input:
            return "Great!"
    
    # "Bored" handling
    elif "bored" in user_input:
        return "Play your favorite games."
    
    # Farewell handling
    elif any(farewell in user_input for farewell in ["bye", "goodbye", "see you"]):
        return "It was a nice time! Feel free to come back anytime."
    
    # Default response
    else:
        return "I'm not sure how to respond to that. Please ask me something else."

# Main loop
while True:
    user_input = input("User: ")
    if user_input.lower() == "exit":
        print("AIBOT: Goodbye!")
        break

    response = chatbot_user_input(user_input)
    print("Chat Bot:", response)
