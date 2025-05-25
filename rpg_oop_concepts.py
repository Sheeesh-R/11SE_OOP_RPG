import os
import datetime
from typing import Optional, List, Dict, Any

# === Utility Functions ===
# Helper functions for console operations and user interaction

def clear_screen() -> None:
    """Clear the console screen.

    This function clears the terminal screen using the appropriate
    command for the operating system (cls for Windows, clear for Unix).
    """
    os.system('cls' if os.name == 'nt' else 'clear')

def press_enter() -> None:
    """Prompt user to press Enter to continue.

    Displays a message and waits for the user to press Enter before
    continuing program execution.
    """
    input("\nPress Enter to continue...\n")

def print_border() -> None:
    """Print a visual separator.

    Creates a horizontal line of dashes to visually separate sections
    of output in the console.
    """
    print("-" * 80)

# === Core Classes ===

# GameLogger class to handle game logging functionality
class GameLogger:
    """Class to handle game logging functionality.

    This class provides methods for logging game events, primarily combat
    actions, with timestamps. It supports both console output and can be
    extended for other logging mechanisms.

    Attributes:
        log_to_console (bool): Whether to output logs to the console
    """

    def __init__(self, log_to_console: bool = True) -> None:
        """Initialize the GameLogger instance.

        Args:
            log_to_console (bool): Whether to output logs to the console
        """
        self.log_to_console = log_to_console
        
    def log_combat(self, attacker: str, defender: str, damage: int) -> None:
        """Log a combat event with timestamp.

        Args:
            attacker (str): Name of the attacking character
            defender (str): Name of the defending character
            damage (int): Amount of damage dealt
        """
        timestamp = datetime.datetime.now().strftime("%H:%M:%S")
        message = f"[{timestamp}] {attacker} attacked {defender} for {damage} damage"
        if self.log_to_console:
            print(message)

# Weapon class to represent different weapons in the game
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

# Base class for all game characters
class Character:
    """Base class for all game characters.

    This class represents a generic game character with attributes and methods
    for combat and character management. It serves as the base class for more
    specialized character types like Boss.

    Attributes:
        name (str): Character's name
        health (int): Current health points
        damage (int): Base damage value
        weapon (Weapon): Character's equipped weapon

    Usage Example:
    ```python
    # Create a character with a weapon
    sword = Weapon("Sword", 5)
    hero = Character("Hero", 100, 10, sword)
    
    # Display character info
    hero.display()
    
    # Attack another character
    enemy = Character("Goblin", 50, 5)
    damage = hero.attack(enemy)
    print(f"Dealt {damage} damage!")
    ```
    """

    def __init__(self, name: str, health: int, damage: int, weapon: Optional[Weapon] = None) -> None:
        """Initialize a new Character instance.

        Args:
            name (str): Character's name
            health (int): Initial health points
            damage (int): Base damage value
            weapon (Weapon, optional): Character's weapon
        """
        self.name = name
        self._health = health
        self.damage = damage
        self.weapon = weapon

    @property
    def health(self) -> int:
        """Get character's current health.

        Returns:
            int: Current health points
        """
        return self._health

    @health.setter
    def health(self, value: int) -> None:
        """Set character's health with validation.

        Args:
            value (int): New health value
        
        Notes:
            Health cannot go below 0
        """
        self._health = max(0, value)

    def get_health(self) -> int:
        """Get character's current health.

        Returns:
            int: Current health points
        
        Notes:
            This method is provided for compatibility with older code.
            Prefer using the health property directly.
        """
        return self.health
    
    def set_health(self, new_health: int) -> None:
        """Set character's health with validation.

        Args:
            new_health (int): New health value
        
        Notes:
            This method is provided for compatibility with older code.
            Prefer using the health property directly.
        """
        self.health = new_health

    def attack(self, enemy: 'Character', logger: Optional[GameLogger] = None) -> int:
        """Attack another character.

        Args:
            enemy (Character): Target character to attack
            logger (GameLogger, optional): Logger instance for combat logging

        Returns:
            int: Total damage dealt
        
        Notes:
            Damage is calculated as:
            base_damage + (weapon_damage_bonus if weapon exists)
        """
        total_damage = self.damage + (self.weapon.damage_bonus if self.weapon else 0)
        enemy.health -= total_damage
        if logger:
            logger.log_combat(self.name, enemy.name, total_damage)
        return total_damage

    def display(self) -> None:
        """Display character information.

        Shows character's name, health, damage, and equipped weapon.
        """
        weapon = self.weapon or "No Weapon"
        print(f"\nName: {self.name}")
        print(f"Health: {self.health}")
        print(f"Damage: {self.damage}")
        print(f"Weapon: {weapon.name} (+{weapon.damage_bonus} damage)" if self.weapon else "No Weapon")

    def __str__(self) -> str:
        """Return a string representation of the character.

        Returns:
            str: Formatted string showing character's name and health
        """
        return f"{self.name} (Health: {self.health})"

    @staticmethod
    def test_character_behavior() -> None:
        """Test character behavior and combat mechanics.

        This method tests:
        - Character creation
        - Weapon usage
        - Attack mechanics
        - Health management
        - Combat logging
        """
        # Create test characters
        sword = Weapon("Test Sword", 5)
        hero = Character("Test Hero", 100, 10, sword)
        enemy = Character("Test Enemy", 50, 5)
        
        # Test logger
        logger = GameLogger()
        
        # Test attack
        damage = hero.attack(enemy, logger)
        assert damage == 15  # 10 base + 5 weapon bonus
        assert enemy.health == 35  # 50 - 15 damage
        
        # Test health management
        enemy.health = 20
        assert enemy.health == 20
        
        # Test no weapon case
        hero.weapon = None
        damage = hero.attack(enemy, logger)
        assert damage == 10  # Only base damage
        
        print("Character behavior tests passed!")

