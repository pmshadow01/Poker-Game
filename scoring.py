# Scoring is communicated a little vaguely right now but is still 100% correct internally. Please don't mind the mess.
valid_card_scoring = {
    "A": 30,
    "K": 25,
    "Q": 20,
    "J": 15,
    "10": 10,
    "9": 9,
    "8": 8,
    "7": 7,
    "6": 6,
    "5": 5,
    "4": 4,
    "3": 3,
    "2": 2,
}

# Class to store all hand rank and individual card scoring
class PokerScore:
    def __init__(self, value = 0):
        self.value = value

    # Individual card scoring(This needs to be changed at some point, the return value doesn't do anything right now. The rest of the function is still relevant.)
    def add_card_scores(self, card_numbers, valid_card_scoring):
        for num in card_numbers:
            if num in valid_card_scoring:
                self.value += valid_card_scoring[num]
        return f"total individual card score: {self.value}"

    # Hand rank scoring
    def high_card(self):
        self.value += 50
        return f"This is a high card."
    
    def pair(self):
        self.value += 60
        return f"This is a pair."

    def two_pair(self):
        self.value += 70
        return f"This is a two pair."
    
    def three_of_a_kind(self):
        self.value += 90
        return f"This is a three of a kind."
    
    def straight(self):
        self.value += 110
        return f"This is a straight."
    
    def flush(self):
        self.value += 125
        return f"This is a flush."
    
    def full_house(self):
        self.value += 175
        return f"This is a full house."
    
    def four_of_a_kind(self):
        self.value += 200
        return f"This is a four of a kind."
    
    def straight_flush(self):
        self.value += 250
        return f"This is a straight flush."
    
    def royal_flush(self):
        self.value += 500
        return f"This is a royal flush! Congrats!!"
        