import string

class TicTacToe:
    def __init__(self):
        self.board = [[" " for _ in range(3)] for _ in range(3)]

    def __str__(self) -> string:
        s = "---------\n"
        for i in range(3):
            for j in range(3):
                if j == 0:
                    s += "|"
                s += " " + str(self.board[i][j])
                if j == 2:
                    s += " |\n"

        s += "---------"
        return s

    def load_board(self, state):
        # print([[state[i * 3 + j] for j in range(3)] for i in range(3)])
        self.board = [[state[i * 3 + j] for j in range(3)] for i in range(3)]

    def winner(self, char) -> bool:
        return any(
            all(self.board[i][j] == char for j in range(3)) or  # Rows
            all(self.board[j][i] == char for j in range(3))  # Columns
            for i in range(3)
        ) or all(self.board[i][i] == char for i in range(3)) or all(self.board[i][2 - i] == char for i in range(3))

    def full_check(self) -> string:
        won_x = self.winner("X")
        won_o = self.winner("O")
        sum_x = sum(1 for i in range(3) for j in range(3) if self.board[i][j] == 'X')
        sum_o = sum(1 for i in range(3) for j in range(3) if self.board[i][j] == 'O')

        free_space = sum(1 for i in range(3) for j in range(3) if self.board[i][j] == '_' or self.board[i][j] == ' ')

        # print("freeSpace", free_space)
        if won_x and won_o:
            return "Impossible"
        if abs(sum_o - sum_x) > 1:
            return "Impossible"
        if won_o:
            return "O wins"
        if won_x:
            return "X wins"
        if not won_o and not won_x and free_space == 0:
            return "Draw"
        return "Game not finished"



    def add(self, x: int, y: int, chat: string) -> string:
        if self.board[x][y] in [" ", "_"]:
            self.board[x][y] = chat
            return ""
        return "This cell is occupied! Choose another one!"
