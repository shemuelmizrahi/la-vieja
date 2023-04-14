from enum import Enum

from constyle import Attributes, Style

red = Style(Attributes.RED)
blue = Style(Attributes.BLUE)
grey = Style(Attributes.GREY)

X = red("X")
O = blue("O")


class State(Enum):
    X_WINS = X
    O_WINS = O
    DRAW = "D"
    PLAYING = " "


def print_board(board: list[str]) -> None:
    print(" " + board[0] + " | " + board[1] + " | " + board[2] + " ")
    print("---+---+---")
    print(" " + board[3] + " | " + board[4] + " | " + board[5] + " ")
    print("---+---+---")
    print(" " + board[6] + " | " + board[7] + " | " + board[8] + " ")
    print()


def state(board: list[str]) -> State:
    for a, b, c in [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6),
    ]:
        if board[a] == board[b] == board[c] and (board[a] == X or board[a] == O):
            return State(board[a])

    return (
        State.PLAYING
        if any(square != X and square != O for square in board)
        else State.DRAW
    )


def input_position(board: list[str]) -> int:
    while True:
        position = int(input("Enter a number between 1 and 9: ")) - 1
        if position < 0 or position > 8:
            print("Error: Number is not between 1 and 9")
            continue
        if board[position] == X or board[position] == O:
            print("Error: That square is already full")
            continue
        return position


def play_turn(board: list[str], turn: str) -> None:
    print("\n" * 40)
    print_board(board)
    print(f"It's {turn} turn")
    position = input_position(board)
    board[position] = turn


def play_game() -> None:
    turn: str = X
    board: list[str] = list(grey(str(n)) for n in range(1, 10))
    current_state: State = state(board)
    while current_state == State.PLAYING:
        play_turn(board, turn)
        turn = O if turn == X else X
        current_state = state(board)

    print_board(board)
    print("Game over!")
    if current_state == State.DRAW:
        print("It's a draw :(")
    else:
        print(f"{current_state.value} wins!")


while True:
    play_game()
    if input("Play again? [Y/n] ").lower()[:1] == "n":
        break
