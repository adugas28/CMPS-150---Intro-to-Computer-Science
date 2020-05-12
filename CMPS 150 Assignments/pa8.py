# Author:           Austin Dugas
# ULID:             C00231110
# Course/Section:   CMPS 150 - Lecture Section #3
# Assignment:       pa8
# Date Assigned:    Monday, November 25, 2019
# Date/Time Due:    Monday, December 2, 2019 -- 11:55 pm
# 
# Description:      Create a card object for each player
#                   Keep a count of the total points for each player
#                   Display the card and point values for the round
#                   Repeat for five rounds (i.e., each player draws five cards)
#                   Display the final winner
#
# Certification of Authenticity:
# I certify that this assignment is entirely my own work.

# Import the random file
import random

# The class for randomly selecting cards for players
class Card:
    # Initialize variables
    def __init__(self):
        self.__suit = random.randint(1,4)
        self.__rank = random.randint(1,13)

    # Define a method for getting the suit for each card
    def GetSuitName(self):
        if self.__suit == 1:
            return "Clubs"
        elif self.__suit == 2:
            return "Diamonds"
        elif self.__suit == 3:
            return "Hearts"
        else:
            return "Spades"

    # Define a method for getting the rank for each card
    def GetRankName(self):
        if self.__rank == 1:
            return "Ace"
        elif self.__rank == 2:
            return "2"
        elif self.__rank == 3:
            return "3"
        elif self.__rank == 4:
            return "4"
        elif self.__rank == 5:
            return "5"
        elif self.__rank == 6:
            return "6"
        elif self.__rank == 7:
            return "7"
        elif self.__rank == 8:
            return "8"
        elif self.__rank == 9:
            return "9"
        elif self.__rank == 10:
            return "10"
        elif self.__rank == 11:
            return "Jack"
        elif self.__rank == 12:
            return "Queen"
        else:
            return "King"

    # Define a method to determine the point value of a card based on its rank
    def GetPointValue(self):
        if self.__rank == 1:
            return 11
        elif self.__rank == 2:
            return 2
        elif self.__rank == 3:
            return 3
        elif self.__rank == 4:
            return 4
        elif self.__rank == 5:
            return 5
        elif self.__rank == 6:
            return 6
        elif self.__rank == 7:
            return 7
        elif self.__rank == 8:
            return 8
        elif self.__rank == 9:
            return 9
        elif self.__rank == 10:
            return 10
        elif self.__rank == 11:
            return 10
        elif self.__rank == 12:
            return 10
        else:
            return 10

# The main function
def main():

    # Create player objects
    player1 = Card()
    player2 = Card()

    # Set up counting variables
    player1Sum = 0
    player2Sum = 0

    # Write counting loop for five rounds of the game
    for i in range(1,6):

        # Print header for each round
        print("Round",i,"           Player 1            Player 2          ")
        print("-----------------------------------------------------------")

        # Call the class to get the suit, rank, and point value for each player
        suit1 = player1.GetSuitName()
        rank1 = player1.GetRankName()
        points1 = player1.GetPointValue()

        suit2 = player2.GetSuitName()
        rank2 = player2.GetRankName()
        points2 = player2.GetPointValue()

        # Sum the total points for each player
        player1Sum = player1Sum + points1
        player2Sum = player2Sum + points2

        # Print the results for each round
        print("Card:           ",rank1,"of",format(suit1,'8s'),"   ",rank2,"of",
              format(suit2,'8s'))
        print("Points Earned:  ", format(points1,'<5d'), "              ",
              format(points2,'<5d'))
        print("Total Points:   ", format(player1Sum,'<5d'),"              ",
              format(player2Sum,'<5d'))

        # Pick new cards for each player
        player1 = Card()
        player2 = Card()

        # Print a space between rounds
        print()

    # Print the winner of the game
    print("*****************************************************")
    print()

    if player1Sum > player2Sum:
        print("Player 1 is the winner!!")
    elif player1Sum < player2Sum:
        print("Player 2 is the winner!!")
    else:
        print("Its a tie!!")

# Call the main function
main()






    
        
