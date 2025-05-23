"""
Villain classes module.

This module defines the Villain class and its subclasses, demonstrating inheritance
from Character and showing how to create different types of enemies.
"""

from typing import TYPE_CHECKING
from character import Character

if TYPE_CHECKING:
    from character import Character


class Villain(Character):
    """Base class for regular enemies that inherit from Character.
    
    This class represents regular enemies that are not as powerful as bosses.
    It inherits from Character but can have its own unique behaviors.
    
    Attributes:
        Inherits all attributes from Character
    
    Methods:
        attack(): Perform a villain attack
    
    Example:
        >>> goblin = Goblin("Goblin", 50, 5)
        >>> goblin.attack(player)  # Performs a goblin attack
    """
    def __init__(self, name: str, health: int, damage: int) -> None:
        """Initialize a new Villain instance.
        
        Args:
            name (str): Villain's name
            health (int): Initial health value
            damage (int): Base damage value
        """
        super().__init__(name, health, damage)

    def attack(self, target: Character, logger: Optional[GameLogger] = None) -> int:
        """Perform a villain attack.
        
        This method overrides the parent class's attack method to add special
        villain behavior. Villains have a chance to perform a critical hit.
        
        Args:
            target (Character): Target character
            logger (Optional[GameLogger]): Logger instance for combat logging
        
        Returns:
            int: Total damage dealt
        
        Example:
            >>> goblin = Goblin("Goblin", 50, 5)
            >>> player = Character("Hero", 100, 10)
            >>> goblin.attack(player)  # Performs a goblin attack
        """
        import random
        
        # 20% chance for a critical hit
        is_critical = random.random() < 0.2
        total_damage = self.damage
        
        if is_critical:
            total_damage *= 1.5
            print(f"{self.name} landed a critical hit!")
            
        if self.weapon:
            total_damage += self.weapon.damage_bonus
            
        target.set_health(target.get_health() - total_damage)
        
        if logger:
            logger.log_combat(self, target, total_damage)
            
        return total_damage


class Goblin(Villain):
    """Represents a Goblin enemy.
    
    This class inherits from Villain and represents a specific type of enemy.
    It has its own unique attributes and behaviors.
    
    Attributes:
        Inherits all attributes from Villain
    
    Example:
        >>> goblin = Goblin("Goblin", 50, 5)
        >>> goblin.attack(player)  # Performs a goblin attack
    """
    def __init__(self, name: str = "Goblin", health: int = 50, damage: int = 5) -> None:
        """Initialize a new Goblin instance.
        
        Args:
            name (str): Goblin's name
            health (int): Initial health value
            damage (int): Base damage value
        """
        super().__init__(name, health, damage)


class Orc(Villain):
    """Represents an Orc enemy.
    
    This class inherits from Villain and represents a specific type of enemy.
    It has its own unique attributes and behaviors.
    
    Attributes:
        Inherits all attributes from Villain
    
    Example:
        >>> orc = Orc("Orc", 75, 8)
        >>> orc.attack(player)  # Performs an orc attack
    """
    def __init__(self, name: str = "Orc", health: int = 75, damage: int = 8) -> None:
        """Initialize a new Orc instance.
        
        Args:
            name (str): Orc's name
            health (int): Initial health value
            damage (int): Base damage value
        """
        super().__init__(name, health, damage)

    def attack(self, target: Character, logger: Optional[GameLogger] = None) -> int:
        """Perform an orc attack with special behavior.
        
        This method overrides the parent class's attack method to add special
        orc behavior. Orcs have a chance to perform a berserk attack.
        
        Args:
            target (Character): Target character
            logger (Optional[GameLogger]): Logger instance for combat logging
        
        Returns:
            int: Total damage dealt
        
        Example:
            >>> orc = Orc("Orc", 75, 8)
            >>> player = Character("Hero", 100, 10)
            >>> orc.attack(player)  # Performs an orc attack
        """
        import random
        
        # 10% chance for berserk attack
        is_berserk = random.random() < 0.1
        total_damage = self.damage
        
        if is_berserk:
            total_damage *= 2
            print(f"{self.name} enters berserk mode!")
            
        if self.weapon:
            total_damage += self.weapon.damage_bonus
            
        target.set_health(target.get_health() - total_damage)
        
        if logger:
            logger.log_combat(self, target, total_damage)
            
        return total_damage
