'''
test
'''
height = 3
width = 3
# board = [[' ',' ',''],[' ',' ',''],[' ',' ','']]  # start with an empty list
sample = [['1','2','3'],['4','5','6'],['7','8','9']]

class Player:
   def __init__(self, name, token):
      self.name = name
      self.token = token

class Game:
   def __init__(self):
      self.board = [['1',' ',' '],[' ',' ',' '],[' ',' ',' ']]
   
   def __repr__(self):
      #drawing a board 
      for i in sample:
         result = " | ".join(i)
      return result

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

def game_begin(board, p1, p2):
   winning_undetermined = True
   print("To place \'X\' or \'O\' on the grid, enter an integer from 1 to 9 as a designated box on the grid.")
   #drawing a board for sample
   for i in sample:
      result = " | ".join(i)
      print(result)
         
   while winning_undetermined:
      # print(p1.token)
      player1_pick = int(input("Make your move: "))
      numb = number_dict.get(player1_pick)
      board.board[numb[0]][numb[1]] = 'x'
      
      for i in board.board:
         result = " | ".join(i)
         print(result)      
      


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

