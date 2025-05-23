"""
Character class module.

This module defines the Character class, demonstrating encapsulation through
private attributes and getter/setter methods. It also shows composition by
containing a Weapon object.
"""

from dataclasses import dataclass
from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from weapon import Weapon


@dataclass
class Character:
    """Represents a game character.
    
    This class demonstrates encapsulation through private attributes
    and getter/setter methods. It also shows composition by
    containing a Weapon object and implements character leveling.
    
    Attributes:
        name (str): Character's name
        _health (int): Character's health (private)
        damage (int): Base damage value
        level (int): Character's level
        experience (int): Character's experience points
        weapon (Optional[Weapon]): Character's equipped weapon
    
    Methods:
        get_health(): Get character's health with validation
        set_health(): Set character's health with validation
        is_alive(): Check if character is alive
        equip_weapon(): Equip a weapon for the character
        attack(): Perform an attack on another character
        gain_experience(): Gain experience points
        level_up(): Increase character level
    
    Example:
        >>> hero = Character("Hero", 100, 10)
        >>> hero.equip_weapon(Weapon("Sword", 5))
        >>> hero.attack(enemy)
        >>> hero.gain_experience(50)
    """
    name: str
    _health: int
    damage: int
    level: int = 1
    experience: int = 0
    weapon: Optional["Weapon"] = None

    def get_health(self) -> int:
        """Get character's health with validation.
        
        This method ensures the character's health is always valid.
        
        Returns:
            int: Current health value
        
        Raises:
            ValueError: If health is negative
        
        Example:
            >>> hero = Character("Hero", 100, 10)
            >>> hero.get_health()  # Returns 100
        """
        if self._health < 0:
            raise ValueError("Health cannot be negative")
        return self._health

    def set_health(self, value: int) -> None:
        """Set character's health with validation.
        
        This method ensures the character's health is always valid.
        
        Args:
            value (int): New health value
        
        Raises:
            ValueError: If health is negative
        
        Example:
            >>> hero = Character("Hero", 100, 10)
            >>> hero.set_health(80)  # Sets health to 80
        """
        if value < 0:
            raise ValueError("Health cannot be negative")
        self._health = value

    def is_alive(self) -> bool:
        """Check if the character is alive.
        
        Returns:
            bool: True if health is greater than 0
        
        Example:
            >>> hero = Character("Hero", 100, 10)
            >>> hero.is_alive()  # Returns True
        """
        return self._health > 0

    def equip_weapon(self, weapon: "Weapon") -> None:
        """Equip a weapon for the character.
        
        This method allows the character to equip a weapon, which will
        provide additional damage bonus during combat.
        
        Args:
            weapon (Weapon): Weapon to equip
        
        Example:
            >>> hero = Character("Hero", 100, 10)
            >>> sword = Weapon("Sword", 5)
            >>> hero.equip_weapon(sword)
        """
        self.weapon = weapon

    def attack(self, target: "Character", logger: Optional["GameLogger"] = None) -> int:
        """Perform an attack on another character.
        
        This method calculates total damage based on base damage and weapon bonus,
        applies the damage to the target, and logs the combat event if a logger is provided.
        
        Args:
            target (Character): Target character to attack
            logger (Optional[GameLogger]): Logger instance for combat logging
        
        Returns:
            int: Total damage dealt
        
        Raises:
            ValueError: If target is None
        
        Example:
            >>> hero = Character("Hero", 100, 10)
            >>> enemy = Character("Goblin", 50, 5)
            >>> hero.attack(enemy)  # Performs attack and returns damage value
        """
        if target is None:
            raise ValueError("Target cannot be None")

        total_damage = self.damage * self.level  # Damage scales with level
        if self.weapon:
            total_damage += self.weapon.damage_bonus

        target.set_health(target.get_health() - total_damage)

        if logger:
            logger.log_combat(self, target, total_damage)

        return total_damage

    def gain_experience(self, amount: int) -> None:
        """Gain experience points and potentially level up.
        
        Args:
            amount (int): Amount of experience points to gain
        
        Example:
            >>> hero = Character("Hero", 100, 10)
            >>> hero.gain_experience(50)
        """
        self.experience += amount
        while self.experience >= self.level * 100:  # Level up at 100, 200, 300, etc.
            self.level_up()

    def level_up(self) -> None:
        """Increase character level and stats.
        
        Example:
            >>> hero = Character("Hero", 100, 10)
            >>> hero.level_up()
        """
        self.level += 1
        self._health += 20  # Increase health on level up
        self.damage += 2    # Increase damage on level up
        print(f"\n{self.name} leveled up to level {self.level}!")
        print(f"Health increased to {self.get_health()}")
        print(f"Damage increased to {self.damage}")

    def __str__(self) -> str:
        """Return a string representation of the character.
        
        Returns:
            str: Character name, level, health, equipped weapon, and inventory status
        
        Example:
            >>> hero = Character("Hero", 100, 10)
            >>> print(hero)  # Output: Hero (Level 1, Health: 100)
        """
        weapon_str = f" with {self.weapon}" if self.weapon else ""
        return f"{self.name} (Level {self.level}, Health: {self.get_health()}{weapon_str})\n{str(self.inventory)}"
