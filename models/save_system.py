"""
Game save/load system.

This module handles saving and loading game state.
"""

import json
from typing import Dict, Any
from pathlib import Path
from datetime import datetime

class SaveSystem:
    """Game save/load system.

    Attributes:
        save_dir (Path): Directory for save files
        current_save: Current save data
    """

    def __init__(self, save_dir: str = "saves"):
        """Initialize the save system.

        Args:
            save_dir (str, optional): Directory for save files. Defaults to "saves".
        """
        self.save_dir = Path(save_dir)
        self.current_save: Dict[str, Any] = {}
        self._ensure_save_dir()

    def _ensure_save_dir(self) -> None:
        """Ensure save directory exists."""
        self.save_dir.mkdir(exist_ok=True)

    def _get_save_path(self, slot: int = 1) -> Path:
        """Get path for a save slot.

        Args:
            slot (int, optional): Save slot number. Defaults to 1.

        Returns:
            Path: Path to save file
        """
        return self.save_dir / f"save_{slot}.json"

    def save_game(self, game_state: Dict[str, Any], slot: int = 1) -> bool:
        """Save game state to a slot.

        Args:
            game_state (Dict[str, Any]): Game state to save
            slot (int, optional): Save slot number. Defaults to 1.

        Returns:
            bool: True if save was successful
        """
        try:
            save_path = self._get_save_path(slot)
            game_state["save_time"] = datetime.now().isoformat()
            with open(save_path, 'w') as f:
                json.dump(game_state, f, indent=4)
            return True
        except Exception as e:
            print(f"Error saving game: {e}")
            return False

    def load_game(self, slot: int = 1) -> Dict[str, Any]:
        """Load game state from a slot.

        Args:
            slot (int, optional): Save slot number. Defaults to 1.

        Returns:
            Dict[str, Any]: Loaded game state
        """
        try:
            save_path = self._get_save_path(slot)
            if save_path.exists():
                with open(save_path, 'r') as f:
                    return json.load(f)
            return {}
        except Exception as e:
            print(f"Error loading game: {e}")
            return {}

    def get_save_slots(self) -> Dict[int, Dict[str, Any]]:
        """Get information about all save slots.

        Returns:
            Dict[int, Dict[str, Any]]: Save slot information
        """
        slots = {}
        for i in range(1, 4):  # Assuming 3 save slots
            save_path = self._get_save_path(i)
            if save_path.exists():
                try:
                    with open(save_path, 'r') as f:
                        save_data = json.load(f)
                        slots[i] = {
                            "last_save": save_data.get("save_time", "Unknown"),
                            "player_name": save_data.get("player_name", "Unknown"),
                            "level": save_data.get("player_level", 1)
                        }
                except:
                    slots[i] = {"error": "Corrupted save"}
            else:
                slots[i] = {"empty": True}
        return slots
