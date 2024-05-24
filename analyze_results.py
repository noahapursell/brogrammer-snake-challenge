import json

FILE = "test_output.json"

with open(FILE, 'r') as file:
    data = json.load(file)

total_frames = 0
num_entries = 0
num_wins = 0

for entry in data:
    num_entries += 1
    total_frames += entry['num_frames']
    if entry['is_win']:
        num_wins += 1

print(f"Win Percentage: {num_wins / num_entries}")
print(f"Average frame count: {total_frames / num_entries}")

