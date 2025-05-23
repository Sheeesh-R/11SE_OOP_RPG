"""
Unit tests for the Game class.
"""

import unittest
from unittest.mock import patch, MagicMock
from game import Game
from character import Character
from boss import Boss
from villain import Goblin, Orc
from sidekick import Sidekick, DefenderSidekick
from constants import (
    WEAPON_ROCK_NAME,
    WEAPON_ROCK_DAMAGE_BONUS,
    WEAPON_PAPER_NAME,
    WEAPON_PAPER_DAMAGE_BONUS
)

class TestGame(unittest.TestCase):
    """Test suite for the Game class."""

    def setUp(self):
        """Set up test fixtures."""
        self.game = Game()
        self.player = Character("Test", 100, 10)
        self.boss = Boss("Test Boss", 150, 15)
        self.goblin = Goblin()
        self.orc = Orc()
        self.sidekick = DefenderSidekick()

    def test_setup_game(self):
        """Test game setup."""
        with patch('builtins.input', return_value='Test'):
            self.game.setup_game()
            self.assertIsNotNone(self.game.player)
            self.assertEqual(self.game.player.name, "Test")

    def test_choose_weapon(self):
        """Test weapon selection."""
        with patch('builtins.input', return_value='1'):
            self.game.player = Character("Test", 100, 10)
            self.game.choose_weapon()
            self.assertIsNotNone(self.game.player.weapon)
            self.assertEqual(self.game.player.weapon.name, WEAPON_ROCK_NAME)

    def test_choose_sidekick(self):
        """Test sidekick selection."""
        with patch('builtins.input', return_value='1'):
            self.game.player = Character("Test", 100, 10)
            self.game.choose_sidekick()
            self.assertIsNotNone(self.game.sidekick)
            self.assertIsInstance(self.game.sidekick, DefenderSidekick)

    def test_combat(self):
        """Test combat mechanics."""
        self.game.player = Character("Test", 100, 10)
        enemy = Goblin()
        
        # Test combat where player wins
        with patch('builtins.input', return_value='1'):
            result = self.game.combat(self.game.player, enemy)
            self.assertTrue(result)
            self.assertTrue(enemy.get_health() <= 0)

        # Test combat where enemy wins
        enemy = Boss("Test Boss", 200, 20)
        with patch('builtins.input', return_value='1'):
            result = self.game.combat(self.game.player, enemy)
            self.assertFalse(result)
            self.assertTrue(self.game.player.get_health() <= 0)

    def test_handle_battles(self):
        """Test battle progression."""
        self.game.player = Character("Test", 100, 10)
        self.game.villains = [Goblin(), Orc()]
        self.game.bosses = [Boss("Test Boss", 150, 15)]
        
        # Test with sidekick assistance
        self.game.sidekick = DefenderSidekick()
        self.game.sidekick.assist_player(self.game.player)
        
        with patch('builtins.input', return_value='1'):
            result = self.game.handle_battles()
            self.assertTrue(result)

    def test_save_load(self):
        """Test game save and load functionality."""
        from save_system import SaveSystem
        
        # Create save system instance
        save_system = SaveSystem()
        
        # Test save game
        game_state = {
            "player": self.player,
            "bosses": [self.boss],
            "villains": [self.goblin, self.orc],
            "sidekick": self.sidekick
        }
        
        # Save game
        result = save_system.save_game(game_state)
        self.assertTrue(result)
        
        # Load game
        loaded_state = save_system.load_game()
        self.assertIsNotNone(loaded_state)
        
        # Clean up
        save_system.delete_save()
