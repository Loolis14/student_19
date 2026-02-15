class AggressiveStrategy():
    """Prioritizes attacking and dealing damage."""
    """Prioritizes attacking and dealing damage
• Plays low-cost creatures first for board presence
• Targets enemy creatures and player directly
• Returns comprehensive turn execution results"""

    def execute_turn(self, hand: list, battlefield: list) -> dict:
        
        ['Goblin Warrior'
,
'Lightning Bolt'],

    def get_strategy_name(self) -> str:
        """Get strategy name."""
        return self.__class__.__name__

    def prioritize_targets(self, available_targets: list) -> list:
        pass
