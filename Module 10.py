#1
#Write a program that generates 26 text files named A.txt, B.txt, and so on up to Z.txt. 
#To each file append a random number between 1 and 100. 
#Create a summary file (summary.txt) that contains the name of the file and the number in that file: A.txt: 67 B.txt: 12...Z.txt: 98


import random

# Generate random numbers and create files
for letter in range(ord('A'), ord('Z')+1):
    filename = chr(letter) + ".txt"
    random_number = random.randint(1, 100)

    with open(filename, "a") as file:
        file.write(str(random_number))

# Create the summary file
summary_filename = "summary.txt"
with open(summary_filename, "w") as summary_file:
    for letter in range(ord('A'), ord('Z')+1):
        filename = chr(letter) + ".txt"
        with open(filename, "r") as file:
            number = file.read()
            summary_file.write(filename + ": " + number + "\n")


#2
#Create a file with some content. As example, you can take this one:
#“Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
#Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. 
#Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. 
#Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum”.

#Create a second file and copy the content of the first file to the second file in upper case.

# Create the first file with content
content = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit 
in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia 
deserunt mollit anim id est laborum."""

first_filename = "first_file.txt"
with open(first_filename, "w") as first_file:
    first_file.write(content)

# Copy the content to the second file in uppercase
second_filename = "second_file.txt"
with open(first_filename, "r") as first_file:
    with open(second_filename, "w") as second_file:
        content_uppercase = first_file.read().upper()
        second_file.write(content_uppercase)

#3
#Write a program that will simulate user scores in a game. 
# Create a list with 5 players’ names after that simulate 100 rounds for each player. 
# As a result of the game create a list with the player's name and score (0-1000 range). And save it to a CSV file.
# The file should look like this:
# Player name, Score
# Josh, 56
# Luke, 784
# Kate, 90
# Mark, 125
# Mary, 877
# Josh, 345

import csv
import random

# List of players' names
players = ["Josh", "Luke", "Kate", "Mark", "Mary"]

# Simulate game rounds and generate scores for each player
player_scores = []
for player in players:
    for _ in range(100):
        score = random.randint(0, 1000)
        player_scores.append((player, score))

# Save player scores to a CSV file
csv_filename = "player_scores.csv"
with open(csv_filename, "w", newline="") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(["Player name", "Score"])  # Write header
    writer.writerows(player_scores)  # Write player scores


# 4
#Write a script that reads the data from the previous CSV file and creates a new file called high_scores.csv 
# where each row contains the player name and their highest score. 
# The final score should be sorted by descending to the highest score.
# The output CSV file should look like this:
# layer name, Highest score
# Kate, 907
# Mary, 897
# Luke, 784
# Mark, 725
# Josh, 345

import csv

# Read player scores from the CSV file
csv_filename = "player_scores.csv"
player_scores = []
with open(csv_filename, "r") as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        player_scores.append(row)

# Find the highest score for each player
highest_scores = {}
for row in player_scores:
    player = row["Player name"]
    score = int(row["Score"])
    if player not in highest_scores or score > highest_scores[player]:
        highest_scores[player] = score

# Sort the highest scores in descending order
sorted_scores = sorted(highest_scores.items(), key=lambda x: x[1], reverse=True)

# Save the highest scores to a new CSV file
high_scores_filename = "high_scores.csv"
with open(high_scores_filename, "w", newline="") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(["Player name", "Highest score"])  # Write header
    writer.writerows(sorted_scores)  # Write highest scores