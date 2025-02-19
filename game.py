import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def is_draw(board):
    return all(cell != " " for row in board for cell in row)

def minimax(board, is_maximizing):
    if check_winner(board, "O"):
        return 1
    if check_winner(board, "X"):
        return -1
    if is_draw(board):
        return 0

    if is_maximizing:
        best_score = -float("inf")
        for row in range(3):
            for col in range(3):
                if board[row][col] == " ":
                    board[row][col] = "O"
                    score = minimax(board, False)
                    board[row][col] = " "
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = float("inf")
        for row in range(3):
            for col in range(3):
                if board[row][col] == " ":
                    board[row][col] = "X"
                    score = minimax(board, True)
                    board[row][col] = " "
                    best_score = min(score, best_score)
        return best_score

def best_move(board):
    best_score = -float("inf")
    move = None
    for row in range(3):
        for col in range(3):
            if board[row][col] == " ":
                board[row][col] = "O"
                score = minimax(board, False)
                board[row][col] = " "
                if score > best_score:
                    best_score = score
                    move = (row, col)
    return move

def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]

    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while True:
        while True:
            try:
                move = int(input("Enter your move (1-9): ")) - 1
                row, col = divmod(move, 3)
                if board[row][col] == " ":
                    board[row][col] = "X"
                    break
                else:
                    print("Cell is already taken. Try again.")
            except (ValueError, IndexError):
                print("Invalid move. Enter a number between 1 and 9.")

        print_board(board)

        if check_winner(board, "X"):
            print("Congratulations! You win!")
            break

        if is_draw(board):
            print("It's a draw!")
            break

        print("AI is making its move...")
        ai_move = best_move(board)
        if ai_move:
            row, col = ai_move
            board[row][col] = "O"

        print_board(board)

        if check_winner(board, "O"):
            print("AI wins! Better luck next time.")
            break

        if is_draw(board):
            print("It's a draw!")
            break

if __name__ == "__main__":
    play_game()
