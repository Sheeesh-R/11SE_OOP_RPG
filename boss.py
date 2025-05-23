"""
Boss class module.

This module defines the Boss class, which extends the Character class,
demonstrating inheritance and method overriding.
"""

from typing import TYPE_CHECKING
from character import Character
from constants import BOSS_WEAPON_DAMAGE_BONUS

if TYPE_CHECKING:
    from character import Character
    from game_logger import GameLogger


class Boss(Character):
    """Represents a boss character that inherits from Character.
    
    This class demonstrates inheritance from Character and overrides the attack method
    to add special boss behavior.
    
    Attributes:
        Inherits all attributes from Character
    
    Methods:
        attack(): Perform a boss attack with special damage
    
    Example:
        >>> boss = Boss("Dragon", 150, 15)
        >>> boss.attack(player)  # Performs a boss attack
    """
    
    def __init__(self, name: str, health: int, damage: int) -> None:
        """Initialize a new Boss instance.
        
        Args:
            name (str): Boss's name
            health (int): Initial health value
            damage (int): Base damage value
        """
        super().__init__(name, health, damage)

    def attack(self, enemy: Character, logger: Optional[GameLogger] = None) -> int:
        """Perform a boss attack with additional special attack damage.
        
        This method overrides the parent class's attack method to add special boss behavior.
        It calculates total damage including a special attack bonus and applies it to the enemy.
        
        Args:
            enemy (Character): Target character
            logger (Optional[GameLogger]): Logger instance for combat logging
        
        Returns:
            int: Total damage dealt
        
        Raises:
            ValueError: If enemy is None
        
        Example:
            >>> boss = Boss("Dragon", 150, 15)
            >>> player = Character("Hero", 100, 10)
            >>> boss.attack(player)  # Performs boss attack with special damage
        """
        if enemy is None:
            raise ValueError("Enemy cannot be None")

        # Bosses have a special attack bonus
        total_damage = self.damage + BOSS_WEAPON_DAMAGE_BONUS

        if self.weapon:
            total_damage += self.weapon.damage_bonus

        enemy.set_health(enemy.get_health() - total_damage)

        if logger:
            logger.log_combat(self, enemy, total_damage)

        return total_damage
