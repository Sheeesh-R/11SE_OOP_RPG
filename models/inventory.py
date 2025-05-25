"""
Inventory management system for game characters.
"""

from typing import List, Dict, Optional
from items.item import Item
from constants import INVENTORY_CONFIG

class Inventory:
    """Inventory class to manage character items.

    Attributes:
        max_slots (int): Maximum number of items in inventory
        items (List[Item]): List of items in inventory
        equipped_items (Dict[str, Item]): Currently equipped items
    """

    def __init__(self, max_slots: int = INVENTORY_CONFIG["max_slots"]):
        """Initialize inventory.

        Args:
            max_slots (int, optional): Maximum number of items. Defaults to 10.
        """
        self.max_slots = max_slots
        self.items: List[Item] = []
        self.equipped_items: Dict[str, Item] = {}

    def add_item(self, item: Item) -> bool:
        """Add an item to inventory.

        Args:
            item (Item): Item to add

        Returns:
            bool: True if item was added, False if inventory is full
        """
        if len(self.items) >= self.max_slots:
            return False
        self.items.append(item)
        return True

    def remove_item(self, item: Item) -> bool:
        """Remove an item from inventory.

        Args:
            item (Item): Item to remove

        Returns:
            bool: True if item was removed, False if not found
        """
        if item in self.items:
            self.items.remove(item)
            return True
        return False

    def use_item(self, item: Item, character: 'Character') -> bool:
        """Use an item from inventory.

        Args:
            item (Item): Item to use
            character (Character): Character using the item

        Returns:
            bool: True if item was used successfully
        """
        if item not in self.items:
            return False
        
        try:
            item.use(character)
            self.remove_item(item)
            return True
        except Exception as e:
            print(f"Error using item: {e}")
            return False

    def equip_item(self, item: Item) -> bool:
        """Equip an item.

        Args:
            item (Item): Item to equip

        Returns:
            bool: True if item was equipped
        """
        if item.item_type not in INVENTORY_CONFIG["item_types"]:
            print(f"Cannot equip item of type {item.item_type}")
            return False

        # Remove existing equipped item of same type
        if item.item_type in self.equipped_items:
            self.unequip_item(item.item_type)

        self.equipped_items[item.item_type] = item
        self.remove_item(item)
        return True

    def unequip_item(self, item_type: str) -> Optional[Item]:
        """Unequip an item of a specific type.

        Args:
            item_type (str): Type of item to unequip

        Returns:
            Optional[Item]: The unequipped item, or None if not equipped
        """
        if item_type not in self.equipped_items:
            return None

        item = self.equipped_items.pop(item_type)
        self.add_item(item)
        return item

    def get_equipped(self, item_type: str) -> Optional[Item]:
        """Get the currently equipped item of a specific type.

        Args:
            item_type (str): Type of item to get

        Returns:
            Optional[Item]: The equipped item, or None if not equipped
        """
        return self.equipped_items.get(item_type)

    def __len__(self) -> int:
        """Return number of items in inventory."""
        return len(self.items)

    def __str__(self) -> str:
        """Return a string representation of the inventory."""
        return f"Inventory (items: {len(self.items)}, max: {self.max_slots})"

    def __repr__(self) -> str:
        """Return a detailed string representation of the inventory."""
        return (f"<Inventory items={len(self.items)} "
                f"equipped={len(self.equipped_items)}>")
