class Sudoku:
    def __init__(self, board):
        self.board = board

    def is_valid_placement(self, row, col, box):
        if len([x for x in self.board[row] if x]) != len(set([x for x in self.board[row] if x])):
            return False

        if len([x[col] for x in self.board if x[col]]) != len(set([x[col] for x in self.board if x[col]])):
            return False

        box_list = []
        for i in range((box // 3) * 3, (box // 3) * 3 + 3):
            for j in range((box % 3) * 3, (box % 3) * 3 + 3):
                box_list.append(board[i][j])

        if len([x for x in box_list if x]) != len(set([x for x in box_list if x])):
            return False

        return True

    def display_board(self):
        for i in range(9):
            if i % 3 == 0 and i != 0:
                print('------------------------------')
            for j in range(9):
                if j % 3 == 0 and j != 0:
                    print('|  ', end='')

                if j == 8:
                    print(self.board[i][j])
                else:
                    if not self.board[i][j]:
                        print(' ', end='')
                    print(self.board[i][j], ' ', end='')

    def is_solved(self):
        if '' not in [x for row in self.board for x in row]:
            return True
        return False

    def find_empty(self):
        for row in range(9):
            for col in range(9):
                if self.board[row][col] == '':
                    return (row, col)

    def solve(self):
        if self.is_solved():
            self.display_board()
            return True

        row, col = self.find_empty()
        box = (row // 3) * 3 + (col // 3)

        for i in range(1, 10):
            self.board[row][col] = i

            if self.is_valid_placement(row, col, box):
                if self.solve():
                    return True

                self.board[row][col] = ''
            else:
                self.board[row][col] = ''

        return False


board = [
    [7, 8, '', 4, '', '', 1, 2, ''],
    [6, '', '', '', 7, 5, '', '', 9],
    ['', '', '', 6, '', 1, '', 7, 8],
    ['', '', 7, '', 4, '', 2, 6, ''],
    ['', '', 1, '', 5, '', 9, 3, ''],
    [9, '', 4, '', 6, '', '', '', 5],
    ['', 7, '', 3, '', '', '', 1, 2],
    [1, 2, '', '', '', 7, 4, '', ''],
    ['', 4, 9, 2, '', 6, '', '', 7]
]


sudoku = Sudoku(board)

sudoku.solve()
