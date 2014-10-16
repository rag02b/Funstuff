import random
import time
#simple version of rock, paper, scissors
choices = ["rock", "paper", "scissors"] #choices in the game
userchoice = raw_input("Do you choose paper, scissors, or rock?  ") #user chooses
compchoice = (random.choice(choices)) #computer chooses random choice

time.sleep(1)

print("The computer chooses ")
print(compchoice)

time.sleep(1)

def game1(choice1, choice2):
	if (choice1 == choice2):
		print("The game is a tie!");
	elif (choice1 == "rock"):
		if (choice2 == "scissors"):
			print("rock wins")
		else:
			print("paper wins");
	elif (choice1 == "paper"):
		if (choice2 == "rock"):
			print("paper wins")
		else:
			print("scissors wins");
	elif (choice1 == "scissors"):
		if (choice2 == "paper"):
			print("scissors wins")
		else:
			print("rock wins");
	else:
		print("What?")
			
			
game1(userchoice, compchoice)

