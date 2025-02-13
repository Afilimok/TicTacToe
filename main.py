from TicTacToe import TicTacToe


def main():
    board = TicTacToe()

    print(board)

    steps = ["X", "O", "X", "O", "X", "O", "X", "O", "X"]
    for step in steps:
        while True:
            try:
                x, y = map(int, input().split())
                if x < 1 or y < 1 or x > 3 or y > 3:
                    print("Coordinates should be from 1 to 3!")
                    continue
                messages = board.add(x - 1, y - 1, step)
                if messages == "":
                    break
                else:
                    print(messages)
            except ValueError:
                print("You should enter numbers!")

        print(board)
        check_message = board.full_check()
        if check_message in ["X wins", "O wins", "Draw"]:
            print(check_message)
            break


if __name__ == "__main__":
    main()
