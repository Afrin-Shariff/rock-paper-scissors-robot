import random
import time

# Elemental strengths
beats = {
    "fire": ["grass", "air"],
    "water": ["fire", "soil"],
    "grass": ["water", "soil"],
    "soil": ["fire", "air"],
    "air": ["water", "grass"]
}

# Element symbols
symbols = {
    "fire": "🔥",
    "water": "💧",
    "grass": "🌿",
    "soil": "🌍",
    "air": "💨"
}

# Computer personality comments
comp_comments = {
    "win": [
        "I won because I’m clearly better. 😎",
        "Another one bites the dust (that's you BTW). 💥",
        "Victory is a taste that I am rather used to. 💨"
    ],
    "lose": [
        "You got lucky. Don’t get used to it. 😒",
        "Fine, you win this round. But I’m watching you. 👀",
        "That was just a fluke and of course I was going easy on you. 😲"
    ],
    "tie": [
        "A tie? We’re evenly matched... for now. 🤝",
        "A tie between the good and great. How can it be? 🤔"
    ]
}

elements = list(beats.keys())

def determine_winner(player, computer):
    if player == computer:
        return "tie"
    elif computer in beats[player]:
        return "win"
    else:
        return "lose"

def play_game():
    print("🌿🔥💧🌍💨 Welcome to Elemental Rock-Paper-Scissors!")
    print("First to 5 wins! Choose one: Fire, Water, Grass, Soil, Air")
    time.sleep(1)

    player_score = 0
    computer_score = 0
    round_number = 1

    while player_score < 5 and computer_score < 5:
        print(f"\n🔢 Round {round_number}")
        player_choice = input("Your choice: ").strip().lower()
        if player_choice not in elements:
            print("❌ Invalid choice. Please pick from Fire, Water, Grass, Soil, or Air.")
            continue

        print("🤖 Thinking...")
        time.sleep(1.2)
        computer_choice = random.choice(elements)
        print(f"🤖 Computer chose: {computer_choice.capitalize()} {symbols[computer_choice]}")
        time.sleep(0.8)

        result = determine_winner(player_choice, computer_choice)

        if result == "win":
            print(f"✅ You win this round! {symbols[player_choice]} beats {symbols[computer_choice]}")
            time.sleep(0.6)
            print("🤖 " + random.choice(comp_comments["lose"]))
            player_score += 1
        elif result == "lose":
            print(f"❌ You lose this round. {symbols[computer_choice]} beats {symbols[player_choice]}")
            time.sleep(0.6)
            print("🤖 " + random.choice(comp_comments["win"]))
            computer_score += 1
        else:
            print(f"⚖️ It's a tie! Both chose {symbols[player_choice]}")
            time.sleep(0.6)
            print("🤖 " + random.choice(comp_comments["tie"]))

        time.sleep(0.5)
        print(f"🏆 Score — You: {player_score} | Computer: {computer_score}")
        round_number += 1
        time.sleep(0.8)

    # Final result
    time.sleep(1)
    if player_score == 5:
        print("\n🎉 You won the game! Elemental mastery achieved!")
        time.sleep(0.8)
        print("🤖 I’ll admit defeat... but I’ll be back. 🔥")
    else:
        print("\n💀 You lost the game. The elements were not in your favor.")
        time.sleep(0.8)
        print("🤖 Bow before the elemental overlord! 💀")

# Start the game
if __name__ == "__main__":
    play_game()