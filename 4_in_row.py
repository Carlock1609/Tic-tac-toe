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
    Ls1 = ['10','11','12','13','14','15']
    Ls2 = ['20','21','22','23','24','25']
    Ls3 = ['30','31','32','33','34','35']
    Ls4 = ['40','41','42','43','44','45']
    Ls5 = ['50','51','52','53','54','55']
    Ls6 = ['60','61','62','13','64','65']
    Ls7 = ['70','71','72','73','74','75']

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

    def move(self, player):
        selected_num = 0

        player_pick = input(f"{player.name}, Make your move: ")
        
        if player_pick == '1':
            selected_num = Game.Ls1[-1]
            Game.Ls1.remove(selected_num)
        elif player_pick =='2':
            selected_num = Game.Ls2[-1]
            Game.Ls2.remove(selected_num)
        elif player_pick =='3':
            selected_num = Game.Ls3[-1]
            Game.Ls3.remove(selected_num)
        elif player_pick =='4':
            selected_num = Game.Ls4[-1]
            Game.Ls4.remove(selected_num)
        elif player_pick =='5':
            selected_num = Game.Ls5[-1]
            Game.Ls5.remove(selected_num)
        elif player_pick =='6':
            selected_num = Game.Ls6[-1]
            Game.Ls6.remove(selected_num)
        elif player_pick =='7':
            selected_num = Game.Ls7[-1]
            Game.Ls7.remove(selected_num)

        numb = Game.number_dict.get(selected_num) # getting coordinate from dictionary

        if self.board[numb[0]][numb[1]] != 'X' or self.board[numb[0]][numb[1]] != 'O':
            self.board[numb[0]][numb[1]] = player.token
        return numb

    def calc_winner(self, player, coor_list):
        #horizontal check
        coor_list.sort()
        horizonal_ls = []
        for i in range(len(coor_list)):
            c = coor_list[i]
            horizonal_ls.append(c[0])
            count = horizonal_ls.count(c[0])
            if count == 4:
                print("you win horizontally")
                exit()

        #vertical check
        vertical_ls = []
        for i in range(len(coor_list)):
            c = coor_list[i]
            vertical_ls.append(c[1])
            count = vertical_ls.count(c[1])
            if count == 4:
                print("you win vertically")
                exit()

        #diagonal check from lower-left o upper-right
        diag_ls = []
        count_ll_ur = 0

        for i in Game.number_dict.keys():
            for n in coor_list:
                if Game.number_dict[i] == n:
                    n = int(i)
                    diag_ls.append(n)


        for i in diag_ls:
            if diag_ls.__contains__(i+9):
                if diag_ls.__contains__(i+18):
                    if diag_ls.__contains__(i+27):
                        print("you're win diagonal from lower-left to upper-right.")
                        exit()
            if diag_ls.__contains__(i+11):
                if diag_ls.__contains__(i+22):
                    if diag_ls.__contains__(i+33):
                        print("you're win diagonal from upper-left to lower-right.")
                        exit()
            

        

        #         previous_ls = i
        #         count_ll_ur += 1
        #     else:
        #         if previous_ls[0] + 1 == i[0] and previous_ls[1] + 1 == i[1]:
        #             count_ll_ur += 1
        #             previous_ls = i
        #             # print(count)
        #             if count_ll_ur == 4:
        #                 print("you win diagonal! ll - ur")
        #                 exit()


        # #diagonal check from upper-left to lower-right
        #         previous_ls = []
        #         count_ul_lr = 0
                
                

def game_begin(board, p1, p2):
    winning_undetermined = True
    coor = []
    player1_numb_ls = []
    player2_numb_ls = []
    print(f"To place {p1.token} or {p2.token} on the grid, enter an integer from 1-7 as a designated box on the grid.")

   #drawing a board
    board.__repr__()
    while winning_undetermined:
        #player 1 move
        coor = board.move(p1)
        player1_numb_ls.append(coor)
        board.calc_winner(p1, player1_numb_ls)
        board.__repr__()

        #play 2 move


        coor = board.move(p2)
        player2_numb_ls.append(coor)
        board.calc_winner(p2, player2_numb_ls)        
        board.__repr__()



      

def main():
   print("Welcome to 4-In-A-Row!\nThis is a two-player game.\n")
   player1_name = input("Player 1, type in your name: ")
   player2_name = input("Player 2, type in your name: ")
   print(f"{player1_name}, you are 'X'. {player2_name}, you are 'O'.")
   p1= Player(player1_name, ' X') # instantiate player 1
   p2 = Player(player2_name, ' O') # instantiate player 2
   board = Game()
   game_begin(board, p1, p2)

main()