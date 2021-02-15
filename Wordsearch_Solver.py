from Wordsearch_class import Wordsearch
from graphics import *

Grid=Wordsearch("mygrid.txt")

#---Show the grid---
win=GraphWin(width=400,height=400)
win.setCoords(-1,Grid.height,Grid.width,-1) #(x1,y1,x2,y2)
#x1,y1 in lower left and x2,y2 in upper right

for i in range(Grid.height):
    for j in range(Grid.width):     
        letter=Text(Point(j,i),Grid.grid[i][j])
        letter.draw(win)
    
#---Find the word---
def FindWord(word):
    location=Grid.Find(word)
    print(location)
    if location==None:
        pass
    else:
        start,end=location[0],location[1]
        myLine=Line(Point(start[1],start[0]),Point(end[1],end[0]))
        myLine.setFill('red')
        myLine.setWidth(2)
        myLine.draw(win)
    return location

word='LUNCH'
FindWord(word)
#mytext=Text(Point((Grid.width-1)/2,-0.5),'Click to close window')
#mytext.draw(win)

win.getMouse()
win.close()
