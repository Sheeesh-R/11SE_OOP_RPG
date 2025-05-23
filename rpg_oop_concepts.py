import os
import datetime
from typing import Optional, List, Dict, Any, NoReturn
from dataclasses import dataclass

# Constants
BORDER_LENGTH: int = 80
WEAPONS: List[Dict[str, Any]] = [
    {"name": "Rock", "damage_bonus": 2},
    {"name": "Paper", "damage_bonus": 3},
    {"name": "Scissors", "damage_bonus": 4}
]

# Type aliases for better readability
WeaponData = Dict[str, Any]
WeaponName = str
DamageValue = int
HealthValue = int
CharacterName = str

# Error classes for specific game-related errors
class GameError(Exception):
    """Base class for game-related errors."""
    pass

class InvalidWeaponError(GameError):
    """Raised when an invalid weapon is selected."""
    pass

class GameOverError(GameError):
    """Raised when the game ends."""
    pass


# ==================== Utility Functions ====================
# This section contains basic utility functions for console operations and user interaction

def clear_screen() -> None:
    """Clear the console screen based on the operating system.
    
    This function handles platform-specific screen clearing commands:
    - Windows: Uses 'cls' command
    - Unix/Linux: Uses 'clear' command
    
    If the operating system is not supported, it falls back to printing newlines.
    
    Raises:
        OSError: If the operating system is not supported
        Exception: For any other unexpected errors
    
    Example:
        >>> clear_screen()  # Clears the screen based on OS
    """
    try:
        if os.name not in ['nt', 'posix']:
            raise OSError(f"Unsupported operating system: {os.name}")
        os.system('cls' if os.name == 'nt' else 'clear')
    except OSError as e:
        print(f"Error: {str(e)}")
        print("\n" * 20)  # Fallback to print newlines
    except Exception as e:
        print(f"Unexpected error clearing screen: {str(e)}")
        print("\n" * 20)  # Fallback to print newlines


def press_enter() -> None:
    """Prompt the user to press Enter to continue.
    
    This function displays a message and waits for user input.
    It handles common input errors gracefully and allows for game interruption.
    
    Raises:
        KeyboardInterrupt: If user interrupts the input
        EOFError: If input stream is closed
    
    Example:
        >>> press_enter()  # Waits for user to press Enter
    """
    try:
        input("\nPress Enter to continue...\n")
    except KeyboardInterrupt:
        print("\nGame interrupted by user.")
        raise SystemExit
    except EOFError:
        print("\nInput stream closed.")
        raise SystemExit


def print_border(length: int = BORDER_LENGTH) -> None:
    """Print a border line for visual separation.
    
    This function creates a visual separator in the console output.
    It validates the input length to ensure it's positive.
    
    Args:
        length (int): Length of the border line. Defaults to BORDER_LENGTH constant.
    
    Raises:
        ValueError: If length is less than 1
    
    Example:
        >>> print_border()  # Prints default length border
        >>> print_border(50)  # Prints custom length border
    """
    if length < 1:
        raise ValueError("Border length must be at least 1")
    print("-" * length)


# ==================== Core Classes ====================
# This section contains the main game classes that demonstrate OOP principles

# GameLogger class to demonstrate association relationship with Game (solid line in UML)
@dataclass
class CombatLog:
    """Data structure for combat log entries.
    
    This class represents a single combat event in the game's history.
    It's used by the GameLogger to maintain a record of all combat actions.
    
    Attributes:
        timestamp (str): Time of the combat event
        attacker (Character): The attacking character
        defender (Character): The defending character
        damage (int): Amount of damage dealt
    
    Example:
        >>> log_entry = CombatLog("14:30:00", player, boss, 25)
    """
    timestamp: str
    attacker: 'Character'
    defender: 'Character'
    damage: int


