from tkinter import *

window=Tk()
window.wm_title('Tic Tac Toe')
canvas1=Canvas(window, width=300, height=300)
canvas1.pack()
down_grid=canvas1.create_rectangle(100,0,200,400,outline='black')
across_grid=canvas1.create_rectangle(0,100,400,200,outline='black')

game = [".",".",".",".",".",".",".",".","."]
0,1,2
3,4,5
6,7,8

def draw_cross(X,Y):
    backstroke=canvas1.create_line(X,Y,X+100,Y+100,fill='blue')
    forwardstroke=canvas1.create_line(X,Y+100,X+100,Y,fill='blue')

def draw_nought(X,Y):
    nought=canvas1.create_oval(X,Y,X+100,Y+100,outline='red')

def draw_players_turn (place):
    if place == 0:
        draw_cross(0,0)
    elif place == 1:
        draw_cross(100,0)
    elif place == 2:
        draw_cross(200,0)
    elif place == 3:
        draw_cross(0,100)
    elif place == 4:
        draw_cross(100,100)
    elif place == 5:
        draw_cross(200,100)
    elif place == 6:
        draw_cross(0,200)
    elif place == 7:
        draw_cross(100,200)
    elif place == 8:
        draw_cross(200,200)

def draw_computers_turn (place):
    if place == 0:
        draw_nought(0,0)
    elif place == 1:
        draw_nought(100,0)
    elif place == 2:
        draw_nought(200,0)
    elif place == 3:
        draw_nought(0,100)
    elif place == 4:
        draw_nought(100,100)
    elif place == 5:
        draw_nought(200,100)
    elif place == 6:
        draw_nought(0,200)
    elif place == 7:
        draw_nought(100,200)
    elif place == 8:
        draw_nought(200,200)
         
def isDraw (gameboard):
    draw = True
    for n in range (0, 9):
        if gameboard[n] == ".":
            draw = False
    if draw:
        return True

def isWin(gameboard):
    if ((gameboard[0] =="O" and gameboard[1] =="O" and gameboard[2] =="O") or
    (gameboard[3] =="O"and gameboard[4] =="O"and gameboard[5] =="O") or
    (gameboard[6] =="O"and gameboard[7] =="O"and gameboard[8] =="O") or
    (gameboard[0] =="O"and gameboard[3] =="O"and gameboard[6] =="O") or
    (gameboard[1] =="O" and gameboard[4] =="O" and gameboard[7] =="O") or
    (gameboard[2] =="O" and gameboard[5] =="O" and gameboard[8] =="O") or
    (gameboard[0] =="O" and gameboard[4] =="O" and gameboard[8] =="O") or
    (gameboard[2] =="O" and gameboard[4] =="O" and gameboard[6] =="O")):
        return True
    

if input("Do you want to go first or second? ") == "first":
    pos=1
else:
    pos = 2
