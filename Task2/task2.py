# Tic-Tac-Toe Game with AI using Minimax

# Constants for players
HUMAN = 'X'
AI = 'O'
EMPTY = ' '

# Initialize board
def create_board():
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

# Display the board
def print_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)

# Check for winner
def check_winner(board, player):
    # Check rows, columns, and diagonals for a win
    win_states = [
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        [board[0][0], board[1][1], board[2][2]],
        [board[2][0], board[1][1], board[0][2]],
    ]
    return [player, player, player] in win_states

# Check if the board is full (draw)
def is_board_full(board):
    return all([cell != EMPTY for row in board for cell in row])

# Evaluate the board
def evaluate(board):
    if check_winner(board, AI):
        return 1  # AI wins
    elif check_winner(board, HUMAN):
        return -1  # Human wins
    else:
        return 0  # Draw

# Minimax algorithm
def minimax(board, depth, is_maximizing):
    score = evaluate(board)
    
    # Return score if the game is over
    if score == 1 or score == -1:
        return score
    if is_board_full(board):
        return 0
    
    # Maximizing player (AI)
    if is_maximizing:
        best_score = -float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = AI
                    score = minimax(board, depth + 1, False)
                    board[i][j] = EMPTY
                    best_score = max(best_score, score)
        return best_score
    
    # Minimizing player (Human)
    else:
        best_score = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = HUMAN
                    score = minimax(board, depth + 1, True)
                    board[i][j] = EMPTY
                    best_score = min(best_score, score)
        return best_score

# Find the best move for AI
def best_move(board):
    best_score = -float('inf')
    move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                board[i][j] = AI
                score = minimax(board, 0, False)
                board[i][j] = EMPTY
                if score > best_score:
                    best_score = score
                    move = (i, j)
    return move

# Main function to play the game
def play_game():
    board = create_board()
    print("Welcome to Tic-Tac-Toe!")
    print_board(board)
    
    while True:
        # Human move
        human_move = input("Enter your move (row and column): ").split()
        row, col = int(human_move[0]), int(human_move[1])
        if board[row][col] != EMPTY:
            print("Invalid move! Try again.")
            continue
        board[row][col] = HUMAN
        
        # Check if human won
        if check_winner(board, HUMAN):
            print_board(board)
            print("You win!")
            break
        if is_board_full(board):
            print_board(board)
            print("It's a draw!")
            break
        
        # AI move
        move = best_move(board)
        if move:
            board[move[0]][move[1]] = AI
        
        # Check if AI won
        if check_winner(board, AI):
            print_board(board)
            print("AI wins!")
            break
        if is_board_full(board):
            print_board(board)
            print("It's a draw!")
            break
        
        print_board(board)

# Start the game
play_game()
