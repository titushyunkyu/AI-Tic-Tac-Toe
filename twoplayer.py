board = [["-", "-", "-"],
         ["-", "-", "-"],
         ["-", "-", "-"]]
current_player = "X"
winner = None
game_running = True

#print the game board
def print_board(board):
    print("\n  1  2  3")
    print("1 "+ board[0][0] + "  " + board[0][1] + "  " + board[0][2])
    print("2 "+ board[1][0] + "  " + board[1][1] + "  " + board[1][2])
    print("3 "+ board[2][0] + "  " + board[2][1] + "  " + board[2][2])

# take player input
def player_input():
    global board, current_player, game_running
    print(f"\nPlayer {current_player}'s turn")
    move = input("Enter your move (format: row col): " )
    while True:
        if len(move) == 3 and move[0].isdigit and move[1] == " " and move[2].isdigit:
            if int(move[0])-1 in range(3) and int(move[2])-1 in range(3):
                row = int(move[0])-1
                col = int(move[2])-1
                if board[row][col] == "-":
                    board[row][col] = current_player
                    end_check(board)
                    return
                else:
                    print_board(board)
                    print("Spot is already take! Please enter an open spot")
                    move = input("Enter your move (format: row col): " )
            else:
                print("\nPlease enter a valid input (example: 1 2)")
                move = input("Enter your move (format: row col): " )
        else:
            print("\nPlease enter a valid input (example: 1 2)")
            move = input("Enter your move (format: row col): " )
        
#check for win or tie
def end_check(board):
    global winner, game_running
    for i in range(3):
        if board[i][0] == board[i][1] and board[i][1] == board[i][2] and board[i][0]!= "-":
            winner = board[i][0]
            print_board(board)
            print(f"\nPlayer {current_player} is the winner!")
            game_running = False
            return
        elif board[0][i] == board[1][i] and board[1][i] == board[2][i] and board[0][i] != "-":
            winner = board[0][i]
            print_board(board)
            print(f"\nPlayer {current_player} is the winner!")
            game_running = False
            return
        elif all(board[i][i] == current_player for i in range(3)) or all(board[i][abs(2-i)] == current_player for i in range(3)):
            winner = board[1][1]
            print_board(board)
            print(f"\nPlayer {current_player} is the winner!")
            game_running = False
            return
    if not any("-" in row for row in board):
        game_running = False
        print("\nIt's a tie!")
        return

# switch the player
def switch_player():
    global current_player
    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"

# main game_play function calling all the functions in the right order.
def game_play():
    global game_running, board
    while game_running == True:
        print_board(board)
        player_input()
        switch_player()

# restarts the board and game_running variable.
def restart():
    global board, game_running
    board = [["-", "-", "-"],
        ["-", "-", "-"],
        ["-", "-", "-"]] 
    game_running = True

if __name__ == "__main__":
    game_play()