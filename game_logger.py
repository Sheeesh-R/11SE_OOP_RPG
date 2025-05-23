"""
Game logging module.

This module manages combat logging functionality, demonstrating association
between Game and logging functionality.
"""

from dataclasses import dataclass
from typing import List, Optional
from datetime import datetime

@dataclass
class CombatLog:
    """Data structure for combat log entries.
    
    This class represents a single combat event in the game's history.
    It's used by the GameLogger to maintain a record of all combat actions.
    
    Attributes:
        timestamp (str): Time of the combat event
        attacker (Character): The attacking character
        defender (Character): The defending character
        damage (int): Amount of damage dealt
    
    Example:
        >>> log_entry = CombatLog("14:30:00", player, boss, 25)
    """
    timestamp: str
    attacker: 'Character'
    defender: 'Character'
    damage: int


class GameLogger:
    """Manages combat logging functionality.
    
    This class handles the logging of combat events in the game.
    It can log to both console and maintain an internal history of all combat actions.
    
    Attributes:
        log_to_console (bool): Whether to log messages to console
        logs (List[CombatLog]): List of combat log entries
    
    Example:
        >>> logger = GameLogger(True)  # Create logger that logs to console
        >>> logger.log_combat(player, boss, 25)  # Log a combat event
    """
    
    def __init__(self, log_to_console: bool = True) -> None:
        """Initialize the GameLogger with console logging option.
        
        Args:
            log_to_console (bool): Whether to enable console logging
        """
        self.log_to_console = log_to_console
        self.logs: List[CombatLog] = []
        
    def log_combat(self, attacker: 'Character', defender: 'Character', damage: int) -> None:
        """Log a combat event with timestamp.
        
        This method records a combat event and optionally logs it to the console.
        
        Args:
            attacker (Character): The attacking character
            defender (Character): The defending character
            damage (int): Amount of damage dealt
        """
        timestamp = datetime.now().strftime("%H:%M:%S")
        log_entry = CombatLog(timestamp, attacker, defender, damage)
        self.logs.append(log_entry)
        
        if self.log_to_console:
            log_message = f"[{timestamp}] COMBAT LOG: {attacker.name} attacked {defender.name} for {damage} damage"
            print(log_message)
            
    def get_combat_history(self) -> List[CombatLog]:
        """Get the complete combat history.
        
        Returns:
            List[CombatLog]: List of all combat log entries
        """
        return self.logs.copy()
