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

    def __contains(self, num):
        for arr in self.__board:
            for current in arr:
                if current == num:
                    return True
        return False


def main():
    magic_square = MagicSquare(3)


if __name__ == "__main__":
    main()
