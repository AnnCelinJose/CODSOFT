import random

board = [" " for _ in range(9)]

def print_board():
    print()
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("--+---+--")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("--+---+--")
    print(board[6] + " | " + board[7] + " | " + board[8])
    print()

def check_winner(player):
    win_conditions = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]

    for condition in win_conditions:
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
                print("Invalid move. Try again.")
        except ValueError:
            print("Please enter a number.")

def ai_move():
    win_conditions = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]

    for condition in win_conditions:
        positions = [board[i] for i in condition]

        if positions.count("O") == 2 and positions.count(" ") == 1:
            move = condition[positions.index(" ")]
            board[move] = "O"
            print("AI chose position", move + 1)
            return

    for condition in win_conditions:
        positions = [board[i] for i in condition]

        if positions.count("X") == 2 and positions.count(" ") == 1:
            move = condition[positions.index(" ")]
            board[move] = "O"
            print("AI chose position", move + 1)
            return

    if board[4] == " ":
        board[4] = "O"
        print("AI chose position 5")
        return

    available = [i for i in range(9) if board[i] == " "]
    move = random.choice(available)
    board[move] = "O"
    print("AI chose position", move + 1)

print("TIC-TAC-TOE AI")
print("You are X")
print("Positions are numbered 1-9")

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