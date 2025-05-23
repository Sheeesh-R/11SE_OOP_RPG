"""
Centralized configuration constants for the RPG game.

This module contains all game configuration values, making it easy to modify
settings without searching through multiple files.
"""

# Game Settings
BORDER_LENGTH = 80

# Weapon Constants
WEAPONS = [
    {"name": "Sword", "damage_bonus": 5, "type": "melee", "description": "A sturdy blade"},
    {"name": "Bow", "damage_bonus": 4, "type": "ranged", "description": "A trusty bow"},
    {"name": "Staff", "damage_bonus": 3, "type": "magic", "description": "An enchanted staff"},
    {"name": "Axe", "damage_bonus": 6, "type": "melee", "description": "A heavy axe"},
    {"name": "Dagger", "damage_bonus": 3, "type": "melee", "description": "A quick dagger"},
    {"name": "Crossbow", "damage_bonus": 5, "type": "ranged", "description": "A powerful crossbow"}
]

# Weapon Types
WEAPON_TYPES = {
    "melee": "Melee weapons deal direct damage",
    "ranged": "Ranged weapons attack from a distance",
    "magic": "Magic weapons deal magical damage"
}

# Boss Constants
BOSS_WEAPON_NAME = "Boss Weapon"
BOSS_WEAPON_DAMAGE_BONUS = 5

# Character stats
GOBLIN_KING_NAME = "Goblin King"
GOBLIN_KING_HEALTH = 50
GOBLIN_KING_DAMAGE = 8

DARK_SORCERER_NAME = "Dark Sorcerer"
DARK_SORCERER_HEALTH = 60
DARK_SORCERER_DAMAGE = 9

# Boss stats
BOSS_STATS = {
    "Dragon": {"health": 150, "damage": 15, "type": "dragon"},
    "Ice Dragon": {"health": 175, "damage": 16, "type": "dragon"},
    "Fire Dragon": {"health": 200, "damage": 18, "type": "dragon"}
}

# Player constants
PLAYER_INITIAL_HEALTH = 100
PLAYER_BASE_DAMAGE = 10

# Combat Settings
MAX_COMBAT_ATTEMPTS = 3

# Game Messages
WELCOME_MESSAGE = "\nWelcome to the RPG Adventure Game!\n"
GAME_OVER_MESSAGE = "\nGame Over\n"
VICTORY_MESSAGE = "\nCongratulations! You have defeated all bosses!\n"
DEFEAT_MESSAGE = "\nDefeat! {enemy_name} was too powerful!\n"

# Error Messages
INVALID_INPUT_ERROR = "Invalid input. Please try again."
MAX_ATTEMPTS_ERROR = "Maximum attempts exceeded."
CHARACTER_NAME_ERROR = "Character name cannot be empty"
WEAPON_SELECTION_ERROR = "Error selecting weapon: {error}"
GAME_OVER_ERROR = "Game over - {reason}"
