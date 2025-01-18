#text-based adventure game developed using Python and Pygame
import pygame
import sys

# Initialize pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600  # Screen width and height
screen = pygame.display.set_mode((WIDTH, HEIGHT))  # Create a game window
pygame.display.set_caption("Adventure of Eldoria")  # Set the title of the window

# Colors
WHITE = (255, 255, 255)  # RGB for white color
BLACK = (0, 0, 0)  # RGB for black color

# Fonts
font_title = pygame.font.Font(None, 60)  # Font for titles
font_text = pygame.font.Font(None, 40)  # Font for general text
font_choice = pygame.font.Font(None, 35)  # Font for choices

# Load images
background = pygame.image.load("forest_background.jpg")  # Load the background image
background = pygame.transform.scale(background, (WIDTH, HEIGHT))  # Scale the image to fit the screen

# Game variables
game_state = "intro"  # Current state of the game (intro, cave, tower, forest, etc.)
choice = None  # Player's choice
input_text = ""  # Input text for riddles or typing scenarios


def render_text_centered(text, y, font, color=WHITE):
    """
    Helper function to render centered text on the screen.
    - text: The string to display.
    - y: Vertical position for the text.
    - font: Font object to render the text.
    - color: Text color.
    """
    rendered_text = font.render(text, True, color)
    text_rect = rendered_text.get_rect(center=(WIDTH // 2, y))  # Center the text horizontally
    screen.blit(rendered_text, text_rect)  # Draw the text on the screen


def fade_effect():
    """
    Creates a fade-in effect for screen transitions.
    - A black transparent overlay gradually disappears to reveal the background.
    """
    fade = pygame.Surface((WIDTH, HEIGHT))  # Create a surface the size of the screen
    fade.fill(BLACK)  # Fill it with black
    for alpha in range(0, 255, 5):  # Gradually increase transparency
        fade.set_alpha(alpha)  # Set transparency level
        screen.blit(background, (0, 0))  # Draw the background
        screen.blit(fade, (0, 0))  # Draw the fading overlay
        pygame.display.update()  # Update the display
        pygame.time.delay(20)  # Small delay to create a smooth effect


def display_intro():
    """
    Display the intro scene with the background, shadow overlay, and text.
    - Introduces the game and presents the first set of choices.
    """
    screen.blit(background, (0, 0))  # Draw the background image
    shadow = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)  # Create a semi-transparent overlay
    shadow.fill((0, 0, 0, 120))  # Set shadow transparency
    screen.blit(shadow, (0, 0))  # Draw the shadow overlay
    render_text_centered("Welcome to the Adventure of Eldoria!", 100, font_title)
    render_text_centered("You awaken in a dark forest with three paths.", 200, font_text)
    render_text_centered("1. Enter the dark cave", 300, font_choice)
    render_text_centered("2. Walk towards the glowing tower", 350, font_choice)
    render_text_centered("3. Explore the dense forest", 400, font_choice)
    render_text_centered("Choose your path (1/2/3):", 500, font_text)


def display_scene(title, options):
    """
    Display a generic scene with a title and a list of options.
    - title: Description of the scene.
    - options: List of choices available in this scene.
    """
    screen.fill(BLACK)  # Clear the screen with black
    render_text_centered(title, 150, font_text)  # Render the title
    for i, option in enumerate(options, start=1):  # Loop through options and display them
        render_text_centered(f"{i}. {option}", 200 + i * 50, font_choice)
    render_text_centered("Choose your path (1/2):", 500, font_text)  # Instructions for player input


def handle_scene_choice(options):
    """
    Update the game state based on the player's choice.
    - options: List of possible outcomes corresponding to choices.
    """
    global game_state

    if choice in {"1", "2", "3"}:  # Ensure the input is valid
        choice_index = int(choice) - 1  # Convert choice to zero-based index
        if choice_index < len(options):  # Check if the choice matches an available option
            game_state = options[choice_index]  # Update the game state
            print(f"Game state updated to: {game_state}")  # Debugging output
        else:
            print(f"Invalid choice '{choice}'. No matching option.")  # Debugging output for invalid options
    else:
        print(f"Invalid input: {choice}. Please select a valid option.")  # Debugging output for invalid input


def display_forest():
    """
    Display the forest scene where the player answers a riddle.
    """
    global input_text
    screen.fill(BLACK)  # Clear the screen with black
    render_text_centered("You venture into the dense forest.", 150, font_text)
    render_text_centered("A treasure chest guarded by a riddle lies before you.", 200, font_text)
    render_text_centered("'I speak without a mouth and hear without ears. What am I?'", 300, font_text)
    render_text_centered("Type your answer below:", 400, font_text)
    render_text_centered(f"{input_text}", 450, font_choice)  # Display the player's current input


def display_outcome(outcome):
    """
    Display the end result of the game.
    - outcome: Either "victory" or "defeat".
    """
    screen.fill(BLACK)  # Clear the screen with black
    title = "Congratulations! You succeeded!" if outcome == "victory" else "Game Over. You were defeated."
    render_text_centered(title, 300, font_title)
    render_text_centered("Press R to restart or Q to quit.", 400, font_choice)


def reset_game():
    """
    Reset the game to its initial state.
    """
    global game_state, choice, input_text
    game_state = "intro"  # Reset game state
    choice = None  # Clear choice
    input_text = ""  # Clear input text
    fade_effect()  # Apply fade effect for a smooth reset


def main():
    """
    Main game loop. Handles events, updates game state, and renders scenes.
    """
    global game_state, choice, input_text
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Quit the game
                pygame.quit()
                sys.exit()

            # Handle state transitions for intro, cave, and tower
            if game_state in ["intro", "cave", "tower"] and event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    choice = "1"
                elif event.key == pygame.K_2:
                    choice = "2"
                elif event.key == pygame.K_3:
                    choice = "3"

                # Call handle_scene_choice based on current game state
                if choice:
                    if game_state == "intro":
                        handle_scene_choice(["cave", "tower", "forest"])
                    elif game_state == "cave":
                        handle_scene_choice(["defeat", "intro"])
                    elif game_state == "tower":
                        handle_scene_choice(["victory", "victory"])

            # Handle text input for the forest state
            elif game_state == "forest":
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:  # Submit the answer
                        game_state = "victory" if input_text.lower() == "echo" else "defeat"
                        input_text = ""  # Clear input
                    elif event.key == pygame.K_BACKSPACE:  # Delete the last character
                        input_text = input_text[:-1]
                    else:  # Add new character to input
                        input_text += event.unicode

            # Restart or quit the game in the end states
            elif game_state in ["victory", "defeat"] and event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:  # Restart the game
                    reset_game()
                elif event.key == pygame.K_q:  # Quit the game
                    pygame.quit()
                    sys.exit()

        # Update the screen based on the current game state
        if game_state == "intro":
            display_intro()
        elif game_state == "cave":
            display_scene("You enter the cave. A troll blocks your way.", ["Fight the troll", "Run away"])
        elif game_state == "tower":
            display_scene("The wizard offers two potions.", ["Red potion (strength)", "Blue potion (wisdom)"])
        elif game_state == "forest":
            display_forest()
        elif game_state in ["victory", "defeat"]:
            display_outcome(game_state)

        pygame.display.flip()  # Update the display


# Run the game
main()
