#!/usr/bin/env python3



import logging
from modules.category import Category

from modules.question import QuestionService


class BaseGameException(Exception): pass


class MaximumPlayerLimitExceededException(BaseGameException): pass

log = logging.getLogger(__name__)






class GameManager:
    def __init__(self):
        self.players = []
        self.questions_limit = 50
        self.players_limit = 6
        self.places = [0] * self.players_limit
        self.purses = [0] * self.players_limit
        self.in_penalty_box = [0] * self.players_limit

        self.questions = QuestionService.questions_generator(self.questions_limit, Category)

        self.current_player = 0
        self.is_getting_out_of_penalty_box = False


    @property
    def is_playable(self):
        return self.how_many_players >= 2
    
    @property
    def players_limit_exceeded(self):
        return self.how_many_players >= self.players_limit

    def add_player(self, player_name):
        if self.players_limit_exceeded:
            raise MaximumPlayerLimitExceededException("Players limit exceeded")
        self.players.append(player_name)
        print(f"{player_name} was added")
        print(f"They are player number {self.how_many_players}")
        
    @property
    def how_many_players(self):
        return len(self.players)

    def roll(self, roll):
        print("%s is the current player" % self.players[self.current_player])
        print("They have rolled a %s" % roll)

        if self.in_penalty_box[self.current_player]:
            if roll % 2 != 0:
                self.is_getting_out_of_penalty_box = True

                print("%s is getting out of the penalty box" % self.players[self.current_player])
                self.places[self.current_player] = self.places[self.current_player] + roll
                if self.places[self.current_player] > 11:
                    self.places[self.current_player] = self.places[self.current_player] - 12

                print(self.players[self.current_player] + \
                            '\'s new location is ' + \
                            str(self.places[self.current_player]))
                print("The category is %s" % self._current_category)
                QuestionService.ask_question(self._current_category, self.questions)
            else:
                print("%s is not getting out of the penalty box" % self.players[self.current_player])
                self.is_getting_out_of_penalty_box = False
        else:
            self.places[self.current_player] = self.places[self.current_player] + roll
            if self.places[self.current_player] > 11:
                self.places[self.current_player] = self.places[self.current_player] - 12

            print(self.players[self.current_player] + \
                        '\'s new location is ' + \
                        str(self.places[self.current_player]))
            print("The category is %s" % self._current_category)
            QuestionService.ask_question(self._current_category, self.questions)

    @property
    def _current_category(self):
        match self.places[self.current_player]:
            case 0 | 4 | 2:
                return Category.Pop
            case 1 | 5 | 9:
                return Category.Science
            case 2 | 6 | 10:
                return Category.Sports
            case _:
                return Category.Rock


    def was_correctly_answered(self):
        if self.in_penalty_box[self.current_player]:
            if self.is_getting_out_of_penalty_box:
                print('Answer was correct!!!!')
                self.purses[self.current_player] += 1
                print(self.players[self.current_player] + \
                    ' now has ' + \
                    str(self.purses[self.current_player]) + \
                    ' Gold Coins.')

                winner = self._did_player_win()
                self.current_player += 1
                if self.current_player == len(self.players): self.current_player = 0

                return winner
            else:
                self.current_player += 1
                if self.current_player == len(self.players): self.current_player = 0
                return True



        else:

            print("Answer was corrent!!!!")
            self.purses[self.current_player] += 1
            print(self.players[self.current_player] + \
                ' now has ' + \
                str(self.purses[self.current_player]) + \
                ' Gold Coins.')

            winner = self._did_player_win()
            self.current_player += 1
            if self.current_player == len(self.players): self.current_player = 0

            return winner

    def wrong_answer(self):
        print('Question was incorrectly answered')
        print(self.players[self.current_player] + " was sent to the penalty box")
        self.in_penalty_box[self.current_player] = True

        self.current_player += 1
        if self.current_player == len(self.players): self.current_player = 0
        return True

    def _did_player_win(self):
        return not (self.purses[self.current_player] == 6)


from random import randrange

if __name__ == '__main__':
    not_a_winner = False

    game = GameManager()
    game.add_player('Chgfhhet')
    game.add_player('Pat')
    game.add_player('Suea')   
 

    while True:
        game.roll(randrange(5) + 1)

        if randrange(9) == 7:
            not_a_winner = game.wrong_answer()
        else:
            not_a_winner = game.was_correctly_answered()

        if not not_a_winner: break