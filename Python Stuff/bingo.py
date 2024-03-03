from random import random, seed, shuffle
from math import floor

answers =  ["Apply, apply, apply!",
  "Water Game",
  "Past Game piece in Kickoff stream",
  "Havabanana Productions",
  "Dean Kamen is wearing denim",
  "Woodie Flowers is an 8-bit character",
  "Corny references to 8-bit games",
  "Knock-off Mario appears",
  "Famous 8-bit character shows up",
  "<i>FIRST</i>-related puns",
  "Gracious Professionals",
  "Dean's Homework",
  "Encryption password is in 1337",
  "Encryption password \"doesn't work!\"",
  "Scripted role-play as 8-bit animation",
  "Scramble to download the game manual",
  "Pre-recorded casually transitions to live",
  '"But before we get to the game..."',
  '"We\'ll get to the game in a moment."',
  "Dozer is in the game animation",
  "Sad because Dozer's not in the game animation",
  "One of the animated robots has a plunger",
  "The team eats a meal together",
  "The team's twitter ends up in the livestream",
  "Someone references last year's game",
  "Sponsor animation loops more than once",
  "Rule update before the end of the day",
  "Someone's theory about the game is right",
  "A theory is wrong",
  "Bumpers are bad",
  "Can't get into the game manual",
  "The stream goes down",
  "Someone mentions Coopertition",
  "Mentor Appreciation",
  "No safety glasses on field tour",
  "Someone asks when food will be ready",
  "TRON movie reference",
  '"VR?" -Matt Scalzo',
  "An alumni of the team is in the stream",
  "FRC related song parody",
  "Last year's design is referenced",
  '"Is this Battle Bots?"',
  "Someone wonders about scouting",
  "Field component plans don't make sense",
  "People argue about a rule",
  "Someone suggests swerve drive",
  "Game pieces are used incorrectly",
  "Water game is <i>actually</i> confirmed",
  '"Has anyone checked Chief Delphi yet?"',
  "Uncomfortably bad acting",
  "War flashbacks to Recycle Rush",
  "Dean Kamen is riding a segway",
  "Alumni come to Kickoff",
  "Winning chairmans' video",
  "Safety animation winner",
  "Frank Merrick, Director of FRC",
  "Humans pretending to be robots",
  "Blobby humans in animation",
  "Animated robots are impossible",
  "New logo revealed",
  "New <i>FIRST</i> sponsor",
  "Surprise items in KOP",
  "Help for rookie teams",
  "Update on <i>FIRST</i> growth",
  "Technical Difficulties",
  "Robot does everything suggestion",
  "A game hint is taken seriously",
  '"Good luck, and see you at the competition!"',
  "Something falls on Dozer",
  "STAR WARS",
  "Woodie Flowers Tribute <3"]

shuffle(answers)

len = 7

print("BINGO TIME".center(46 * len - 1))
print()

answers[floor(len * len / 2)] = "FREE SPACE"

for row in range(0,len):
    for col in range(0,len):
        print(answers[len * row + col].center(45), end=" ")
    print()
    print()