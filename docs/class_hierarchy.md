# RPG Game Class Hierarchy

## Character Classes

### Base Classes

```python
class Character:
    """Base class for all characters in the game.
    
    Attributes:
        name (str): Character's name
        health (int): Current health points
        max_health (int): Maximum health points
        damage (int): Base damage
        level (int): Current level
        experience (int): Current experience points
        inventory (Inventory): Character's inventory
        equipped_weapon (Optional[Item]): Currently equipped weapon
    """
```

### Player Character

```python
class Player(Character):
    """Main player character class.
    
    Attributes:
        sidekick (Optional[Sidekick]): Companion character
        quest_log (List[Quest]): Current quests
    """
```

### Sidekick Classes

```python
class Sidekick(Character):
    """Base class for player companions.
    
    Attributes:
        loyalty (int): Loyalty level to player
        special_ability (Callable): Unique ability
    """

# Specialized Sidekick Classes
class DefenderSidekick(Sidekick):
    """Sidekick focused on defense.
    
    Special Ability: Shield Bash
    """

class HealerSidekick(Sidekick):
    """Sidekick focused on healing.
    
    Special Ability: Healing Light
    """
```

### Villain Classes

```python
class Villain(Character):
    """Base class for villain characters.
    
    Attributes:
        evil_level (int): Measure of villainy
        dark_powers (List[str]): Special abilities
    """

# Regular Enemies
class Goblin(Villain):
    """Basic goblin enemy.
    
    Special Ability: Goblin Rush
    """

class Orc(Villain):
    """Strong orc enemy.
    
    Special Ability: Brutal Strike
    """
```

### Boss Classes

```python
class Boss(Character):
    """Base class for boss enemies.
    
    Attributes:
        boss_level (int): Boss difficulty level
        special_attacks (List[str]): Unique attacks
    """

# Special Boss Types
class FireBoss(Boss):
    """Fire-based boss enemy.
    
    Special Ability: Inferno Blast
    """

class IceBoss(Boss):
    """Ice-based boss enemy.
    
    Special Ability: Frost Nova
    """
```

## Item Classes

```python
class Item:
    """Base class for all items.
    
    Attributes:
        name (str): Item name
        description (str): Item description
        item_type (str): Type of item
        value (int): Item value
    """

# Weapon Types
class Weapon(Item):
    """Base class for weapons.
    
    Attributes:
        damage_bonus (int): Additional damage
    """

class Rock(Weapon):
    """Rock weapon.
    
    Special Behavior: Can break shields
    """

class Paper(Weapon):
    """Paper weapon.
    
    Special Behavior: Can wrap around enemies
    """

class Scissors(Weapon):
    """Scissors weapon.
    
    Special Behavior: Can cut through armor
    """
```

## Usage Examples

```python
# Creating a player with sidekick
player = Player("Hero", 100, 10)
sidekick = DefenderSidekick("Robin", 60, 5)
sidekick.weapon = Weapon("Shield", 3)
player.sidekick = sidekick

# Creating specialized weapons
rock = Rock("Rock", 2)
paper = Paper("Paper", 3)
scissors = Scissors("Scissors", 4)

# Creating boss enemies
fire_boss = FireBoss("Inferno King", 200, 20)
ice_boss = IceBoss("Frost Lord", 180, 18)
```

## Design Decisions

1. **Inheritance Structure**
   - Used inheritance to create specialized character types
   - Base classes provide common functionality
   - Subclasses add specific behaviors and attributes

2. **Polymorphism**
   - Weapons use polymorphism for different behaviors
   - Characters have different attack patterns
   - Bosses have unique special abilities

3. **Encapsulation**
   - Protected character attributes
   - Controlled access through methods
   - Hidden implementation details

4. **Abstraction**
   - Base classes define common interfaces
   - Derived classes implement specific behaviors
   - Clear separation of concerns
