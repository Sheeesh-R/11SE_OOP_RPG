"""
Quest system for the RPG game.
"""

from typing import List, Dict, Optional
from dataclasses import dataclass
from constants import GAME_CONFIG

@dataclass
class QuestObjective:
    """Represents a single objective in a quest.
    
    Attributes:
        description (str): Description of the objective
        target (int): Target amount to complete
        current (int): Current progress
        completed (bool): Whether the objective is completed
    """
    description: str
    target: int
    current: int = 0
    completed: bool = False

class Quest:
    """Represents a quest in the game.
    
    Attributes:
        name (str): Name of the quest
        description (str): Description of the quest
        objectives (List[QuestObjective]): List of quest objectives
        rewards (Dict[str, Any]): Quest rewards
        completed (bool): Whether the quest is completed
    """

    def __init__(self, name: str, description: str, objectives: List[Dict], rewards: Dict):
        """Initialize a quest.

        Args:
            name (str): Name of the quest
            description (str): Description of the quest
            objectives (List[Dict]): List of objective dictionaries
            rewards (Dict): Quest rewards
        """
        self.name = name
        self.description = description
        self.objectives = [QuestObjective(**obj) for obj in objectives]
        self.rewards = rewards
        self.completed = False

    def update_objective(self, objective_index: int, amount: int = 1) -> bool:
        """Update progress on a quest objective.

        Args:
            objective_index (int): Index of the objective to update
            amount (int, optional): Amount to increment. Defaults to 1.

        Returns:
            bool: True if objective was updated
        """
        if 0 <= objective_index < len(self.objectives):
            objective = self.objectives[objective_index]
            objective.current += amount
            objective.completed = objective.current >= objective.target
            self.completed = all(obj.completed for obj in self.objectives)
            return True
        return False

    def get_progress(self) -> str:
        """Get the progress string for all objectives.

        Returns:
            str: Progress string
        """
        progress = []
        for obj in self.objectives:
            progress.append(f"{obj.description}: {obj.current}/{obj.target}")
        return "\n".join(progress)

    def complete(self, character: 'Character') -> None:
        """Complete the quest and give rewards.

        Args:
            character (Character): Character completing the quest
        """
        if not self.completed:
            return

        for reward_type, reward_value in self.rewards.items():
            if reward_type == "experience":
                character.gain_experience(reward_value)
            elif reward_type == "gold":
                character.inventory.add_item(Item("Gold", f"{reward_value} gold coins", "GOLD", reward_value))
            elif reward_type == "item":
                character.inventory.add_item(Item(**reward_value))
