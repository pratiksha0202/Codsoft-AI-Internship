# Basic Rule-Based Chatbot

def chatbot_response(user_input):
    # Lowercase input to make the chatbot case-insensitive
    user_input = user_input.lower()
    
    # Respond to greetings
    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I assist you today?"

    # Respond to queries about weather
    elif "weather" in user_input:
        return "I'm not connected to the internet, but you can check the weather online!"

    # Respond to "how are you" queries
    elif "how are you" in user_input:
        return "I'm just a bot, but I'm doing great! How about you?"

    # Respond to thanks
    elif "thank you" in user_input or "thanks" in user_input:
        return "You're welcome! Happy to help."

    # Provide a fallback response if input is not recognized
    else:
        return "I'm sorry, I didn't understand that. Can you please ask something else?"

# Main interaction loop
print("Welcome to the chatbot! (Type 'exit' to end the conversation)")
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Chatbot: Goodbye!")
        break
    response = chatbot_response(user_input)
    print(f"Chatbot: {response}")
