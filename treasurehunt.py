print("welcome to treasure hunt")
choice1=input('which way you want to go? "left" or "right"\n').lower()
if choice1=="left":
    choice2=input('You are at a lake. Do you want to wait for the boat or swim? type "wait" or "swim"\n').lower()
    if choice2=="wait":
        choice3=input('which door you want to go with? type "red","blue" or "yellow"\n').lower()
        if choice3=="blue":
            print("You have found the treasure,YOU WIN!!!")
        elif choice3=="red":
            print("bitten by snakes, GAME OVER.")
        elif choice3=="yellow":
            print("Burned by fire, GAME OVER.")  
        else:
            print("Door does not exist, GAME OVER")         
    else:
        print("You got eaten by sharks, GAME OVER.")    
else:
    print("you fell into a hole, GAME OVER.")
