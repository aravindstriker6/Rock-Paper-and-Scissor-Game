import random

while True:
    try:
        game_type = int(input("Enter how many points game u want to play with the computer: "))
        i = 0
        j = 0
        k = 0
        while i < game_type:
            while True:
                select = input("Enter the choice to play the game: ").lower()
                print(select)
                options = ['rock', 'paper', 'scissor']
                computer_select = random.choice(options)
                print(f"Computer pls enter the choice: {computer_select}")
                if select in options:
                    print("U have entered a valid option , all the best mate")
                    if select == computer_select:
                        print("It is a Tie :)")
                        j = j + 1
                        k = k + 1
                        i = i + 1
                        break
                    elif select == 'rock' and computer_select == 'scissor':
                        print("Yaay u win!!! :) :) :)")
                        i = i + 1
                        j = j + 1
                        break
                    elif select == 'paper' and computer_select == 'rock':
                        print("Yaay u win!!! :) :) :)")
                        i = i + 1
                        j = j + 1
                        break
                    elif select == 'scissor' and computer_select == 'paper':
                        print("Yaay u win!!! :) :) :)")
                        i = i + 1
                        j = j + 1
                        break
                    else:
                        print(" Sorry u lose!! :( :( , better luck next time")
                        i = i + 1
                        k = k + 1
                        break
                else:
                    print("Please enter a valid option ****")
                    continue
            if j > int(game_type / 2) or k > int(game_type / 2):
                break
            else:
                continue
        if j > k:
            print()
            print("      ***** Game Over *****    ")
            print(f'U are the winner and u have scored {j} points')
        elif j < k:
            print()
            print("       ***** Game Over *****     ")
            print(f"U lose :( , computer is the winner and it has scored {k} points")
        else:
            print()
            print("     ***** Game Over *****     ")
            print(f"The match is tied and both of u played really well")
        break
    except (ValueError, TypeError, IndentationError, SyntaxError) as err:
        print(f"There is a error in code and the error is {err}")
        continue
