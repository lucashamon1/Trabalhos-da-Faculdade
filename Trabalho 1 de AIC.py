from graphics import *
import time
def main():
    if  True:
        win = GraphWin('Paris', 1000,800)
        dia = Image(Point(500,400),'OIP-_1_.gif')
        noite = Image(Point(500,400),'OIP.gif')
        botao = Circle(Point(500,100), 80)
        botao.setFill('red')
        dia.draw(win)
        botao.draw(win)
        cont = 0 
        if cont == 0 or cont == 2:
            clique1 = win.getMouse()
            x1 = float(clique1.getX())
            y1 = float(clique1.getY())
            if (x1 >= 420 and x1 <= 580) and (y1 >= 20 and y1 <=180):
                dia.undraw()
                noite.draw(win)
                cont = 1
        if cont == 1:
            clique2 = win.getMouse()
            x2 = float(clique2.getX())
            y2 = float(clique2.getY())
            if (x2 >= 420 and x2 <= 580) and (y2 >= 20 and y2 <=180):
                noite.undraw()
                dia.draw(win)
                cont = 2 
    win.getMouse()
    win.close()   
main()