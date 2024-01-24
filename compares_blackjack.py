"""Functions to help play and score a game of blackjack.

How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""


def value_of_card(card):
    """Determine the scoring value of a card.

    :param card: str - given card.
    :return: int - value of a given card.  See below for values.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """

    FACES = "JQK"
    
    if card == 'A':
        return 1
    elif card in FACES:
        return 10
    else:
        return int(card) 
    
# print(value_of_card('K'))   # 10
# print(value_of_card('4'))   # 4
# print(value_of_card('A'))   # 1


def higher_card(card_one, card_two):
    """Determine which card has a higher value in the hand.

    :param card_one, card_two: str - cards dealt in hand.  See below for values.
    :return: str or tuple - resulting Tuple contains both cards if they are of equal value.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """

    if value_of_card(card_one) == value_of_card(card_two):
        return (card_one, card_two)
    else:
        return card_one if value_of_card(card_one) > value_of_card(card_two) else card_two

# print(higher_card('K', 'J'))


def value_of_ace(card_one, card_two):
    """Calculate the most advantageous value for the ace card.

    :param card_one, card_two: str - card dealt. See below for values.
    :return: int - either 1 or 11 value of the upcoming ace card.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """

    if 'A' == card_one or 'A' == card_two:
        return 1
    else:
        result = value_of_card(card_one) + value_of_card(card_two)
        # print(f"{sum} (for {value_of_card(card_one)} and {value_of_card(card_two)})")
        return 11 if result + 11 < 22 else 1

# print(value_of_ace('Q', 'A'))       # 1
# print(value_of_ace('6', 'K'))       # 1
# print(value_of_ace('7', '3'))       # 11
# print(value_of_ace('2', '3'))       # 11


def is_blackjack(card_one, card_two):
    """Determine if the hand is a 'natural' or 'blackjack'.

    :param card_one, card_two: str - card dealt. See below for values.
    :return: bool - is the hand is a blackjack (two cards worth 21).

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """

    if (card_one == 'A' and card_two in 'JKQ10') or (card_two == 'A' and card_one in 'JKQ10'):
        return True
    else:
        return False
    
# print(is_blackjack('10', 'A'))      # True
    


def can_split_pairs(card_one, card_two):
    """Determine if a player can split their hand into two hands.

    :param card_one, card_two: str - cards dealt.
    :return: bool - can the hand be split into two pairs? (i.e. cards are of the same value).
    """

    return value_of_card(card_one) == value_of_card(card_two) 


def can_double_down(card_one, card_two):
    """Determine if a blackjack player can place a double down bet.

    :param card_one, card_two: str - first and second cards in hand.
    :return: bool - can the hand can be doubled down? (i.e. totals 9, 10 or 11 points).
    """

    TOTALS = [9, 10, 11]
    return value_of_card(card_one) + value_of_card(card_two) in TOTALS
