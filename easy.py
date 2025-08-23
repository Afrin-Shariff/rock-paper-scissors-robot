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