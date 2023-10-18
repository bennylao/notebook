class ChessBoard:
    def __init__(self):
        self.__whites = [Chess(9812, "e1"), Chess(9813, "d1"), Chess(9814, "a1"), Chess(9814, "h1"), Chess(9815, "c1"),
                         Chess(9815, "f1"), Chess(9816, "b1"), Chess(9816, "g1")]
        self.__blacks = [Chess(9818, "e8"), Chess(9819, "d8"), Chess(9820, "a8"), Chess(9821, "h8"), Chess(9821, "c8"),
                         Chess(9821, "f8"), Chess(9822, "b8"), Chess(9822, "g8")]
        for i in range(8):
            self.__whites.append(Chess(9817, chr(97 + i) + str(2)))
            self.__blacks.append(Chess(9823, chr(97 + i) + str(7)))

    def __display(self):
        chess_board = [[""] * 8 for i in range(8)]
        for chess in self.__whites:
            i, j = chess.translate_pos()
            chess_board[i][j] = chess.display()
        for chess in self.__blacks:
            i, j = chess.translate_pos()
            chess_board[i][j] = chess.display()
        row = ["|\t" + "\t|\t".join(col) + "\t|" for col in chess_board]
        chess_board = str("\n" + "-" * 65 + "\n").join(row)
        print(chess_board)

    def __checkmate(self, side):
        match side:
            case "w":
                if not any(chess.display() == chr(9818) for chess in self.__blacks):
                    return True
            case "b":
                if not any(chess.display() == chr(9812) for chess in self.__whites):
                    return True

    def __move_chess(self, start_pos, end_pos, side):
        # check if starting position and ending position are both on the board
        if not ("a" <= start_pos[0] <= "h" and "a" <= end_pos[0] <= "h" and
                1 <= int(start_pos[1]) <= 8 and 1 <= int(end_pos[1]) <= 8):
            return False
        ally_list = []
        enemy_list = []
        match side:
            case "w":
                ally_list = self.__whites
                enemy_list = self.__blacks
            case "b":
                ally_list = self.__blacks
                enemy_list = self.__whites
        for chess in ally_list:
            # check if there is ally on the starting position for moving
            # also check if there is another ally on the ending position, which blocks the move
            if chess.get_pos() == start_pos and not any(item.get_pos() == end_pos for item in ally_list):
                # check valid chess move
                chess.move(end_pos)
                for enemy in enemy_list:
                    if enemy.get_pos() == end_pos:
                        enemy_list.remove(enemy)
                        break
                return True
        else:
            return False

    def start_game(self):
        self.__display()
        is_win = False
        is_valid = False
        while is_win is False:
            print("White's Turn!")
            while is_valid is False:
                [white_start_pos, white_end_pos] = [
                    input("Please enter the position of the chest you wanna move from: ").lower(),
                    input("Please enter the position of the chest you wanna move to: ").lower()]
                is_valid = self.__move_chess(white_start_pos, white_end_pos, "w")
                if not is_valid:
                    print("move is invalid!")
            else:
                is_valid = False
                self.__display()
                if self.__checkmate("w"):
                    print("***Congratulations***")
                    print("White won!")
                    break

            print("Black's Turn!")
            while is_valid is False:
                [black_start_pos, black_end_pos] = [
                    input("Please enter the position of the chest you wanna move from: ").lower(),
                    input("Please enter the position of the chest you wanna move to: ").lower()]
                is_valid = self.__move_chess(black_start_pos, black_end_pos, "b")
                if not is_valid:
                    print("move is invalid!")
            else:
                is_valid = False
                self.__display()
                if self.__checkmate("b"):
                    print("***Congratulations***")
                    print("Black won!")
                    break


class Chess:
    def __init__(self, unicode, position):
        self.__unicode = unicode
        self.__position = position

    def get_pos(self):
        return self.__position

    def display(self):
        return chr(self.__unicode)

    def translate_pos(self):
        return 8 - int(self.__position[1]), ord(self.__position[0]) - 97

    def move(self, new_position):
        self.__position = new_position


if __name__ == "__main__":
    c = ChessBoard()
    c.start_game()
