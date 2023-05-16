import random

class Player:
    moves = ['rock', 'paper', 'scissors']
    def __init__(self):
        self.moves_result = []
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        self.moves_result.append((my_move, their_move))


class RandomPlayer(Player):
    def move(self):
        index = random.randint(0, 2)
        return self.moves[index]


class HumanPlayer(Player):
    def move(self):
        while True:
            user_input = input("rock, paper, scissors? > ").lower()
            if user_input in self.moves:
                return user_input


class ReflectPlayer(Player):
    def move(self):
        """Plays a move of an opponent from a last round"""
        if self.moves_result:
            return self.moves_result[-1][1]
        else:
            index = random.randint(0, 2)
            return self.moves[index]

class CyclePlayer(Player):
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


