'''
test
'''
height = 3
width = 3
board = [[' ',' ',''],[' ',' ',''],[' ',' ','']]  # start with an empty list
sample = [[1,2,3],[4,5,6],[7,8,9]]

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




#drawing a board for sample
for i in range (len(sample)): 
   print(sample[i])

user1 = int(input("choose a box that you want to put 'X': "))

temp = number_dict.get(user1)

board[temp[0]][temp[1]] = 'X'

#drawing a board for real game
for i in range (len(board)): 
   print(board[i])

