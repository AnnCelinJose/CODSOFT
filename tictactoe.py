import random

board = [" " for _ in range(9)]

WINS = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8],
    [0, 3, 6], [1, 4, 7], [2, 5, 8],
    [0, 4, 8], [2, 4, 6]
]


def print_positions():
    print("\nPositions:")
    print("1 | 2 | 3")
    print("--+---+--")
    print("4 | 5 | 6")
    print("--+---+--")
    print("7 | 8 | 9\n")


def print_board():
    print()
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("--+---+--")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("--+---+--")
    print(board[6] + " | " + board[7] + " | " + board[8])
    print()


def check_winner(player):
    for condition in WINS:
        if all(board[i] == player for i in condition):
            return True
    return False


def board_full():
    return " " not in board


def player_move():
    while True:
        try:
            move = int(input("Enter position (1-9): ")) - 1

            if 0 <= move <= 8 and board[move] == " ":
                board[move] = "X"
                break
            else:
                print("Invalid move.")
        except ValueError:
            print("Please enter a number.")


# ---------- MINIMAX ----------

def minimax(is_maximizing):

    if check_winner("O"):
        return 1

    if check_winner("X"):
        return -1

    if board_full():
        return 0

    if is_maximizing:
        best = -100

        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(False)
                board[i] = " "
                best = max(best, score)

        return best

    else:
        best = 100

        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(True)
                board[i] = " "
                best = min(best, score)

        return best


def ai_move():

    best_score = -100
    move = -1

    print("\nAI is thinking...")

    for i in range(9):
        if board[i] == " ":
            board[i] = "O"

            score = minimax(False)

            board[i] = " "

            if score > best_score:
                best_score = score
                move = i

    # Strategy explanation
    if move == 4:
        print("Strategy: Taking the center.")

    else:
        print("Strategy: Calculating the best move using Minimax.")

    board[move] = "O"
    print("AI chose position", move + 1)


# ---------- GAME ----------

print("TIC-TAC-TOE AI")
print("You are X")
print_positions()

while True:

    print_board()

    player_move()

    if check_winner("X"):
        print_board()
        print("You Win!")
        break

    if board_full():
        print_board()
        print("It's a Draw!")
        break

    ai_move()

    if check_winner("O"):
        print_board()
        print("AI Wins!")
        break

    if board_full():
        print_board()
        print("It's a Draw!")
        break
