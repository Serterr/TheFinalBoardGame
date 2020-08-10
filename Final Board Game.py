#-----------------------------------------------   
#Program Name: Term Project Board Game
#Student Name: Neill DesJardins
#-----------------------------------------------
#Program Purpose: To create a playable board game where the goal is for the player to turn all of the tiles white
#-----------------------------------------------

from graphics import *
global col_list
global rect_list
global move_list
from random import *
import time


#-----------------------------------------------
# Function purpose: To launch the game for the player
# Syntax: play_boardgame()
# Parameter: None
# Return value: None
#-----------------------------------------------


def play_boardgame():
    global col_list
    global rect_list
    global move_list
    global solving
    global win4
    solving = 0
    clickcount = 0;
    size = size_selector()
    win = GraphWin("BoardGame", size * 50 - 5, size * 50 + 100)
    rect = Rectangle(Point(0, size*50), Point(size*50 - 5, size * 50 + 100))
    rect.setFill('teal')
    rect.setOutline('grey')
    rect.draw(win)
    solvetext =  Text(Point(size*25,size*50 + 25), "Click here to autosolve")
    solvetext.setTextColor('white')
    solvetext.draw(win)    
    col_list = []
    rect_list = []
    move_list = []
    #Clock & Click Initialization
    T0 = time.time()
    T1 = time.time()
    T1 = T1 - T0
    T1 = int(T1)
    clocktext =  Text(Point(size*45,size*50 + 75),  T1)
    clocktext.setTextColor('white')
    clocktext.draw(win)
    clockhud = Text(Point(size*35,size*50 + 75),  "Time:")
    clockhud.setTextColor('white')
    clockhud.draw(win)
    clicktext =  Text(Point(size*20,size*50 + 75),  clickcount)
    clicktext.setTextColor('white')
    clicktext.draw(win)
    clickhud = Text(Point(size*10,size*50 + 75),  "Clicks:")
    clickhud.setTextColor('white')
    clickhud.draw(win)    
    # y, and x are all used to incriment while loops
    y = 0
    while y < size:
        x = 0
        while x < size:
            rect = Rectangle(Point((x)*50, ((y)*50)), Point((x + 1)*50, ((y + 1)*50)))
            rect.setFill('White')
            rect.setOutline('grey')
            rect.draw(win)
            rect_list.append(rect)
            x = x + 1
            col_list = col_list + ['w']
        y =  y + 1
        #randomize 100 clicks to start
    while x < 100:
        points = randint(0, size*size - 1)
        clicker(size, points)
        x = x + 1
        #While black tiles remain
    while 'b' in col_list:    
        P = win.checkMouse()
        #CLock stuff
        time.sleep(0.05)
        T1 = time.time()
        T1 = T1 - T0
        T1 = int(T1)
        clocktext.undraw()
        clocktext =  Text(Point(size*45,size*50 + 75),  T1)
        clocktext.setTextColor('white')
        clocktext.draw(win)
        #End clock
        #Click Counter
        clicktext.undraw()
        clicktext =  Text(Point(size*20,size*50 + 75),  clickcount)
        clicktext.setTextColor('white')
        clicktext.draw(win)        
        if P != None:
            #If click is below the board, the player wants to solve the puzzle
            if P.getY() > size*50:
                solving = 1
                solver()
            #Else perform board click
            else:
                xco = P.getX()//50
                yco = P.getY()//50
                points = (xco + (yco)*(size))
                clicker(size, points)
                clickcount = clickcount + 1
    win2 = GraphWin("Winner", 300, 50)
    win4.close()
    wintext =  Text(Point(150,25), "Click here to play again!")
    wintext.draw(win2)
    win2.getMouse() 
    win.close()
    win2.close()
    play_boardgame()
    
               
    

#-----------------------------------------------
# Function purpose: To change white tiles to black
# Syntax: changewhite(i)
# Parameter: i is the location of the tile to be flipped
# Return value: None
#-----------------------------------------------               
                
def changewhite(i):
    global rect_list
    global col_list
    rect_list[i].setFill('black')
    col_list.pop(i)
    col_list.insert(i, 'b')
    
#-----------------------------------------------
# Function purpose: To change black tiles to white
# Syntax: changeblack(i)
# Parameter: i is the location of the tile to be flipped
# Return value: None
#-----------------------------------------------
   
def changeblack(i):
    global rect_list
    global col_list
    rect_list[i].setFill('white')
    col_list.pop(i)
    col_list.insert(i, 'w')

#-----------------------------------------------
# Function purpose: To change white tiles to black and black tiles to white
# Syntax: changer(i)
# Parameter: i is the location of the tile to be flipped
# Return value: None
#-----------------------------------------------
    
def changer(i):
    global col_list
    global rect_list
    global move_list
    if solving == 0:
        move_list.append(int(i))
    if col_list[int(i)] == 'b':
        changeblack(int(i))
    else:
        changewhite(int(i))


#-----------------------------------------------
# Function purpose: Solves the puzzle by reproducing every click
# Syntax: solver()
# Parameter: sNone
# Return value: None
#-----------------------------------------------
def solver():
    global col_list
    global rect_list
    global move_list
    while (len(move_list) > 0):
        i = move_list.pop(0)
        changer(i)
#-----------------------------------------------
# Function purpose: To interpret how a clicked tile should alter the game board and to inact that change. Used for player clicks and for the initial randomization of the game
# Syntax: clicker(size, points)
# Parameter: size - the size of the board  points - the location of the clicked tile
# Return value: None
#-----------------------------------------------
        
