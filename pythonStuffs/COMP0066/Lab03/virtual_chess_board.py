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
        chess_board = [[""] * 8 for _ in range(8)]
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

    def __move_pawn(self, start_pos, end_pos, side):
        ally_list = []
        enemy_list = []
        valid_moving_range = ()
        match side:
            case "w":
                ally_list = self.__whites
                enemy_list = self.__blacks
                valid_moving_range = (1, 2)
            case "b":
                ally_list = self.__blacks
                enemy_list = self.__whites
                valid_moving_range = (-1, -2)
        movement = int(end_pos[1]) - int(start_pos[1])
        if movement not in valid_moving_range:
            raise InvalidMoveException(end_pos)
        # pawn can move diagonally when there is an enemy
        if ord(end_pos[0]) - ord(start_pos[0]) == valid_moving_range[0] == movement:
            if not any(enemy.get_pos() == end_pos for enemy in enemy_list):
                raise InvalidMoveException(end_pos)
        else:
            if any(enemy.get_pos() == end_pos for enemy in enemy_list):
                raise InvalidMoveException(end_pos)
            if (movement == valid_moving_range[1] and
                    (any(enemy.get_pos() == end_pos[0] + str(int(end_pos[1]) - valid_moving_range[0])
                         for enemy in enemy_list) or
                     any(ally.get_pos() == end_pos[0] + str(int(end_pos[1]) - valid_moving_range[0])
                         for ally in ally_list))):
                raise InvalidMoveException(end_pos)

    @staticmethod
    def __check_rook(chess, new_pos, ally_list, enemy_list):
        if new_pos[0] != chess.get_pos()[0]:
            for i in range(min(ord(new_pos[0]), ord(chess.get_pos()[0])) + 1,
                           max(ord(new_pos[0]), ord(chess.get_pos()[0]))):
                if (any(ally.get_pos() == chr(i) + new_pos[1] for ally in ally_list) or
                        any(enemy.get_pos() == chr(i) + new_pos[1] for enemy in enemy_list)):
                    raise InvalidMoveException(new_pos)
        else:
            for i in range(min(int(new_pos[1]), int(chess.get_pos()[1])) + 1,
                           max(int(new_pos[1]), int(chess.get_pos()[1]))):
                if (any(ally.get_pos() == new_pos[0] + str(i) for ally in ally_list) or
                        any(enemy.get_pos() == chr(i) + new_pos[1] for enemy in enemy_list)):
                    raise InvalidMoveException(new_pos)

    @staticmethod
    def __check_bishop(chess, new_pos, ally_list, enemy_list):
        col_diff = ord(new_pos[0]) - ord(chess.get_pos()[0])
        row_diff = int(new_pos[1]) - int(chess.get_pos()[1])
        col_list = []
        row_list = []
        for i in range(min(ord(new_pos[0]), ord(chess.get_pos()[0])) + 1,
                       max(ord(new_pos[0]), ord(chess.get_pos()[0]))):
            col_list.append(chr(i))
        for i in range(min(int(new_pos[1]), int(chess.get_pos()[1])) + 1,
                       max(int(new_pos[1]), int(chess.get_pos()[1]))):
            row_list.append(str(i))
        if col_diff < 0:
            col_list.reverse()
        if row_diff < 0:
            row_list.reverse()
        move_path = list(map(lambda col, row: col + row, col_list, row_list))
        if (any(ally.get_pos() in move_path for ally in ally_list) or
                any(enemy.get_pos() in move_path for enemy in enemy_list)):
            raise InvalidMoveException(new_pos)

    # this function does not check the moves of pawn
    @staticmethod
    def __check_basic_move(chess, new_pos, ally_list, enemy_list):
        match chess.get_unicode():
            # moves of king
            case 9812 | 9818:
                if abs(ord(new_pos[0]) - ord(chess.get_pos()[0])) > 1 or abs(
                        int(new_pos[1]) - int(chess.get_pos()[1])) > 1:
                    raise InvalidMoveException(new_pos)
            # moves of queen
            case 9813 | 9819:
                if not (new_pos[0] == chess.get_pos()[0] or new_pos[1] == chess.get_pos()[1] or
                        abs(ord(new_pos[0]) - ord(chess.get_pos()[0])) == abs(ord(new_pos[1]) - ord(chess.get_pos()[1]))
                        ):
                    raise InvalidMoveException(new_pos)
                if abs(ord(new_pos[0]) - ord(chess.get_pos()[0])) == abs(ord(new_pos[1]) - ord(chess.get_pos()[1])):
                    ChessBoard.__check_bishop(chess, new_pos, ally_list, enemy_list)
                else:
                    ChessBoard.__check_rook(chess, new_pos, ally_list, enemy_list)

            # moves of rook
            case 9814 | 9820:
                if not (new_pos[0] == chess.get_pos()[0] or new_pos[1] == chess.get_pos()[1]):
                    raise InvalidMoveException(new_pos)
                ChessBoard.__check_rook(chess, new_pos, ally_list, enemy_list)

            # moves of bishop
            case 9815 | 9821:
                if not abs(ord(new_pos[0]) - ord(chess.get_pos()[0])) == abs(ord(new_pos[1]) - ord(chess.get_pos()[1])):
                    raise InvalidMoveException(new_pos)
                ChessBoard.__check_bishop(chess, new_pos, ally_list, enemy_list)

            # moves of knight
            case 9816 | 9822:
                row_move = abs(int(new_pos[1]) - int(chess.get_pos()[1]))
                col_move = abs(ord(new_pos[0]) - ord(chess.get_pos()[0]))
                if not (2 >= col_move >= 1 == abs(row_move - col_move) and 1 <= row_move <= 2):
                    raise InvalidMoveException(new_pos)

    def __move_chess(self, start_pos, end_pos, side):
        # check if starting position and ending position are both on the board
        if len(start_pos) != 2 or len(end_pos) != 2:
            return False
        elif not ("a" <= start_pos[0] <= "h" and "a" <= end_pos[0] <= "h" and
                  "1" <= start_pos[1] <= "8" and "1" <= end_pos[1] <= "8"):
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
            if chess.get_pos() == start_pos and not any(ally.get_pos() == end_pos for ally in ally_list):
                # check valid chess move
                try:
                    # if it is a pawn
                    if chess.get_unicode() == 9817 or chess.get_unicode() == 9823:
                        self.__move_pawn(start_pos, end_pos, side)
                        chess.move(end_pos)
                    else:
                        self.__check_basic_move(chess, end_pos, ally_list, enemy_list)
                        chess.move(end_pos)
                except InvalidMoveException as e:
                    print(e)
                    return False
                for enemy in enemy_list:
                    if enemy.get_pos() == end_pos:
                        enemy_list.remove(enemy)
                        break
                return True
        else:
            return False

    def start_game(self):
        self.__display()
        help_string = ("In each turn, player has to enter two positions." +
                       "The chess on the first specified position will move to the second position " +
                       "if they are valid.")
        is_win = False
        is_valid = False
        while is_win is False:
            print("White's Turn!")
            while is_valid is False:
                white_start_pos = input("Please enter the position of the chest you wanna move from: ").lower()
                if white_start_pos == "-help":
                    print(help_string)
                    continue
                white_end_pos = input("Please enter the position of the chest you wanna move to: ").lower()
                if white_end_pos == "-help":
                    print(help_string)
                    continue
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
                black_start_pos = input("Please enter the position of the chest you wanna move from: ").lower()
                if black_start_pos == "-help":
                    print(help_string)
                    continue
                black_end_pos = input("Please enter the position of the chest you wanna move to: ").lower()
                if black_end_pos == "-help":
                    print(help_string)
                    continue
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


class InvalidMoveException(Exception):
    """Raised when the move of the chess is not valid."""

    def __init__(self, new_pos):
        self.new_pos = new_pos
        super().__init__(f"Moving to {self.new_pos} is not valid!")


class Chess:
    def __init__(self, unicode, position):
        self.__unicode = unicode
        self.__position = position

    def get_pos(self):
        return self.__position

    def display(self):
        return chr(self.__unicode)

    def get_unicode(self):
        return self.__unicode

    def translate_pos(self):
        return 8 - int(self.__position[1]), ord(self.__position[0]) - 97

    def move(self, new_position):
        self.__position = new_position


if __name__ == "__main__":
    c = ChessBoard()
    c.start_game()
