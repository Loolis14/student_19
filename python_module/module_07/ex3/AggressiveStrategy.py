class AggressiveStrategy():
    """Prioritizes attacking and dealing damage."""

    def execute_turn(self, hand: list, battlefield: list) -> dict:
        """Returns comprehensive turn execution results."""
        targets = self.prioritize_targets(battlefield)
        mana_turn = 5
        mana_left = 5
        cards_played = []
        hand_to_play = list(hand)

        while mana_left > 0:
            card = min(hand_to_play, key=lambda c: c.cost)
            if card.cost > mana_left:
                break
            mana_left -= card.cost
            cards_played.append(card)
            hand_to_play.remove(card)
        damage = AggressiveStrategy.get_damage(cards_played)
        return {
            'cards_played': [card.name for card in cards_played],
            'mana_used': mana_turn - mana_left,
            'targets_attacked': targets,
            'damage_dealt': damage
        }

    def get_strategy_name(self) -> str:
        """Get strategy name."""
        return self.__class__.__name__

    def prioritize_targets(self, available_targets: list) -> list:
        """Targets enemy creatures and player directly."""
        targets = []
        for target in available_targets:
            if 'Player' in target or 'Creature' in target:
                targets.append(target)
        return targets

    @staticmethod
    def get_damage(cards: list) -> int:
        """Get the damage of the cards on list."""
        damage = 0
        for card in cards:
            if card.__class__.__name__ == "SpellCard":
                damage += int(card.effect_type[1])
            else:
                damage += card.attack
        return damage
