"""
Unit tests for the Character class.
"""

import unittest
from character import Character
from weapon import Weapon
from constants import (
    WEAPON_ROCK_NAME,
    WEAPON_ROCK_DAMAGE_BONUS,
    WEAPON_PAPER_NAME,
    WEAPON_PAPER_DAMAGE_BONUS
)

class TestCharacter(unittest.TestCase):
    """Test suite for the Character class."""

    def setUp(self):
        """Set up test fixtures."""
        self.character = Character("Test", 100, 10)
        self.weapon = Weapon(WEAPON_ROCK_NAME, WEAPON_ROCK_DAMAGE_BONUS)

    def test_initialization(self):
        """Test character initialization."""
        self.assertEqual(self.character.name, "Test")
        self.assertEqual(self.character.get_health(), 100)
        self.assertEqual(self.character.damage, 10)
        self.assertIsNone(self.character.weapon)

    def test_equip_weapon(self):
        """Test equipping a weapon."""
        self.character.equip_weapon(self.weapon)
        self.assertIsNotNone(self.character.weapon)
        self.assertEqual(self.character.weapon.name, WEAPON_ROCK_NAME)
        self.assertEqual(self.character.weapon.damage_bonus, WEAPON_ROCK_DAMAGE_BONUS)

    def test_attack(self):
        """Test character attack."""
        target = Character("Target", 100, 10)
        
        # Test attack without weapon
        damage = self.character.attack(target)
        self.assertEqual(damage, 10)
        self.assertEqual(target.get_health(), 90)
        
        # Test attack with weapon
        self.character.equip_weapon(self.weapon)
        damage = self.character.attack(target)
        self.assertEqual(damage, 10 + WEAPON_ROCK_DAMAGE_BONUS)
        self.assertEqual(target.get_health(), 90 - (10 + WEAPON_ROCK_DAMAGE_BONUS))

    def test_health_validation(self):
        """Test health validation."""
        with self.assertRaises(ValueError):
            self.character.set_health(-10)
        
        self.character.set_health(0)
        self.assertEqual(self.character.get_health(), 0)

    def test_is_alive(self):
        """Test is_alive method."""
        self.assertTrue(self.character.is_alive())
        self.character.set_health(0)
        self.assertFalse(self.character.is_alive())

    def test_string_representation(self):
        """Test string representation."""
        self.assertEqual(str(self.character), "Test (Health: 100)")
        self.character.equip_weapon(self.weapon)
        self.assertEqual(str(self.character), f"Test (Health: 100) with {self.weapon}")
