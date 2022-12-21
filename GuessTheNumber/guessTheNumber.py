while True:
    import random

    upper_limit = int(input('Enter upper limit: '))
    lower_limit = int(input('Enter lower limit: '))

    random_number = random.randint(lower_limit, upper_limit)
    print("you will have to choose a number between ", upper_limit, ' and ', lower_limit)

    chance = 0
    while chance < 8:
        chance += 1
        guess = int(input('Enter your guess: '))
        if random_number == guess:
            print('Congragulation, You did it. The number was ', random_number)
            break
        elif guess < random_number:
            print('You guess a small Number.')
        elif guess > random_number:
            print('You guess a large number')
        if chance == 7:
            print("\n You've run out of chances")
            print("\n The number was ", random_number)
            print("Better luck next time")
            break
    print("\n")
    break