def clicker(size, points):
        
        
    if points == 0:
        for i in [points, points + 1, points + size]:
            changer(i)
    elif points == size - 1:
        for i in [points, points - 1, points + size]:
            changer(i)
    elif points == size*size -size:
        for i in [points, points + 1, points - size]:
            changer(i)
    elif points == size*size - 1:
        for i in [points, points - 1, points - size]:
            changer(i)
    elif points > 0 and points < size -1:
        for i in [points, points -1, points + 1, points + size]:
            changer(i)
    elif points > size*size - size and points < size*size - 1:
        for i in [points, points -1, points + 1, points - size]:
            changer(i)
    elif points == 2*size-1 or points == 3*size-1 or points == 4*size -1 or points == 5*size - 1 or points == 6*size - 1 or points == 7*size - 1 or points == 8*size - 1 or points == 9*size - 1 or points == 10*size -1 or points == 11*size -1:
        for i in [points, points - 1, points - size,points + size]:
            changer(i)
    elif points == size or points ==2*size or points == 3*size or points == 4*size or points == 5*size or points == 6*size or points == 7*size or points == 8*size or points == 9*size or points == 10*size or points == 11*size:
        for i in [points, points + 1, points - size, points + size]:
            changer(i)
    else:
        for i in [points,points + 1, points - 1, points + size, points - size]:
            changer(i)

#-----------------------------------------------
# Function purpose: To create a window that allows the player to select the size of that board, and another window that displays the rules of the game
# Syntax: size_selector()
# Parameter: None
# Return value: The desired size of the board
#-----------------------------------------------
           
def size_selector():
    global win4
    win3 = GraphWin("Welcome!", 200, 200)
    rect = Rectangle(Point(0, 0), Point(200, 100))
    rect.setFill('white')
    rect.draw(win3)
    recttext = Text(Point(100, 25), 'Welcome to a unique and')
    recttext.draw(win3)
    recttext = Text(Point(100, 50), 'original boardgame by Neill')
    recttext.draw(win3)
    recttext = Text(Point(100, 75), 'Please select a board size')
    recttext.draw(win3)
    rect = Rectangle(Point(0, 150), Point(50, 200))
    rect.setFill('black')
    rect.draw(win3)
    rect = Rectangle(Point(50, 100), Point(100, 150))
    rect.setFill('black')
    rect.draw(win3)
    rect = Rectangle(Point(100, 150), Point(150, 200))
    rect.setFill('black')
    rect.draw(win3)
    rect = Rectangle(Point(150, 100), Point(200, 150))
    rect.setFill('black')
    rect.draw(win3)
    rect = Rectangle(Point(0, 100), Point(50, 150))
    rect.setFill('white')
    rect.draw(win3)
    rect = Rectangle(Point(50, 150), Point(100, 200))
    rect.setFill('white')
    rect.draw(win3)
    rect = Rectangle(Point(100, 100), Point(150, 150))
    rect.setFill('white')
    rect.draw(win3)
    rect = Rectangle(Point(150, 150), Point(200, 200))
    rect.setFill('white')
    rect.draw(win3)    
    recttext = Text(Point(25, 175), '5')
    recttext.setTextColor('white')
    recttext.draw(win3)
    recttext = Text(Point(75, 125), '8')
    recttext.setTextColor('white')
    recttext.draw(win3)
    recttext = Text(Point(125, 175), '10')
    recttext.setTextColor('white')
    recttext.draw(win3)
    recttext = Text(Point(175, 125), '12')
    recttext.setTextColor('white')
    recttext.draw(win3)
    size = 0
    win4 = GraphWin('Rules', 250, 250)
    y = -1
    while y < 5:
        x = 0
        y = y + 1
        while x < 5:
            rect = Rectangle(Point((x)*50, ((y)*50)), Point((x + 1)*50, ((y + 1)*50)))
            rect.setOutline('grey')
            if y % 2:
                if x % 2:
                    rect.setFill('white')
                else: 
                    rect.setFill('black')
            if not y % 2:
                if x % 2:
                    rect.setFill('black')
                else:
                    rect.setFill('white')
            rect.draw(win4)
            x = x + 1
            recttext = Text(Point(25, 175), '5')
    recttext = Text(Point(125, 38), 'When a tile is clicked, that tile,')
    recttext.setTextColor('teal')
    recttext.draw(win4)
    recttext = Text(Point(125, 76), 'the one above it, below it, to its')
    recttext.setTextColor('teal')
    recttext.draw(win4)
    recttext = Text(Point(125, 114), 'right, and to its left will change color')
    recttext.setTextColor('teal')
    recttext.draw(win4)
    recttext = Text(Point(125, 152), 'The objective is to make')
    recttext.setTextColor('teal')
    recttext.draw(win4)
    recttext = Text(Point(125, 190), 'all of the tiles white')
    recttext.setTextColor('teal')
    recttext.draw(win4)
    recttext = Text(Point(125, 228), 'Good luck!')
    recttext.setTextColor('teal')
    recttext.draw(win4)                    
        
    while size == 0:
        P = win3.getMouse()
        xco = P.getX()//50
        yco = P.getY()//50
        points = (xco + (yco)*(size))
        if xco == 0 and yco == 3:
            size = 5
        if xco == 1 and yco == 2:
            size = 8
        if xco == 2 and yco == 3:
            size = 10
        if xco == 3 and yco == 2:
            size = 12
    win3.close()
    return size
                