class GameLogger:
    """Manages combat logging functionality.
    
    This class handles the logging of combat events in the game.
    It can log to both console and maintain an internal history of all combat actions.
    
    Attributes:
        log_to_console (bool): Whether to log messages to console
        logs (List[CombatLog]): List of combat log entries
    
    Example:
        >>> logger = GameLogger(True)  # Create logger that logs to console
        >>> logger.log_combat(player, boss, 25)  # Log a combat event
    """
    
    def __init__(self, log_to_console: bool = True) -> None:
        """Initialize the GameLogger with console logging option.
        
        Args:
            log_to_console (bool): Whether to enable console logging
        """
        self.log_to_console = log_to_console
        self.logs: List[CombatLog] = []
        
    def log_combat(self, attacker: 'Character', defender: 'Character', damage: int) -> None:
        """Log a combat event with timestamp.
        
        This method records a combat event and optionally logs it to the console.
        
        Args:
            attacker (Character): The attacking character
            defender (Character): The defending character
            damage (int): Amount of damage dealt
        """
        timestamp = datetime.datetime.now().strftime("%H:%M:%S")
        log_entry = CombatLog(timestamp, attacker, defender, damage)
        self.logs.append(log_entry)
        
        if self.log_to_console:
            log_message = f"[{timestamp}] COMBAT LOG: {attacker.name} attacked {defender.name} for {damage} damage"
            print(log_message)
            
    def get_combat_history(self) -> List[CombatLog]:
        """Get the complete combat history.
        
        Returns:
            List[CombatLog]: List of all combat log entries
        """
        return self.logs.copy()


# Define a Weapon class to represent different weapons in the game
@dataclass
class Weapon:
    """Represents a weapon in the game.
    
    This class demonstrates encapsulation by validating weapon properties.
    It's designed to be composed within the Character class.
    
    Attributes:
        name (str): Name of the weapon
        damage_bonus (int): Additional damage bonus provided by the weapon
    
    Methods:
        validate_damage_bonus(): Validate the damage bonus value
    
    Example:
        >>> sword = Weapon("Sword", 5)
        >>> print(sword)  # Output: Sword (+5 Damage)
    """
    name: str
    damage_bonus: int
    
    def __post_init__(self) -> None:
        """Validate the damage bonus value after initialization.
        
        This method ensures that the weapon's damage bonus is valid.
        """
        self.validate_damage_bonus()
    
    def validate_damage_bonus(self) -> None:
        """Validate the damage bonus value.
        
        Raises:
            ValueError: If damage bonus is negative
        """
        if self.damage_bonus < 0:
            raise ValueError("Damage bonus cannot be negative")
    
    def __str__(self) -> str:
        """Return a string representation of the weapon.
        
        Returns:
            str: Weapon name and damage bonus
        """
        return f"{self.name} (+{self.damage_bonus} Damage)"


# Define a Character class to represent a game character
@dataclass
class Character:
    """Represents a game character.
    
    This class demonstrates encapsulation through private health attribute
    and getter/setter methods. It also shows composition by containing a Weapon.
    
    Attributes:
        name (str): Character's name
        _health (int): Character's health (private)
        damage (int): Base damage value
        weapon (Optional[Weapon]): Character's equipped weapon
    
    Methods:
        get_health(): Get character's health with validation
        set_health(): Set character's health with validation
        is_alive(): Check if character is alive
        equip_weapon(): Equip a weapon for the character
        attack(): Perform an attack on another character
    
    Example:
        >>> hero = Character("Hero", 100, 10)
        >>> hero.equip_weapon(Weapon("Sword", 5))
        >>> hero.attack(enemy)
    """
    name: str
    _health: int
    damage: int
    weapon: Optional[Weapon] = None
    
    def get_health(self) -> HealthValue:
        """Get character's health with validation.
        
        This method ensures the character's health is always valid.
        
        Returns:
            HealthValue: Current health value
        
        Raises:
            ValueError: If health is negative
        
        Example:
            >>> hero = Character("Hero", 100, 10)
            >>> hero.get_health()  # Returns 100
        """
        if self._health < 0:
            raise ValueError("Health cannot be negative")
        return self._health
    
    def set_health(self, value: HealthValue) -> None:
        """Set character's health with validation.
        
        This method ensures the character's health is always valid.
        
        Args:
            value (HealthValue): New health value
        
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
        """
        return self.get_health() > 0


# Define a Boss class that inherits from Character, representing a boss enemy
class Boss(Character):
    """Represents a boss character that inherits from Character.
    
    Attributes:
        Inherits all attributes from Character
        
    Methods:
        attack(): Perform a boss attack with special damage
    """
    
    def __init__(self, name: str, health: int, damage: int) -> None:
        """Initialize a new Boss instance.
        
        Args:
            name (str): Boss's name
            health (int): Initial health value
            damage (int): Base damage value
        """
        # Pass weapon details to parent constructor instead of creating a Weapon object here
        super().__init__(name, health, damage, "Boss Weapon", 5)

    def attack(self, enemy: 'Character', logger: Optional[GameLogger] = None) -> DamageValue:
        """Perform a boss attack with additional special attack damage.
        
        Args:
            enemy (Character): Target character
            logger (Optional[GameLogger]): Logger instance for combat logging
            
        Returns:
            DamageValue: Total damage dealt
            
        Raises:
            ValueError: If enemy is None
        """
        if enemy is None:
            raise ValueError("Enemy cannot be None")
            
        additional_damage = 1  # Example of special attack causing additional damage
        total_damage = super().attack(enemy, logger)  # Call Character's attack, then add bonus
        # Use getter and setter instead of direct attribute access
        current_health = enemy.get_health()
        enemy.set_health(current_health - additional_damage)  # Apply additional damage
        print(f"{self.name} uses a special attack! (+{additional_damage} Damage)")
        # Use the logger if provided for the special attack
        if logger:
            logger.log_combat(self, enemy, additional_damage)
        return total_damage + additional_damage


