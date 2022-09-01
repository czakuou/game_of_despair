
import pytest
from game import  GameManager, MaximumPlayerLimitExceededException
from modules.category import Category


def test_game_can_add_player_to_the_game():
    game = GameManager()
    player = "chris"
    
    game.add_player(player)
    
    assert game.how_many_players == 1
    assert game.players[0] == player


def test_game_can_add_maximum_number_of_players():
    game = GameManager()
    players = ('a', 'b', 'c', 'd', 'e', 'f')
    
    for player in players:
        game.add_player(player)
    
    assert game.how_many_players == len(players)


def test_game_cannot_exceed_the_players_limit():
    game = GameManager()
    players = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k')
    
    with pytest.raises(MaximumPlayerLimitExceededException):
        for player in players:
            game.add_player(player)


def test_game_can_create_questions_at_the_start_of_the_game():
    game = GameManager()
    
    assert len(game.questions[Category.Rock]) == game.questions_limit
    assert len(game.questions[Category.Sports]) == game.questions_limit
    assert len(game.questions[Category.Science]) == game.questions_limit
    assert len(game.questions[Category.Pop]) == game.questions_limit