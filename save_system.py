"""
Game save and load system.

This module handles saving and loading game state to/from JSON files.
"""

import json
from typing import Optional, Dict, Any, Type
from pathlib import Path
from datetime import datetime
from constants import (
    WEAPON_ROCK_NAME,
    WEAPON_PAPER_NAME,
    WEAPON_SCISSORS_NAME
)

SAVE_FILE = "save_game.json"


class SaveSystem:
    """Manages game save and load functionality.
    
    This class handles saving and loading game state to/from JSON files.
    It ensures data integrity and provides error handling for save operations.
    
    Attributes:
        save_file (Path): Path to the save file
        
    Methods:
        save_game(): Save current game state
        load_game(): Load saved game state
        delete_save(): Delete the save file
    """
    
    def __init__(self) -> None:
        """Initialize the save system."""
        self.save_file = Path(SAVE_FILE)
        
    def save_game(self, game_state: Dict[str, Any]) -> bool:
        """Save the current game state to a file.
        
        Args:
            game_state (Dict[str, Any]): Dictionary containing game state
        
        Returns:
            bool: True if save was successful, False otherwise
        
        Raises:
            ValueError: If game state is invalid
            IOError: If save file cannot be written
        """
        try:
            # Validate game state
            if not self._validate_game_state(game_state):
                raise ValueError("Invalid game state")
                
            # Add save timestamp
            game_state["save_timestamp"] = datetime.now().isoformat()
            
            # Write to file
            self.save_file.write_text(
                json.dumps(game_state, indent=4),
                encoding="utf-8"
            )
            return True
            
        except ValueError as ve:
            print(f"Error saving game: {str(ve)}")
            return False
        except IOError as ie:
            print(f"Error writing to save file: {str(ie)}")
            return False

    def load_game(self) -> Optional[Dict[str, Any]]:
        """Load the saved game state from file.
        
        Returns:
            Optional[Dict[str, Any]]: Loaded game state or None if load fails
        
        Raises:
            IOError: If save file cannot be read
            ValueError: If saved data is corrupted
        """
        try:
            if not self.save_file.exists():
                print("No save file found")
                return None
                
            # Read and validate save data
            save_data = json.loads(self.save_file.read_text(encoding="utf-8"))
            
            if not self._validate_game_state(save_data):
                raise ValueError("Corrupted save data")
                
            return save_data
            
        except IOError as ie:
            print(f"Error reading save file: {str(ie)}")
            return None
        except ValueError as ve:
            print(f"Error loading game: {str(ve)}")
            return None

    def delete_save(self) -> None:
        """Delete the save file if it exists."""
        if self.save_file.exists():
            self.save_file.unlink()

    def _validate_game_state(self, game_state: Dict[str, Any]) -> bool:
        """Validate the game state dictionary.
        
        Args:
            game_state (Dict[str, Any]): Game state to validate
        
        Returns:
            bool: True if game state is valid, False otherwise
        """
        required_keys = [
            "player", "bosses", "villains", "sidekick",
            "current_boss", "current_villain", "game_config"
        ]
        
        return all(key in game_state for key in required_keys)

    @staticmethod
    def serialize_character(character: Any) -> Dict[str, Any]:
        """Serialize a character object to dictionary.
        
        Args:
            character (Any): Character object to serialize
        
        Returns:
            Dict[str, Any]: Serialized character data
        """
        return {
            "name": character.name,
            "health": character.get_health(),
            "damage": character.damage,
            "weapon": {
                "name": character.weapon.name if character.weapon else None,
                "damage_bonus": character.weapon.damage_bonus if character.weapon else 0
            } if character.weapon else None
        }

    @staticmethod
    def deserialize_character(data: Dict[str, Any], cls: Type) -> Any:
        """Deserialize a dictionary to character object.
        
        Args:
            data (Dict[str, Any]): Character data
            cls (Type): Character class to instantiate
        
        Returns:
            Any: Deserialized character object
        """
        from character import Character
        from weapon import Weapon
        
        character = cls(data["name"], data["health"], data["damage"])
        
        if data["weapon"]:
            weapon = Weapon(data["weapon"]["name"], data["weapon"]["damage_bonus"])
            character.equip_weapon(weapon)
            
        return character
