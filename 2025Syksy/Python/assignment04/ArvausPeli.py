import random
while True:
    menu = input("Start game? (y/n): ")
    if menu.lower() == ("n"):
        break
    elif menu.lower() == ("y"):
        num = random.randint(1,10)
        while True:
            guess = int(input("arvaa mikä luku (1-10): "))
            if guess < num:
                print("Liian pieni arvaus")
            elif guess > num:
                print("Liian suuri arvaus")
            elif guess == num:
                print("Oikein")
                break
    else:
        print("please type either 'y' to start a new game, or 'n' to exit program")