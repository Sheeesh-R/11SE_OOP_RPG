"""
Main entry point for the RPG game.

This module serves as the clean entry point for the game, demonstrating minimal
code in the main module and proper module organization.
"""

from game import Game


def main() -> None:
    """Main function to start the game."""
    game = Game()
    game.run()


if __name__ == "__main__":
    main()
