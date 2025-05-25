"""
Weapon class for game characters.

This module defines the Weapon class used by game characters to enhance their
combat capabilities.
"""

class Weapon:
    """Class representing weapons in the game.

    Attributes:
        name (str): Name of the weapon
        damage_bonus (int): Additional damage bonus provided by the weapon
    """

    def __init__(self, name: str, damage_bonus: int) -> None:
        """Initialize a new Weapon instance.

        Args:
            name (str): Name of the weapon
            damage_bonus (int): Damage bonus provided by the weapon
        """
        self.name = name
        self.damage_bonus = damage_bonus

    def __str__(self) -> str:
        """Return a string representation of the weapon.

        Returns:
            str: Formatted string showing weapon name and damage bonus
        """
        return f"{self.name} (+{self.damage_bonus} damage)"
