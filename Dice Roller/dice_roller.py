"""
This code is a Dice Roller and Analyzer application written in Python. 
It allows users to simulate rolling dice, analyze the results statistically, and visualize the distribution of the rolls using a histogram.
"""
import random  # Import random module for generating random numbers
import statistics  # Import statistics module for analyzing numerical data
import matplotlib.pyplot as plt  # Import Matplotlib for data visualization

def roll_dice(num_rolls=1, sides=6):
    """
    Simulate rolling dice.
    Args:
        num_rolls (int): Number of dice to roll.
        sides (int): Number of sides on each die.
    Returns:
        list: A list of integers representing dice rolls.
    """
    return [random.randint(1, sides) for _ in range(num_rolls)]

def analyze_rolls(rolls):
    """
    Analyze the dice rolls to calculate statistical measures.
    Args:
        rolls (list): List of integers representing dice rolls.
    Returns:
        dict: A dictionary containing the mean, median, and mode of the rolls.
    """
    mean = statistics.mean(rolls)  # Calculate the average value
    median = statistics.median(rolls)  # Find the middle value
    mode = statistics.multimode(rolls)  # Find the most frequently occurring value(s)
    return {"mean": mean, "median": median, "mode": mode}

def plot_rolls(rolls, sides):
    """
    Create a histogram to visualize the distribution of dice rolls.
    Args:
        rolls (list): List of integers representing dice rolls.
        sides (int): Number of sides on the dice.
    """
    plt.hist(rolls, bins=range(1, sides+2), edgecolor='black', align='left', rwidth=0.8)
    plt.title(f"Dice Roll Distribution (Rolls: {len(rolls)}, Sides: {sides})")  # Title for the plot
    plt.xlabel("Dice Value")  # Label for the x-axis
    plt.ylabel("Frequency")  # Label for the y-axis
    plt.xticks(range(1, sides+1))  # Ensure the x-axis ticks match dice values
    plt.grid(axis='y', linestyle='--', alpha=0.7)  # Add gridlines for better readability
    plt.show()  # Display the plot

def main():
    """
    Main function to interact with the user, roll dice, and display results.
    """
    print("🎲 Welcome to the Dice Roller and Analyzer 🎲")
    while True:  # Loop to allow multiple rounds of dice rolling
        try:
            # Get user input for the number of dice and sides
            num_dice = int(input("How many dice would you like to roll? (Enter a number): "))
            sides = int(input("How many sides do your dice have? (e.g., 6 for standard dice): "))
            
            # Simulate rolling the dice
            rolls = roll_dice(num_dice, sides)

            # Display the rolled values
            print("\nYou rolled:", rolls)
            
            # Analyze the rolls and display the statistics
            analysis = analyze_rolls(rolls)
            print(f"\nStatistics:\n - Mean: {analysis['mean']:.2f}\n - Median: {analysis['median']:.2f}\n - Mode: {', '.join(map(str, analysis['mode']))}")

            # Generate and display a histogram of the rolls
            print("\nGenerating a visual representation...")
            plot_rolls(rolls, sides)

            # Ask the user if they want to roll again
            cont = input("\nWould you like to roll again? (yes/no): ").strip().lower()
            if cont not in ["yes", "y"]:
                print("🎲 Thanks for using the Dice Roller and Analyzer. Goodbye! 🎲")
                break
        except ValueError:
            # Handle invalid input (e.g., non-integer values)
            print("⚠️ Invalid input. Please enter a valid number.")
        except Exception as e:
            # Handle unexpected errors
            print(f"❌ An error occurred: {e}")

# Execute the main function when the script is run
main()
