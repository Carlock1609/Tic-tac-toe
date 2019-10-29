'''
filename: 4_in_row.py
'''
class Player:
    def __init__(self, name, token):
        self.name = name
        self.token = token

class Game:
    number_dict = {'10': [0, 0], '20': [0, 1], '30': [0, 2], '40': [0, 3], '50': [0, 4], '60': [0, 5], '70': [0, 6],
                    '11': [1, 0], '21': [1, 1], '31': [1, 2], '41': [1, 3], '51': [1, 4], '61': [1, 5], '71': [1, 6],
                    '12': [2, 0], '22': [2, 1], '32': [2, 2], '42': [2, 3], '52': [2, 4], '62': [2, 5], '72': [2, 6],
                    '13': [3, 0], '23': [3, 1], '33': [3, 2], '43': [3, 3], '53': [3, 4], '63': [3, 5], '73': [3, 6],
                    '14': [4, 0], '24': [4, 1], '34': [4, 2], '44': [4, 3], '54': [4, 4], '64': [4, 5], '74': [4, 6],
                    '15': [5, 0], '25': [5, 1], '35': [5, 2], '45': [5, 3], '55': [5, 4], '65': [5, 5], '75': [5, 6],
                   }

    def __init__(self):
        self.board =  [
            ['10','20','30','40','50','60','70'],
            ['11','21','31','41','51','61','71'],
            ['12','22','32','42','52','62','72'],
            ['13','23','33','43','53','63','73'],
            ['14','24','34','44','54','64','74'],
            ['15','25','35','45','55','65','75']
                ]
   
    def __repr__(self):
      #drawing a board 
      for i in self.board:
         result = " | ".join(i)
         print(result)   

p1 = Game()

print(p1.__repr__())

# def move(self, player):            
#     player_pick = int(input(f"{player.name}, Make your move: "))
#     numb = number_dict.get(player_pick)

#     if self.board[numb[0]][numb[1]] != '👻' or self.board[numb[0]][numb[1]] != '☠️':
#         self.board[numb[0]][numb[1]] = player.token
#         return player_pick
#     else:
#         print("This box is taken. Try another one!")
#         self.move(player)
# def game_begin(board, p1, p2):
#    winning_undetermined = True
#    player1_numb_ls = []
#    player2_numb_ls = []

#    print(f"To place {p1.token} or {p2.token} on the grid, enter an integer from 1-9 as a designated box on the grid.")
   
#    #drawing a board for sample
#    board.__repr__()

#    while winning_undetermined:
#       #player 1 move
#       player_pick = board.move(p1)
#       player1_numb_ls.append(player_pick)
#       is_Winning, winner_name = board.calc_winner(p1, player1_numb_ls)

#       if is_Winning == True:
#          board.__repr__()
#          print(f"{winner_name}, you won!!!")
#          exit()

#       #print the game board
#       board.__repr__()
#       # Check for tie
#       if len(player1_numb_ls) + len(player2_numb_ls) == 9:
#             print("Tie! Board is full!")
#             exit()

#       #player 2 move
#       player_pick = board.move(p2)
#       player2_numb_ls.append(player_pick)
#       is_Winning, winner_name = board.calc_winner(p2, player2_numb_ls)

#       if is_Winning == True:
#          board.__repr__()
#          print(f"{winner_name}, you won!!!")
#          exit()
      
#       board.__repr__()
#       # Check for tie
#       if len(player1_numb_ls) + len(player2_numb_ls) == 9:
#          print("Tie! Board is full!")
#          exit()


# def main():
#    print("Welcome to 4-In-A-Row!\nThis is a two-player game.\n")
#    player1_name = input("Player 1, type in your name: ")
#    player2_name = input("Player 2, type in your name: ")
#    print(f"{player1_name}, you are 'X'. {player2_name}, you are 'O'.")
#    p1= Player(player1_name, 'X') # instantiate player 1
#    p2 = Player(player2_name, 'O') # instantiate player 2
#    board = Game()
#    game_begin(board, p1, p2)