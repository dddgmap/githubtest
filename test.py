import random
###YourName=input('what is your name? ')
###print('your name is '+ YourName)
###Age=int(input('How old are you? '))
###Ageindays=(Age*365)
###print('You are',Ageindays,'days old')
###hobby=input('what is you favourite colour?')
###if hobby=='red':
###    print('red is my fave too')
###elif hobby=='green':
###    print(hobby +' is Jacobs fave')
###else:
###        print(hobby + ' is a nice colour')

tronk=1
while(tronk<145):
    tronk=(random.randint(0,150))
    print(tronk)

fish=['cod','haddock','salmon']
jenny=1
while(jenny>0):
    jenny=(random.randint(0,2))
    print(fish[jenny])

print(random.choice(fish))
print(random.choice(fish))

comp='You have'
adj=[' smashing',' crud',' amazing']
ting=['parents','trousers','earlobes']
yo=comp+random.choice(adj)+" "
yo=yo+random.choice(ting)+"."
print (yo)

for n in range(0,11):
    print (n*13)

from tkinter import *
window=Tk()
window.wm_title('pig trousers')
canvas1=Canvas(window, width=310, height=310)
canvas1.pack()
down_grid=canvas1.create_rectangle(100,10,200,300,outline='black')
across_grid=canvas1.create_rectangle(10,100,300,200,outline='black')
def draw_line(X,Y):
    liney=canvas1.create_polygon(X,Y,X+50,Y+50,20,0,0,200,150,150)

def draw_cross(X,Y):
    backstroke=canvas1.create_line(X,Y,X+100,Y+100,fill='blue')
    forwardstroke=canvas1.create_line(X,Y+100,X+100,Y,fill='blue')

def draw_nought(X,Y):
    nought=canvas1.create_oval(X,Y,X+100,Y+100,outline='red')
draw_line(20,20)
draw_cross(100,100)
draw_nought(200,100)
draw_cross(0,0)
draw_nought(200,200)
