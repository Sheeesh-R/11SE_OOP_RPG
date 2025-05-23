"""
Game configuration settings.

This module contains all configurable settings for the RPG game, including
combat mechanics, game rules, and difficulty settings.
"""

from typing import Dict, List, TypedDict
from constants import (
    WEAPON_ROCK_NAME,
    WEAPON_ROCK_DAMAGE_BONUS,
    WEAPON_PAPER_NAME,
    WEAPON_PAPER_DAMAGE_BONUS,
    WEAPON_SCISSORS_NAME,
    WEAPON_SCISSORS_DAMAGE_BONUS
)

class CombatConfig(TypedDict):
    """Configuration for combat mechanics."""
    critical_hit_chance: float
    critical_hit_multiplier: float
    berserk_chance: float
    berserk_multiplier: float
    coordinated_attack_chance: float
    coordinated_attack_multiplier: float

class GameConfig(TypedDict):
    """Configuration for game settings."""
    max_health: int
    base_damage: int
    health_recovery: int
    difficulty: str
    combat: CombatConfig

# Combat configuration
COMBAT_CONFIG: CombatConfig = {
    "critical_hit_chance": 0.2,  # 20% chance for critical hits
    "critical_hit_multiplier": 1.5,  # 50% extra damage
    "berserk_chance": 0.1,  # 10% chance for berserk attacks
    "berserk_multiplier": 2.0,  # Double damage
    "coordinated_attack_chance": 0.3,  # 30% chance for coordinated attacks
    "coordinated_attack_multiplier": 1.5  # 50% extra damage
}

# Game configuration
GAME_CONFIG: GameConfig = {
    "max_health": 100,
    "base_damage": 10,
    "health_recovery": 10,
    "difficulty": "normal",
    "combat": COMBAT_CONFIG
}

# Weapon configurations
WEAPONS_CONFIG: List[Dict[str, Any]] = [
    {"name": WEAPON_ROCK_NAME, "damage_bonus": WEAPON_ROCK_DAMAGE_BONUS, "type": "rock"},
    {"name": WEAPON_PAPER_NAME, "damage_bonus": WEAPON_PAPER_DAMAGE_BONUS, "type": "paper"},
    {"name": WEAPON_SCISSORS_NAME, "damage_bonus": WEAPON_SCISSORS_DAMAGE_BONUS, "type": "scissors"}
]

# Boss configurations
BOSS_CONFIGS: List[Dict[str, Any]] = [
    {"name": "Dragon", "health": 150, "damage": 15, "type": "dragon"},
    {"name": "Ice Dragon", "health": 175, "damage": 16, "type": "dragon"},
    {"name": "Fire Dragon", "health": 200, "damage": 18, "type": "dragon"}
]

# Villain configurations
VILLAIN_CONFIGS: List[Dict[str, Any]] = [
    {"name": "Goblin", "health": 50, "damage": 5, "type": "goblin"},
    {"name": "Orc", "health": 75, "damage": 8, "type": "orc"},
    {"name": "Goblin King", "health": 60, "damage": 6, "type": "goblin"}
]

# Sidekick configurations
SIDEKICK_CONFIGS: List[Dict[str, Any]] = [
    {"name": "Shieldbearer", "health": 80, "damage": 3, "type": "defender"},
    {"name": "Healer", "health": 50, "damage": 2, "type": "support"}
]

# Game rules
GAME_RULES: Dict[str, Any] = {
    "win_conditions": {
        "all_bosses_defeated": True,
        "player_alive": True
    },
    "lose_conditions": {
        "player_dead": True,
        "boss_alive": True
    },
    "combat_turns": {
        "player_first": True,
        "sidekick_second": True,
        "enemy_third": True
    }
}

# Difficulty settings
DIFFICULTY_SETTINGS: Dict[str, Dict[str, Any]] = {
    "easy": {
        "enemy_health_multiplier": 0.8,
        "enemy_damage_multiplier": 0.8,
        "player_health_multiplier": 1.2,
        "player_damage_multiplier": 1.2
    },
    "normal": {
        "enemy_health_multiplier": 1.0,
        "enemy_damage_multiplier": 1.0,
        "player_health_multiplier": 1.0,
        "player_damage_multiplier": 1.0
    },
    "hard": {
        "enemy_health_multiplier": 1.2,
        "enemy_damage_multiplier": 1.2,
        "player_health_multiplier": 0.8,
        "player_damage_multiplier": 0.8
    }
}
