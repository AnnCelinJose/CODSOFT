import random

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


def print_board(board):
    print()
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("--+---+--")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("--+---+--")
    print(board[6] + " | " + board[7] + " | " + board[8])
    print()


def check_winner(board, player):
    for condition in WINS:
        if all(board[i] == player for i in condition):
            return True
    return False


def board_full(board):
    return " " not in board


def player_move(board):
    while True:
        try:
            move = int(input("Enter position (1-9): ")) - 1

            if 0 <= move <= 8 and board[move] == " ":
                board[move] = "X"
                break
            else:
                print("Invalid move. Try again.")

        except ValueError:
            print("Please enter a number.")


# ---------- EASY AI ----------

def easy_ai(board):
    available = [i for i in range(9) if board[i] == " "]
    move = random.choice(available)

    print("\nAI Strategy: Choosing a random move.")
    board[move] = "O"
    print("AI chose position", move + 1)


# ---------- MINIMAX ----------

def minimax(board, is_maximizing):

    if check_winner(board, "O"):
        return 1

    if check_winner(board, "X"):
        return -1

    if board_full(board):
        return 0

    if is_maximizing:
        best_score = -100

        for i in range(9):
            if board[i] == " ":
                board[i] = "O"

                score = minimax(board, False)

                board[i] = " "
                best_score = max(best_score, score)

        return best_score

    else:
        best_score = 100

        for i in range(9):
            if board[i] == " ":
                board[i] = "X"

                score = minimax(board, True)

                board[i] = " "
                best_score = min(best_score, score)

        return best_score


def impossible_ai(board):

    best_score = -100
    best_move = -1

    print("\nAI is thinking...")

    for i in range(9):
        if board[i] == " ":
            board[i] = "O"

            score = minimax(board, False)

            board[i] = " "

            if score > best_score:
                best_score = score
                best_move = i

    if best_score == 1:
        print("AI Strategy: Found a winning move.")
    elif best_score == 0:
        print("AI Strategy: Preventing defeat and aiming for a draw.")
    else:
        print("AI Strategy: Searching for the best possible move.")

    print("Move Score:", best_score)

    board[best_move] = "O"
    print("AI chose position", best_move + 1)


# ---------- GAME ----------

print("===== TIC-TAC-TOE AI =====")
print("You are X")
print_positions()

while True:

    board = [" " for _ in range(9)]

    print("Difficulty Levels")
    print("1. Easy")
    print("2. Impossible")

    choice = input("Choose difficulty (1 or 2): ")

    while True:

        print_board(board)

        player_move(board)

        if check_winner(board, "X"):
            print_board(board)
            print("Congratulations! You Win!")
            break

        if board_full(board):
            print_board(board)
            print("It's a Draw!")
            break

        if choice == "1":
            easy_ai(board)
        else:
            impossible_ai(board)

        if check_winner(board, "O"):
            print_board(board)
            print("AI Wins!")
            break

        if board_full(board):
            print_board(board)
            print("It's a Draw!")
            break

    again = input("\nPlay again? (y/n): ").lower()

    if again != "y":
        print("Thank you for playing!")
        break
