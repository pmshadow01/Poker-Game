# Scoring for individual cards, will be changed later
valid_card_scoring = {
    "A": 50,
    "K": 35,
    "Q": 30,
    "J": 25,
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

    # Individual card scoring
    def add_card_scores(self, card_numbers, valid_card_scoring):
        for num in card_numbers:
            if num in valid_card_scoring:
                self.value += valid_card_scoring[num]
        return f"total individual card score: {self.value}"

    # Hand rank scoring
    def high_card(self):
        self.value += 10
        return "this hand scored: 10"
    
    def pair(self):
        self.value += 15
        return "this hand scored: 15"

    def two_pair(self):
        self.value += 20
        return "this hand scored: 20"
    
    def three_of_a_kind(self):
        self.value += 30
        return "this hand scored: 30"
    
    def straight(self):
        self.value += 40
        return "this hand scored: 40"
    
    def flush(self):
        self.value += 45
        return "this hand scored: 45"
    
    def full_house(self):
        self.value += 60
        return "this hand scored: 60"
    
    def four_of_a_kind(self):
        self.value += 80
        return "this hand scored: 80"
    
    def straight_flush(self):
        self.value += 100
        return "this hand scored: 100"
    
    def royal_flush(self):
        self.value += 300
        return "this hand scored: 300, nice!!"
        