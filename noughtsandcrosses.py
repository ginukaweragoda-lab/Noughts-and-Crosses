import random
import os.path
import json

random.seed()

def draw_board(board):
    
    print("-------------")
    for row in board:
        print("| " + " | ".join(row) + " |")
        print("-------------")

def welcome(board):
    
    print("Welcome to Tic-Tac-Toe!")
    draw_board(board)

def initialise_board(board):
    
    return [[' ' for _ in range(3)] for _ in range(3)]

def get_player_move(board):
    
    while True:
        try:
            move = int(input("Enter your move (1-9): "))
            if move < 1 or move > 9:
                print("Invalid input. Please enter a number between 1 and 9.")
                continue
            
            row, col = divmod(move - 1, 3)  
            if board[row][col] == ' ':
                return row, col
            else:
                print("Cell already occupied. Try again.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 9.")

def choose_computer_move(board):
    
    while True:
        row, col = random.randint(0, 2), random.randint(0, 2)
        if board[row][col] == ' ':
            return row, col

def check_for_win(board, mark):
    
    for row in range(3):
        if all([cell == mark for cell in board[row]]):
            return True
    for col in range(3):
        if all([board[row][col] == mark for row in range(3)]):
            return True
    if all([board[i][i] == mark for i in range(3)]) or all([board[i][2 - i] == mark for i in range(3)]):
        return True
    return False

def check_for_draw(board):
    
    return all([cell != ' ' for row in board for cell in row])

def play_game(board):
    
    board = initialise_board(board)
    welcome(board)
    player_turn = True  
    while True:
        if player_turn:
            row, col = get_player_move(board)
            board[row][col] = 'X'
            draw_board(board)
            if check_for_win(board, 'X'):
                print("You win!")
                return 1
        else:
            row, col = choose_computer_move(board)
            board[row][col] = 'O'
            draw_board(board)
            if check_for_win(board, 'O'):
                print("Computer wins!")
                return -1
        if check_for_draw(board):
            draw_board(board)
            print("It's a draw!")
            return 0
        player_turn = not player_turn

def menu():
    
    print("1 - Play the game")
    print("2 - Save score in leaderboard")
    print("3 - Load and display leaderboard")
    print("q - Quit")
    choice = input("Enter your choice: ")
    return choice

def load_scores():
    
    if os.path.exists('leaderboard.txt'):
        with open('leaderboard.txt', 'r') as f:
            return json.load(f)
    return {}

def save_score(score):
    
    name = input("Enter your name: ")
    leaders = load_scores()
    leaders[name] = score
    with open('leaderboard.txt', 'w') as f:
        json.dump(leaders, f)

def display_leaderboard(leaders):
    
    if leaders:
        print("Leaderboard:")
        sorted_leaders = sorted(leaders.items(), key=lambda x: x[1], reverse=True)
        for name, score in sorted_leaders:
            print(f"{name}: {score}")
    else:
        print("No scores available.")



