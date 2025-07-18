def print_board(board):
    print("\n")
    for row in board:
        print(" | ".join(row))
        print("-" * 9)
    print("\n")

def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(row[col] == player for row in board):
            return True
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_draw(board):
    return all(cell in ['X', 'O'] for row in board for cell in row)

def get_move(player):
    while True:
        try:
            move = input(f"Player {player}, enter your move (row and column: 1 1): ").split()
            if len(move) != 2:
                raise ValueError("Enter two numbers.")
            row, col = map(int, move)
            if not (1 <= row <= 3 and 1 <= col <= 3):
                raise ValueError("Numbers must be between 1 and 3.")
            return row - 1, col - 1
        except ValueError as e:
            print(f"Invalid input: {e}. Try again.")

def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    print("Welcome to Tic Tac Toe!")
    print_board(board)
    while True:
        row, col = get_move(current_player)
        if board[row][col] != " ":
            print("Cell already taken. Try a different move.")
            continue
        board[row][col] = current_player
        print_board(board)
        if check_winner(board, current_player):
            print(f"Player {current_player} wins!")
            break
        if is_draw(board):
            print("It's a draw!")
            break
        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    main()
