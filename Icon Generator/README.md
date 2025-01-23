# Icon Generator

A Python-based interactive icon generator that creates icons with various shapes, colors, and customizations. This script uses the Pillow library to draw shapes and add text to the icons, and Pygame to display the generated icons.

## Features

- **Supported Shapes**: Circle, Square, Triangle, Star, Hexagon, Pentagon.
- **Customizable Options**:
  - Icon size (width and height).
  - Shape and background colors.
  - Border color and width.
  - Add text with customizable font, size, and color.
- **Interactive CLI**: User-friendly prompts to customize the icon.
- **Real-Time Display**: Automatically opens the generated icon in a Pygame window.

## Requirements

- Python 3.6+
- Pillow library
- Pygame library

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/geco97/PythonProjects
   cd PythonProjects/Icon Generator
   ```

2. Install dependencies:

   ```bash
   pip install Pillow pygame
   ```

## Usage

Run the script and follow the interactive prompts to generate your icon:

```bash
python main.py
```

### Example Interaction

```
Welcome to the Icon Generator!
Enter the output file name (e.g., icon.png) [default: icon.png]: my_icon.png
Enter the width of the icon [default: 128]: 200
Enter the height of the icon [default: 128]: 200
Choose a shape (circle, square, triangle, star, hexagon, pentagon) [default: circle]: star
Enter the shape color (e.g., red, #FF5733) [default: blue]: #FF5733
Enter the background color (or leave empty for transparent) [default: transparent]: transparent
Enter the border color (or leave empty for none) [default: none]: #FFFFFF
Enter the border width (0 for no border) [default: 0]: 5
Do you want to add text to the icon? (yes/no) [default: no]: yes
Enter the text to display [default: A]: Star
Enter the text color [default: white]: yellow
Enter the font size [default: 20]: 40
Icon saved to my_icon.png
```

The generated icon will be saved as `my_icon.png` in the current directory and displayed in a Pygame window.

## File Structure

```
project-folder/
├── main.py        # Main script with interactive generator
├── README.md      # Project documentation
└── requirements.txt # List of dependencies
```

## Custom Shapes

- **Circle**: Perfect circle.
- **Square**: Regular square.
- **Triangle**: Equilateral triangle.
- **Star**: Five-pointed star with alternating radii.
- **Hexagon**: Regular six-sided polygon.
- **Pentagon**: Regular five-sided polygon.


## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
