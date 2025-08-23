import random
import time

# Score tracking
players_score = 0
computers_score = 0
round_number = 1

# Valid choices
possible_actions = ["rock", "paper", "scissors"]

# Outcome messages
win_messages = [
    "That was just luck!",
    "You're getting good at this!",
    "Nice move, but don't get cocky!"
]
lose_messages = [
    "I am so great at this unlike you.",
    "Better luck next time!",
    "Oof, that was rough!"
]
tie_messages = [
    "It is a tie. I will get you next round.",
    "Great minds think alike!",
    "No points this time!"
]

# ASCII art
ascii_art = {
    "rock": "🪨",
    "paper": "📄",
    "scissors": "✂️"
}

def get_result(player, computer):
    if player == computer:
        return "tie"
    elif (player == "rock" and computer == "scissors") or \
         (player == "paper" and computer == "rock") or \
         (player == "scissors" and computer == "paper"):
        return "win"
    else:
        return "lose"

def print_scores(player_score, computer_score):
    time.sleep(0.5)
    print(f"🧍 You: {player_score} | 🤖 Computer: {computer_score}\n")
    time.sleep(0.5)

# Game intro
print("🎮 Welcome to Rock, Paper, Scissors!")
print("First to 5 wins. Let's see who's the real champion.")
print("Note: First round is practice. P.S. this game is case sensitive.\n")
time.sleep(1)

# Practice round
practice_action = input("Practice round! Choose (rock, paper, scissors): ").lower()
practice_computer = random.choice(possible_actions)
print(f"You chose {ascii_art.get(practice_action, practice_action)} and the computer chose {ascii_art[practice_computer]}")
time.sleep(1)

# Main game loop
while players_score < 5 and computers_score < 5:
    print(f"\n🔢 Round {round_number}")
    players_action = input("Your move (rock, paper, scissors): ").lower()

    if players_action not in possible_actions:
        print("❌ Invalid choice. Try again.\n")
        continue

    print("⏳ Rock...")
    time.sleep(0.4)
    print("📄 Paper...")
    time.sleep(0.4)
    print("✂️ Scissors...")
    time.sleep(0.4)
    print("🔫 Shoot!\n")
    time.sleep(0.6)

    computers_action = random.choice(possible_actions)
    result = get_result(players_action, computers_action)

    print(f"You chose {ascii_art[players_action]} and the computer chose {ascii_art[computers_action]}")
    time.sleep(0.6)

    if result == "win":
        players_score += 1
        print("✅ You win this round!")
        print("🤖 " + random.choice(win_messages))
    elif result == "lose":
        computers_score += 1
        print("❌ You lost this round.")
        print("🤖 " + random.choice(lose_messages))
    else:
        print("⚖️ It's a tie.")
        print("🤖 " + random.choice(tie_messages))

    print_scores(players_score, computers_score)
    round_number += 1

# Final result
time.sleep(1)
if players_score == 5:
    print("🏆 You reached 5 points first. YOU WIN!")
    time.sleep(0.6)
    print("🤖 I’ll admit defeat... but next time, I won’t go easy on you.")
else:
    print("💀 The computer reached 5 points first. YOU LOSE!")
    time.sleep(0.6)
    print("🤖 Bow before the RPS overlord! 🧠✂️📄🪨")