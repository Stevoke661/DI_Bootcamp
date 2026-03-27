#The tic tac toe implementation
def display_board(board):
    """Prints the current 3x3 grid."""
    print("\n")
    for i in range(3):
        print(f" {board[i][0]} | {board[i][1]} | {board[i][2]} ")
        if i < 2:
            print("-----------")
    print("\n")

def player_input(board, player):
    """Gets and validates the player's move."""
    while True:
        try:
            move = input(f"Player {player}, enter your move (row and col 0-2, e.g., '0 1'): ")
            row, col = map(int, move.split())
            
            if row in range(3) and col in range(3):
                if board[row][col] == ' ':
                    return row, col
                else:
                    print("That square is already taken!")
            else:
                print("Invalid range! Please enter numbers between 0 and 2.")
        except ValueError:
            print("Invalid format! Enter two numbers separated by a space.")

def check_win(board, player):
    """Checks rows, columns, and diagonals for a win."""
    # Check Rows and Columns
    for i in range(3):
        if all([board[i][j] == player for j in range(3)]) or \
           all([board[j][i] == player for j in range(3)]):
            return True
    
    # Check Diagonals
    if (board[0][0] == board[1][1] == board[2][2] == player) or \
       (board[0][2] == board[1][1] == board[2][0] == player):
        return True
        
    return False

def check_tie(board):
    """Checks if the board is full with no winner."""
    for row in board:
        if ' ' in row:
            return False
    return True

def play():
    """Main game loop."""
    # Step 1: Initialize the board
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'
    game_over = False

    print("Welcome to Tic Tac Toe!")
    
    while not game_over:
        display_board(board)
        
        # Get move and update board
        row, col = player_input(board, current_player)
        board[row][col] = current_player
        
        # Check game state
        if check_win(board, current_player):
            display_board(board)
            print(f"Congratulations! Player {current_player} wins!")
            game_over = True
        elif check_tie(board):
            display_board(board)
            print("It's a tie!")
            game_over = True
        else:
            # Switch player: If X, go to O; if O, go to X.
            current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
    play()