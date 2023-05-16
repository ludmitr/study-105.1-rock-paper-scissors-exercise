"""Test module"""
import rps
import players
import random


if __name__ == '__main__':
    game_players = [
        players.AllRockPlayer(),
        players.RandomPlayer(),
        players.ReflectPlayer(),
        players.CyclePlayer()
    ]
    p1 = players.HumanPlayer()
    p2 = random.choice(game_players)
    game = rps.Game(p1, p2)
    game.play_game()
