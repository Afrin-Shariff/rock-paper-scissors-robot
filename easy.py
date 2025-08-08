import random
import time

players_score = 0
computers_score = 0

print("Hello and welcome to this rock, paper, scissors game.")
print("If you win 5 times before the computer then you win. If not then......")
print("YOU LOSE")
print("Note = 1st round is practice and this is case sensitive")

# Practice round
players_action = input("Practice round! Do you choose (rock, paper or scissors?): ")
possible_actions = ["rock", "paper", "scissors"]
computers_action = random.choice(possible_actions)
print("You chose", players_action, "and the computer chose", computers_action)

# Main game loop
while players_score < 5 and computers_score < 5:
    players_action = input("Do you choose (rock, paper or scissors?): ")

    if players_action not in possible_actions:
        print("Invalid choice. Try again.")
        continue

    computers_action = random.choice(possible_actions)
    print("You chose", players_action, "and the computer chose", computers_action)

    if computers_action == "rock":
        if players_action == "paper":
            players_score += 1
            print("The computer chose", computers_action)
            print("You are on", players_score, "and I am on", computers_score)
        elif players_action == "rock":
            print("The computer chose", computers_action)
            print("It is a tie. I will get you next round")
            print("You are on", players_score, "and I am on", computers_score)
        else:
            computers_score += 1
            print("The computer chose", computers_action)
            print("I am so great at this unlike you")
            print("You are on", players_score, "and I am on", computers_score)

    elif computers_action == "paper":
        if players_action == "scissors":
            players_score += 1
            print("The computer chose", computers_action)
            print("That was just luck!")
            print("You are on", players_score, "and I am on", computers_score)
        elif players_action == "paper":
            print("The computer chose", computers_action)
            print("It is a tie. I will get you next round")
            print("You are on", players_score, "and I am on", computers_score)
        else:
            computers_score += 1
            print("The computer chose", computers_action)
            print("I am so great at this unlike you")
            print("You are on", players_score, "and I am on", computers_score)

    elif computers_action == "scissors":
        if players_action == "rock":
            players_score += 1
            print("The computer chose", computers_action)
            print("That was just luck!")
            print("You are on", players_score, "and I am on", computers_score)
        elif players_action == "scissors":
            print("The computer chose", computers_action)
            print("It is a tie. I will get you next round")
            print("You are on", players_score, "and I am on", computers_score)
        else:
            computers_score += 1
            print("The computer chose", computers_action)
            print("I am so great at this unlike you")
            print("You are on", players_score, "and I am on", computers_score)

# Game result
if players_score == 5:
    print("🏆 You reached 5 points first. YOU WIN!")
else:
    print("💀 The computer reached 5 points first. YOU LOSE!")