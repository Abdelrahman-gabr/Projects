#File:    Tic TAC TOC game
#purpose: The player who has 3 numbers there sum = 15 wins
#Authour: Abdelrahman Mohamed Gabr  
#ID:      20231098

# Welcome message and game rules
print("Welcome to Tic TAC TOC game")
print("The player who has 3 numbers whose sum equals 15 wins")
print("Player 1 takes odd numbers from 1 to 9")
print("Player 2 takes even numbers from 0 to 8")
print("NOTE: Numbers cannot be chosen twice")
print()

# Initial board setup
board = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
print(board[0] + "|" + board[1] + "|" + board[2])
print(board[3] + "|" + board[4] + "|" + board[5])
print(board[6] + "|" + board[7] + "|" + board[8])
print()

# Define player number choices and other game variables
player_1_nums = [1, 3, 5, 7, 9]
player_2_nums = [0, 2, 4, 6, 8]
chosen_nums = []
positions = []
x = 0
i = 0

# Main game loop
while i < 5:
    # Player 1's turn
    while True:
        pl1_pick = input("Player 1, choose an odd number from 1 to 9: ")
        try:
            pl1_pick = int(pl1_pick)
        except ValueError:
            print("ERROR: Please select a valid number")

        if pl1_pick in player_1_nums:
            if pl1_pick in chosen_nums:
                print("Number was already chosen, please select another number")
            else:
                while True:
                    po = int(input("Choose a position from 1 to 9: ")) - 1
                    if po in positions:
                        print("Position already chosen, please select another")
                    else:
                        positions.append(po)
                        chosen_nums.append(pl1_pick)
                        board[po] = str(pl1_pick)
                        print(board[0] + "|" + board[1] + "|" + board[2])
                        print(board[3] + "|" + board[4] + "|" + board[5])
                        print(board[6] + "|" + board[7] + "|" + board[8])

                        # Check win condition after three turns
## As nunbers represent string so i change each to equvilant ASKII then add them if sum == ASKII of 15 (159) so i cheek the condition of win

                        if i >= 2:
                            if (ord(board[0]) + ord(board[1]) + ord(board[2]) == 159 or
                                    ord(board[0]) + ord(board[4]) + ord(board[8]) == 159 or
                                    ord(board[0]) + ord(board[3]) + ord(board[6]) == 159 or
                                    ord(board[1]) + ord(board[4]) + ord(board[7]) == 159 or
                                    ord(board[2]) + ord(board[5]) + ord(board[8]) == 159 or
                                    ord(board[2]) + ord(board[4]) + ord(board[6]) == 159 or
                                    ord(board[3]) + ord(board[4]) + ord(board[5]) == 159 or
                                    ord(board[6]) + ord(board[7]) + ord(board[8]) == 159):
                                print("Player 1 wins!")
                                x = 1
                                break
                        break
            break
        else:
            print("ERROR: Please choose an odd number from 1 to 9")

    if x == 1:
        break
    if i == 4:
        print("Game ends in a draw!")
        break

    # Player 2's turn
    while True:
        pl2_pick = input("Player 2, choose an even number from 0 to 8: ")
        try:
            pl2_pick = int(pl2_pick)
        except ValueError:
            print("ERROR: Please select a valid number")

        if pl2_pick in player_2_nums:
            if pl2_pick in chosen_nums:
                print("Number was already chosen, please select another number")
            else:
                while True:
                    po = int(input("Choose a position from 1 to 9: ")) - 1
                    if po in positions:
                        print("Position already chosen, please select another")
                    else:
                        positions.append(po)
                        chosen_nums.append(pl2_pick)
                        board[po] = str(pl2_pick)
                        print(board[0] + "|" + board[1] + "|" + board[2])
                        print(board[3] + "|" + board[4] + "|" + board[5])
                        print(board[6] + "|" + board[7] + "|" + board[8])

                        # Check win condition after three turns
                        if i >= 2:
                            if (ord(board[0]) + ord(board[1]) + ord(board[2]) == 159 or
                                    ord(board[0]) + ord(board[4]) + ord(board[8]) == 159 or
                                    ord(board[0]) + ord(board[3]) + ord(board[6]) == 159 or
                                    ord(board[1]) + ord(board[4]) + ord(board[7]) == 159 or
                                    ord(board[2]) + ord(board[5]) + ord(board[8]) == 159 or
                                    ord(board[2]) + ord(board[4]) + ord(board[6]) == 159 or
                                    ord(board[3]) + ord(board[4]) + ord(board[5]) == 159 or
                                    ord(board[6]) + ord(board[7]) + ord(board[8]) == 159):
                                print("Player 2 wins!")
                                x = 1
                                break
                        break
            break
        else:
            print("ERROR: Please choose an even number from 0 to 8")

    if x == 1:
        break
    if i == 4:
        print("Game ends in a draw!")
        break

    i += 1