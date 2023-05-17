"""This module contains different type of players for rps.py"""
import random


class Player:
    """ Base class for players, providing common attributes and methods."""
    moves = ['rock', 'paper', 'scissors']

    def __init__(self):
        self.moves_result = []
        self.my_score = 0

    def update_score(self, points_won=1):
        """Updates personal score of a player"""
        self.my_score += points_won

    def move(self):
        """Making a move, depending on the children"""
        pass

    def learn(self, my_move, their_move):
        """ Records the moves made by the player and their opponent."""
        pass


class AllRockPlayer(Player):
    """A player class that inherits from the Player
     class and plays always rock move"""
    def move(self):
        """Returns always rock"""
        rock: str = self.moves[0]
        return rock


class RandomPlayer(Player):
    """A player class that inherits from the
    Player class and plays a random move"""
    def move(self) -> str:
        """Returns a random move"""
        index = random.randint(0, len(self.moves)-1)
        random_move = self.moves[index]
        return random_move


class HumanPlayer(Player):
    """A player class that inherits from the Player class
    and allows the user to input their move."""
    def move(self) -> str:
        """Asks a user for input and returns when it right"""
        while True:
            user_input_move = input("rock, paper or scissors? > ").lower()
            if user_input_move in self.moves:
                return user_input_move
            print(f"The move {user_input_move} is invalid. Try again!")


class ReflectPlayer(Player):
    """A player class that inherits from the Player class
    and plays the opponent's last move."""
    def move(self) -> str:
        """Plays a move of an opponent from a last round"""
        if self.moves_result:
            return self.moves_result[-1][1]
        else:
            index = random.randint(0, len(self.moves)-1)
            return self.moves[index]

    def learn(self, my_move, their_move):
        """ Records the moves made by the player and their opponent."""
        self.moves_result.append((my_move, their_move))


class CyclePlayer(Player):
    """A player class that inherits from the Player class
     and cycles through the different moves in order"""
    def move(self):
        """Plays a move that is different from a last round opponent"""
        if self.moves_result:
            my_last_move: str = self.moves_result[-1][0]
            my_last_move_index = self.moves.index(my_last_move)
            my_next_move_index = (my_last_move_index + 1) % len(self.moves)

            return self.moves[my_next_move_index]
        else:
            index = random.randint(0, len(self.moves)-1)
            return self.moves[index]

    def learn(self, my_move, their_move):
        """ Records the moves made by the player and their opponent."""
        self.moves_result.append((my_move, their_move))
