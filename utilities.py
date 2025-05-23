"""
Utility functions for console operations and game constants.

This module contains basic functions for handling console operations and game constants.
"""

import os
from typing import Optional, List, Dict, Any
from constants import (
    BORDER_LENGTH,
    WEAPONS,
    WeaponData,
    WeaponName,
    DamageValue,
    HealthValue,
    CharacterName
)

# Type aliases are now imported from constants.py


def clear_screen() -> None:
    """Clear the console screen based on the operating system.
    
    This function handles platform-specific screen clearing commands:
    - Windows: Uses 'cls' command
    - Unix/Linux: Uses 'clear' command
    
    If the operating system is not supported, it falls back to printing newlines.
    
    Raises:
        OSError: If the operating system is not supported
        Exception: For any other unexpected errors
    
    Example:
        >>> clear_screen()  # Clears the screen based on OS
    """
    try:
        if os.name not in ['nt', 'posix']:
            raise OSError(f"Unsupported operating system: {os.name}")
        os.system('cls' if os.name == 'nt' else 'clear')
    except OSError as e:
        print(f"Error: {str(e)}")
        print("\n" * 20)  # Fallback to print newlines
    except Exception as e:
        print(f"Unexpected error clearing screen: {str(e)}")
        print("\n" * 20)  # Fallback to print newlines


def press_enter() -> None:
    """Prompt the user to press Enter to continue.
    
    This function displays a message and waits for user input.
    It handles common input errors gracefully and allows for game interruption.
    
    Raises:
        KeyboardInterrupt: If user interrupts the input
        EOFError: If input stream is closed
    
    Example:
        >>> press_enter()  # Waits for user to press Enter
    """
    try:
        input("\nPress Enter to continue...\n")
    except KeyboardInterrupt:
        print("\nGame interrupted by user.")
        raise SystemExit
    except EOFError:
        print("\nInput stream closed.")
        raise SystemExit


def print_border(length: int = BORDER_LENGTH) -> None:
    """Print a border line for visual separation.
    
    This function creates a visual separator in the console output.
    It validates the input length to ensure it's positive.
    
    Args:
        length (int): Length of the border line. Defaults to BORDER_LENGTH constant.
    
    Raises:
        ValueError: If length is less than 1
    
    Example:
        >>> print_border()  # Prints default length border
        >>> print_border(50)  # Prints custom length border
    """
    if length < 1:
        raise ValueError("Border length must be at least 1")
    print("-" * length)
