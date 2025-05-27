# RPG Project Guidelines

This document provides simple, clear rules for our RPG game project. These guidelines help keep our code clean and easy to understand.

## Language and Style

- Use **Australian/British English** spelling throughout all documentation and code comments:
  - colour (not color)
  - behaviour (not behavior)
  - organise (not organize)
  - centre (not center)
  - licence (noun), license (verb)
  - practise (verb), practice (noun)
  - customise (not customize)
  - analyse (not analyze)
  - defence (not defense)
  - initialise (not initialize)

## Related Documentation

For more information, refer to:
- [README.md](README.md) - Project overview and setup instructions
- [CHANGELOG.md](CHANGELOG.md) - Version history and changes
- [ROADMAP.md](ROADMAP.md) - Future development plans
- [UML_class_diagram.md](UML_class_diagram.md) - Class structure and relationships

## 1. Writing Good Code

### Keep It Simple
- Write code that's easy to read and understand
- Break big tasks into small, focused functions (try to keep functions under 30 lines)
- Use clear, descriptive names for variables and functions
  - Good: `player_health`, `calculate_damage()`
  - Bad: `x`, `foo()`, `temp`

### Code Style
- Follow basic [PEP 8](https://www.python.org/dev/peps/pep-0008/) guidelines:
  - Use 4 spaces for indentation (not tabs)
  - Put spaces around operators (`x = 5 + 3`, not `x=5+3`)
  - Use lowercase with underscores for variable and function names (`player_name`, not `PlayerName` or `playername`)

### Comments
- Write comments to explain "why" not "what"
  ```python
  # Bad (explains what the code does - this is obvious)
  x = x + 1  # Add 1 to x
  
  # Good (explains why we're doing this)
  x = x + 1  # Compensate for zero-based indexing
  ```
- Keep comments up-to-date with the code

## 2. File Organization

### Simple Structure for Educational Projects
- Keep the project structure simple and straightforward
- Use a modular approach with separate files for different classes/components
- Avoid complex package structures, setup files, or installation requirements
- Focus on readability and ease of understanding over technical sophistication

### File Organization Guidelines
- Group related files in logical directories (e.g., `utils` for utility functions)
- Use clear, descriptive filenames that indicate their purpose
- Keep files focused on a single responsibility
- Use comments to explain file purpose at the top of each file

## 3. Git Basics

### Commits
- Write clear, short commit messages (50 chars or less)
- Start with a verb in present tense:
  - "Add player movement"
  - "Fix combat damage calculation"
  - "Update README with controls"

### Branching
- Create a new branch for each feature/fix:
  ```
  git checkout -b feature/player-jump
  git checkout -b fix/combat-bug
  ```

## 4. Documentation

### Code Documentation
- Write docstrings for all functions and classes:
  ```python
  def calculate_damage(attacker, defender):
      """
      Calculate damage dealt from attacker to defender.
      
      Args:
          attacker: The attacking character
          defender: The defending character
          
      Returns:
          int: The amount of damage dealt
      """
      # Function code here
  ```

### Project Documentation
- Keep `README.md` updated with:
  - How to install and run the game
  - Basic controls and gameplay
  - How to contribute
- Update `CHANGELOG.md` when making changes

## 5. Making Changes

1. Check for existing issues or create a new one
2. Create a new branch for your changes
3. Make small, focused changes
4. Test your changes
5. Submit a pull request with a clear description

## Remember

- Don't overcomplicate things
- Ask questions if you're unsure


---
Last Updated: 2025-05-23
