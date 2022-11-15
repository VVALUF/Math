import random
import operator


def random_problem():
    operators = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv,
    }

    nr1 = random.randint(1, 100)
    nr2 = random.randint(1, 100)
    sign = random.choice(list(operators.keys()))
    answer = operators.get(sign)(nr1, nr2)
    print(f'What is {nr1} {sign} {nr2} ?')
    return answer

def question():
    answer = random_problem()
    player = float(input())
    return player == answer

def game():
    score = 0
    print('Welcome to my math game!\n')
    for i in range(10):
        if question() == True:
            score += 1
            print('Correct!')
        else:
            print('Incorrect!')
    print(f'You got {score}' + ' out of 10 quastions.\n')

again = 'yes'
while again == 'yes':
    game()
    print('Do you want to play again?\n')
    again = input