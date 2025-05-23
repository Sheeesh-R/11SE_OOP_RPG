"""
Weapon class module.

This module defines the Weapon class, demonstrating a simple class with attributes
and methods, and serves as a component for the Character class.
"""

from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from character import Character


@dataclass
class Weapon:
    """Represents a weapon in the game.
    
    This class demonstrates encapsulation by validating weapon properties.
    It's designed to be composed within the Character class.
    
    Attributes:
        name (str): Name of the weapon
        damage_bonus (int): Additional damage bonus provided by the weapon
    
    Methods:
        validate_damage_bonus(): Validate the damage bonus value
    
    Example:
        >>> sword = Weapon("Sword", 5)
        >>> print(sword)  # Output: Sword (+5 Damage)
    """
    name: str
    damage_bonus: int

    def __post_init__(self) -> None:
        """Validate the damage bonus value after initialization.
        
        This method ensures that the weapon's damage bonus is valid.
        """
        self.validate_damage_bonus()

    def validate_damage_bonus(self) -> None:
        """Validate the damage bonus value.
        
        Raises:
            ValueError: If damage bonus is negative
        """
        if self.damage_bonus < 0:
            raise ValueError("Damage bonus cannot be negative")

    def __str__(self) -> str:
        """Return a string representation of the weapon.
        
        Returns:
            str: Weapon name and damage bonus
        """
        return f"{self.name} (+{self.damage_bonus} Damage)"
