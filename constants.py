"""
Centralized constants for the RPG game.

This module contains all configuration values and constants used throughout the game.
Constants are organized by category for better maintainability.
"""

# Game Configuration
GAME_CONFIG = {
    "name": "RPG Adventure",
    "version": "1.0.0",
    "fps": 60,
    "logging": {
        "enabled": True,
        "format": "[{timestamp}] {message}"
    }
}

# Weapon Constants
WEAPONS = {
    "ROCK": {
        "name": "Rock",
        "damage_bonus": 2,
        "description": "A basic weapon made of stone"
    },
    "PAPER": {
        "name": "Paper",
        "damage_bonus": 3,
        "description": "A mysterious weapon made of enchanted paper"
    },
    "SCISSORS": {
        "name": "Scissors",
        "damage_bonus": 4,
        "description": "Sharp and precise cutting tool"
    },
    "SWORD": {
        "name": "Sword",
        "damage_bonus": 5,
        "description": "A classic weapon of the brave"
    },
    "AXE": {
        "name": "Axe",
        "damage_bonus": 7,
        "description": "Heavy weapon for powerful attacks"
    },
    "BOW": {
        "name": "Bow",
        "damage_bonus": 4,
        "description": "Ranged weapon for precision strikes"
    },
    "BOSS_WEAPON": {
        "name": "Boss Weapon",
        "damage_bonus": 5,
        "description": "Special weapon wielded by bosses"
    }
}

# Character Types
CHARACTER_TYPES = {
    "PLAYER": {
        "initial_health": 110,
        "initial_damage": 10,
        "description": "The brave hero of the story"
    },
    "BOSS": {
        "base_health": 50,
        "base_damage": 8,
        "description": "Powerful enemies that must be defeated"
    },
    "SIDEKICK": {
        "base_health": 80,
        "base_damage": 6,
        "description": "Companions that aid the hero"
    },
    "VILLAIN": {
        "base_health": 70,
        "base_damage": 7,
        "description": "Enemies that serve the dark forces"
    }
}

# Boss Constants
BOSSES = {
    "GOBLIN_KING": {
        "name": "Goblin King",
        "health": 50,
        "damage": 8,
        "description": "The tyrant ruler of the goblin horde",
        "weapon": "BOSS_WEAPON"
    },
    "DARK_SORCERER": {
        "name": "Dark Sorcerer",
        "health": 60,
        "damage": 9,
        "description": "Master of dark magic and forbidden arts",
        "weapon": "BOSS_WEAPON"
    }
}

# Combat Constants
COMBAT_CONFIG = {
    "turn_delay": 1.0,  # seconds
    "critical_hit": {
        "chance": 0.15,  # 15% chance
        "multiplier": 2.0
    },
    "status_effects": {
        "poison": {
            "damage_per_turn": 5,
            "duration": 3
        },
        "freeze": {
            "turns_skipped": 1
        }
    }
}

# UI Constants
UI_CONFIG = {
    "border": {
        "char": "=",
        "length": 80
    },
    "colors": {
        "GREEN": "\033[92m",
        "RED": "\033[91m",
        "YELLOW": "\033[93m",
        "BLUE": "\033[94m",
        "RESET": "\033[0m"
    }
}

# Game States
GAME_STATES = {
    "INITIAL": "initial",
    "READY": "ready",
    "IN_PROGRESS": "in_progress",
    "VICTORY": "victory",
    "GAME_OVER": "game_over",
    "PAUSED": "paused"
}

# Inventory System Constants
INVENTORY_CONFIG = {
    "max_slots": 10,
    "item_types": {
        "WEAPON": "Weapon",
        "ARMOR": "Armor",
        "POTION": "Potion",
        "KEY_ITEM": "Key Item"
    },
    "potions": {
        "HEALING": {
            "name": "Healing Potion",
            "heal_amount": 20,
            "description": "Restores health"
        },
        "STRENGTH": {
            "name": "Strength Potion",
            "damage_bonus": 3,
            "duration": 3,
            "description": "Temporarily increases damage"
        }
    }
}

# Leveling System Constants
LEVELING_CONFIG = {
    "base_exp_per_level": 100,
    "exp_multiplier": 1.5,
    "max_level": 20,
    "level_up_bonuses": {
        "health": 10,
        "damage": 2,
        "defense": 1
    }
}

# Sound Effects
SOUND_EFFECTS = {
    "ATTACK": "attack.wav",
    "VICTORY": "victory.wav",
    "DEFEAT": "defeat.wav",
    "LEVEL_UP": "level_up.wav",
    "POTION_USE": "potion_use.wav"
}

# Test Constants
TEST_CONFIG = {
    "player": {
        "name": "Test Hero",
        "health": 100,
        "damage": 10,
        "weapon": "SWORD"
    },
    "weapon": {
        "name": "Test Sword",
        "damage_bonus": 5
    }
}
