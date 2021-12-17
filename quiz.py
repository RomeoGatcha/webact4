import random


class Quiz:

    __questions = {  # put here ↓ the question             put ↓ here the option---------   ↓ put here the correct answer (must be letters from a - d)
        'Question1': {'question': 'first question', 'Options': ["1opt1", "opt2", "opt3", "opt4", "a"]},
        'Question2': {'question': 'second question', 'Options': ["2opt1", "opt2", "opt3", "opt4", "a"]},
        'Question3': {'question': 'third question', 'Options': ["3opt1", "opt2", "opt3", "opt4", "a"]},
        'Question4': {'question': 'fourth question', 'Options': ["4opt1", "opt2", "opt3", "opt4", "a"]},
        'Question5': {'question': 'fifth question', 'Options': ["5opt1", "opt2", "opt3", "opt4", "a"]},
        'Question6': {'question': 'sixth question', 'Options': ["6opt1", "opt2", "opt3", "opt4", "a"]},
        'Question7': {'question': 'seventh question', 'Options': ["7opt1", "opt2", "opt3", "opt4", "a"]},
        'Question8': {'question': 'eight question', 'Options': ["8opt1", "opt2", "opt3", "opt4", "a"]},
        'Question9': {'question': 'nineth question', 'Options': ["9opt1", "opt2", "opt3", "opt4", "a"]},
        'Question10': {'question': 'tenth question', 'Options': ["10opt1", "opt2", "opt3", "opt4", "a"]},
    }

    def __init__(self) -> None:
        self.__score = 0
        self.__correctTotal = 0
        self.__incorrectTotal = 0

    def loadQuestions(self, noOfQuestions: int):
        question = []   # keys of __question dict
        loadQuestion = {}   # for shuffled Questions

        # this loop is for getting the keys of __quiestion dictionary
        while 0 < noOfQuestions:
            shuffleQuestion = random.choice(
                list(self.__questions.keys()))  # get random keys
            if shuffleQuestion not in question:  # check if their's repeated question
                question.append(shuffleQuestion)
            else:
                noOfQuestions += 1
            noOfQuestions -= 1

        # this loop is for appending the shuffled question in loadQuestion dict
        count = 1
        for q in question:
            loadQuestion[f'Question{count}'] = self.__questions[q]['question']
            loadQuestion[f'Options{count}'] = self.__questions[q]['Options']
            count += 1

        return loadQuestion     # return the shuffled quetion dict

    def checkAnswer(self, question: str, answer) -> bool:
        answerCheck = ''

        for key, val in self.__questions.items():
            if(self.__questions[key]['question'] == question):
                # get the list of options
                answerCheck = self.__questions[key]['Options']

        if answer == answerCheck[-1]:  # compare the answer and the correct answer
            self.__score += 50
            self.__correctTotal += 1

        if (not(answer == answerCheck[-1])):
            self.__incorrectTotal += 1

        # return true if correct if not return else
        return answer == answerCheck[-1]

    def getScore(self) -> int:
        return self.__score

    def getCorrectTotal(self) -> int:
        return self.__correctTotal

    def getIncorrectTotal(self) -> int:
        return self.__incorrectTotal
