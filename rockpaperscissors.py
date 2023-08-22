rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
choice=input('choose "rock" "paper" or "scissors"\n').lower()
resp_list=["rock","paper","scissors"]
responce=random.choice(resp_list)

if choice=="rock":
  print(rock)
  if responce==resp_list[2]:
    print(scissors)
    print("You win!")
  elif responce!=resp_list[1]:
    print(rock)
    print("Draw")
  else:
    print(paper)
    print("You lose")
  
elif choice=="paper":
  print(paper)
  if responce==resp_list[0]:
    print(rock)
    print("You win!")
  elif responce!=resp_list[2]:
    print(paper)
    print("Draw") 
  else:
    print(scissors)
    print("You lose")

elif choice=="scissors":
  print(scissors)
  if responce==resp_list[1]:
    print(paper)
    print("You win!")
  elif responce!=resp_list[0]:
    print(scissors)
    print("Draw")
  else:
    print(rock)
    print("You lose")

#if responce=="rock":
 # print(rock)
#elif responce=="paper":
 # print(paper)
#elif responce=="scissors":
  #print(scissors)


  
  









