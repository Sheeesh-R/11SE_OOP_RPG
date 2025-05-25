"""
Base class for all game items.
"""

from typing import Optional, Dict, Any
from constants import INVENTORY_CONFIG

class Item:
    """Base class for all items in the game.

    Attributes:
        name (str): Name of the item
        description (str): Description of the item
        item_type (str): Type of the item (WEAPON, ARMOR, POTION, etc.)
        value (int): Value of the item in game currency
    """

    def __init__(self, name: str, description: str, item_type: str, value: int = 0):
        """Initialize an item.

        Args:
            name (str): Name of the item
            description (str): Description of the item
            item_type (str): Type of the item
            value (int, optional): Value of the item. Defaults to 0.
        """
        self.name = name
        self.description = description
        self.item_type = item_type
        self.value = value

    def use(self, character: 'Character') -> None:
        """Use the item on a character.

        Args:
            character (Character): Character using the item

        Raises:
            NotImplementedError: If the item type doesn't support use
        """
        raise NotImplementedError(f"Cannot use {self.item_type} item directly")

    def __str__(self) -> str:
        """Return a string representation of the item."""
        return f"{self.name} ({self.item_type})"

    def __repr__(self) -> str:
        """Return a detailed string representation of the item."""
        return (f"<Item name={self.name} type={self.item_type} "
                f"value={self.value}>")
