"""
Utility functions for console operations.

This module provides functions for managing console output and user interaction.
"""

import os

def clear_screen() -> None:
    """Clear the console screen.

    Uses appropriate command based on the operating system:
    - 'cls' for Windows
    - 'clear' for Unix-like systems
    """
    os.system('cls' if os.name == 'nt' else 'clear')

def press_enter() -> None:
    """Prompt user to press Enter to continue.

    Displays a message and waits for Enter key press.
    """
    input("Press Enter to continue...")

def print_border(message: str, char: str = "=") -> None:
    """Print a message with a border.

    Args:
        message (str): Message to display
        char (str): Character to use for the border
    """
    border = char * (len(message) + 4)
    print(f"\n{border}")
    print(f"{char} {message} {char}")
    print(f"{border}\n")
