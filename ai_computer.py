import random

board = [["-", "-", "-"],
         ["-", "-", "-"],
         ["-", "-", "-"]]
current_player = "X"
winner = None
game_running = True
num_of_simulations = 0

#print the game board
def print_board():
    print("\n  1  2  3")
    print("1 "+ board[0][0] + "  " + board[0][1] + "  " + board[0][2])
    print("2 "+ board[1][0] + "  " + board[1][1] + "  " + board[1][2])
    print("3 "+ board[2][0] + "  " + board[2][1] + "  " + board[2][2])

# take player input
def player_input():
    global board, current_player, game_running
    move = input("\nEnter your move (format: row col): " )
    while True:
        if len(move) == 3 and move[0].isdigit and move[1] == " " and move[2].isdigit:
            if int(move[0])-1 in range(3) and int(move[2])-1 in range(3):
                row = int(move[0])-1
                col = int(move[2])-1
                if board[row][col] == "-":
                    board[row][col] = current_player
                    print("\nYour Move: ")
                    print_board()
                    end_check(board)
                    print("\nPlease wait for the Computer's move...")
                    return
                else:
                    print_board()
                    print("\nSpot is already take! Please enter an open spot")
                    move = input("Enter your move (format: row col): " )
            else:
                print_board()
                print("\nPlease enter a valid input (example: 1 2)")
                move = input("Enter your move (format: row col): " )
        else:
            print_board()
            print("\nPlease enter a valid input (example: 1 2)")
            move = input("Enter your move (format: row col): " )

# check if board is full ends
def no_moves(board):
    if any("-" in row for row in board):
        return False
    else:
        return True

# check if game ended. win, loss, tie.   
def end_check(pan):
    global winner, game_running
    for i in range(3):
        if pan[i][0] == pan[i][1] and pan[i][1] == pan[i][2] and pan[i][0]!= "-":
            winner = pan[i][0]
            game_running = False
            return
        elif pan[0][i] == pan[1][i] and pan[1][i] == pan[2][i] and pan[0][i] != "-":
            winner = pan[0][i]
            game_running = False
            return
        elif all(pan[i][i] == "X" for i in range(3)) or all(pan[i][i] == "O" for i in range(3)) or all(pan[i][abs(2-i)] == "X" for i in range(3)) or all(pan[i][abs(2-i)] == "O" for i in range(3)):
            winner = pan[1][1]
            game_running = False
            return
    if no_moves(pan) == True:
        winner = "Tie"
        game_running = False
        return

# print winner from player perspective.
def print_winner():
    global winner
    if winner == "X":
        print_board()
        print("\nYou Win!")
    elif winner == "O":
        print_board()
        print("\nYou Lose!")
    elif winner == "Tie":
        print_board()
        print("\nIt's a Tie!")

# switch the player.
def switch_player():
    global current_player
    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"
    return

# functions for the computer to evaluate the board.

# evaluates the possible moves on the board and returns a new list.
def possible_moves(board):
    copy_of_board = [row[:] for row in board]
    moves = []
    for i in range(3):
        for j in range(3):
            if copy_of_board[i][j] == "-":
                moves.append([i, j])
    return moves

# restarts the board and game_running variable.
def restart():
    global board, game_running, winner
    board = [["-", "-", "-"],
        ["-", "-", "-"],
        ["-", "-", "-"]] 
    game_running = True
    winner = None

# simulates random positions and their outcomes and assigns a score to each possible next move.
# returns a tuple of the spot with the highest assigned score (computer most likely to win).
def best_next():
    global game_running, winner, current_player
    evaluations = {}
    for i in range(num_of_simulations):    
        current_player = "O"
        copy_of_board = [row[:] for row in board]
        score = 0
        moves = possible_moves(board)
        move = random.choice(moves)
        first_move = tuple(move)
        while winner == None:
            row = move[0]
            col = move[1]
            copy_of_board[row][col] = current_player            
            end_check(copy_of_board)
            if winner != None:
                break
            moves.remove(move)
            move = random.choice(moves)
            switch_player()
        if winner == "X":
            score = -1
        elif winner == "O":
            score = 1
        # weigh the score for a tie so that when the computer is given an ultimatum between winning with a risk to lose and drawing, the computre will choose to draw.
        elif winner == "Tie":
            score = 0.2
        if first_move in evaluations:
            evaluations[first_move] += score
        else:
            evaluations[first_move] = score
        winner = None
        game_running = True
    for key, value in evaluations.items():
        evaluations[key] = value
    current_player = "X"
    best_spot = max(evaluations, key=evaluations.get)
    return best_spot

# function that automatically plays the computer's move based on the best_next return value.
def ai_make_move():
    global current_player, board
    best_move = best_next()
    print("\nComputer's Move: ")
    board[best_move[0]][best_move[1]] = "O"

# sets the number of simulations based on the difficulty that the user desires. 
# higher number of simulations result in better accuracy for the computer algorithm, and therefore higher difficulty
def difficulty():
    global num_of_simulations
    level = input("\nPlease choose a difficulty level:\n\t (a) Easy\n\t (b) Medium\n\t (c) Hard\n\t (d) Extremely Hard\nType either a, b, c, or d: ")
    if level == "a":
        lvl = "Easy" 
        num_of_simulations = 10
    elif level == "b":
        lvl = "Medium"
        num_of_simulations = 50
    elif level == "c":
        lvl = "Hard"
        num_of_simulations = 1000
    elif level == "d":
        lvl = "Extremely Hard"
        num_of_simulations = 100000
    print(f"\nTic-Tac-Toe vs. computer mode - {lvl}")

# main function for the game play
def game_play():
    difficulty()
    while game_running == True:
        print_board()
        player_input()
        end_check(board)
        if winner != None:
            print_winner()
            break
        ai_make_move()
        end_check(board)
        if winner != None:
            print_winner()
            break

if __name__ == "__main__":
    game_play()
