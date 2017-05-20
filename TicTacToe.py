# current_board stores the current state of the board. It's a list of lists
current_board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

def draw_board():
    for outer_index in range(3):
        to_print = ""
        for inner_index in range(3):
            to_print += current_board[outer_index][inner_index]
            if inner_index != 2:
                to_print += " | "
        print(to_print)
        if outer_index != 2:
            print("--+---+--")


def check_victory(symbol, last_move_row, last_move_col):
    if check_horizontal(last_move_row, symbol):
        return True
    if check_vertical(last_move_col, symbol):
        return True
    if (last_move_row == 1 and last_move_col == 1) or (last_move_row == 0 and last_move_col == 0) or (last_move_row == 2 and last_move_col ==2):
        if check_diagonal(symbol):
            return True
    if (last_move_row == 0 and last_move_col == 2) or (last_move_row == 2 and last_move_col == 0):
        if check_diagonal(symbol):
            return True


def check_horizontal(row_number, symbol):
    if current_board[row_number][0] == symbol and current_board[row_number][1] == symbol and current_board[row_number][2] == symbol:
        return True
    return False


def check_vertical(col_number, symbol):
    if current_board[0][col_number] == symbol and current_board[1][col_number] == symbol and current_board[2][col_number] == symbol:
        return True
    return False


def check_diagonal(symbol):
    if current_board[0][0] == symbol and current_board[1][1] == symbol and current_board[2][2] == symbol:
        return True

    if current_board[0][2] == symbol and current_board[1][1] == symbol and current_board[2][0] == symbol:
        return True

    return False


def user_input(symbol):
    while True:
        coor_row = input("please enter the row you wish to put your symbol")
        coor_col = input("please enter the column you wish to put your symbol")

        if int(coor_row) > 2 or int(coor_col) > 2 or int(coor_row) < 0 or int(coor_col) < 0:
            print("invalid input! The column and row must be between 0 and 2")
            continue
        if current_board[int(coor_row)][int(coor_col)] == " ":
            current_board[int(coor_row)][int(coor_col)] = symbol
            break
        else:
            print("that space is already occupied! try again")
            continue
    return coor_row, coor_col


def main():
    player1_turn = True
    player1_moves = 0
    # player1 will be O
    player2_moves = 0
    # player2 will be X
    move_tuple = ()
    while True:
        
        draw_board()
        if player1_moves >= 3 and player1_turn is False:
            if check_victory("O", int(move_tuple[0]), int(move_tuple[1])):
                print("Player 1 wins!")
                break

        if player2_moves >= 3 and player1_turn is True:
            if check_victory("X", int(move_tuple[0]), int(move_tuple[1])):
                print("Player 2 wins!")
                break

        if player1_moves + player2_moves == 9:
            print("The game is tied!")
            break
        
        if (player1_turn):
            print("Player 1's turn")
            move_tuple = user_input("O")
            player1_moves += 1
            player1_turn = False
        else:
            print("Player2's turn")
            move_tuple = user_input("X")
            player2_moves += 1
            player1_turn = True
    draw_board()


main()
