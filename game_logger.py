"""
Game logging functionality.

This module provides a logging system for tracking game events and combat actions.
"""

from datetime import datetime
from typing import Optional

class GameLogger:
    """Class to handle game logging functionality.

    This class provides methods for logging game events, primarily combat
    actions, with timestamps. It supports both console output and can be
    extended for other logging mechanisms.

    Attributes:
        log_to_console (bool): Whether to output logs to the console
    """

    def __init__(self, log_to_console: bool = True) -> None:
        """Initialize the GameLogger instance.

        Args:
            log_to_console (bool): Whether to output logs to the console
        """
        self.log_to_console = log_to_console
        
    def log_combat(self, attacker: str, defender: str, damage: int) -> None:
        """Log a combat event with timestamp.

        Args:
            attacker (str): Name of the attacking character
            defender (str): Name of the defending character
            damage (int): Amount of damage dealt
        """
        timestamp = datetime.now().strftime("%H:%M:%S")
        message = f"[{timestamp}] {attacker} attacked {defender} for {damage} damage"
        if self.log_to_console:
            print(message)