#computer is X
gameover = False
while not gameover:
    canvas1.update()
    #check for a draw
    if isDraw(game):
        gameover = True
        print("Draw")
        
    #check if human player has won
    if isWin(game):
        gameover = True
        print("You win")
    #player chose to go first, input players chosen square.    
    if pos == 1:
        print(game[0:3])
        print(game[3:6])
        print(game[6:9])
        print("0,1,2")
        print("3,4,5")
        print("6,7,8")
        if not gameover and not isDraw(game) and not isWin(game):
            place = int(input("Where do you want to put your O? "))
            if game[place] == ".":
                game[place] = "O"
            else:
                print("That place has already been taken.")
                
    #computer went first or player went first and did not choose a corner
    if (game==[".",".",".",".",".",".",".",".","."]
    or game==[".","O",".",".",".",".",".",".","."]
    or game==[".",".","O",".",".",".",".",".","."]
    or game==[".",".",".",".","O",".",".",".","."]
    or game==[".",".",".",".",".","O",".",".","."]
    or game==[".",".",".",".",".",".",".","O","."]):
        #go in top left.
        game[0] = "X"
   
    #if player has gone in a corner, go in opposite corner
    elif game==["O",".",".",".",".",".",".",".","."]:
        game[8] = "X"
    elif game ==[".",".","O",".",".",".",".",".","."]:
        game[6] = "X"
    elif game ==[".",".",".",".",".",".","O",".","."]:
        game[2] = "X"
    elif game ==[".",".",".",".",".",".",".",".","O"]:
        game[0] = "X"

    #player has 2 in a row on top row? block. computer has 2 in a row on top row? finish!
    elif game[0] == "O" and game [1] == "O" and game [2] == ".":
        game[2] = "X"
    elif game[0] == "X" and game [1] == "X" and game [2] == ".":
        game[2] = "X"
        gameover = True
        print("Computer Wins")
        print(game[0:3])
        print(game[3:6])
        print(game[6:9])
        
    elif game[0] == "X" and game [1] == "X" and game [2] == ".":
        game[2] = "X"
        gameover = True
        print("Computer Wins")
        print(game[0:3])
        print(game[3:6])
        print(game[6:9])
        
    elif game[0] == "O" and game[1] == "." and game[2]=="O":
        game[1] = "X"
    elif game[0] == "X" and game[1] == "." and game[2]=="X":
        game[1] = "X"
        gameover = True
        print("Computer Wins")
        print(game[0:3])
        print(game[3:6])
        print(game[6:9])
        
    elif game[0] == "." and game[1] == "O" and game[2]=="O":
        game[0] = "X"
    elif game[0] == "." and game[1] == "X" and game[2]=="X":
        game[0] = "X"
        gameover = True
        print("Computer Wins")
        print(game[0:3])
        print(game[3:6])
        print(game[6:9])
        
    #2 in a row on middle row?
    elif game[3] == "O" and game [4] == "O" and game [5] == ".":
        game[5] = "X"
    elif game[3] == "X" and game [4] == "X" and game [5] == ".":
        game[5] = "X"
        gameover = True
        print("Computer Wins")
        print(game[0:3])
        print(game[3:6])
        print(game[6:9])        
    elif game[3] == "X" and game [4] == "X" and game [5] == ".":
        game[5] = "X"
        gameover = True
        print("Computer Wins")
        print(game[0:3])
        print(game[3:6])
        print(game[6:9])        
    elif game[3] == "O" and game[4] == "." and game[5]=="O":
        game[4] = "X"
    elif game[3] == "X" and game[4] == "." and game[5]=="X":
        game[4] = "X"
        gameover = True
        print("Computer Wins")
        print(game[0:3])
        print(game[3:6])
        print(game[6:9])        
    elif game[3] == "." and game[4] == "O" and game[5]=="O":
        game[3] = "X"
    elif game[3] == "." and game[4] == "X" and game[5]=="X":
        game[3] = "X"
        gameover = True
        print("Computer Wins")
        print(game[0:3])
        print(game[3:6])
        print(game[6:9])        

    #2 in a row on bottom row?
    elif game[6] == "O" and game [7] == "O" and game [8] == ".":
        game[8] = "X"
    elif game[6] == "X" and game [7] == "X" and game [8] == ".":
        game[8] = "X"
        gameover = True
        print("Computer Wins")
        print(game[0:3])
        print(game[3:6])
        print(game[6:9])       
    elif game[6] == "X" and game [7] == "X" and game [8] == ".":
        game[8] = "X"
        gameover = True
        print("Computer Wins")
        print(game[0:3])
        print(game[3:6])
        print(game[6:9])        
    elif game[6] == "O" and game[7] == "." and game[8]=="O":
        game[7] = "X"
    elif game[6] == "X" and game[7] == "." and game[8]=="X":
        game[7] = "X"
        gameover = True
        print("Computer Wins")
        print(game[0:3])
        print(game[3:6])
        print(game[6:9])        
    elif game[6] == "." and game[7] == "O" and game[8]=="O":
        game[6] = "X"
    elif game[6] == "." and game[7] == "X" and game[8]=="X":
        game[6] = "X"
        gameover = True
        print("Computer Wins")
        print(game[0:3])
        print(game[3:6])
        print(game[6:9])        
    #0,1,2
    #3,4,5
    #6,7,8

    #2 in left column?
    elif game[0] == "O" and game [3] == "O" and game [6] == ".":
        game[6] = "X"
    elif game[0] == "X" and game [3] == "X" and game [6] == ".":
        game[6] = "X"
        gameover = True
        print("Computer Wins")
        print(game[0:3])
        print(game[3:6])
        print(game[6:9])        
    elif game[0] == "X" and game [3] == "X" and game [6] == ".":
        game[6] = "X"
        gameover = True
        print("Computer Wins")
        print(game[0:3])
        print(game[3:6])
        print(game[6:9])        
    elif game[0] == "O" and game[3] == "." and game[6]=="O":
        game[3] = "X"
    elif game[0] == "X" and game[3] == "." and game[6]=="X":
        game[3] = "X"
        gameover = True
        print("Computer Wins")
        print(game[0:3])
        print(game[3:6])
        print(game[6:9])        
    elif game[0] == "." and game[3] == "O" and game[6]=="O":
        game[0] = "X"
    elif game[0] == "." and game[3] == "X" and game[6]=="X":
        game[0] = "X"
        gameover = True
        print("Computer Wins")    
        print(game[0:3])
        print(game[3:6])
        print(game[6:9])
        
    #2 in middle column?
    elif game[1] == "O" and game [4] == "O" and game [7] == ".":
        game[7] = "X"
    elif game[1] == "X" and game [4] == "X" and game [7] == ".":
        game[7] = "X"
        gameover = True
        print("Computer Wins")
        print(game[0:3])
        print(game[3:6])
        print(game[6:9])        
    elif game[1] == "X" and game [4] == "X" and game [7] == ".":
        game[7] = "X"
        gameover = True
        print("Computer Wins")
        print(game[0:3])
        print(game[3:6])
        print(game[6:9])
        
    elif game[1] == "O" and game[4] == "." and game[7]=="O":
        game[4] = "X"
    elif game[1] == "X" and game[4] == "." and game[7]=="X":
        game[4] = "X"
        gameover = True
        print("Computer Wins")
        print(game[0:3])
        print(game[3:6])
        print(game[6:9])
        
    elif game[1] == "." and game[4] == "O" and game[7]=="O":
        game[1] = "X"
    elif game[1] == "." and game[4] == "X" and game[7]=="X":
        game[1] = "X"
        gameover = True
        print("Computer Wins")  
        print(game[0:3])
        print(game[3:6])
        print(game[6:9])
        
    #2 in right column?
    elif game[2] == "O" and game [5] == "O" and game [8] == ".":
        game[8] = "X"
    elif game[2] == "X" and game [5] == "X" and game [8] == ".":
        game[8] = "X"
        gameover = True
        print("Computer Wins")
        print(game[0:3])
        print(game[3:6])
        print(game[6:9])
        
    elif game[2] == "X" and game [5] == "X" and game [8] == ".":
        game[8] = "X"
        gameover = True
        print("Computer Wins")
        print(game[0:3])
        print(game[3:6])
        print(game[6:9])
        
    elif game[2] == "O" and game[5] == "." and game[8]=="O":
        game[5] = "X"
    elif game[2] == "X" and game[5] == "." and game[8]=="X":
        game[5] = "X"
        gameover = True
        print("Computer Wins")
        print(game[0:3])
        print(game[3:6])
        print(game[6:9])        
    elif game[2] == "." and game[5] == "O" and game[8]=="O":
        game[2] = "X"
    elif game[2] == "." and game[5] == "X" and game[8]=="X":
        game[2] = "X"
        gameover = True
        print("Computer Wins")
        print(game[0:3])
        print(game[3:6])
        print(game[6:9])        
    #0,1,2
    #3,4,5
    #6,7,8
        
    #forward diagonal
    elif game[0] == "O" and game [4] == "O" and game [8] == ".":
        game[8] = "X"
    elif game[0] == "X" and game [4] == "X" and game [8] == ".":
        game[8] = "X"
        gameover = True
        print("Computer Wins")
        print(game[0:3])
        print(game[3:6])
        print(game[6:9])        
    elif game[0] == "X" and game [4] == "X" and game [8] == ".":
        game[8] = "X"
        gameover = True
        print("Computer Wins")
        print(game[0:3])
        print(game[3:6])
        print(game[6:9])        
    elif game[0] == "O" and game[4] == "." and game[8]=="O":
        game[4] = "X"
    elif game[0] == "X" and game[4] == "." and game[8]=="X":
        game[4] = "X"
        gameover = True
        print("Computer Wins")
        print(game[0:3])
        print(game[3:6])
        print(game[6:9])        
    elif game[0] == "." and game[4] == "O" and game[8]=="O":
        game[0] = "X"
    elif game[0] == "." and game[4] == "X" and game[8]=="X":
        game[0] = "X"
        gameover = True
        print("Computer Wins")
        print(game[0:3])
        print(game[3:6])
        print(game[6:9])
        
    #back diagonal
    elif game[2] == "O" and game [4] == "O" and game [6] == ".":
        game[6] = "X"
    elif game[2] == "X" and game [4] == "X" and game [6] == ".":
        game[6] = "X"
        gameover = True
        print("Computer Wins")
        print(game[0:3])
        print(game[3:6])
        print(game[6:9])        
    elif game[2] == "X" and game [4] == "X" and game [6] == ".":
        game[6] = "X"
        gameover = True
        print("Computer Wins")
        print(game[0:3])
        print(game[3:6])
        print(game[6:9])
    elif game[2] == "O" and game[4] == "." and game[6]=="O":
        game[4] = "X"
    elif game[2] == "X" and game[4] == "." and game[6]=="X":
        game[4] = "X"
        gameover = True
        print("Computer Wins")
        print(game[0:3])
        print(game[3:6])
        print(game[6:9])
    elif game[2] == "." and game[4] == "O" and game[6]=="O":
        game[2] = "X"
    elif game[2] == "." and game[4] == "X" and game[6]=="X":
        game[2] = "X"
        gameover = True
        print("Computer Wins")
        print(game[0:3])
        print(game[3:6])
        print(game[6:9])

    #else go in an empty corner
    else:
        if game[0]==".":
            game[0] = "X"
        elif game[8]==".":
            game[8] = "X"
        elif game[2] == ".":
            game[2] = "X"
        elif game[6] == ".":
            game[6] = "X"
        #else go in the empty square
        elif game[1] ==".":
            game[1] = "X"
        elif game[3] == ".":
            game[3] = "X"
        elif game[4] == ".":
            game[4] = "X"
        elif game[5] == ".":
            game[5] = "X"
        elif game[7] == ".":
            game[7] = "X"
    #player chose to go second, input player's chosen square
    if pos == 2:
        print(game[0:3])
        print(game[3:6])
        print(game[6:9])
        print("0,1,2")
        print("3,4,5")
        print("6,7,8")
        if not gameover and not isDraw(game) and not isWin(game):

            place = int(input("Where do you want to put your O? "))
            if game[place] == ".":
                game[place] = "O"
            else:
                print("That place has already been taken.")
     













    
        




