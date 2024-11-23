import random
import time

def calculator_game():
    print("Welcome to the Ultimate Calculator Game!")
    print("Choose your difficulty level:")
    print("1. Easy (1-10 numbers, + and -)")
    print("2. Medium (1-20 numbers, +, -, *)")
    print("3. Hard (1-50 numbers, all operations with decimals)")
    
    # Select difficulty level
    while True:
        difficulty = input("Enter 1, 2, or 3 to choose difficulty: ").strip()
        if difficulty in ['1', '2', '3']:
            difficulty = int(difficulty)
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")
    
    # Configure difficulty settings
    if difficulty == 1:
        max_num = 10
        operations = ['+', '-']
        time_limit = 10
    elif difficulty == 2:
        max_num = 20
        operations = ['+', '-', '*']
        time_limit = 8
    else:
        max_num = 50
        operations = ['+', '-', '*', '/']
        time_limit = 6

    points = 0
    streak = 0
    high_score = 0

    print(f"\nGame starting with a {time_limit}-second timer! Type 'quit' anytime to exit.")
    while True:
        # Generate random numbers and operation
        num1 = random.randint(1, max_num)
        num2 = random.randint(1, max_num)
        operation = random.choice(operations)

        # Ensure no division by zero
        if operation == '/' and num2 == 0:
            num2 = random.randint(1, max_num)

        # Calculate correct answer
        if operation == '+':
            correct_answer = num1 + num2
        elif operation == '-':
            correct_answer = num1 - num2
        elif operation == '*':
            correct_answer = num1 * num2
        elif operation == '/':
            correct_answer = round(num1 / num2, 2)

        # Display the problem and start the timer
        print(f"\nProblem: {num1} {operation} {num2}")
        start_time = time.time()
        
        player_answer = input("Your answer: ").strip()

        # Allow the player to quit
        if player_answer.lower() == 'quit':
            print(f"\nGame over! You scored {points} points.")
            print(f"Your highest streak: {streak}")
            if points > high_score:
                high_score = points
                print(f"New High Score: {high_score}!")
            break

        # Check time limit
        elapsed_time = time.time() - start_time
        if elapsed_time > time_limit:
            print(f"Time's up! You took {elapsed_time:.2f} seconds.")
            streak = 0
            continue

        # Validate and compare player's answer
        try:
            player_answer = float(player_answer)
            if abs(player_answer - correct_answer) < 0.01:
                print("Correct! +1 point")
                points += 1
                streak += 1
                if streak % 3 == 0:
                    print(f"Bonus! {streak} in a row! +2 points")
                    points += 2
            else:
                print(f"Wrong! The correct answer was {correct_answer}.")
                streak = 0
        except ValueError:
            print("Invalid input! Please enter a number.")
            streak = 0

def main():
    # Start the enhanced calculator game
    calculator_game()

main()
