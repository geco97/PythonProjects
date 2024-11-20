import random
import time

# Word lists for different difficulty levels
easy_words = ["cat", "dog", "bat", "sun", "map"]
medium_words = ["python", "function", "variable", "tuple", "list"]
hard_words = ["dictionary", "structure", "iteration", "algorithm", "recursion"]

# Function to scramble a word
def scramble_word(word):
    scrambled = list(word)
    random.shuffle(scrambled)
    return ''.join(scrambled)

# Function to display a hint
def get_hint(word):
    hint_length = max(1, len(word) // 3)  # Reveal about a third of the letters
    hint = word[:hint_length] + "*" * (len(word) - hint_length)
    return hint

# Function to play a round
def play_round(word, time_limit):
    scrambled = scramble_word(word)
    print(f"\nScrambled word: {scrambled}")
    print(f"Hint: {get_hint(word)}")
    print(f"You have {time_limit} seconds to solve this!")

    start_time = time.time()

    while True:
        player_input = input("Your guess: ").lower()

        if player_input == "quit":
            print("You chose to quit the game.")
            return False, 0
        elif player_input == word:
            print("Correct! 🎉")
            return True, time.time() - start_time
        else:
            print("Wrong guess. Try again!")

        # Check if the time limit has passed
        if time.time() - start_time > time_limit:
            print(f"Time's up! The correct word was: {word}")
            return False, 0

# Function to play the game
def play_game():
    print("Welcome to the Enhanced Word Scramble Game!")
    print("Unscramble the letters to form a correct word.")
    print("Type 'quit' anytime to exit the game.\n")
    
    # Difficulty selection
    print("Choose a difficulty level:")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")
    
    while True:
        try:
            difficulty = int(input("Enter your choice (1/2/3): "))
            if difficulty == 1:
                words = easy_words
                time_limit = 15
                break
            elif difficulty == 2:
                words = medium_words
                time_limit = 10
                break
            elif difficulty == 3:
                words = hard_words
                time_limit = 7
                break
            else:
                print("Invalid choice. Please choose 1, 2, or 3.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    score = 0

    while True:
        word = random.choice(words)
        correct, _ = play_round(word, time_limit)
        if correct:
            score += 1
            print(f"Your current score is: {score}")
        else:
            print(f"Game over! Your final score is: {score}")
            break

# Main function to start the game
def main():
    play_game()

# Run the game
main()
