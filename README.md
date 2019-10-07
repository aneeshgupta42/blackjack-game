# Command Line based Blackjack game

## Runtime Instructions

To run the code, follow these steps:

1. `cd` into the blackjack-game repository on your local machine.
2. To install the game package, enter:

   `pip install -e .`

   Now you should be able to run the game routine on the command line using the appropriate keyword.

   To start playing the game, navigate to the project directory and enter `game` in the terminal.

   The game is a standard, single-player game of blackjack. The player's hand is known to them. The dealer's hand is not. At each turn, the player chooses to either hit or stick, till either the player or the dealer has blackjack.

## Design and Tools used:

The code for this game is written entirely in Python3. No external libraries were used.

The code was divided into different classes. These were used for representing a card, a deck of cards, a player's hand of cards, and the overall game flow. Helper classes are in a different subfolder to further compartmentalize the code.

I organized the code as a package. The player can install the package (using the above instructions), and need only type `game` to play the game. This makes it a bit more user friendly than having to run python on a particular file to run the game.

Disclaimer: This code adapts some parts of itself from a blackjack game I had to write as part of a computer science tutorial class.

Made by: Aneesh Gupta. aneesh[dot]gupta[at]duke[dot]edu
