"""
Sidekick classes module.

This module defines the Sidekick class and its subclasses, demonstrating
composition and specialized behaviors for player companions.
"""

from typing import TYPE_CHECKING, Optional
from character import Character

if TYPE_CHECKING:
    from character import Character


class Sidekick(Character):
    """Base class for player companions that inherit from Character.
    
    This class represents characters that can assist the player in combat.
    It inherits from Character but adds support for assisting the player.
    
    Attributes:
        Inherits all attributes from Character
        player (Optional[Character]): Reference to the player character
    
    Methods:
        assist_player(): Assist the player in combat
        attack(): Perform a sidekick attack
    
    Example:
        >>> sidekick = Sidekick("Robin", 60, 5)
        >>> sidekick.assist_player(player)  # Assists the player
    """
    def __init__(self, name: str, health: int, damage: int) -> None:
        """Initialize a new Sidekick instance.
        
        Args:
            name (str): Sidekick's name
            health (int): Initial health value
            damage (int): Base damage value
        """
        super().__init__(name, health, damage)
        self.player: Optional[Character] = None

    def assist_player(self, player: Character) -> None:
        """Assist the player in combat.
        
        This method allows the sidekick to assist the player in combat.
        Different sidekicks can implement this method to provide different
        types of assistance.
        
        Args:
            player (Character): Player character to assist
        
        Example:
            >>> sidekick = Sidekick("Robin", 60, 5)
            >>> player = Character("Hero", 100, 10)
            >>> sidekick.assist_player(player)  # Assists the player
        """
        self.player = player

    def attack(self, target: Character, logger: Optional[GameLogger] = None) -> int:
        """Perform a sidekick attack.
        
        This method overrides the parent class's attack method to add special
        sidekick behavior. Sidekicks have a chance to perform a coordinated
        attack with their player.
        
        Args:
            target (Character): Target character
            logger (Optional[GameLogger]): Logger instance for combat logging
        
        Returns:
            int: Total damage dealt
        
        Example:
            >>> sidekick = Sidekick("Robin", 60, 5)
            >>> enemy = Character("Goblin", 50, 5)
            >>> sidekick.attack(enemy)  # Performs a sidekick attack
        """
        import random
        
        # 30% chance for coordinated attack if player is alive
        is_coordinated = False
        if self.player and self.player.is_alive():
            is_coordinated = random.random() < 0.3
            
        total_damage = self.damage
        
        if is_coordinated:
            total_damage *= 1.5
            print(f"{self.name} and {self.player.name} perform a coordinated attack!")
            
        if self.weapon:
            total_damage += self.weapon.damage_bonus
            
        target.set_health(target.get_health() - total_damage)
        
        if logger:
            logger.log_combat(self, target, total_damage)
            
        return total_damage


class DefenderSidekick(Sidekick):
    """Represents a defensive sidekick that focuses on protecting the player.
    
    This class inherits from Sidekick and represents a specialized type of
    sidekick that focuses on defensive abilities.
    
    Attributes:
        Inherits all attributes from Sidekick
    
    Methods:
        defend_player(): Provide defensive assistance to the player
    
    Example:
        >>> sidekick = DefenderSidekick("Shieldbearer", 80, 3)
        >>> sidekick.defend_player(player)  # Provides defensive assistance
    """
    def __init__(self, name: str = "Shieldbearer", health: int = 80, damage: int = 3) -> None:
        """Initialize a new DefenderSidekick instance.
        
        Args:
            name (str): Sidekick's name
            health (int): Initial health value
            damage (int): Base damage value
        """
        super().__init__(name, health, damage)

    def defend_player(self) -> None:
        """Provide defensive assistance to the player.
        
        This method allows the sidekick to provide defensive assistance
        to the player, such as blocking attacks or healing.
        
        Example:
            >>> sidekick = DefenderSidekick("Shieldbearer", 80, 3)
            >>> sidekick.defend_player()  # Provides defensive assistance
        """
        if self.player:
            print(f"{self.name} is defending {self.player.name}!")
            # In a full implementation, this would include actual defensive mechanics


class SupportSidekick(Sidekick):
    """Represents a support sidekick that focuses on healing and buffs.
    
    This class inherits from Sidekick and represents a specialized type of
    sidekick that focuses on support abilities.
    
    Attributes:
        Inherits all attributes from Sidekick
    
    Methods:
        heal_player(): Heal the player character
    
    Example:
        >>> sidekick = SupportSidekick("Healer", 50, 2)
        >>> sidekick.heal_player(player)  # Heals the player
    """
    def __init__(self, name: str = "Healer", health: int = 50, damage: int = 2) -> None:
        """Initialize a new SupportSidekick instance.
        
        Args:
            name (str): Sidekick's name
            health (int): Initial health value
            damage (int): Base damage value
        """
        super().__init__(name, health, damage)

    def heal_player(self) -> None:
        """Heal the player character.
        
        This method allows the sidekick to heal the player character.
        
        Example:
            >>> sidekick = SupportSidekick("Healer", 50, 2)
            >>> sidekick.heal_player()  # Heals the player
        """
        if self.player:
            heal_amount = 10  # Base heal amount
            new_health = min(self.player.get_health() + heal_amount, 100)  # Cap at max health
            self.player.set_health(new_health)
            print(f"{self.name} heals {self.player.name} for {heal_amount} health!")
