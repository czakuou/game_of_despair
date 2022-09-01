

from game import GameManager
from modules.category import Category
from modules.question import Question, QuestionService


def test_can_add_rock_collection():
    game = GameManager()
    question = Question(Category.Rock, 1)
    
    QuestionService._add_question(question, game.questions)
    expexted_result = game.questions_limit + 1
    
    assert len(game.questions[Category.Rock]) == expexted_result
    

def test_can_add_pop_collection():
    game = GameManager()
    question = Question(Category.Pop, 1)
    
    QuestionService._add_question(question, game.questions)
    expexted_result = game.questions_limit + 1
    
    assert len(game.questions[Category.Pop]) == expexted_result
    

def test_can_add_sport_collection():
    game = GameManager()
    question = Question(Category.Sports, 1)
    
    QuestionService._add_question(question, game.questions)
    expexted_result = game.questions_limit + 1
    
    assert len(game.questions[Category.Sports]) == expexted_result
    

def test_can_add_science_collection():
    game = GameManager()
    question = Question(Category.Science, 1)
    
    QuestionService._add_question(question, game.questions)
    expexted_result = game.questions_limit + 1
    
    assert len(game.questions[Category.Science]) == expexted_result