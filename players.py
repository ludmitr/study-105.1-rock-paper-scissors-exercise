"""This module contains different type of players for rps.py"""
import random

class Player:
    """ Base class for players, providing common attributes and methods."""
    moves = ['rock', 'paper', 'scissors']

    def __init__(self):
        self.moves_result = []

    def move(self):
        pass

    def learn(self, my_move, their_move):
        """ Records the moves made by the player and their opponent."""
        self.moves_result.append((my_move, their_move))


class AllRockPlayer(Player):
    """A player class that inherits from the Player
     class and plays always rock move"""
    def move(self):
        return self.moves

class RandomPlayer(Player):
    """A player class that inherits from the
    Player class and plays a random move"""
    def move(self):
        index = random.randint(0, 2)
        return self.moves[index]


class HumanPlayer(Player):
    """A player class that inherits from the Player class and allows the user to input their move."""
    def move(self):
        """Asks a user for input and returns when it right"""
        while True:
            user_input = input("rock, paper, scissors? > ").lower()
            if user_input in self.moves:
                return user_input


class ReflectPlayer(Player):
    """A player class that inherits from the Player class and plays the opponent's last move."""
    def move(self):
        """Plays a move of an opponent from a last round"""
        if self.moves_result:
            return self.moves_result[-1][1]
        else:
            index = random.randint(0, 2)
            return self.moves[index]


class CyclePlayer(Player):
    """A player class that inherits from the Player class
     and plays a move different from the opponent's last move."""
    def move(self):
        """Plays a move that is different from a last round opponent"""
        if self.moves_result:
            opponent_last_move = self.moves_result[-1][1]
            moves_to_make = [move for move in self.moves if move != opponent_last_move]
            index = random.randint(0, 1)
            return moves_to_make[index]
        else:
            index = random.randint(0, 2)
            return self.moves[index]


