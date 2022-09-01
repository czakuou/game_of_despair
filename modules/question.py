from collections import defaultdict
import logging

from dataclasses import dataclass

from modules.category import Category


log = logging.getLogger(__name__)

@dataclass(frozen=True)
class Question:
    category: Category
    number: int
        

class QuestionService:
    def _add_question(question: Question, collection):
        collection[question.category].append(f"{question.category} number {question.number}")

    @staticmethod
    def ask_question(current_category: Category, collection):
        match current_category:
            case Category.Pop:
                log.info(collection[Category.Pop].pop(0))
            case Category.Science:
                log.info(collection[Category.Science].pop(0))
            case Category.Sports:
                log.info(collection[Category.Sports].pop(0))
            case Category.Rock:
                log.info(collection[Category.Rock].pop(0))
                
    @staticmethod
    def questions_generator(limit: int, categories: Category) -> defaultdict:
        questions_collection: defaultdict[list[Question]] = defaultdict(list) 
        for i in range(limit):
            QuestionService._add_question(Question(categories.Rock, i), questions_collection)
            QuestionService._add_question(Question(categories.Science, i), questions_collection)
            QuestionService._add_question(Question(categories.Sports, i), questions_collection)
            QuestionService._add_question(Question(categories.Pop, i), questions_collection)
        return questions_collection