# ==================== Game Logic ====================
# This section contains the main game logic and flow control

class Game:
    """Manages the game flow and state.
    
    This class orchestrates the entire game experience, from character creation
    to combat and boss battles. It demonstrates composition by containing
    Character and Boss instances.
    
    Attributes:
        player (Optional[Character]): Player character
        bosses (List[Boss]): List of boss enemies
        logger (GameLogger): Combat logger instance
    
    Methods:
        show_intro(): Display game introduction
        setup_game(): Initialize player character
        choose_weapon(): Let player choose a weapon
        get_valid_input(): Get validated user input
        combat(): Handle combat between characters
        display_combat_status(): Show current combat status
        handle_boss_battles(): Manage boss battles
        run(): Start the main game loop
    
    Example:
        >>> game = Game()
        >>> game.run()  # Start the game
    """
    player: Optional[Character] = None
    bosses: List[Boss] = field(default_factory=list)
    logger: GameLogger = field(default_factory=GameLogger)
    
    def show_intro(self) -> None:
        """Display game introduction and set up the game.
        
        This method shows the game's opening screen and prompts the player
        to enter their character name.
        
        Raises:
            ValueError: If player name is empty
        """
        clear_screen()
        print_border()
        print("\nWelcome to the RPG Adventure Game!\n")
        print("You are a brave hero on a quest to defeat powerful bosses.")
        print("Choose your weapon wisely and prepare for battle!\n")
        print_border()
        
        name = input("Enter your character name: ").strip()
        if not name:
            raise ValueError("Character name cannot be empty")
            
        self.setup_game(name)
        press_enter()
    
    def setup_game(self, name: CharacterName) -> None:
        """Initialize player character and game state.
        
        Args:
            name (CharacterName): Player character's name
        """
        self.player = Character(name, 100, 10)
        self.choose_weapon()
        
        # Initialize bosses
        self.bosses = [
            Boss("Goblin", 50, 5),
            Boss("Orc", 75, 8),
            Boss("Dragon", 150, 15)
        ]
    
    def choose_weapon(self) -> None:
        """Let the player choose a weapon for their character.
        
        This method displays available weapons and lets the player select one.
        It validates the selection and equips the chosen weapon.
        
        Raises:
            InvalidWeaponError: If no valid weapon is selected
        """
        clear_screen()
        print_border()
        print("\nChoose your weapon:\n")
        
        for i, weapon_data in enumerate(WEAPONS, 1):
            weapon = Weapon(weapon_data["name"], weapon_data["damage_bonus"])
            print(f"{i}. {weapon}")
        
        print_border()
        
        while True:
            try:
                choice = int(input("\nEnter your choice (1-3): "))
                if 1 <= choice <= len(WEAPONS):
                    selected_weapon = Weapon(
                        WEAPONS[choice - 1]["name"],
                        WEAPONS[choice - 1]["damage_bonus"]
                    )
                    self.player.equip_weapon(selected_weapon)
                    print(f"\nYou have chosen {selected_weapon}!")
                    press_enter()
                    break
                else:
                    print("Invalid choice. Please try again.")
            except ValueError:
                print("Please enter a number between 1 and 3.")
            except Exception as e:
                raise InvalidWeaponError(f"Error selecting weapon: {str(e)}")
    
    def get_valid_input(self, prompt: str, options: List[str], max_attempts: int = 3) -> int:
        """Get valid user input with retry mechanism.
        
        This method ensures that the user provides valid input within a specified
        number of attempts before exiting.
        
        Args:
            prompt (str): Input prompt message
            options (List[str]): Valid input options
            max_attempts (int): Maximum number of attempts before exiting
        
        Returns:
            int: Index of the chosen option
        
        Raises:
            ValueError: If max attempts exceeded
            KeyboardInterrupt: If user interrupts input
        """
        attempts = 0
        while attempts < max_attempts:
            try:
                choice = input(prompt).strip()
                if choice in options:
                    return options.index(choice)
                else:
                    attempts += 1
                    print(f"Invalid choice. Attempts remaining: {max_attempts - attempts}")
            except KeyboardInterrupt:
                print("\nGame interrupted by user.")
                raise SystemExit
            
        raise ValueError("Maximum attempts exceeded")
    
    def combat(self, player: Character, enemy: Character) -> bool:
        """Handle combat between characters.
        
        This method manages the turn-based combat between two characters,
        alternating attacks until one character's health reaches zero.
        
        Args:
            player (Character): Player character
            enemy (Character): Enemy character
        
        Returns:
            bool: True if player wins, False if enemy wins
        
        Raises:
            ValueError: If either player or enemy is None
        """
        if player is None or enemy is None:
            raise ValueError("Both characters must be valid")
            
        while player.is_alive() and enemy.is_alive():
            clear_screen()
            self.display_combat_status(player, enemy)
            
            # Player's turn
            damage = player.attack(enemy, self.logger)
            print(f"\n{player.name} attacks {enemy.name} for {damage} damage!")
            if not enemy.is_alive():
                return True
                
            # Enemy's turn
            damage = enemy.attack(player, self.logger)
            print(f"\n{enemy.name} attacks {player.name} for {damage} damage!")
            if not player.is_alive():
                return False
                
            press_enter()
    
    def display_combat_status(self, player: Character, enemy: Character) -> None:
        """Display current combat status.
        
        Shows the health status of both characters in a formatted way.
        
        Args:
            player (Character): Player character
            enemy (Character): Enemy character
        """
        print_border()
        print(f"\n{player.name}'s Health: {player.get_health()}")
        print(f"{enemy.name}'s Health: {enemy.get_health()}")
        print_border()
    
    def handle_boss_battles(self) -> None:
        """Manage boss battles sequence.
        
        This method handles the progression through all boss battles,
        displaying appropriate messages and managing game state.
        
        Raises:
            GameOverError: If game ends
        """
        if self.player is None:
            raise GameOverError("Player character not initialized")
            
        for boss in self.bosses:
            clear_screen()
            self.introduce_boss(boss)
            press_enter()
            
            if self.combat(self.player, boss):
                self.print_victory_message(boss)
                press_enter()
            else:
                self.print_defeat_message(boss)
                self.end_game(False)
                raise GameOverError("Game over - player defeated")
                
        self.end_game(True)
    
    def introduce_boss(self, boss: Boss) -> None:
        """Introduce a boss character.
        
        Displays the boss's name and prepares the player for battle.
        
        Args:
            boss (Boss): Boss character to introduce
        """
        print_border()
        print(f"\nA wild {boss.name} appears!")
        print(f"Prepare yourself, {self.player.name}!")
        print_border()
    
    def print_victory_message(self, enemy: Character) -> None:
        """Display victory message.
        
        Shows a congratulatory message when the player defeats an enemy.
        
        Args:
            enemy (Character): Defeated enemy character
        """
        print_border()
        print(f"\nVictory! You defeated {enemy.name}!")
        print_border()
    
    def print_defeat_message(self, enemy: Character) -> None:
        """Display defeat message.
        
        Shows a message when the player is defeated by an enemy.
        
        Args:
            enemy (Character): Enemy character
        """
        print_border()
        print(f"\nDefeat! {enemy.name} was too powerful!")
        print_border()
    
    def end_game(self, victory: bool) -> None:
        """End the game with a message.
        
        Displays the final game result and thanks the player.
        
        Args:
            victory (bool): Whether the player won
        """
        clear_screen()
        print_border()
        if victory:
            print("\nCongratulations! You have defeated all bosses!")
            print("You are truly a hero!")
        else:
            print("\nGame Over")
            print("Better luck next time!")
        print_border()
    
    def run(self) -> None:
        """Start the main game loop.
        
        This method orchestrates the entire game flow from start to finish.
        
        Raises:
            GameOverError: If game ends
        """
        try:
            self.show_intro()
            self.handle_boss_battles()
        except GameOverError as e:
            print(f"\n{str(e)}")
        except Exception as e:
            print(f"\nAn unexpected error occurred: {str(e)}")
        finally:
            press_enter()


# ==================== Main Execution ====================

if __name__ == "__main__":
    game = Game()
    game.run()
