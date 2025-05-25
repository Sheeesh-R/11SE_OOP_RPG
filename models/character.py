"""
Character class with enhanced functionality.
"""

from typing import Optional, List
from constants import CHARACTER_TYPES, WEAPONS
from items.item import Item
from models.inventory import Inventory

class Character:
    """Base class for all characters in the game.

    Attributes:
        name (str): Character's name
        health (int): Current health points
        max_health (int): Maximum health points
        damage (int): Base damage
        level (int): Current level
        experience (int): Current experience points
        inventory (Inventory): Character's inventory
        equipped_weapon (Optional[Item]): Currently equipped weapon
    """

    def __init__(self, name: str, health: int, damage: int, weapon: Optional[Item] = None):
        """Initialize a character.

        Args:
            name (str): Character's name
            health (int): Initial health points
            damage (int): Base damage
            weapon (Optional[Item], optional): Starting weapon. Defaults to None.
        """
        self.name = name
        self.max_health = health
        self.health = health
        self.damage = damage
        self.level = 1
        self.experience = 0
        self.inventory = Inventory()
        self.equipped_weapon = weapon

    def attack(self, target: 'Character') -> int:
        """Attack another character.

        Args:
            target (Character): Target character

        Returns:
            int: Damage dealt
        """
        total_damage = self.damage
        if self.equipped_weapon:
            total_damage += self.equipped_weapon.damage_bonus
        
        target.take_damage(total_damage)
        return total_damage

    def take_damage(self, damage: int) -> int:
        """Take damage from an attack.

        Args:
            damage (int): Damage amount

        Returns:
            int: Actual damage taken
        """
        self.health = max(0, self.health - damage)
        return damage

    def heal(self, amount: int) -> None:
        """Heal health points.

        Args:
            amount (int): Amount to heal
        """
        self.health = min(self.max_health, self.health + amount)

    def level_up(self) -> None:
        """Level up the character."""
        self.level += 1
        self.max_health += CHARACTER_TYPES["PLAYER"]["level_up_bonuses"]["health"]
        self.damage += CHARACTER_TYPES["PLAYER"]["level_up_bonuses"]["damage"]
        self.health = self.max_health

    def gain_experience(self, amount: int) -> None:
        """Gain experience points.

        Args:
            amount (int): Amount of experience points to gain
        """
        self.experience += amount
        required_exp = self.calculate_required_experience()
        
        while self.experience >= required_exp:
            self.level_up()
            self.experience -= required_exp
            required_exp = self.calculate_required_experience()

    def calculate_required_experience(self) -> int:
        """Calculate experience needed for next level.

        Returns:
            int: Required experience points
        """
        return CHARACTER_TYPES["PLAYER"]["base_exp_per_level"] * (self.level ** CHARACTER_TYPES["PLAYER"]["exp_multiplier"])

    def add_item(self, item: Item) -> bool:
        """Add an item to inventory.

        Args:
            item (Item): Item to add

        Returns:
            bool: True if item was added
        """
        return self.inventory.add_item(item)

    def use_item(self, item: Item) -> bool:
        """Use an item from inventory.

        Args:
            item (Item): Item to use

        Returns:
            bool: True if item was used
        """
        return self.inventory.use_item(item, self)

    def equip_weapon(self, weapon: Item) -> bool:
        """Equip a weapon.

        Args:
            weapon (Item): Weapon to equip

        Returns:
            bool: True if weapon was equipped
        """
        if weapon.item_type != "WEAPON":
            return False
        
        self.equipped_weapon = weapon
        return True

    def display(self) -> None:
        """Display character stats."""
        print(f"Name: {self.name}")
        print(f"Level: {self.level}")
        print(f"Health: {self.health}/{self.max_health}")
        print(f"Damage: {self.damage}")
        if self.equipped_weapon:
            print(f"Weapon: {self.equipped_weapon}")
        print(f"Experience: {self.experience}/{self.calculate_required_experience()}")

    def __str__(self) -> str:
        """Return a string representation of the character."""
        return f"{self.name} (Level {self.level})"

    def __repr__(self) -> str:
        """Return a detailed string representation of the character."""
        return (f"<Character name={self.name} level={self.level} "
                f"health={self.health}/{self.max_health}>")
