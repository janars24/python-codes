print('''
                 /\.
                /|_\`.
               /__|_\/`.
              /__|__|\/.`.
             /_|__|__|\/`/`.
            /|__|___|__\/`/
           /__|___|___|_\/   ''')
print("******************************")
print("Welcome to Treasure Hunt Game!")
print("******************************")
print("Your mission is to find the treasure!")

choice1 = input('You\'re at a crossroad. Choose "left" or "right": ').lower()

if choice1 == "left":
    choice2 = input('You\'ve come to a river bank. '
                    'Choose whether you want to "swim" or "wait" : ').lower()
    if choice2 == "wait":
        choice3 = input('You\'ve come to a castle, choose any one of the three door. '
                            '"Yellow", "Blue" or "Red"' ).lower()
        if choice3 == "yellow":
            print("Congrats!, you found the treasure")
        elif choice3 == "blue":
            print("Eaten by Beast. Game Over!")
        elif choice3 == "red":
            print("Burned by Fire, Game Over!")
        else:
            print("Game Over!")
    else :
        print("Attacked by Trout. GameOver!")
else:
    print("You fell into an infinite hole. Game over!")