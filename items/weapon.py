"""
Weapon classes with specialized behaviors.
"""

from typing import Optional
from items.item import Item
from constants import WEAPONS

class Weapon(Item):
    """Base class for all weapons.

    Attributes:
        damage_bonus (int): Additional damage bonus
        attack_type (str): Type of attack (physical, magical, etc.)
    """

    def __init__(self, name: str, description: str, damage_bonus: int, attack_type: str = "physical"):
        """Initialize a weapon.

        Args:
            name (str): Weapon name
            description (str): Weapon description
            damage_bonus (int): Additional damage bonus
            attack_type (str, optional): Type of attack. Defaults to "physical".
        """
        super().__init__(name, description, "WEAPON")
        self.damage_bonus = damage_bonus
        self.attack_type = attack_type

    def use(self, character: 'Character') -> None:
        """Equip the weapon on a character.

        Args:
            character (Character): Character equipping the weapon
        """
        character.equip_weapon(self)

    def calculate_damage(self, base_damage: int) -> int:
        """Calculate total damage with weapon bonus.

        Args:
            base_damage (int): Base damage from character

        Returns:
            int: Total damage
        """
        return base_damage + self.damage_bonus

    def __str__(self) -> str:
        """Return a string representation of the weapon."""
        return f"{self.name} (+{self.damage_bonus} {self.attack_type})"

class Rock(Weapon):
    """Rock weapon specialized against shielded enemies.

    Special Behavior: Has a chance to break enemy shields
    """

    def __init__(self):
        """Initialize a Rock weapon."""
        super().__init__(
            WEAPONS["ROCK"]["name"],
            WEAPONS["ROCK"]["description"],
            WEAPONS["ROCK"]["damage_bonus"],
            "physical"
        )

    def use(self, character: 'Character') -> None:
        """Equip the Rock weapon.

        Args:
            character (Character): Character equipping the weapon
        """
        super().use(character)
        print(f"{character.name} wields the {self.name} - ready to shatter shields!")

class Paper(Weapon):
    """Paper weapon specialized in wrapping enemies.

    Special Behavior: Can wrap enemies, reducing their movement
    """

    def __init__(self):
        """Initialize a Paper weapon."""
        super().__init__(
            WEAPONS["PAPER"]["name"],
            WEAPONS["PAPER"]["description"],
            WEAPONS["PAPER"]["damage_bonus"],
            "magical"
        )

    def use(self, character: 'Character') -> None:
        """Equip the Paper weapon.

        Args:
            character (Character): Character equipping the weapon
        """
        super().use(character)
        print(f"{character.name} wields the {self.name} - ready to ensnare foes!")

class Scissors(Weapon):
    """Scissors weapon specialized in cutting through armor.

    Special Behavior: Has a chance to bypass enemy armor
    """

    def __init__(self):
        """Initialize a Scissors weapon."""
        super().__init__(
            WEAPONS["SCISSORS"]["name"],
            WEAPONS["SCISSORS"]["description"],
            WEAPONS["SCISSORS"]["damage_bonus"],
            "physical"
        )

    def use(self, character: 'Character') -> None:
        """Equip the Scissors weapon.

        Args:
            character (Character): Character equipping the weapon
        """
        super().use(character)
        print(f"{character.name} wields the {self.name} - ready to pierce armor!")
