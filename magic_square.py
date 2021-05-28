class MagicSquare:
    def __init__(self, size):
        if size < 3:
            raise Exception("Size must be 3 or greater.")
        self.__size = size
        self.__magic_constant = int(((size ** 3) + size) / 2)
        self.__board = [[0 for i in range(size)] for j in range(size)]

    def __place(self, row, col, num):
        self.__board[row][col] = num

    def __remove(self, row, col):
        self.__board[row][col] = 0

    # Sequential search; consider alternatives for 2D array?
    def __contains(self, num):
        for arr in self.__board:
            for current in arr:
                if current == num:
                    return True
        return False

    def __check_neg_diag(self, row, col, num):
        if row != col:
            return True
        sum = 0
        for i in range(self.__size):
            sum += self.__board[i][i]
        if (row == (self.__size - 1)) and ((num + sum) != self.__magic_constant):
            return False
        return sum <= self.__magic_constant

    def __check_pos_diag(self, row, col, num):
        if (row + col) != (self.__size - 1):
            return True
        sum = 0
        r = self.__size - 1
        for c in range(self.__size):
            sum += self.__board[r][c]
            r -= 1
        if (col == (self.__size - 1)) and ((num + sum) != self.__magic_constant):
            return False
        return sum <= self.__magic_constant

    def __check_valid(self, row, col, num):
        if (self.__board[row][col] != 0) or self.__contains(num):
            return False
        if not (self.__check_neg_diag(row, col, num) and self.__check_pos_diag(row, col, num)):
            return False


def main():
    magic_square = MagicSquare(3)


if __name__ == "__main__":
    main()
