import random

class FruitQuiz:
    def __int__(self):
        self.fruit = {'apple':'red'
                       'orange':'orange'
                       'watermelon':'watermelon'
                       'watermelon':'watermelon'
                       'bannana':'yellow'}
    def quiz(self):
        while(True):
            fruit, color = random.choice(list(self.fruits.items))

    print("what is the color of {}".format(fruit))
    user_answer = input()

    if(user_answer.lower() == color):
        print("Correct answer")
    else:
        print("Wrong answer")

        option = int(input("Enter 0 if you want to play again else enter 1: "))
        if(option):
            break
        fq=FruitQuiz()
        fq.Quiz
