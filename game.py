import random
from random import randint
board = [['.','.','.','.','.','.','.','.','.','.'],
         ['.','.','.','.','.','.','.','.','.','.'],
         ['.','.','.','.','.','.','.','.','.','.'],
         ['.','.','.','.','.','.','.','.','.','.'],
         ['.','.','.','.','.','.','.','.','.','.'],
         ['.','.','.','.','.','.','.','.','.','.'],
         ['.','.','.','.','.','.','.','.','.','.'],
         ['.','.','.','.','.','.','.','.','.','.'],
         ['.','.','.','.','.','.','.','.','.','.'],
         ['.','.','.','.','.','.','.','.','.','.']]

def generateBomb():
    n, N = 9, 10
    points = {(randint(0, n), randint(0, n)) for i in range(N)}
    while len(points) < N:
        points |= {(randint(0, n), randint(0, n))}

    points = list(list(x) for x in points)
    return points

def generateBoard(bombs1):
    temp = [[0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0]]
    for i in bombs1:
        #print(i)
        temp[i[0]][i[1]] = -10
        if (i[0]!=0 and i[0]!=9) and (i[1]!=0 and i[1]!=9):
            temp[i[0]-1][i[1]-1]+=1
            temp[i[0]-1][i[1]]+=1
            temp[i[0]-1][i[1]+1]+=1
            temp[i[0]][i[1]-1]+=1
            temp[i[0]][i[1]+1]+=1
            temp[i[0]+1][i[1]+1]+=1
            temp[i[0]+1][i[1]]+=1
            temp[i[0]+1][i[1]-1]+=1
        else:
            if i[0]==0 and (i[1]!=0 and i[1]!=9):
                temp[i[0]][i[1]-1]+=1
                temp[i[0]][i[1]+1]+=1
                temp[i[0]+1][i[1]]+=1
                temp[i[0]+1][i[1]-1]+=1
                temp[i[0]+1][i[1]+1]+=1

            if i[0]==9 and (i[1]!=0 and i[1]!=9):
                temp[i[0]][i[1]-1]+=1
                temp[i[0]][i[1]+1]+=1
                temp[i[0]-1][i[1]]+=1
                temp[i[0]-1][i[1]-1]+=1
                temp[i[0]-1][i[1]+1]+=1

            if i[1]==0 and (i[0]!=0 and i[0]!=9):
                temp[i[0]-1][i[1]+1]+=1
                temp[i[0]-1][i[1]]+=1
                temp[i[0]+1][i[1]+1]+=1
                temp[i[0]+1][i[1]]+=1
                temp[i[0]][i[1]+1]+=1

            if i[1]==9 and (i[0]!=0 and i[0]!=9):
                temp[i[0]-1][i[1]-1]+=1
                temp[i[0]-1][i[1]]+=1
                temp[i[0]+1][i[1]-1]+=1
                temp[i[0]+1][i[1]]+=1
                temp[i[0]][i[1]-1]+=1
            
            if i[0]==0 and i[1]==0:
                temp[i[0]][i[1]+1]+=1
                temp[i[0]+1][i[1]]+=1
                temp[i[0]+1][i[1]+1]+=1
            
            if i[0]==0 and i[1]==9:
                temp[i[0]][i[1]-1]+=1
                temp[i[0]+1][i[1]]+=1
                temp[i[0]+1][i[1]-1]+=1
            
            if i[0]==9 and i[1]==0:
                temp[i[0]-1][i[1]]+=1
                temp[i[0]][i[1]+1]+=1
                temp[i[0]-1][i[1]+1]+=1
            
            if i[0]==9 and i[1]==9:
                temp[i[0]][i[1]-1]+=1
                temp[i[0]-1][i[1]]+=1
                temp[i[0]-1][i[1]-1]+=1
    return temp

# t = generateBoard(generateBomb())
# ans = []
# for j in t:
#     row = []
#     for n in j:
#         if n == 0:
#             print('.',end = ' ')
#             row.append('.')
#         elif n<0:
#             print('B',end = ' ')
#             row.append('B')
#         else:
#             print(n,end = ' ')
#             row.append(n)
#     print('\n')
#     ans.append(row)

def printB(board):
    for row in board:
        for c in row:
            print(c,end=' ')
        print('\n')

def check(board, temp, bombs):
    temp2 = [['.','.','.','.','.','.','.','.','.','.'],
            ['.','.','.','.','.','.','.','.','.','.'],
            ['.','.','.','.','.','.','.','.','.','.'],
            ['.','.','.','.','.','.','.','.','.','.'],
            ['.','.','.','.','.','.','.','.','.','.'],
            ['.','.','.','.','.','.','.','.','.','.'],
            ['.','.','.','.','.','.','.','.','.','.'],
            ['.','.','.','.','.','.','.','.','.','.'],
            ['.','.','.','.','.','.','.','.','.','.'],
            ['.','.','.','.','.','.','.','.','.','.']]
    temp3 = [['.','.','.','.','.','.','.','.','.','.'],
            ['.','.','.','.','.','.','.','.','.','.'],
            ['.','.','.','.','.','.','.','.','.','.'],
            ['.','.','.','.','.','.','.','.','.','.'],
            ['.','.','.','.','.','.','.','.','.','.'],
            ['.','.','.','.','.','.','.','.','.','.'],
            ['.','.','.','.','.','.','.','.','.','.'],
            ['.','.','.','.','.','.','.','.','.','.'],
            ['.','.','.','.','.','.','.','.','.','.'],
            ['.','.','.','.','.','.','.','.','.','.']]
    for i in range(0,10):
        for j in range(0,10):
            if board[i][j]=='F':
                temp2[i][j]='F'
            if temp[i][j]<0:
                temp3[i][j] = 'F'
    # printB(temp2)
    # print('\n\n')
    # printB(temp3)
    if temp2==temp3:
        return True
    else:
        return False

def game(board):
    bombs = generateBomb()
    temp = generateBoard(bombs)
    game_over = False
    # For checking purpose
    print(bombs)
    printB(board)
    print('\n')
    count = 10
    while not game_over:
        print("Provide coordinates and Option(Click => C or Flag => F): ")
        a = int(input())
        b = int(input())
        opt = input()
        if a>9 or b>9 or a<0 or b<0:
            print("Invalid input, try again!!")
            continue
        if board[a][b]!='F' and board[a][b]!='.':
            print("Invalid move")
            continue 
        coord = [a,b]
        if coord in bombs:
            if opt=='F':
                if count==0:
                    print("Out of flags, Invalid Solution")
                else:
                    count-=1
                    print("Flags left : ",count)
                    board[a][b] = 'F'
                    if count == 0:
                        if check(board,temp,bombs):
                            print("Game over")
                            game_over = True
                    printB(board)
                continue
            else:
                print("Game over")
                game_over = True
        else:
            board[a][b] = temp[a][b]
            printB(board)
            print('\n')

game(board)
