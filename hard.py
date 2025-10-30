import random

#score variables
p_score = 0
cpu_score = 0

# Function to evaluate and show score after each round
def evaluate(player, cpu):
    global p_score, cpu_score
    if player == cpu:
        print("It's a tie.")
    elif (
        (player == "rock" and cpu == "scissors") or
        (player == "paper" and cpu == "rock") or
        (player == "scissors" and cpu == "paper")
    ):
        p_score += 1
        print("You win this round!")
    else:
        cpu_score += 1
        print("Computer wins this round!")
    print("📊 Score — You:",p_score, "| Computer:",cpu_score)

print("WELCOME to the rock paper scissors robot 2.0. The computer will try to predict some of your moves and try to beat you. I wish you all the best and don't be too sad if you lose")

#main loop 1

while p_score < 5 or cpu_score < 5:    

    #variables
    r = "rock"
    p = "paper"
    s = "scissors"

    Pa1 = ["rock" , "paper"]
    Pa2 = ["rock" , "scissors"]
    Pa3 = ["paper" , "scissors"]

    possible_actions = ["rock", "paper", "scissors"]
    cpu = random.choice(possible_actions)

    #1st move
    A = input("rock paper or scissors")
    print("You chose", A, "and the computer chose", cpu)
    evaluate(A, cpu)

    possible_actions = ["rock", "paper", "scissors"]
    cpu = random.choice(possible_actions)

    #2nd move
    B = input("rock paper or scissors")
    print("You chose", B, "and the computer chose", cpu)
    evaluate(B, cpu)

    possible_actions = ["rock", "paper", "scissors"]
    cpu = random.choice(possible_actions)

    #3rd move
    C = input("rock paper or scissors")
    print("You chose", C, "and the computer chose", cpu)
    evaluate(C, cpu)

    #logic
    if A == B and B == C and A == r:
        D = input("rock paper scissors")
        cpu1 = random.choice(Pa1)
        print("You chose", D, "and the computer chose", cpu1)
    if A == B and A == r:
        D = input("rock paper scissors")
        cpu1 = random.choice(Pa1)
        print("You chose", D, "and the computer chose", cpu1)
    if B == C and B == p:
        D = input("rock paper scissors")
        cpu1 = random.choice(Pa1)
        print("You chose", D, "and the computer chose", cpu1)
    if B == C and B == s:
        D = input("rock paper scissors")
        cpu2 = random.choice(Pa2)
        print("You chose", D, "and the computer chose", cpu2)
    if A == C and A == r:
        D = input("rock paper scissors")
        cpu3 = random.choice(Pa3)
        print("You chose", D, "and the computer chose", cpu3)
    if  A != B and B != C:
        D = input("rock paper scissors")
        cpu = random.choice(possible_actions)
        print("You chose", D, "and the computer chose", cpu)

    #winner or loser
    if cpu_score == 5:
        print("HAHAHAHA I BEAT YOU. I AM CLEARLY BETTER THAN YOU!!!!!")
        break
    
    if p_score == 5:
        print("OH WOW! How did you win????? Next time I will be serious; I was just going easy on you today!!!!!")
        print("YOU BETTER WATCH OUT!!!!!!")
        break
        