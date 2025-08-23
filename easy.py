import random
import time

# Score tracking
players_score = 0
computers_score = 0

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

def print_scores():
    print(f"🧍 You: {players_score} | 🤖 Computer: {computers_score}\n")

print("🎮 Welcome to Rock, Paper, Scissors!")
print("First to 5 wins. Let's see who's the real champion.")
print("Note: First round is practice. P.S. this game is case sensitive.\n")

# Practice round
players_action = input("Practice round! Choose (rock, paper, scissors): ").lower()
computers_action = random.choice(possible_actions)
print(f"You chose {ascii_art.get(players_action, players_action)} and the computer chose {ascii_art[computers_action]}")

# Main game loop
while players_score < 5 and computers_score < 5:
    players_action = input("Your move (rock, paper, scissors): ").lower()

    if players_action not in possible_actions:
        print("❌ Invalid choice. Try again.\n")
        continue

    print("⏳ Rock...")
    time.sleep(0.1)
    print("📄 Paper...")
    time.sleep(0.1)
    print("✂️ Scissors...")
    time.sleep(0.1)
    print("🔫 Shoot!\n")
    time.sleep(0.1)

    computers_action = random.choice(possible_actions)
    result = get_result(players_action, computers_action)

    print(f"You chose {ascii_art[players_action]} and the computer chose {ascii_art[computers_action]}")

    if result == "win":
        players_score += 1
        print("✅ You win this round!")
        print(random.choice(win_messages))
    elif result == "lose":
        computers_score += 1
        print("❌ You lost this round.")
        print(random.choice(lose_messages))
    else:
        print("⚖️ It's a tie.")
        print(random.choice(tie_messages))

    print_scores()

# Final result
if players_score == 5:
    print("🏆 You reached 5 points first. YOU WIN!")
else:
    print("💀 The computer reached 5 points first. YOU LOSE!")