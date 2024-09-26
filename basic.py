import random

num = random.randrange(1000, 10000)

n = int(input("Guess the 4 digit number:"))

if (n == num):
    print("Great! You guessed the number in just 1 try! You're a Mastermind!")
else:
    attempts = 0

    while (n != num):
        attempts += 1

        count = 0

        n = str(n)

        num = str(num)

        correct = ['X']*4

        for i in range(0, 4):

            if (n[i] == num[i]):
                count += 1
                correct[i] = n[i]

    