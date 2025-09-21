from collections import Counter
import random
from scoring import PokerScore, valid_card_scoring
from rounds import RoundManager

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
discard_pile = []

roundmgr = RoundManager(actual_deck, discard_pile, score)

actual_deck = list(default_deck)


# Starting hand
for _ in range(9):
    hand_state.extend([actual_deck.pop(random.randrange(len(actual_deck)))])

print(f"Remaining cards: {actual_deck}")
print(f"Your hand: {sorted(hand_state)}")
print(f"Starting score threshold is: {roundmgr.score_threshold}")

def check_hand_rank(hand):

    # This looks at the number of the card, not including the suit for hands that don't
    # care what the suit is
    card_numbers = [card[:-1] for card in hand]
    # Similar to card_numbers, except this only looks at the suit for hands that
    # care about the suit
    card_suits = [card[-1] for card in hand]

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
    is_straight = any(sorted(card_numbers, key=lambda card: ORDER.index(card)) == ORDER[i:i+5] for i in range(len(ORDER) - 4))

    # Logic to check for flush
    is_flush = all(suit == card_suits[0] for suit in card_suits)

    # Edge case logic for A2345 straights
    edge_case_straight = all(cards in card_numbers for cards in ["A", "2", "3", "4", "5"])

    # Check for Royal Flush
    if is_straight and is_flush and any(face == "A" for face in card_numbers):
        return score.royal_flush()
    # Check for Straight Flush
    if (is_straight and is_flush) or (edge_case_straight and is_flush):
        return score.straight_flush()
    # Check Four Of A Kind
    if first_card == 4:
        return score.four_of_a_kind()
    # Check Full House
    if first_card == 3 and second_card == 2:
        return score.full_house()
    # Check Flush
    if is_flush:
        return score.flush()
    # Check Straight
    if is_straight or edge_case_straight:
        return score.straight()
    # Check Three Of A Kind
    if first_card == 3 and second_card <= 1:
        return score.three_of_a_kind()
    # Check Two Pair
    if first_card == 2 and second_card == 2:
        return score.two_pair()
    # Check Pair
    if first_card > second_card and first_card == 2:
        return score.pair()
    # Check High Card
    if first_card == 1:
        return score.high_card()
    
def show_status():
    print(f"Remaining cards: {sorted(actual_deck)}")
    print(f"Your hand: {sorted(hand_state)}")
    print(check_hand_rank(play))
    print(f"Total score: {score.value}")
    print(f"Hands remaining: {roundmgr.hands_played}")

# Keeps going until the deck is 0, then the game ends for now. Will add a set number of hand plays for the player to reach a certain score threshold instead
while roundmgr.hands_played > 0:
    user_input = input("Enter 5 cards from hand: ")
    play = user_input.upper().split()
    valid_play = all(card in hand_state for card in play) and len(play) == 5
    if valid_play:
        drawn = [actual_deck.pop(random.randrange(len(actual_deck))) for _ in range(5)]
        hand_state.extend(drawn)
        roundmgr.hands_played -= 1
        for card in play:
            hand_state.remove(card)
    else:
        print(f"Invalid hand")
        print(f"Your hand: {sorted(hand_state)}")
        continue

    show_status()
    if score.value >= roundmgr.score_threshold:
        print("Moving to next round")
        roundmgr.next_round()
        if roundmgr.round_num > 3:
            print("You win!")
            break
    if roundmgr.hands_played == 0:
        print("Better luck next time!")
        break