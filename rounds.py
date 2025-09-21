class RoundManager:
    def __init__(self, actual_deck, hand_state, discard_pile, score, hands_per_round=5, start_threshold=100, threshold_step=200):
        self.actual_deck = actual_deck
        self.discard_pile = discard_pile
        self.hand_state = hand_state
        self.score = score

        self.hands_per_round = hands_per_round
        self.score_threshold = start_threshold
        self.threshold_step = threshold_step
        self.round_num = 1
        self.hands_played = hands_per_round

    def next_round(self):
        # Reset hands played
        self.hands_played = self.hands_per_round

        # Return discard pile to the deck
        self.actual_deck.extend(self.discard_pile)
        self.discard_pile.clear()

        # Increment round and threshold
        self.round_num += 1
        self.score_threshold += self.threshold_step

        # Reset score
        self.score.value = 0

        # Print status at start of new round
        print(f"--- Round {self.round_num} ---")
        print(f"Remaining cards: {sorted(self.actual_deck)}")
        print(f"Score threshold is now: {self.score_threshold}")
        print(f"Your hand: {sorted(self.hand_state)}")
