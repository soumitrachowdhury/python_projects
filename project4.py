# Rock,Paper,Scissors Game!
import random
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

rock1= '''
    _______
 (____   '---
(_____)
(_____)
 (____)
  (___)__.---
'''

paper1= '''
        _______
 ____(____   '---
(______
 (_______
  (_______
     (__________.---
'''
scissors1='''
       _______
____(____   '---
(______
 (__________
    (____)
     (___)__.---
'''

output=[rock,paper,scissors]
output1=[rock1,paper1,scissors1]

user_input=int(input("Welcome to Rock,Paper,Scissors GAME!\n"
                 "Please choose '0' for Rock,'1' for Paper or '2' for Scissors: "))
computer_input=random.randint(0,2)



if user_input==computer_input:
    print("\nYou chose: "+"\n"+output[user_input])
    print("\nComputer chose: " + "\n" + output1[computer_input])
    print("It is a Draw")
elif user_input==0 and computer_input==1:
    print("\nYou chose: " + "\n" + output[user_input])
    print("\nComputer chose: " + "\n" + output1[computer_input])
    print("You lost :(")
elif user_input==0 and computer_input==2:
    print("\nYou chose: " + "\n" + output[user_input])
    print("\nComputer chose: " + "\n" + output1[computer_input])
    print("You WIN! :)")
elif user_input==1 and computer_input==0:
    print("\nYou chose: " + "\n" + output[user_input])
    print("\nComputer chose: " + "\n" + output1[computer_input])
    print("You WIN! :)")
elif user_input==1 and computer_input==2:
    print("\nYou chose: " + "\n" + output[user_input])
    print("\nComputer chose: " + "\n" + output1[computer_input])
    print("You lost :(")
elif user_input==2 and computer_input==0:
    print("\nYou chose: " + "\n" + output[user_input])
    print("\nComputer chose: " + "\n" + output1[computer_input])
    print("You lost :(")
elif user_input==2 and computer_input==1:
    print("\nYou chose: " + "\n" + output[user_input])
    print("\nComputer chose: " + "\n" + output1[computer_input])
    print("You WIN! :)")
else:
    print("Your choice is invalid. GAME OVER :(")