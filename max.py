import random
import datetime
import time
import requests

# --- NEW: Function to display the demo keyboard ---
def show_keyboard():
    """Displays the available commands to the user as a text-based menu."""
    print("\nBot: Here are some things you can ask me:")
    print("──────────────────────────────────")
    print("  ▶ hello / hi   - For a greeting")
    print("  ▶ time         - To get the current time")
    print("  ▶ date         - To get the current date")
    print("  ▶ joke         - To hear a programming joke")
    print("  ▶ who are you  - To learn about me")
    print("  ▶ bye          - To exit the chat")
    print("──────────────────────────────────")


def run_chatbot():
    """
    A simple, rule-based chatbot with a demo keyboard.
    """
    # Greet the user
    print("Bot: Hello! I'm a simple chatbot.")
    
    # --- MODIFIED: Show the keyboard at the start ---
    show_keyboard()

    # Main loop to keep the conversation going
    while True:
        # Get user input and normalize it
        user_input = input("You: ").lower().strip()

        # Exit condition
        if user_input == "bye":
            print("Bot: Goodbye! Have a great day.")
            break

        # Greeting
        elif "hello" in user_input or "hi" in user_input:
            responses = ["Hello there!", "Hi!", "Hey! What can I do for you?"]
            print(f"Bot: {random.choice(responses)}")

        # Time request
        elif "time" in user_input:
            # The current time is fetched for Bangladesh (UTC+6)
            current_time = datetime.datetime.now().strftime("%I:%M %p")
            print(f"Bot: The current time in Bangladesh is {current_time}.")

        # Date request
        elif "date" in user_input:
            current_date = datetime.datetime.now().strftime("%A, %B %d, %Y")
            print(f"Bot: Today's date is {current_date}.")

        # 'How are you'
        elif "how are you" in user_input:
            responses = ["I'm just a bot, but I'm functioning perfectly!", "I'm doing great, thanks for asking!"]
            print(f"Bot: {random.choice(responses)}")

        # Bot's name
        elif "your name" in user_input or "who are you" in user_input:
             print("Bot: I am a simple Python bot, designed to be helpful.")
        
        # Joke request
        elif "joke" in user_input:
            try:
                response = requests.get("https://official-joke-api.appspot.com/random_programming_joke")
                response.raise_for_status()
                joke_data = response.json()
                print(f"Bot: {joke_data['setup']}")
                time.sleep(2)
                print(f"Bot: ... {joke_data['punchline']}")
            except requests.exceptions.RequestException as e:
                print(f"Bot: Sorry, I couldn't fetch a joke right now. Error: {e}")

        # --- MODIFIED: The 'else' block now shows the keyboard ---
        else:
            print("Bot: I'm sorry, I don't understand that.")
            show_keyboard() # Show the helpful menu again


# This line makes sure the function runs when the script is executed
if __name__ == "__main__":
    run_chatbot()
