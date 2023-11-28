def print_board(board):
    for row in board:
        print(' '.join(row))
    print()

def is_valid_move(board, row, col):
    return 0 <= row < 3 and 0 <= col < 3 and board[row][col] == ' '

def is_winner(board, player):
    # Check rows and columns
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True

    # Check diagonals
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def is_board_full(board):
    return all(board[i][j] != ' ' for i in range(3) for j in range(3))

def evaluate_board(board):
    if is_winner(board, 'O'):
        return 1
    elif is_winner(board, 'X'):
        return -1
    else:
        return 0

def minimax(board, depth, is_max):
    score = evaluate_board(board)

    if score == 1:
        return score

    if score == -1:
        return score

    if is_board_full(board):
        return 0

    if is_max:
        best = float('-inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    best = max(best, minimax(board, depth + 1, not is_max))
                    board[i][j] = ' '
        return best
    else:
        best = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    best = min(best, minimax(board, depth + 1, not is_max))
                    board[i][j] = ' '
        return best

def find_best_move(board):
    best_val = float('-inf')
    best_move = (-1, -1)

    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'O'
                move_val = minimax(board, 0, False)
                board[i][j] = ' '

                if move_val > best_val:
                    best_move = (i, j)
                    best_val = move_val

    row, col = best_move
    board[row][col] = 'O'

def play_game():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    player_turn = True

    print("Tic Tac Toe - You are X, and the computer is O")

    while True:
        print_board(board)

        if player_turn:
            # Player's turn
            row, col = map(int, input("Enter row (0-2) and column (0-2) to make a move (e.g., 1 2): ").split())

            if is_valid_move(board, row, col):
                board[row][col] = 'X'
                player_turn = False  # Switch to computer's turn
            else:
                print("Invalid move. Try again.")
        else:
            # Computer's turn
            find_best_move(board)
            player_turn = True  # Switch to player's turn

        # Check if there is a winner or if the board is full
        if is_winner(board, 'X'):
            print_board(board)
            print("Congratulations! You win!")
            break
        elif is_winner(board, 'O'):
            print_board(board)
            print("Computer wins! Better luck next time.")
            break
        elif is_board_full(board):
            print_board(board)
            print("It's a draw!")
            break

if __name__ == "__main__":
    play_game()