# Boss class representing powerful enemies that inherit from Character
class Boss(Character):
    """Class representing boss enemies.

    Boss characters inherit from Character and have special attack abilities.
    They are designed to be more challenging opponents.
    """

    def __init__(self, name: str, health: int, damage: int) -> None:
        """Initialize a new Boss instance.

        Args:
            name (str): Boss's name
            health (int): Initial health points
            damage (int): Base damage value
        """
        super().__init__(name, health, damage, Weapon("Boss Weapon", 5))

    def attack(self, enemy: Character, logger: Optional[GameLogger] = None) -> int:
        """Perform a special attack with additional damage.

        Args:
            enemy (Character): Target character to attack
            logger (GameLogger, optional): Logger instance for combat logging

        Returns:
            int: Total damage dealt (base + special attack)
        """
        base_damage = super().attack(enemy, logger)
        additional_damage = 2
        enemy.health -= additional_damage
        if logger:
            logger.log_combat(self.name, enemy.name, additional_damage)
        print(f"{self.name} uses a special attack! (+{additional_damage} damage)")
        return base_damage + additional_damage

    def __str__(self) -> str:
        """Return a string representation of the boss.

        Returns:
            str: Formatted string showing boss name and health
        """
        return f"Boss: {super().__str__()}"


# === Game Logic ===

