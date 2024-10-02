import random

# ### 3.1 Game menu function
board = []
game_mode = None
game_turn = 1
def game_menu():
   
   print( '''
   ----GAME MENU----
   1. Start a Game
   2. Print the Board 
   3. Place a Stone
   4. Reset the Game 
   5. Exit
   -----------------
   ''')
   return

# Test code for 3.1 here [The code in this cell should be commented]
'''
# This should output 5 options of the game menu
game_menu()
'''




# ### 3.2 Creating the Board
def create_board(size):
   # Created a board using nested loops for initialization
   board = []
   for y in range(size):
       row = []
       for x in range(size):
           row.append(0)
       board.append(row)
   return board

# Test code for 3.2 here [The code in this cell should be commented]
'''
# Test1 : This should be 81 outputs of zero
create_board(9)

# Test1 : this should be 169 outputs of zero
create_board(13)

# Test1 : this should be 225 outputs of zero
create_board(15)
'''




# ### 3.3 Is the target position occupied?
def is_occupied(board, x, y):
   if board[x][y] != 0:
       return True
   else:
       return False

# Test code for 3.3 here [The code in this cell should be commented]
'''
# Test1 : Check if position (0,0) is occupied (should output False)
test1 = is_occupied(board, 0, 0)
print("Test1 outputs: ", test1)

# Test2 : Check if position (1,0) is occupied (should output True)
test2 = is_occupied(board, 1, 0)
print("Test2 outputs: ", test2)
'''



# ### 3.4 Placing a Stone at a Specific Intersection
def place_on_board(board, stone, position):
   print(position)
   # Convert x row into Integer
   x = int(position[0])
   
   # Convert y column into Interger(By using ord function, we can get unicode of position[1] value)
   y = ord(position[1].upper()) - ord('A')
   
   # Check if x and y axis are out of bounds
   if x < 0 or x >= len(board) or y < 0 or y >= len(board):
       print("Selected position is out of bounds!")
       return False
   elif is_occupied(board, x, y):
       return False
   else:
       board[x][y] = stone
       return True

# Test code for 3.4 here [The code in this cell should be commented]
'''
# Valid position x is between 0 to length of board(9 or 13 or 15)
# Valid position y is between A to length of board(9=I or 13=M or 15=O)
# Test 1: Placing a stone at a valid position (should output True)
board = create_board(9)
test1 = place_on_board(board, 1, (1, 'A'))
print("Test outputs: ", test1)

# Test 2: Placing a stone at a valid position (should output False)
test2 = place_on_board(board, 1, (10, 'J'))
print("Test outputs: ", test2)
'''



# ### 3.5 Printing the Board
def print_board(board):
   
   board_row = []
   
   # Display an alphabetical letters depending on board size
   # ord('A')+i returns ASCII value of 'A' + i index and convert it to character with chr method
   for i in range(len(board)):
       board_row.append(chr(ord('A') + i))
   print("  ".join(board_row))
   
   # Enumerate function is used to iterate over both the index and the value of the elements in the board list
   for i, row in enumerate(board):
       for j, value in enumerate(row):
           
           # Check if loop is at the end oof row or not
           # If it is end of board list length then stop illustrating "--" else keep "--"
           # Basically, all values in the board list are filled with 0 to describe that the position is empty
           # If stone is placed in the position, then it is filled with 1(black stone) or 2(white stone)
           if j == len(row)-1:
               if value == 0:
                   print(" ", end = "")
               else:
                   if value == 1:
                       print("●", end = "")
                   else:
                       print("○", end = "")
           else:
               if value == 0:
                   print(" --", end = "")
               else:
                   if value == 1:
                       print("●--", end = "")
                   else:
                       print("○--", end = "")
                       
       # Print column number every end of row                
       print(i)
       
       # If outer loop is not at the end of the board length, then represent the vertical bar(|)
       # If loop reaches the end of the board length, then skip respresenting the vertical bar(|)
       if(i != len(board)-1):
           for j, value in enumerate(row):
               if j == len(row)-1:
                   print("| ")
               else:
                   print("|  ", end = "")
                   
# Test code for 3.5 here [The code in this cell should be commented]
'''
board = create_board(9)
# Test : Printing first row with an alphabetical letters (should output A to I)
board_row = []
for i in range(len(board)):
    board_row.append(chr(ord('A') + i))
print("  ".join(board_row))

# Test : Printing horizontal lines 
for i, row in enumerate(board):
    for j, value in enumerate(row):
        if j == len(row)-1:
            if value == 0:
                print(" ", end = "")
            else:
                if value == 1:
                    print("●", end = "")
                else:
                    print("○", end = "")
        else:
            if value == 0:
                print(" --", end = "")
            else:
                if value == 1:
                    print("●--", end = "")
                else:
                    print("○--", end = "")
    # Test : Printing column number every end of row (should output 0 to 8)               
    print(i)
    # Test : Printing vertical lines 
    if(i != len(board)-1):
            for j, value in enumerate(row):
                if j == len(row)-1:
                    print("| ")
                else:
                    print("|  ", end = "")
'''



# ### 3.6 Check Available Moves
def check_available_moves(board):
   rows = len(board)
   cols = len(board[0])
   available_moves = []
   for i in range(rows):
       for j in range(cols):
           if not is_occupied(board, i, j):
               # Get alphabetic characters corresponding to addition of j indes
               # ord('A') + j returns ASCII value of 'A' + j index
               available_moves.append((int(i), chr(ord('A') + j)))
   return available_moves

