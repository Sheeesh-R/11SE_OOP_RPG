"""
Entry point for the RPG game.

This module contains the main entry point for the game, demonstrating
minimal code in the main module as per Python best practices.
"""

from game import Game

def main() -> None:
    """Main entry point for the game.

    Creates a new game instance and starts the game loop.
    """
    game = Game()
    game.run()

if __name__ == "__main__":
    main()
