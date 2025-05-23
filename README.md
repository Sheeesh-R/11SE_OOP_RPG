# RPG Lesson: Object-Oriented Programming 

A Python-based RPG game that demonstrates core OOP principles and design patterns.

## Project Structure

This is a modular implementation demonstrating OOP concepts in Python:

```
rpg_game/
│
├── main.py                   # Entry point
├── utilities.py              # Console operations and game constants
├── weapon.py                 # Weapon class implementation
├── character.py             # Base Character class
├── boss.py                  # Boss class (inherits from Character)
├── villain.py               # Villain class (inherits from Character)
├── sidekick.py              # Sidekick class (inherits from Character)
├── game_logger.py           # Combat logging functionality
├── game.py                  # Main game logic
├── config.py                # Game configuration settings
├── save_system.py           # Game save/load functionality
├── tests/                   # Unit tests directory
│   ├── test_character.py   # Character class tests
│   └── test_game.py        # Game class tests
├── README.md                # Project documentation
├── ROADMAP.md              # Development plans
└── UML_class_diagram.md    # Class structure and relationships
```

The code is organized into logical modules, each with a specific responsibility, making it easier to maintain and extend.

## Getting Started

### Prerequisites
- Python 3.8 or higher
- No additional dependencies required

### Running the Game
1. Ensure Python is installed on your system
2. Open a terminal
3. Navigate to the project directory
4. Run the game:
   ```bash
   python rpg_oop_concepts.py
   ```

## How to Play

1. Enter your character name when prompted
2. Choose a weapon from the available options
3. Fight through a series of boss battles
4. Use your weapon's damage bonus strategically
5. Try to defeat all bosses to win the game

## Key Features

### 1. Character System
- Create and customize your character
- Choose from different weapons with unique damage bonuses
- Track health and damage stats

### 2. Combat System
- Turn-based combat mechanics
- Damage calculation with weapon bonuses
- Combat logging system
- Boss-specific attack patterns

### 3. Game Flow
- Sequential boss battles
- Progress tracking
- Victory and defeat conditions
- Comprehensive logging of combat events

## Code Organization

The code is organized into several logical sections:

### Utility Functions
- Console operations (`clear_screen`, `press_enter`, `print_border`)
- Input validation
- Basic game operations

### Core Classes
- `Weapon`: Represents different weapons with damage bonuses
- `Character`: Base class for game characters
- `Boss`: Specialized enemy characters
- `GameLogger`: Handles combat logging
- `Game`: Manages overall game flow

### Game Logic
- Character initialization
- Weapon selection
- Combat mechanics
- Boss battles
- Game state management

## Usage Examples

### Creating a Weapon
```python
# Create a new weapon
sword = Weapon(name="Sword", damage_bonus=5)
print(sword)  # Output: Sword (+5 Damage)
```

### Creating a Character
```python
# Create a new character
player = Character(
    name="Hero",
    health=100,
    damage=10,
    weapon=sword
)
print(f"{player.name} has {player.get_health()} health")
```

### Combat Example
```python
# Initialize game and start combat
player = Character("Hero", 100, 10)
boss = Boss("Dragon", 150, 15)

# Create a logger instance
game_logger = GameLogger(log_to_console=True)

# Start combat
player.attack(boss, game_logger)
boss.attack(player, game_logger)
```

## Error Handling

The game includes comprehensive error handling for:
- Invalid weapon selection
- Game over conditions
- Input validation
- Combat logging failures

## Contributing

Feel free to submit issues and enhancement requests.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Thanks to all contributors who have helped improve this project
- Special thanks to those who provided feedback on the OOP implementation

## COIPEA: Core OOP Concepts Demonstrated

This code demonstrates all six fundamental Object-Oriented Programming principles (COIPEA):
- **C**lasses and **O**bjects
- **I**nheritance
- **P**olymorphism
- **E**ncapsulation
- **A**bstraction

### 1. Classes and Objects
- The code defines several classes (`GameLogger`, `Weapon`, `Character`, `Boss`, `Game`) that encapsulate data and behavior
- Objects are instantiated from these classes (e.g., player character, bosses, weapons)

### 2. Inheritance
- `Boss` inherits from `Character`, demonstrating class hierarchy
- The `super().__init__()` call in `Boss.__init__` shows proper parent constructor invocation
- Method overriding is shown in `Boss.attack()` which extends the parent's method

### 3. Polymorphism
- Method overriding in `Boss.attack()` demonstrates polymorphism - same method name but different behavior than parent class
- The `attack()` method behaves differently depending on the actual object type (Character vs Boss)
- This allows for treating different object types through a common interface

