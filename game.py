"""
Main game logic and flow.

This module contains the Game class that manages the game flow and state.
"""

from typing import Optional, List
from console_utils import clear_screen, press_enter, print_border
from game_logger import GameLogger
from character import Character
from boss import Boss

class CombatManager:
    """Manages combat interactions between characters.

    This class handles all combat-related logic, including:
    - Turn-based combat system
    - Damage calculation
    - Combat logging
    - Victory/defeat conditions

    Usage Example:
    ```python
    # Create combat manager
    manager = CombatManager()
    
    # Start combat between two characters
    manager.start_combat(player, boss)
    ```
    """

    def __init__(self, logger: GameLogger):
        """Initialize combat manager with logging functionality.

        Args:
            logger (GameLogger): Logger instance for combat events
        """
        self.logger = logger

    def start_combat(self, attacker: Character, defender: Character) -> bool:
        """Start combat between two characters.

        Args:
            attacker (Character): Character initiating combat
            defender (Character): Character defending

        Returns:
            bool: True if attacker wins, False if defender wins
        """
        while True:
            # Attacker's turn
            damage = attacker.attack(defender, self.logger)
            print(f"\n{attacker} attacks {defender} for {damage} damage!")
            
            if defender.health <= 0:
                print(f"\n{attacker} defeated {defender}!")
                return True
                
            # Defender's turn
            damage = defender.attack(attacker, self.logger)
            print(f"\n{defender} attacks {attacker} for {damage} damage!")
            
            if attacker.health <= 0:
                print(f"\n{defender} defeated {attacker}!")
                return False
            
            press_enter()

class GameState:
    """Enum for game states."""
    INITIAL = "initial"
    READY = "ready"
    IN_PROGRESS = "in_progress"
    VICTORY = "victory"
    GAME_OVER = "game_over"

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
        self._state = GameState.INITIAL
        self._player: Optional[Character] = None
        self._bosses: List[Boss] = []
        self._current_boss_index = 0
        self._logger = GameLogger()
        self._combat_manager = CombatManager(self._logger)

    @property
    def state(self) -> str:
        """Get the current game state.

        Returns:
            str: Current game state
        """
        return self._state

    @property
    def player(self) -> Optional[Character]:
        """Get the player character.

        Returns:
            Optional[Character]: The player character or None if not created
        """
        return self._player

    @property
    def bosses(self) -> List[Boss]:
        """Get the list of bosses.

        Returns:
            List[Boss]: List of boss enemies
        """
        return self._bosses

    @property
    def current_boss(self) -> Optional[Boss]:
        """Get the current boss being fought.

        Returns:
            Optional[Boss]: The current boss or None if no boss is active
        """
        if self._current_boss_index < len(self._bosses):
            return self._bosses[self._current_boss_index]
        return None

    def update_state(self, new_state: str) -> None:
        """Update the game state.

        Args:
            new_state (str): New game state to set
        """
        self._state = new_state
        self._logger.log_combat("Game", "State", f"Changed to {new_state}")

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

    def choose_weapon(self) -> tuple[str, int]:
        """Let player choose a weapon.

        Returns:
            tuple[str, int]: Tuple containing weapon name and damage bonus
        """
        weapons = [
            ("Sword", 5),
            ("Axe", 7),
            ("Bow", 4)
        ]
        print("Choose your weapon:")
        for i, (name, _) in enumerate(weapons, 1):
            print(f"{i}. {name}")
        while True:
            try:
                choice = int(input("Enter your choice (1-3): "))
                if 1 <= choice <= len(weapons):
                    return weapons[choice - 1]
                print("Invalid choice. Please try again.")
            except ValueError:
                print("Please enter a number.")

    def handle_boss_battles(self) -> None:
        """Handle all boss battles in sequence.

        This method manages the combat loop for each boss until:
        - All bosses are defeated
        - Player is defeated
        """
        for boss in self.bosses:
            print_border(f"Boss Battle: {boss.name}")
            
            # Start combat with current boss
            if not self.combat_manager.start_combat(self.player, boss):
                print("\nYou have been defeated!")
                break
            
            print(f"\nVictory over {boss.name}!")
            press_enter()

    def run(self) -> None:
        """Start and run the game.

        This method:
        1. Shows game introduction
        2. Handles boss battles
        3. Displays game outcome
        """
        self.show_intro()
        self.handle_boss_battles()
        
        if self.player and self.player.health > 0:
            print("\nCongratulations! You have defeated all the bosses!")
        else:
            print("Game Over. Better luck next time!")
        press_enter()

    @staticmethod
    def test_game_state() -> None:
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

if __name__ == "__main__":
    game = Game()
    game.run()
