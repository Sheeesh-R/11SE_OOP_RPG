"""
Inventory system for managing character items and equipment.
"""

from typing import Dict, List, Optional
from dataclasses import dataclass
from constants import WEAPONS, WEAPON_TYPES

class Inventory:
    """Represents a character's inventory.
    
    This class manages items, equipment, and consumables for a character.
    It demonstrates encapsulation and composition principles.
    
    Attributes:
        items (Dict[str, int]): Dictionary of items and their quantities
        equipped_weapon (Optional[Weapon]): Currently equipped weapon
        max_size (int): Maximum number of items in inventory
    
    Methods:
        add_item(): Add an item to inventory
        remove_item(): Remove an item from inventory
        equip_weapon(): Equip a weapon
        unequip_weapon(): Unequip current weapon
        get_inventory(): Get current inventory status
    """
    
    def __init__(self, max_size: int = 10):
        """Initialize the inventory.
        
        Args:
            max_size (int): Maximum number of items in inventory
        """
        self.items: Dict[str, int] = {}
        self.equipped_weapon: Optional["Weapon"] = None
        self.max_size = max_size

    def add_item(self, item_name: str, quantity: int = 1) -> bool:
        """Add an item to the inventory.
        
        Args:
            item_name (str): Name of the item
            quantity (int): Number of items to add
        
        Returns:
            bool: True if item was added, False if inventory is full
        """
        if len(self.items) >= self.max_size:
            print("\nInventory is full!")
            return False
            
        if item_name in self.items:
            self.items[item_name] += quantity
        else:
            self.items[item_name] = quantity
        
        print(f"\nAdded {quantity} {item_name}(s) to inventory")
        return True

    def remove_item(self, item_name: str, quantity: int = 1) -> bool:
        """Remove an item from the inventory.
        
        Args:
            item_name (str): Name of the item
            quantity (int): Number of items to remove
        
        Returns:
            bool: True if item was removed, False if not enough items
        """
        if item_name not in self.items:
            print(f"\nNo {item_name} in inventory!")
            return False
            
        if self.items[item_name] < quantity:
            print(f"\nNot enough {item_name} in inventory!")
            return False
            
        self.items[item_name] -= quantity
        if self.items[item_name] == 0:
            del self.items[item_name]
        
        print(f"\nRemoved {quantity} {item_name}(s) from inventory")
        return True

    def equip_weapon(self, weapon: "Weapon") -> bool:
        """Equip a weapon.
        
        Args:
            weapon (Weapon): Weapon to equip
        
        Returns:
            bool: True if weapon was equipped, False if already equipped
        """
        if self.equipped_weapon:
            print("\nUnequip current weapon first!")
            return False
            
        self.equipped_weapon = weapon
        print(f"\nEquipped {weapon.name}")
        return True

    def unequip_weapon(self) -> bool:
        """Unequip the current weapon.
        
        Returns:
            bool: True if weapon was unequipped, False if no weapon equipped
        """
        if not self.equipped_weapon:
            print("\nNo weapon equipped!")
            return False
            
        print(f"\nUnequipped {self.equipped_weapon.name}")
        self.equipped_weapon = None
        return True

    def get_inventory(self) -> Dict[str, int]:
        """Get current inventory status.
        
        Returns:
            Dict[str, int]: Dictionary of items and quantities
        """
        return self.items

    def __str__(self) -> str:
        """Return a string representation of the inventory.
        
        Returns:
            str: Inventory contents and equipped weapon
        """
        inventory_str = "\nInventory:"
        if not self.items:
            inventory_str += " Empty"
        else:
            for item, qty in self.items.items():
                inventory_str += f"\n- {item}: {qty}"
        
        if self.equipped_weapon:
            inventory_str += f"\n\nEquipped: {self.equipped_weapon}"
        else:
            inventory_str += "\n\nEquipped: None"
        
        return inventory_str

@dataclass
class Weapon:
    """Represents a weapon in the game.
    
    This class demonstrates encapsulation and composition.
    It's used by the Inventory class to manage weapons.
    
    Attributes:
        name (str): Weapon name
        damage_bonus (int): Additional damage bonus
        weapon_type (str): Type of weapon (melee, ranged, magic)
        description (str): Weapon description
    """
    name: str
    damage_bonus: int
    weapon_type: str
    description: str

    def __str__(self) -> str:
        """Return a string representation of the weapon.
        
        Returns:
            str: Weapon details
        """
        return f"{self.name} ({self.weapon_type}): {self.description}"

    @classmethod
    def from_config(cls, config: dict) -> "Weapon":
        """Create a weapon from configuration.
        
        Args:
            config (dict): Weapon configuration
        
        Returns:
            Weapon: New weapon instance
        """
        return cls(
            name=config["name"],
            damage_bonus=config["damage_bonus"],
            weapon_type=config["type"],
            description=config["description"]
        )