### 4. Encapsulation
- Each class encapsulates its own data (attributes) and behavior (methods)
- Classes have clear responsibilities and manage their own state
- Objects maintain their internal state and expose functionality through methods
- The `Character` class demonstrates proper encapsulation with:
  - A private `_health` attribute (indicated by the underscore prefix)
  - Public `get_health()` and `set_health()` methods for controlled access
  - Data validation in the setter to ensure health is never negative
  - Consistent use of getters/setters throughout the codebase (e.g., in combat logic)
  - The `Weapon` class is composed within the `Character` class, demonstrating strong composition

### 5. Abstraction
- Classes represent abstract concepts (Character, Weapon, Game) hiding implementation details
- The Game class abstracts away the complexity of game flow management
- Users of the classes only need to understand the interface, not internal workings

### 6. Additional Relationships
- **Composition**: Strong composition between `Character` and `Weapon` (a character "has-a" weapon)
- **Dependency**: `GameLogger` demonstrates a dependency relationship (explicitly mentioned as "dotted line in UML")

## UML Class Diagram Concepts

The code demonstrates several UML class diagram concepts including classes, relationships (inheritance, composition, dependency), and various class members.

For a detailed analysis of UML concepts in this code, see [UML_class_diagram.md](UML_class_diagram.md).

## Design Patterns and Principles

### 1. Single Responsibility Principle
- Each class has a clear, focused purpose
- Utility functions are separated into logical groups (e.g., `clear_screen`, `press_enter` in console utilities)
- The `GameLogger` class handles all logging functionality
- The `Weapon` class focuses solely on weapon properties and behavior

### 2. Game Loop Pattern
- The `Game.run()` method implements a simple game loop

### 3. Factory Method (simplified)
- `choose_weapon()` acts as a factory for creating weapon configurations

## OOP Learning Value

### 1. Clear Demonstration of OOP Concepts
- **Inheritance**: The `Boss` class extends `Character` and overrides the `attack` method
- **Encapsulation**: Private attributes with getters/setters in `Character` class
- **Composition**: `Character` contains a `Weapon` object
- **Dependency**: `Game` depends on `GameLogger` for logging
- **Polymorphism**: Different attack behaviours between `Character` and `Boss`

### 2. Progressive Learning Path
1. Start with basic utility functions
2. Introduce simple classes (`Weapon`)
3. Build more complex classes with relationships (`Character`, `Boss`)
4. Show how classes interact in the `Game` class

### 3. Code Organization
- Clear separation of concerns
- Logical grouping of related functionality
- Consistent naming conventions
- Proper use of Python's module system


## Areas for Improvement

1. **Multiple Classes at Once**
   - The code introduces several classes simultaneously, which might be overwhelming
   - Consider starting with a simpler version and gradually adding complexity

2. **Testing Coverage**
   - Add more comprehensive unit tests
   - Include edge case testing
   - Test error handling scenarios

3. **Additional Features**
   - Implement more weapon types
   - Add character leveling system
   - Include more boss types
   - Add inventory system

4. **Code Optimization**
   - Improve combat algorithms
   - Optimize logging performance
   - Add caching for frequently accessed data

## Version History

See [CHANGELOG.md](CHANGELOG.md) for details on what has changed in each version.

## Support

For support, please:
1. Check the documentation first
2. Search for similar issues
3. Create a new issue if needed
4. Include detailed error messages and steps to reproduce

## Contact

For questions or feedback, please contact:
- Email: your.email@example.com
- GitHub: @yourusername
   - A more step-by-step approach might build one class at a time

2. **Some Advanced Concepts**
   - Static methods (`@staticmethod`) might need additional explanation
   - The distinction between composition and dependency might be subtle for beginners

3. **Limited Visibility Examples**
   - Doesn't demonstrate private/protected attributes with Python's underscore convention
   - Missing encapsulation examples with getters/setters

## Learning Recommendations

### Suggested Learning Approach
1. **Start with the Big Picture**
   - Play the game in action
   - Discuss with a peer the overall architecture and class relationships

2. **Progressive Implementation**
   - Begin with the `Weapon` class (simplest)
   - Move to `Character` class and introduce encapsulation
   - Show inheritance with the `Boss` class
   - Finally, demonstrate the `Game` class that ties everything together

3. **Hands-On**
   - Extend the `Character` class with new abilities
   - Implement a new weapon type with special effects
   - Add a new game mechanic using the existing class structure

4. **Code Review**
   - Walk through the code together with a peer, discussing design decisions
   - Highlight good practices and potential improvements
   - Connect the implementation to the corresponding UML diagram

## Future Enhancements

See [ROADMAP.md](ROADMAP.md) for planned improvements, including:
- Refactoring into a multi-file package structure
- Adding new character types and abilities
- Implementing an inventory system
- Enhancing the combat system

