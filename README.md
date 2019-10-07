# Command Line based BlackJack game

## Runtime Instructions

To run the code, follow these steps:

1. `cd` into the blackjack-game repository on your local machine.
2. Install the game package:

   `pip install -e .`

   Now you should be able to run the game routine on the command line using the appropriate keyword.

   To start playing the game, navigate to the project directory and enter `game` in the terminal.

## Design and Tools used:

The code for this game is written entirely in Python. No external libraries were used.

The code was divided into different classes. These were used for representing a card, a deck of cards, a hand of cards, and the overall game flow. These helper classes are in a different subfolder to further compartmentalize the code.

I organized the code as a package. The player can install the package (using the above instructions), and need only type `game` to play the game. This makes it a bit more user friendly than having to run python on a particular file to run the game.
