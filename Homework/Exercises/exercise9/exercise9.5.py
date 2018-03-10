from random import random
"""
Robert Matthews
CS 1400
Section 002
Exercise 9

9.5
Chapter 9, Programming Exercises #4, pg 309. Hint: Modify the code in Chapter 9 for racquetball so that it plays rally 
volleyball instead. Submit the source code as your answer. In comments, list what lines changed and how they changed.
"""

# racquetball code from the textbook
# one of the changes I made was adapting the code to follow proper python 3.5 structure. (lowercase functions, line
# spacing, etc etc
# changed game over function to follow volleyball scoring to end the game at 25 and they must win by 2
# adjusted scoring to include a point where the team wins a rally even if they didn't serve


def main():
    print_intro()
    prob_a, prob_b, n = get_inputs()
    wins_a, wins_b = sim_n_games(n, prob_a, prob_b)
    print_summary(wins_a, wins_b)


def print_intro():
    print("This program simulates a game of racquetball between two")
    print('players called "A" and "B". The ability of each player is')
    print("indicated by a probability (a number between 0 and 1) that")
    print("the player wins the point when serving. Player A always")
    print("has the first serve.")


# returns the three simulation parameters prob_a, prob_b, and n
def get_inputs():
    a = float(input("What is the probability player A wins a serve? "))
    b = float(input("What is the probability player B wins a serve? "))
    n = int(input("How many games to simulate? "))
    return a, b, n


# simulates n games of racquetball between players whose abilities are
# represented by the probability of winning a serve
# returns a number of wins for A and B
def sim_n_games(n, prob_a, prob_b):
    wins_a = wins_b = 0
    for i in range(n):
        score_a, score_b = sim_one_game(prob_a, prob_b)
        if score_a > score_b:
            wins_a = wins_a + 1
        else:
            wins_b = wins_b + 1
    return wins_a, wins_b


# simulates a single fame of racquetball between players whose
# abilities are represented by the probability of winning a serve
# returns final scores for A and B
def sim_one_game(prob_a, prob_b):
    serving = "A"
    score_a = 0
    score_b = 0
    while not game_over(score_a, score_b):
        if random() < prob_a and random > prob_b:
            score_a = score_a + 1
        else:
            score_b = score_b + 1
    return score_a, score_b


# a and b represent scores for a racquetball game
# returns true is the game is over, false otherwise
def game_over(a, b):
    return a == 25 and a + 2 >= b or b == 25 and b + 2 >= a


# prints a summary of wins for each player
def print_summary(wins_a, wins_b):
    n = wins_a + wins_b
    print("\nGames simulated:", n)
    print("Wins for A: {0} ({1:0.1%})".format(wins_a, wins_a/n))
    print("Wins for B: {0} ({1:0.1%})".format(wins_b, wins_b/n))


main()

