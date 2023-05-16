"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""
import players


def main():
    """Entry point of the program."""
    game = Game(players.HumanPlayer(), players.CyclePlayer())
    game.play_game()


def beats(one: str, two: str) -> bool:
    """
    Determines if one move beats another move in Rock, Paper, Scissors.

    Args:
        one: Move of player one.
        two: Move of player two.

    Returns:
        True if player one's move beats player two's move, False otherwise.
    """

    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
    """ Represents a game of Rock, Paper, Scissors between two players."""

    def __init__(self, p1: players.Player, p2: players.Player):
        self.p1 = p1
        self.p2 = p2
        # index represent round. None is Draw, 1,2 represent players who won
        self.round_score = []

    def play_round(self) -> str:
        """Plays a single round of the game.
        returns string results of a round"""
        move1 = self.p1.move()
        move2 = self.p2.move()
        winner = self.who_won(move1, move2)

        output_text = f"Player 1: {move1}  Player 2: {move2} ----> "
        if winner:
            output_text += f"Player {winner} won"
            if winner == 1:
                self.p1.update_score()
            else:
                self.p2.update_score()
        else:
            output_text += "Draw!"
        output_text += f"\nFirst player score:{self.p1.my_score}," \
                       f"Second player score:{self.p2.my_score}"
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

        return output_text

    def play_game(self):
        """Plays the game with multiple rounds"""
        print("Game start!")
        for game_round in range(3):
            print(f"Round {game_round}:")
            text_result_of_round = self.play_round()
            print(text_result_of_round)

        # calculate and print the winner
        out_text = "GAME RESULT: "
        winner = self.calculate_winner()
        if winner:
            out_text += f"Player {winner} WON!!! "
        else:
            out_text += "DRAW!!!"
        out_text += f"First player score: {self.p1.my_score}, " \
                    f"Second player score: {self.p2.my_score}"
        print(out_text)

    def calculate_winner(self):
        """calculates and return the winner of the game.
        1,2 if player 1,2 won and None for draw
        returns int or None"""
        player_one = 0
        player_two = 0
        for result in self.round_score:
            if result and result == 1:
                player_one += 1
            elif result:
                player_two += 1
        if player_one > player_two:
            winner = 1
        elif player_two > player_one:
            winner = 2
        else:
            winner = None

        return winner

    def who_won(self, move1: str, move2: str):
        """returns None for Draw, 1 or 2 if player 1 or 2 won,
        also save score to round_score  """
        # adding result of a round to self.round_score
        if beats(move1, move2):
            self.round_score.append(1)
        elif beats(move2, move1):
            self.round_score.append(2)
        else:
            self.round_score.append(None)

        return self.round_score[-1]


if __name__ == '__main__':
    main()
