import random

#'Value' of 'Suite'
class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return " of ".join((self.value, self.suit))

class Deck:
    def __init__(self):
        suits = ["Spades", "Hearts", "Clubs", "Diamonds"]
        values = ["A", "2", "3", "4", "5", "6",
        "7", "8", "9", "10", "J", "Q", "K"]

        self.cards = [Card(s, v) for s in suits for v in values]

    def shuffle(self):
        if len(self.cards) > 1:
            random.shuffle(self.cards)

    def deal(self):
        if len(self.cards) > 1:
            return self.cards.pop(0)
