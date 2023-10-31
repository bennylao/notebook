import random
import logging


def generate_game(square):
    game = (" {square1} | {square2} | {square3} \n"
            "-----------\n"
            " {square4} | {square5} | {square6} \n"
            "-----------\n"
            " {square7} | {square8} | {square9} \n"
            "-----------\n"
            .format(square1=square[0], square2=square[1], square3=square[2],
                    square4=square[3], square5=square[4], square6=square[5],
                    square7=square[6], square8=square[7], square9=square[8]))
    print(game)


def check_is_win(string, square):
    is_win = False
    for i in range(0, 9, 3):
        if square[i] == string and square[i+1] == string and square[i+2] == string:
            is_win = True
    for i in range(3):
        if square[i] == string and square[i+3] == string and square[i+6] == string:
            is_win = True
    if (square[0] == string and square[4] == string and square[8] == string or
            (square[2] == string and square[4] == string and square[6] == string)):
        is_win = True

    return is_win


def tic_tac_toe():
    logging.info("tic-tac-toe-game initialised successfully!", )
    square = [" "] * 9
    available_position = list(range(1, 10))
    end = False
    generate_game(square)
    while " " in square and not end:
        while True:
            i = int(input("# Make your move ! [1-9] : "))
            if square[i - 1] == " " and 1 <= i <= 9:
                break
            print("Invalid number! Try again!")

        square[i - 1] = "O"
        if check_is_win("O", square):
            generate_game(square)
            print("*** Congratulations! You won! ***")
            break
        available_position.remove(i)
        j = random.choice(available_position)
        square[j-1] = "X"
        available_position.remove(j)
        generate_game(square)
        if check_is_win("X", square):
            print("*** You lost! ***")
            break


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, filename='output.log',
                        filemode ='w',
                        format='%(module)s - %(levelname)s - %(message)s')
    tic_tac_toe()
