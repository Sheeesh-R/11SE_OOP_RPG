"""
Base character class for game entities.

This module defines the base Character class and its related functionality.
"""

from typing import Optional
from weapon import Weapon
from game_logger import GameLogger

class Character:
    """Base class for all game characters.

    This class represents a generic game character with attributes and methods
    for combat and character management. It serves as the base class for more
    specialized character types like Boss.

    Attributes:
        name (str): Character's name
        health (int): Current health points
        damage (int): Base damage value
        weapon (Weapon): Character's equipped weapon

    Usage Example:
    ```python
    # Create a character with a weapon
    sword = Weapon("Sword", 5)
    hero = Character("Hero", 100, 10, sword)
    
    # Display character info
    hero.display()
    
    # Attack another character
    enemy = Character("Goblin", 50, 5)
    damage = hero.attack(enemy)
    print(f"Dealt {damage} damage!")
    ```
    """

    def __init__(self, name: str, health: int, damage: int, weapon: Optional[Weapon] = None) -> None:
        """Initialize a new Character instance.

        Args:
            name (str): Character's name
            health (int): Initial health points
            damage (int): Base damage value
            weapon (Weapon, optional): Character's weapon
        """
        self.name = name
        self._health = health
        self.damage = damage
        self.weapon = weapon

    @property
    def health(self) -> int:
        """Get character's current health.

        Returns:
            int: Current health points
        """
        return self._health

    @health.setter
    def health(self, value: int) -> None:
        """Set character's health with validation.

        Args:
            value (int): New health value
        
        Notes:
            Health cannot go below 0
        """
        self._health = max(0, value)

    def get_health(self) -> int:
        """Get character's current health.

        Returns:
            int: Current health points
        
        Notes:
            This method is provided for compatibility with older code.
            Prefer using the health property directly.
        """
        return self.health
    
    def set_health(self, new_health: int) -> None:
        """Set character's health with validation.

        Args:
            new_health (int): New health value
        
        Notes:
            This method is provided for compatibility with older code.
            Prefer using the health property directly.
        """
        self.health = new_health

    def attack(self, enemy: 'Character', logger: Optional[GameLogger] = None) -> int:
        """Attack another character.

        Args:
            enemy (Character): Target character to attack
            logger (GameLogger, optional): Logger instance for combat logging

        Returns:
            int: Total damage dealt
        
        Notes:
            Damage is calculated as:
            base_damage + (weapon_damage_bonus if weapon exists)
        """
        total_damage = self.damage + (self.weapon.damage_bonus if self.weapon else 0)
        enemy.health -= total_damage
        if logger:
            logger.log_combat(self.name, enemy.name, total_damage)
        return total_damage

    def display(self) -> None:
        """Display character information.

        Shows character's name, health, damage, and equipped weapon.
        """
        weapon = self.weapon or "No Weapon"
        print(f"\nName: {self.name}")
        print(f"Health: {self.health}")
        print(f"Damage: {self.damage}")
        print(f"Weapon: {weapon.name} (+{weapon.damage_bonus} damage)" if self.weapon else "No Weapon")

    def __str__(self) -> str:
        """Return a string representation of the character.

        Returns:
            str: Formatted string showing character's name and health
        """
        return f"{self.name} (Health: {self.health})"

    @staticmethod
    def test_character_behavior() -> None:
        """Test character behavior and combat mechanics.

        This method tests:
        - Character creation
        - Weapon usage
        - Attack mechanics
        - Health management
        - Combat logging
        """
        # Create test characters
        sword = Weapon("Test Sword", 5)
        hero = Character("Test Hero", 100, 10, sword)
        enemy = Character("Test Enemy", 50, 5)
        
        # Test logger
        logger = GameLogger()
        
        # Test attack
        damage = hero.attack(enemy, logger)
        assert damage == 15  # 10 base + 5 weapon bonus
        assert enemy.health == 35  # 50 - 15 damage
        
        # Test health management
        enemy.health = 20
        assert enemy.health == 20
        
        # Test no weapon case
        hero.weapon = None
        damage = hero.attack(enemy, logger)
        assert damage == 10  # Only base damage
        
        print("Character behavior tests passed!")