# Main game class that manages game flow and state
class Game:
    """Main game class that manages game flow and state.

    This class handles the overall game logic, including:
    - Player character creation
    - Boss management
    - Combat system
    - Game progression
    - Victory/defeat conditions

    Usage Example:
    ```python
    # Create and start a new game
    game = Game()
    game.run()  # This will start the game loop

    # Access game state
    player = game.player  # Get player character
    bosses = game.bosses  # Get list of bosses
    logger = game.logger  # Get game logger
    ```
    """
    
    def __init__(self):
        """Initialize game state and dependencies.

        Sets up the initial game state with:
        - No player character (will be created during setup)
        - Empty list of bosses (will be populated during setup)
        - Game logger for combat events
        """
        self.player: Optional[Character] = None
        self.bosses: List[Boss] = []
        self.logger = GameLogger()

    def show_intro(self) -> None:
        """Display game introduction and set up the game.

        This method:
        1. Clears the screen
        2. Shows the game introduction message
        3. Prompts for player name
        4. Calls setup_game to create character
        """
        clear_screen()
        print("Welcome to the RPG Adventure!")
        print("In a world where darkness looms, you are the chosen hero destined to defeat the evil bosses and restore peace.")
        self.setup_game(input("Enter your character's name: ").capitalize())

    def setup_game(self, name: str) -> None:
        """Create player character and bosses.

        Args:
            name (str): Player's chosen character name

        This method:
        1. Prompts player to choose a weapon
        2. Creates player character with chosen weapon
        3. Displays character information
        4. Creates list of boss enemies
        """
        weapon_name, weapon_damage = self.choose_weapon()
        self.player = Character(name, 110, 10, Weapon(weapon_name, weapon_damage))
        self.player.display()
        press_enter()
        self.bosses = [
            Boss("Goblin King", 50, 8),
            Boss("Dark Sorcerer", 60, 9)
        ]

    def test_game_state(self) -> None:
        """Test the game state and character creation.

        This method is used for testing purposes to verify:
        - Player character creation
        - Boss creation
        - Weapon assignment
        - Initial health values
        """
        # Test player creation
        test_player = Character("Test Hero", 100, 10, Weapon("Test Sword", 5))
        assert test_player.health == 100
        assert test_player.damage == 10
        assert test_player.weapon.name == "Test Sword"
        
        # Test boss creation
        test_boss = Boss("Test Boss", 50, 8)
        assert test_boss.health == 50
        assert test_boss.damage == 8
        assert test_boss.weapon.name == "Boss Weapon"

        print("Game state tests passed!")

    def choose_weapon(self) -> tuple[str, int]:
        """Let player choose a weapon."""
        weapons = [
            {"name": "Rock", "damage_bonus": 2},
            {"name": "Paper", "damage_bonus": 3},
            {"name": "Scissors", "damage_bonus": 4}
        ]
        options = [weapon["name"] for weapon in weapons]
        while True:
            choice = input("\nChoose your weapon (Rock, Paper, Scissors): ").capitalize()
            if choice in options:
                weapon_data = weapons[options.index(choice)]
                return weapon_data["name"], weapon_data["damage_bonus"]
            print("Invalid choice. Please try again.")

    def combat(self, player: Character, enemy: Character) -> bool:
        """Handle combat between characters."""
        while player.health > 0 and enemy.health > 0:
            self.display_combat_status(player, enemy)
            damage_dealt = player.attack(enemy, self.logger)
            print(f"You dealt {damage_dealt} damage to {enemy.name}")
            if enemy.health <= 0:
                self.print_victory_message(enemy)
                return True

            damage_received = enemy.attack(player, self.logger)
            print(f"{enemy.name} dealt {damage_received} damage to you")
            if player.health <= 0:
                self.print_defeat_message(enemy)
                return False
            press_enter()

    def display_combat_status(self, player: Character, enemy: Character) -> None:
        """Show current combat status."""
        clear_screen()
        print(f"\n=== Combat: {enemy.name} ===")
        print("\nPlayer:")
        self.player.display()
        print("\nEnemy:")
        enemy.display()
        print("\n=== Actions ===")

    def handle_boss_battles(self) -> None:
        """Manage boss battles sequence."""
        for boss in self.bosses:
            self.introduce_boss(boss)
            if not self.combat(self.player, boss):
                self.end_game(False)
                return
        self.end_game(True)

    def introduce_boss(self, boss: Boss) -> None:
        """Introduce a boss before combat."""
        clear_screen()
        print(f"\n=== New Enemy: {boss.name} ===")
        boss.display()
        press_enter()

    def print_victory_message(self, enemy: Character) -> None:
        """Display victory message."""
        print_border()
        print(f"Victory! You defeated {enemy.name}!")
        press_enter()

    def print_defeat_message(self, enemy: Character) -> None:
        """Display defeat message."""
        print_border()
        print(f"Defeat! You were defeated by {enemy.name}!")
        press_enter()

    def end_game(self, won: bool) -> None:
        """End the game with appropriate message."""
        clear_screen()
        if won:
            print("Congratulations! You have defeated all the bosses!")
        else:
            print("Game Over. Better luck next time!")
        press_enter()

    def run(self) -> None:
        """Start and run the game."""
        self.show_intro()
        self.handle_boss_battles()

# Start the game if this file is executed
if __name__ == "__main__":
    game = Game()
    game.run()
