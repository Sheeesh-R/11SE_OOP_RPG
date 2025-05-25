"""
Utility functions for the RPG game.

This module contains helper functions used throughout the game.
"""

import random
import time
from typing import Optional
from constants import COLORS

def clear_screen() -> None:
    """Clear the console screen.

    Uses appropriate command based on the operating system:
    - 'cls' for Windows
    - 'clear' for Unix-like systems
    """
    try:
        import os
        os.system('cls' if os.name == 'nt' else 'clear')
    except:
        print("\n" * 50)  # Fallback for environments without os access

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

def color_text(text: str, color: str) -> str:
    """Apply color to text using ANSI escape codes.

    Args:
        text (str): Text to color
        color (str): Color name from COLORS constant

    Returns:
        str: Colored text
    """
    if color in COLORS:
        return f"{COLORS[color]}{text}{COLORS['RESET']}"
    return text

def roll_dice(sides: int = 6) -> int:
    """Simulate rolling a dice.

    Args:
        sides (int): Number of sides on the dice

    Returns:
        int: Random number between 1 and sides
    """
    return random.randint(1, sides)

def calculate_damage(base_damage: int, critical_chance: float = 0.15) -> int:
    """Calculate damage with chance for critical hit.

    Args:
        base_damage (int): Base damage value
        critical_chance (float): Chance for critical hit (0.0 to 1.0)

    Returns:
        int: Final damage value
    """
    if random.random() < critical_chance:
        return int(base_damage * 2)  # Double damage for critical hit
    return base_damage

def format_health(health: int, max_health: int) -> str:
    """Format health display with color coding.

    Args:
        health (int): Current health value
        max_health (int): Maximum health value

    Returns:
        str: Formatted health string
    """
    health_percent = (health / max_health) * 100
    if health_percent >= 75:
        color = "GREEN"
    elif health_percent >= 50:
        color = "YELLOW"
    else:
        color = "RED"
    
    return color_text(f"{health}/{max_health}", color)

def validate_input(prompt: str, valid_inputs: list[str]) -> str:
    """Get validated user input.

    Args:
        prompt (str): Input prompt message
        valid_inputs (list[str]): List of valid input values

    Returns:
        str: Validated user input
    """
    while True:
        user_input = input(prompt).strip().lower()
        if user_input in valid_inputs:
            return user_input
        print(f"Invalid input. Please choose from: {', '.join(valid_inputs)}")
