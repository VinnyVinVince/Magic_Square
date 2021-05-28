class MagicSquare:
    def __init__(self, size):
        if size < 3:
            raise Exception("Size is too small.")
        self.__magic_constant = int(((size ** 3) + size) / 2)
        self.__board = [[-1 for i in range(size)] for j in range(size)]

    def get_size(self):
        return len(self.__board)

    def remove(self, row, col):
        self.__board[row][col] = 0


def main():
    magic_square = MagicSquare(3)


if __name__ == "__main__":
    main()
