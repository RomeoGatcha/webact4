import quiz as q


triviaGame = q.Quiz()

noOfQuestion = int(input("Enter no. of Question (1 - 20): "))

setOfQuestion = triviaGame.loadQuestions(noOfQuestion)


# this loop is for displaying the question and options
for i in range(1, noOfQuestion+1):
    Question = setOfQuestion[f'Question{i}']
    Options = setOfQuestion[f'Options{i}']

    print(f"\nQuestion {i}: {Question}?")   # display question

    choices = 'a'
    for y in range(1, len(Options)):
        print(f'{choices} : {Options[y-1]}')    # display options
        choices = chr(ord(choices)+1)

    # check if is correct
    isCorrect = triviaGame.checkAnswer(
        Question, answer=str(input("Select your answer:")))

    if isCorrect:
        print(f'\nYour score: {triviaGame.getScore()}\nHooray! +50 points!')
    else:
        print(
            f'\nYour score: {triviaGame.getScore()}\nOops! No point this time.')


print(f'''\nYour Total score: {triviaGame.getScore()}
Total Correct: {triviaGame.getCorrectTotal()}
Total Incorrect: {triviaGame.getIncorrectTotal()}''')