# Test code for 3.6 here [The code in this cell should be commented]
'''
# Test : If board size is 2, it should output 2*2=4 available moves
# Test Result : [(0, 'A'), (0, 'B'), (1, 'A'), (1, 'B')]

def check_available_moves(board):
    rows = 2
    cols = 2
    available_moves = []
    for i in range(rows):
        for j in range(cols):
            if not is_occupied(board, i, j):
                available_moves.append((int(i), chr(ord('A') + j)))
    return available_moves

check_available_moves(board)
'''



# ### 3.7 Check for the Winner
def check_for_winner(board):
   rows = len(board)
   cols = len(board[0])
   # Check horizontal lines
   for i in range(rows):
       count = 1
       for j in range(cols - 1):
           if board[i][j] != 0 and (board[i][j] == board[i][j + 1]):
               count += 1
           else:
               count = 1
           if count == 5:
               return board[i][j]
           
   # Check vertical lines
   for j in range(cols):
       count = 1
       for i in range(rows - 1):
           if board[i][j] != 0 and (board[i][j] == board[i + 1][j]):
               count += 1
           else:
               count = 1
           if count == 5:
               return board[i][j]
   
   # Check diagonal lines (ascending)
   for i in range(rows):
       for j in range(cols):
           if board[i][j] != 0:
               count = 1
               k = i
               l = j
               while count < 5 and 0 <= k + 1 < rows and 0 <= l - 1 < cols:
                   if board[k][l] == board[i][j] and board[k][l] == board[k + 1][l - 1]:
                       count += 1
                       k += 1
                       l -= 1
                   else:
                       break
               if count == 5:
                   return board[i][j]
           
   # Check diagonal lines (descending)
   for i in range(rows):
       for j in range(cols):
           if board[i][j] != 0:
               count = 1
               k = i
               l = j
               while count < 5 and 0 <= k + 1 < rows and 0 <= l + 1 < cols:
                   if board[k][l] == board[i][j] and board[k][l] == board[k + 1][l + 1]:
                       count += 1
                       k += 1
                       l += 1
                   else:
                       break
               if count == 5:
                   return board[i][j]
           
   available_moves = check_available_moves(board)
   if len(available_moves) == 0:
       return "Draw"
   return None

# Test code for 3.7 here [The code in this cell should be commented]
#
#
#



# ### 3.8 Random Computer Player
def random_computer_player(board, player_move):
   # Convert x row into Integer
   x = int(player_move[0])
   
   # Convert y column into Integer(By using ord function, we can get unicode of position[1] value)
   y = ord(player_move[1].upper()) - ord('A')
   
   # All positions within the 3*3 square
   potential_positions = [(x + 1, y + 1), (x, y + 1), (x - 1, y + 1), (x + 1, y), (x - 1, y), (x + 1, y - 1), (x, y - 1), (x - 1, y - 1)]
   available_moves = check_available_moves(board)
   valid_positions = []
   
   # If there are available moves
   if len(available_moves) > 0:
       for item in potential_positions:
           # Conver value of y axis to Integer to compare if new item is the same with array returned from available_moves function
           new_item = (item[0], chr(ord('A') + (item[1])))
           if new_item in available_moves:
               valid_positions.append(item)
   
   # If there are valid positions
   if len(valid_positions) > 0:
       # Randomly select available positions
       chosen_position = random.choice(valid_positions)
       # Convert value of y axis back to character in uppercase to satisfy place_on_board function's argument type
       converted_position = (chosen_position[0], chr(ord('A') + (chosen_position[1])))
       place_on_board(board, 2, converted_position)
       
   else:
       print("No valid positions available")

# Test code for 3.8 here [The code in this cell should be commented]
#
#
#




# ### 3.9 Play Game
def play_turn(turn):
    if turn == 1:
        return 2
    else:
        return 1
while True:
    game_menu()
    user_input = input("Select menu number: ")
    
    if user_input == "1":
        while True:
            option = input("Select board size:\n1.<9X9>\n2.<13X13>\n3.<15X15>\n")
            
            if option in ["1", "2", "3"]:
                sizes = [9, 13, 15]
                selected_size = sizes[int(option) - 1]
                board = create_board(selected_size)
                print("A new board is successfully created!")
                game_mode = input("Select a mode:\n1.<Player vs Plaver>\n2.<Player vs Computer>\n")
                game_turn = 1
                break
            else:
                print("Wrong option!\nPlease select a board size!")
        
    elif user_input == "2":
        if len(board) > 0:
            print_board(board)
        else:
            print("No board found!\nPlease select 'Start a Game' first!")
            
    elif user_input == "3":
        if len(board) == 0:
            print("No board found!\nPlease select 'Start a Game' first!")
        else:
            while True:
                if game_turn == 1:
                    print("Black Stone Turn!")
                else:
                    print("White Stone Turn!")
                selected_x = input("Select X axis from 0 to {0}: ".format(len(board) - 1))
                selected_y = input("Select Y axis from A to {0}: ".format(chr(ord('A') + len(board) - 1)))
                isplaced = place_on_board(board, game_turn, (int(selected_x), selected_y))
                if isplaced:
                    game_turn = play_turn(game_turn)
                    if game_mode == "2" and game_turn == 2:
                        random_computer_player(board, (int(selected_x), selected_y))
                        game_turn = play_turn(game_turn)
                result = check_for_winner(board)
                print_board(board)
                if result == "Draw":
                    print("DRAW!!")
                elif result != None:
                    if result == 1:
                        print("===WINNER IS BLACK STONE!===")
                        break
                    elif result == 2:
                        print("===WINNER IS WHITE STONE!===")
                        break
    elif user_input == "4":
        board = []
        game_mode = None
        game_turn = 1
        print("Gomoku is successfully reset!")
    else:
        print("Thank you for playing Gomoku! See you next time :)")
        break


#Run the game (Your tutor will run this cell to start playing the game)
#
#
#

