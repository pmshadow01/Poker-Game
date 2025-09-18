from collections import Counter
import random
from scoring import PokerScore, valid_card_scoring

score = PokerScore()

# Used to check for straights and straight flush
ORDER = ['A','K','Q','J','10','9','8','7','6','5','4','3','2']

# Default deck state, resembling an actual deck of cards
default_deck = (
'2H', '3H', '4H', '5H', '6H', '7H', '8H', '9H', '10H', 'JH', 'QH', 'KH', 'AH',
'2D', '3D', '4D', '5D', '6D', '7D', '8D', '9D', '10D', 'JD', 'QD', 'KD', 'AD',
'2C', '3C', '4C', '5C', '6C', '7C', '8C', '9C', '10C', 'JC', 'QC', 'KC', 'AC',
'2S', '3S', '4S', '5S', '6S', '7S', '8S', '9S', '10S', 'JS', 'QS', 'KS', 'AS'
)

actual_deck = []
hand_state = []

# At some point, the actual deck players use will not be the same as they started with.
# There needs to be a default deck start state once more features are added.
actual_deck.extend(default_deck)

# Starting hand
for _ in range(9):
    hand_state.extend([actual_deck.pop(random.randrange(len(actual_deck)))])

# Game start sort of
print(f"Remaining cards: {actual_deck}")
print(f"Your hand: {sorted(hand_state)}")

def check_hand_rank(hand_state):

    # Checks for the usual poker hand size, this will be slightly edited later
    if len(hand_state) != 5:
        return "Invalid poker hand"

    # This looks at the number of the card, not including the suit for hands that don't
    # care what the suit is
    card_numbers = [card[:-1] for card in hand_state]
    # Similar to card_numbers, except this only looks at the suit for hands that
    # care about the suit
    card_suits = [card[-1] for card in hand_state]

    # Individual card scoring
    score.add_card_scores(card_numbers, valid_card_scoring)

    # Counts the # of occurences with the card_numbers variable, to check for 
    # non number/suit related hands
    count_check = Counter(card_numbers)
    # Returns a list of tuples that includes: (element, count of element)
    count_hand_check = count_check.most_common(2)

    # Variables pointing to the index references of the above
    first_card = count_hand_check[0][1]
    second_card = count_hand_check[1][1]

    # Logic to check for straight and straight flush
    is_straight = any(
    sorted(card_numbers, key=lambda card: ORDER.index(card)) == ORDER[i:i+5]
    for i in range(len(ORDER) - 4))

    # Logic to check for flush
    is_flush = all(suit == card_suits[0] for suit in card_suits)

    # Edge case logic for A2345 straights
    edge_case_straight = all(cards in card_numbers for cards in ["A", "2", "3", "4", "5"])

    # Check for Royal Flush
    if is_straight and is_flush and any(face == "A" for face in card_numbers):
        return f"This is a royal flush, {score.royal_flush()}"
    # Check for Straight Flush
    if (is_straight and is_flush) or (edge_case_straight and is_flush):
        return f"This is a straight flush, {score.straight_flush()}"
    # Check Four Of A Kind
    if first_card == 4:
        return f"This is a four of a kind, {score.four_of_a_kind()}"
    # Check Full House
    if first_card == 3 and second_card == 2:
        return f"This is a full house, {score.full_house()}"
    # Check Flush
    if is_flush:
        return f"This is a flush, {score.flush()}"
    # Check Straight
    if is_straight or edge_case_straight:
        return f"This is a straight, {score.straight()}"
    # Check Three Of A Kind
    if first_card == 3 and second_card <= 1:
        return f"This is a three of a kind, {score.three_of_a_kind()}"
    # Check Two Pair
    if first_card == 2 and second_card == 2:
        return f"This is a two pair, {score.two_pair()}"
    # Check Pair
    if first_card > second_card and first_card == 2:
        return f"This is a pair, {score.pair()}"
    # Check High Card
    if first_card == 1:
        return f"This is a high card, {score.high_card()}"

# Keeps going until the deck is 0, then the game ends for now. Will add a set number of hand plays for the player to reach a certain score threshold instead
while len(actual_deck) != 0:
    user_input = input("Enter 5 cards from hand: ")
    play = user_input.split()
    valid_hand = all(card in hand_state for card in play)
    if valid_hand:
        drawn = [actual_deck.pop(random.randrange(len(actual_deck))) for _ in range(5)]
        hand_state.extend(drawn)
        for card in play:
            hand_state.remove(card)
    else:
        print(f"Invalid hand")
        print(f"Your hand: {sorted(hand_state)}")
        continue

    print(f"Remaining cards: {sorted(actual_deck)}")
    print(f"Your hand: {sorted(hand_state)}")
    print(check_hand_rank(play))
    print(f"Total score: {score.value}")

# To be added later: instead of return statements on the hand name,
# functions will be imported for actual scoring. Then a round system, then something
# like a card shop to create more hand possibilities such as Flush Five and
# Five Of A Kind, similar to the actual Balatro game.