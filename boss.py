"""
Boss enemies in the game.

This module defines the Boss class, which represents powerful enemies that
inherit from the base Character class and have special attack abilities.
"""

from typing import Optional
from character import Character
from game_logger import GameLogger

class Boss(Character):
    """Class representing boss enemies.

    Boss characters inherit from Character and have special attack abilities.
    They are designed to be more challenging opponents.

    Usage Example:
    ```python
    # Create a boss
    goblin_king = Boss("Goblin King", 50, 8)
    
    # Boss attacks with special damage
    damage = goblin_king.attack(player)
    print(f"Boss dealt {damage} damage!")
    ```
    """

    def __init__(self, name: str, health: int, damage: int) -> None:
        """Initialize a new Boss instance.

        Args:
            name (str): Boss's name
            health (int): Initial health points
            damage (int): Base damage value
        """
        super().__init__(name, health, damage, Weapon("Boss Weapon", 5))

    def attack(self, enemy: Character, logger: Optional[GameLogger] = None) -> int:
        """Perform a special attack with additional damage.

        Args:
            enemy (Character): Target character to attack
            logger (GameLogger, optional): Logger instance for combat logging

        Returns:
            int: Total damage dealt (base + special attack)
        """
        base_damage = super().attack(enemy, logger)
        additional_damage = 2
        enemy.health -= additional_damage
        if logger:
            logger.log_combat(self.name, enemy.name, additional_damage)
        print(f"{self.name} uses a special attack! (+{additional_damage} damage)")
        return base_damage + additional_damage

    def __str__(self) -> str:
        """Return a string representation of the boss.

        Returns:
            str: Formatted string showing boss name and health
        """
        return f"Boss: {super().__str__()}"