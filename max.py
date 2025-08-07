import random
import datetime
import time
import requests

# -------------------------------------------------------------------
# UPDATE 1: Command functions are now separate for better organization
# -------------------------------------------------------------------

def get_greeting():
    """Returns a random greeting."""
    responses = ["Hello there!", "Hi!", "Hey! What can I do for you?"]
    return random.choice(responses)

def get_time():
    """Returns the current time, specifying the location."""
    # Using the provided context: Location is Bangladesh (UTC+6)
    current_time = datetime.datetime.now().strftime("%I:%M %p")
    return f"The current time in Bangladesh is {current_time}."

def get_date():
    """Returns the current date."""
    current_date = datetime.datetime.now().strftime("%A, %B %d, %Y")
    return f"Today's date is {current_date}."

def get_joke():
    """Fetches and returns a random programming joke."""
    try:
        response = requests.get("https://official-joke-api.appspot.com/random_programming_joke")
        response.raise_for_status()  # Raise an exception for bad status codes
        joke_data = response.json()
        # Add a delay for comedic timing in the main loop
        return f"{joke_data['setup']}\nBot: ... {joke_data['punchline']}"
    except requests.exceptions.RequestException as e:
        return f"Sorry, I couldn't fetch a joke right now. Error: {e}"

def get_bot_info():
    """Returns information about the bot."""
    return "I am a simple Python bot, upgraded to be location-aware and more efficient!"

def get_location():
    """Returns the bot's operational location."""
    return "I'm currently operating from beautiful Bangladesh! (Timezone: UTC+06:00)"

# -------------------------------------------------------------------
# UPDATE 2: A "keyboard" menu of available commands
# -------------------------------------------------------------------

def show_keyboard():
    """Displays the available commands to the user."""
    print("\nBot: Here's what I can do:")
    print("──────────────────────────────────")
    print("  ▶ hello        - For a greeting")
    print("  ▶ time         - Get the time in Bangladesh")
    print("  ▶ date         - Get the current date")
    print("  ▶ joke         - Hear a programming joke")
    print("  ▶ location     - Find out where I am")
    print("  ▶ who are you  - Learn about me")
    print("  ▶ bye          - To exit the chat")
    print("──────────────────────────────────")

# -------------------------------------------------------------------
# UPDATE 3: The main function now uses a command dictionary
# This is much cleaner and easier to expand than if/elif/else.
# -------------------------------------------------------------------

def run_chatbot():
    """Main function to run the chatbot."""
    
    # Command dictionary: maps keywords (in tuples) to functions
    commands = {
        ('hello', 'hi', 'hey'): get_greeting,
        ('time',): get_time,
        ('date',): get_date,
        ('joke',): get_joke,
        ('who are you', 'your name'): get_bot_info,
        ('where', 'location'): get_location,
    }

    print("Bot: Hello! I've just been updated.")
    show_keyboard()

    # Main loop
    while True:
        user_input = input("You: ").lower().strip()
        
        if user_input == "bye":
            print("Bot: Goodbye! Have a great day.")
            break

        found_command = False
        # Check user input against the keywords in our command dictionary
        for keywords, func in commands.items():
            if any(keyword in user_input for keyword in keywords):
                response = func()
                # Special handling for joke's comedic timing
                if "..." in response:
                    part1, part2 = response.split("\nBot: ... ")
                    print(f"Bot: {part1}")
                    time.sleep(2)
                    print(f"Bot: ... {part2}")
                else:
                    print(f"Bot: {response}")
                found_command = True
                break
        
        if not found_command:
            print("Bot: I'm sorry, I don't recognize that command.")
            show_keyboard()

# This line makes sure the function runs when the script is executed
if __name__ == "__main__":
    run_chatbot()
