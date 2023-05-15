"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""
import random


"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    moves = ['rock', 'paper', 'scissors']
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


def beats(one: str, two: str) -> bool:
    """Returns True if one beats two, false if not"""

    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class RandomPlayer(Player):
    def move(self):
        index = random.randint(0,2)
        return self.moves[index]


class HumanPlayer(Player):
    def move(self):
        while True:
            user_input = (input("rock, paper, scissors? > ")).lower()
            if user_input in self.moves:
                return user_input


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        # index represent round. None is Draw, 1,2 represent players who won
        self.round_score = []

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        winner = self.who_won(move1, move2)
        output_text = f"Player 1: {move1}  Player 2: {move2} ----> "
        if winner:
            output_text += f"Player {winner} won"
        else:
            output_text += "Draw!"
        print(output_text)

        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        print("Game start!")
        for round in range(3):
            print(f"Round {round}:")
            self.play_round()
        print("Game over!")

    def who_won(self, move1: str, move2: str):
        "return None for Draw, 1 or 2 if player 1 or 2 won, also save score to "
        if beats(move1, move2):
            self.round_score.append(1)
        elif beats(move2, move1):
            self.round_score.append(2)
        else:
            self.round_score.append(None)

        return self.round_score[-1]



if __name__ == '__main__':
    print(beats("rock", "papaer"))
    game = Game(RandomPlayer(), RandomPlayer())
    game.play_game()