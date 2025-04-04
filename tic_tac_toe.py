import math

def print_board(board):
    for row in board:
        print(" " + " | ".join(row))
        print("-" * 9)

def check_winner(board):
    # Check rows and columns for a winner
    for i in range(3):
        if board[i][0] != ' ' and board[i][0] == board[i][1] == board[i][2]:
            return board[i][0]
        if board[0][i] != ' ' and board[0][i] == board[1][i] == board[2][i]:
            return board[0][i]
    # Check diagonals
    if board[0][0] != ' ' and board[0][0] == board[1][1] == board[2][2]:
        return board[0][0]
    if board[0][2] != ' ' and board[0][2] == board[1][1] == board[2][0]:
        return board[0][2]
    return None

def is_draw(board):
    # It's a draw if there is no winner and no empty cells
    if check_winner(board) is None:
        for row in board:
            if ' ' in row:
                return False
        return True
    return False

def minimax(board, depth, is_maximizing):
    winner = check_winner(board)
    if winner == 'X':
        return 1
    elif winner == 'O':
        return -1
    elif is_draw(board):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    score = minimax(board, depth + 1, False)
                    board[i][j] = ' '
                    best_score = max(best_score, score)
        return best_score
    else:
        best_score = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    score = minimax(board, depth + 1, True)
                    board[i][j] = ' '
                    best_score = min(best_score, score)
        return best_score

def get_best_move(board, player):
    """
    Given the current board and the player ('X' or 'O'),
    return the best move as a tuple (row, col).
    """
    best_move = None
    if player == 'X':
        best_score = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    score = minimax(board, 0, False)
                    board[i][j] = ' '
                    if score > best_score:
                        best_score = score
                        best_move = (i, j)
    else:
        best_score = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    score = minimax(board, 0, True)
                    board[i][j] = ' '
                    if score < best_score:
                        best_score = score
                        best_move = (i, j)
    return best_move

def main():
    print("Welcome to Tic-Tac-Toe!")
    user_choice = ""
    while user_choice not in ['X', 'O']:
        user_choice = input("Do you want to play as X or O? ").upper().strip()
    ai_choice = 'O' if user_choice == 'X' else 'X'
    
    # X always goes first.
    current_turn = 'X'
    board = [[' ' for _ in range(3)] for _ in range(3)]
    
    print(f"You are {user_choice}, I am {ai_choice}.")
    
    while True:
        print("\nCurrent board:")
        print_board(board)
        
        # Check for terminal game state.
        winner = check_winner(board)
        if winner:
            if winner == user_choice:
                print("Congratulations! You win!")
            else:
                print("I win!")
            break
        if is_draw(board):
            print("It's a draw!")
            break
        
        if current_turn == user_choice:
            valid_move = False
            while not valid_move:
                try:
                    move = input("Enter your move (row column): ")
                    row_str, col_str = move.strip().split()
                    row, col = int(row_str) - 1, int(col_str) - 1  # convert to 0-based index
                    if row not in range(3) or col not in range(3):
                        print("Invalid move: row and column must be between 1 and 3.")
                        continue
                    if board[row][col] != ' ':
                        print("Invalid move: cell already occupied.")
                        continue
                    board[row][col] = user_choice
                    print(f"You played at ({row + 1}, {col + 1})")
                    valid_move = True
                except ValueError:
                    print("Invalid input format. Please enter row and column numbers separated by a space.")
        else:
            # AI's move using minimax algorithm.
            best_move = get_best_move(board, ai_choice)
            if best_move:
                board[best_move[0]][best_move[1]] = ai_choice
                print(f"I play at ({best_move[0] + 1}, {best_move[1] + 1})")
        
        # Switch turns.
        current_turn = 'O' if current_turn == 'X' else 'X'
    
    # Display final board.
    print("\nFinal board:")
    print_board(board)

main()