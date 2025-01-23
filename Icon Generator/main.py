import os
import math
import pygame
from PIL import Image, ImageDraw, ImageFont


def create_icon(
    output_path,
    size=(128, 128),
    shape="circle",
    shape_color="blue",
    background_color=None,
    border_color=None,
    border_width=0,
    text=None,
    text_color="white",
    font_path=None,
    font_size=20
):
    """
    Creates an enhanced icon with customizable options and displays it using Pygame.

    Parameters:
        output_path (str): Path to save the icon.
        size (tuple): Size of the icon (width, height).
        shape (str): Shape to draw ("circle", "square", "triangle", "star", "hexagon", "pentagon").
        shape_color (str): Color of the shape.
        background_color (str): Background color. Use None for transparency.
        border_color (str): Color of the border. Ignored if border_width is 0.
        border_width (int): Width of the border.
        text (str): Optional text to add to the icon.
        text_color (str): Color of the text.
        font_path (str): Path to the font file for text. Uses default if None.
        font_size (int): Size of the text.
    """
    def get_polygon_points(center, radius, sides, rotation=0):
        """Generate points for a regular polygon."""
        angle = 2 * math.pi / sides
        points = [
            (
                center[0] + radius * math.cos(rotation + i * angle),
                center[1] + radius * math.sin(rotation + i * angle)
            )
            for i in range(sides)
        ]
        return points

    # Create the base image
    icon = Image.new("RGBA", size, (255, 255, 255, 0) if background_color is None else background_color)
    draw = ImageDraw.Draw(icon)

    # Draw the shape
    padding = border_width if border_width else 0
    center = (size[0] // 2, size[1] // 2)
    radius = (size[0] - 2 * padding) // 2

    if shape == "circle":
        draw.ellipse([padding, padding, size[0] - padding, size[1] - padding], fill=shape_color, outline=border_color, width=border_width)
    elif shape == "square":
        draw.rectangle([padding, padding, size[0] - padding, size[1] - padding], fill=shape_color, outline=border_color, width=border_width)
    elif shape == "triangle":
        points = get_polygon_points(center, radius, 3, rotation=-math.pi / 2)
        draw.polygon(points, fill=shape_color, outline=border_color)
    elif shape == "star":
        points = []
        for i in range(10):  # 5 points + 5 inner points
            angle = math.pi / 5 * i
            r = radius if i % 2 == 0 else radius / 2  # Alternate between outer and inner radius
            points.append((center[0] + r * math.cos(angle), center[1] + r * math.sin(angle)))
        draw.polygon(points, fill=shape_color, outline=border_color)
    elif shape == "hexagon":
        points = get_polygon_points(center, radius, 6, rotation=math.pi / 6)
        draw.polygon(points, fill=shape_color, outline=border_color)
    elif shape == "pentagon":
        points = get_polygon_points(center, radius, 5, rotation=-math.pi / 2)
        draw.polygon(points, fill=shape_color, outline=border_color)
    else:
        raise ValueError("Unsupported shape. Use 'circle', 'square', 'triangle', 'star', 'hexagon', or 'pentagon'.")

    # Add optional text
    if text:
        try:
            font = ImageFont.truetype(font_path if font_path else "arial.ttf", font_size)
        except OSError:
            print("Default font not found. Using PIL's default font.")
            font = ImageFont.load_default()

        # Calculate text dimensions using textbbox
        text_bbox = draw.textbbox((0, 0), text, font=font)
        text_width = text_bbox[2] - text_bbox[0]
        text_height = text_bbox[3] - text_bbox[1]
        text_position = ((size[0] - text_width) // 2, (size[1] - text_height) // 2)

        # Draw the text
        draw.text(text_position, text, font=font, fill=text_color)

    # Save the icon
    icon.save(output_path, format="PNG")
    print(f"Icon saved to {output_path}")

    


def display_image_with_pygame(image_path):
    """Display an image using Pygame."""
    pygame.init()

    # Load the image
    image = pygame.image.load(image_path)
    window_size = image.get_size()
    screen = pygame.display.set_mode(window_size)
    pygame.display.set_caption("Generated Icon")

    # Display the image
    running = True
    while running:
        screen.fill((0, 0, 0))  # Clear screen with black
        screen.blit(image, (0, 0))  # Draw the image at (0, 0)
        pygame.display.flip()  # Update the display

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()


def interactive_icon_generator():
    """Interactive prompt for icon creation."""
    print("Welcome to the Icon Generator!")
    
    output_path = input("Enter the output file name (e.g., icon.png) [default: icon.png]: ").strip() or "icon.png"
    width = input("Enter the width of the icon [default: 128]: ").strip()
    width = int(width) if width else 128
    height = input("Enter the height of the icon [default: 128]: ").strip()
    height = int(height) if height else 128
    shape = input("Choose a shape (circle, square, triangle, star, hexagon, pentagon) [default: circle]: ").strip().lower() or "circle"
    shape_color = input("Enter the shape color (e.g., red, #FF5733) [default: blue]: ").strip() or "blue"
    
    background_color = input("Enter the background color (or leave empty for transparent) [default: transparent]: ").strip()
    background_color = None if not background_color or background_color.lower() == "transparent" else background_color
    
    border_color = input("Enter the border color (or leave empty for none) [default: none]: ").strip()
    border_color = None if not border_color else border_color
    
    border_width = input("Enter the border width (0 for no border) [default: 0]: ").strip()
    border_width = int(border_width) if border_width else 0
    
    add_text = input("Do you want to add text to the icon? (yes/no) [default: no]: ").strip().lower() or "no"
    text, text_color, font_size = None, "white", 20
    if add_text == "yes":
        text = input("Enter the text to display [default: A]: ").strip() or "A"
        text_color = input("Enter the text color [default: white]: ").strip() or "white"
        font_size = input("Enter the font size [default: 20]: ").strip()
        font_size = int(font_size) if font_size else 20

    create_icon(
        output_path=output_path,
        size=(width, height),
        shape=shape,
        shape_color=shape_color,
        background_color=background_color,
        border_color=border_color,
        border_width=border_width,
        text=text,
        text_color=text_color,
        font_size=font_size,
    )
    # Display the image using Pygame
    display_image_with_pygame(output_path)

# Run the interactive icon generator
interactive_icon_generator()
