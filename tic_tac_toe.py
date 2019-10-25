'''
test
'''
height = 3
width = 3
# board = [[' ',' ',''],[' ',' ',''],[' ',' ','']]  # start with an empty list
sample = [['1','2','3'],['4','5','6'],['7','8','9']]
number_dict = {
    1: [0, 0],
    2: [0, 1],
    3: [0, 2],
    4: [1, 0],
    5: [1, 1],
    6: [1, 2],
    7: [2, 0],
    8: [2, 1],
    9: [2, 2]
}

class Player:
   def __init__(self, name, token):
      self.name = name
      self.token = token

class Game:
   def __init__(self):
      self.board = [['1','2','3'],['4','5','6'],['7','8','9']]
   
   def __repr__(self):
      #drawing a board 
      for i in self.board:
         result = " | ".join(i)
         print(result)     

   def calc_winner(self, player, ls):
      ls.sort()
      if ls.__contains__(1) and ls.__contains__(2) and ls.__contains__(3): # Across top
         return True, player.name
      elif ls.__contains__(4) and ls.__contains__(5) and ls.__contains__(6): # Across middle
         return True, player.name
      elif ls.__contains__(7) and ls.__contains__(8) and ls.__contains__(9): # Across Bottom
         return True, player.name
      elif ls.__contains__(1) and ls.__contains__(4) and ls.__contains__(7): # Vert left
         return True, player.name         
      elif ls.__contains__(2) and ls.__contains__(5) and ls.__contains__(8): # Vert middle
         return True, player.name
      elif ls.__contains__(3) and ls.__contains__(6) and ls.__contains__(9): # Vert Right
         return True, player.name
      elif ls.__contains__(1) and ls.__contains__(5) and ls.__contains__(9): # Top left lower right
         return True, player.name
      elif ls.__contains__(3) and ls.__contains__(5) and ls.__contains__(7): # Top right to bottom left
         return True, player.name
      else:
         return False, player.name
   
   def move(self, player):
      player_pick = int(input(f"{player.name}, Make your move: "))
      numb = number_dict.get(player_pick)

      if self.board[numb[0]][numb[1]] != 'X' or self.board[numb[0]][numb[1]] != 'O':
         self.board[numb[0]][numb[1]] = player.token
         return player_pick
      else:
         print("This box is already take. Try another one!")
         self.move(player)

def game_begin(board, p1, p2):
   winning_undetermined = True
   player1_numb_ls = []
   player2_numb_ls = []

   print("To place \'X\' or \'O\' on the grid, enter an integer from 1 to 9 as a designated box on the grid.")
   #drawing a board for sample
   for i in sample:
      result = " | ".join(i)
      print(result)
         
   while winning_undetermined:
      #player 1 move
      player_pick = board.move(p1)
      player1_numb_ls.append(player_pick)
      is_Winning, winner_name = board.calc_winner(p1, player1_numb_ls)

      if is_Winning == True:
         board.__repr__()
         print(f"{winner_name}, you're win!!!")
         exit()

      #print the game board
      board.__repr__()
      # Check for tie
      if len(player1_numb_ls) + len(player2_numb_ls) == 9:
            print("Tie! Board is full!")
            exit()

      #player 2 move
      player_pick = board.move(p2)
      player2_numb_ls.append(player_pick)
      is_Winning, winner_name = board.calc_winner(p2, player2_numb_ls)

      if is_Winning == True:
         board.__repr__()
         print(f"{winner_name}, you're win!!!")
         exit()
         
      
      board.__repr__()
      # Check for tie
      if len(player1_numb_ls) + len(player2_numb_ls) == 9:
         print("Tie! board is full!")
         exit()

def main():
   print("Welcome to tic-tac-toe!\nThis is a two-player game.\n")
   player1_name = input("Player 1, type in your name: ")
   player2_name = input("Player 2, type in your name: ")
   print(f"{player1_name}, you are 'X'. {player2_name}, you are 'O'.")
   p1= Player(player1_name, 'X') # instantiate player 1
   p2 = Player(player2_name, 'O') # instantiate player 2
   board = Game()
   # print(board.__repr__())
   game_begin(board, p1, p2)

main()

# #drawing a board for sample
# for i in range (len(sample)): 
#    print(sample[i])

# user1 = int(input("choose a box that you want to put 'X': "))

# temp = number_dict.get(user1)

# board[temp[0]][temp[1]] = 'X'

# #drawing a board for real game
# for i in range (len(board)): 
#    print(board[i])

