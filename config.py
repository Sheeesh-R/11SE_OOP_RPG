"""
Game configuration management.

This module handles loading and saving game configuration.
"""

import json
from typing import Dict, Any
from pathlib import Path

class Config:
    """Game configuration manager.

    Attributes:
        config_path (Path): Path to the config file
        config_data (Dict[str, Any]): Configuration data
    """

    def __init__(self, config_path: str = "config.json"):
        """Initialize the config manager.

        Args:
            config_path (str, optional): Path to config file. Defaults to "config.json".
        """
        self.config_path = Path(config_path)
        self.config_data = self._load_config()

    def _load_config(self) -> Dict[str, Any]:
        """Load configuration from file.

        Returns:
            Dict[str, Any]: Configuration data
        """
        try:
            if self.config_path.exists():
                with open(self.config_path, 'r') as f:
                    return json.load(f)
            return self._get_default_config()
        except Exception as e:
            print(f"Error loading config: {e}")
            return self._get_default_config()

    def _get_default_config(self) -> Dict[str, Any]:
        """Get default configuration.

        Returns:
            Dict[str, Any]: Default configuration
        """
        return {
            "game": {
                "version": "1.0.0",
                "fps": 60,
                "logging": {
                    "enabled": True,
                    "level": "INFO"
                }
            },
            "audio": {
                "volume": 0.5,
                "music_volume": 0.3
            },
            "graphics": {
                "resolution": "1920x1080",
                "fullscreen": False
            },
            "controls": {
                "move_up": "W",
                "move_down": "S",
                "move_left": "A",
                "move_right": "D"
            }
        }

    def save_config(self) -> None:
        """Save configuration to file."""
        try:
            with open(self.config_path, 'w') as f:
                json.dump(self.config_data, f, indent=4)
        except Exception as e:
            print(f"Error saving config: {e}")

    def get(self, key: str, default: Any = None) -> Any:
        """Get a configuration value.

        Args:
            key (str): Configuration key
            default (Any, optional): Default value. Defaults to None.

        Returns:
            Any: Configuration value
        """
        return self.config_data.get(key, default)

    def set(self, key: str, value: Any) -> None:
        """Set a configuration value.

        Args:
            key (str): Configuration key
            value (Any): Value to set
        """
        self.config_data[key] = value
        self.save_config()
