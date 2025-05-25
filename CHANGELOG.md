# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Core game structure and classes
  - Character class with health, damage, and weapon management
  - Game class managing game flow and state
  - SaveSystem for game persistence
  - Inventory system for character items
  - Quest system with objectives and rewards
  - Weapon system with damage bonuses
  - Combat system with player and enemy interactions
  - Game logger for tracking events
- Main game loop implementation
- Character creation and management
- Boss battle system
- Save/load functionality with multiple save slots
- Basic UI with clear screen and border utilities
- Configuration management system

### Changed
- Improved code organization with separate modules
- Enhanced character combat mechanics
- Added proper type hints and documentation
- Implemented better error handling
- Added save state validation

### Fixed
- Various bug fixes in combat system
- Fixed save file corruption handling
- Fixed inventory management issues
- Fixed character health management

### Security
- Added input validation for save/load operations
- Implemented proper file handling for save files
- Added error handling for corrupted save data

## [2025-05-23]

### Added
- Forked from [Mr-Zamora/11SE_OOP_RPG](https://github.com/Mr-Zamora/11SE_OOP_RPG.git)
- Initial project setup and structure
- Basic README with project information
- CHANGELOG.md for tracking changes

### Changed
- N/A

### Deprecated
- N/A

### Removed
- N/A

### Fixed
- N/A
