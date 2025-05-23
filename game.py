"""
Main game module.

This module contains the Game class, which manages the game flow and state.
It coordinates between different game entities and handles user interaction.
"""

from typing import Optional, List, TYPE_CHECKING
from utilities import clear_screen, press_enter, print_border
from character import Character
from boss import Boss
from villain import Goblin, Orc
from sidekick import Sidekick, DefenderSidekick, SupportSidekick
from game_logger import GameLogger
from constants import (
    WELCOME_MESSAGE,
    GAME_OVER_MESSAGE,
    VICTORY_MESSAGE,
    DEFEAT_MESSAGE,
    CHARACTER_NAME_ERROR,
    WEAPON_SELECTION_ERROR,
    GAME_OVER_ERROR,
    MAX_COMBAT_ATTEMPTS
)

if TYPE_CHECKING:
    from character import Character
    from sidekick import Sidekick

class Game:
    """Manages the game flow and state.
    
    This class orchestrates the entire game experience, from character creation
    to combat and boss battles. It demonstrates composition by containing
    Character, Boss, Villain, and Sidekick instances.
    
    Attributes:
        player (Optional[Character]): Player character
        bosses (List[Boss]): List of boss enemies
        villains (List[Villain]): List of regular enemies
        sidekick (Optional[Sidekick]): Player's companion
        logger (GameLogger): Combat logger instance
    """
    player: Optional[Character] = None
    bosses: List[Boss] = []
    villains: List[Villain] = []
    sidekick: Optional[Sidekick] = None
    logger: GameLogger = GameLogger()

    def __init__(self) -> None:
        """Initialize the game instance."""
        self.player = None
        self.bosses = []
        self.villains = []
        self.sidekick = None
        self.logger = GameLogger()

    def show_intro(self) -> None:
        """Display game introduction and set up the game.
        
        This method shows the game's opening screen and prompts the player
        to enter their character name.
        
        Raises:
            ValueError: If player name is empty
        """
        clear_screen()
        print_border()
        print(WELCOME_MESSAGE)
        print("You are a brave hero on a quest to defeat powerful bosses.")
        print("Choose your weapon wisely and prepare for battle!\n")
        print_border()
        
        name = input("Enter your character name: ").strip()
        if not name:
            raise ValueError(CHARACTER_NAME_ERROR)
            
        self.setup_game(name)
        press_enter()

    def setup_game(self, name: str) -> None:
        """Initialize player character and game state.
        
        Args:
            name (str): Player character's name
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
        
        from utilities import WEAPONS
        from weapon import Weapon

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
                raise ValueError(f"Error selecting weapon: {str(e)}")

    def choose_sidekick(self) -> None:
        """Let the player choose a sidekick to assist them.
        
        This method displays available sidekicks and lets the player select one.
        It validates the selection and sets up the sidekick to assist the player.
        
        Raises:
            ValueError: If no valid sidekick is selected
        """
        clear_screen()
        print_border()
        print("\nChoose your sidekick:\n")
        
        sidekicks = [
            ("Shieldbearer", DefenderSidekick),
            ("Healer", SupportSidekick)
        ]

        for i, (name, _) in enumerate(sidekicks, 1):
            print(f"{i}. {name}")
        
        print_border()
        
        while True:
            try:
                choice = int(input("\nEnter your choice (1-2): "))
                if 1 <= choice <= len(sidekicks):
                    sidekick_name, sidekick_class = sidekicks[choice - 1]
                    self.sidekick = sidekick_class(sidekick_name)
                    self.sidekick.assist_player(self.player)
                    print(f"\n{sidekick_name} joins your adventure!")
                    press_enter()
                    break
                else:
                    print("Invalid choice. Please try again.")
            except ValueError:
                print("Please enter a number between 1 and 2.")
            except Exception as e:
                raise ValueError(f"Error selecting sidekick: {str(e)}")

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
        It also handles sidekick assistance if available.
        
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
            
            # Sidekick's turn if available
            if self.sidekick and self.sidekick.is_alive():
                self.sidekick.assist_player(player)
                sidekick_damage = self.sidekick.attack(enemy, self.logger)
                print(f"\n{self.sidekick.name} assists {player.name}!")
                print(f"{self.sidekick.name} attacks {enemy.name} for {sidekick_damage} damage!")
            
            if not enemy.is_alive():
                # Grant experience points for defeating enemy
                exp_gain = enemy.damage * 10  # Base exp based on enemy's damage
                if isinstance(enemy, Boss):
                    exp_gain *= 2  # Double exp for bosses
                player.gain_experience(exp_gain)
                print(f"\n{player.name} gained {exp_gain} experience points!")
                return True
                
            # Enemy's turn
            damage = enemy.attack(player, self.logger)
            print(f"\n{enemy.name} attacks {player.name} for {damage} damage!")
            
            # Sidekick's defensive turn if available
            if self.sidekick and self.sidekick.is_alive():
                if isinstance(self.sidekick, DefenderSidekick):
                    self.sidekick.defend_player()
                elif isinstance(self.sidekick, SupportSidekick):
                    self.sidekick.heal_player()
            
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

    def handle_battles(self) -> None:
        """Manage all battles in the game.
        
        This method handles both regular enemy battles and boss battles,
        displaying appropriate messages and managing game state.
        
        Raises:
            GameOverError: If game ends
        """
        if self.player is None:
            raise ValueError("Player character not initialized")
            
        # Handle regular enemies first
        for enemy in self.villains:
            clear_screen()
            self.introduce_enemy(enemy)
            press_enter()
            
            if self.combat(self.player, enemy):
                self.print_victory_message(enemy)
                press_enter()
            else:
                self.print_defeat_message(enemy)
                self.end_game(False)
                raise ValueError("Game over - player defeated")
        
        # Then handle boss battles
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
                raise ValueError("Game over - player defeated")
                
        self.end_game(True)

    def introduce_enemy(self, enemy: Character) -> None:
        """Introduce a regular enemy character.
        
        Displays the enemy's name and prepares the player for battle.
        
        Args:
            enemy (Character): Enemy character to introduce
        """
        print_border()
        print(f"\nA wild {enemy.name} appears!")
        print(f"Prepare yourself, {self.player.name}!")
        print_border()

    def introduce_boss(self, boss: Boss) -> None:
        """Introduce a boss character with special message.
        
        Displays the boss's name and prepares the player for a challenging battle.
        
        Args:
            boss (Boss): Boss character to introduce
        """
        print_border()
        print(f"\nA powerful {boss.name} appears!")
        print(f"This is a formidable foe, {self.player.name}!")
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
            ValueError: If game ends
        """
        try:
            self.show_intro()
            self.handle_boss_battles()
        except ValueError as e:
            print(f"\n{str(e)}")
        except Exception as e:
            print(f"\nAn unexpected error occurred: {str(e)}")
        finally:
            press_enter()
