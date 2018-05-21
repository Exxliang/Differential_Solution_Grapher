#PROGRAM NAME: DIFFERENTIAL GRAPHER
#WRITTEN BY: ERIC LIANG
#BLOCK: 2-A
#DESCRIPTION: A SYSTEM WHICH LETS YOU FIND SOLUTIONS TO DIFFERENTIAL EQUATIONS
###############################################################################

from graphics import *
from math import *
import time

print "Welcome to the Differential Grapher!"
print "Here, you can visualize differential equations with Euler's method and vector fields."
print

#SETS THE WINDOW'S BOUNDARIES
a = input("Min X-Value: ")
c = input("Max X-Value: ")
b = input("Min Y-Value: ")
d = input("Max Y-Value: ")

win = GraphWin("Differential Grapher",800,800)
win.setCoords(a,b,c,d)
win.setBackground("white")

def clr_screen():
        #CLEARS THE SCREEN OF POINTS AND ARROWS
        clear = Rectangle(Point(a,b),Point(c,d))
        clear.setOutline("white")
        clear.setFill("white")
        clear.draw(win)
        x_axis = Line(Point(0,d),Point(0,b))
        y_axis = Line(Point(c,0),Point(a,0))
        x_axis.setArrow("both")
        y_axis.setArrow("both")
        x_axis.draw(win)
        y_axis.draw(win)
        
class DiffEqu():
    #INCLUDES ALL THE FUNCTIONS ASSOCIATED WITH THE DIFFERENTIAL EQUATION    
    background = False
    def __init__(self,equ):
        #SETS THE EQUATION IN USE    
        self.equ = equ

    def solution(self):
        #ENABLES THE USER TO FIND SOLUTIONS BY CLICKING INITIAL POINTS
        xx = input("Step: (0.1 to 0.4) ")
        self.xx = xx
        colour = raw_input("Colour of Solution: ")
        choice = raw_input("Click or Point? (C or P) ")
        print
        if choice.lower() == "c":
                print "Click an initial value!\n"
                print "Press 'e' and click one more time to exit.\n"
        else:
                print "Input your desired points.\n"
                print "Input 'e' for both x and y to exit.\n"        
        while True:
            if choice.lower() == "c":
                p = win.getMouse()
                x,y = p.getX(),p.getY()
            elif choice.lower() == "p":
                x = raw_input("X-Coordinate: ")
                y = raw_input("Y-Coordinate: ")
                if x == "e" and y == "e":
                    return
                x,y = float(x),float(y)
                print
            while a <= x <= c and b <= y <= d:
                dydx = eval(self.equ)
                x1 = x + xx
                y1 = dydx*(xx) + y
                lin = Line(Point(x,y),Point(x1,y1))
                lin.setOutline(colour)
                lin.setArrow("last")
                lin.draw(win)
                x,y = x1,y1
                time.sleep(0.005)
            end_signal = win.checkKey()
            if end_signal == "e":
                return

    def slope(self):
        #FINDS THE TANGENT SLOPE AT A POINT AND DRAWS THAT POINT
        choice = raw_input("Click or Point? (C or P) ")
        print
        if choice.lower() == "c":
            print "Click a place!\n"
            p = win.getMouse()
            x,y = p.getX(),p.getY()
        else:
            print "Input your point.\n"
            x = input("X-Value: (%s to %s) " % (str(a),str(c)))
            y = input("Y-Value: (%s to %s) " % (str(b),str(d))) 
        m = eval(self.equ)
        yr = m*(c-x) + y
        yl = m*(a-x) + y
        lin = Line(Point(a,yl),Point(c,yr))
        lin.setOutline("blue")
        lin.draw(win)
        pin = Circle(Point(x,y),(d-b)*0.0025)
        pin.setFill("black")
        pin.draw(win)
        print "At (%s,%s), the slope is %s." % (str(x),str(y),str(m))

    def VecField(self):
        #DRAWS A VECTOR FIELD ACCORDING TO PARAMETERS
        z = input("Density: (3 to 6) ")
        xx = input("Step: (0.1 to 0.4) ")
        for i in range(z*a,z*(c+1)):
                for j in range(z*b,z*(d+1)):
                    x = i/float(z)
                    y = j/float(z)
                    dydx = eval(self.equ)
                    x1 = x + xx
                    y1 = dydx*(xx) + y
                    lin = Line(Point(x,y),Point(x1,y1))
                    lin.setOutline("grey")
                    lin.draw(win)
        self.background = True

    def point(self):
        #RETURNS POINT WHERE MOUSE CLICKS
        print "Please click your desired point.\n"
        p = win.getMouse()
        x = p.getX()
        y = p.getY()
        print "(%s,%s)" % (str(x),str(y))

def main():
    #ORGANIZES THE CONTENT AND ALLOWS THE USER TO MAKE CHOICES ON THE EQUATION    
    print
    clr_screen()
    name = raw_input("Enter your equation: ")
    Equation = DiffEqu(name)
    # v SHOWS THE OPTIONS THE PLAYER HAS
    while True:
        print
        print "--------------------------------------------------------------------------------"
        choice = input("1: Graph Solutions, 2: Find Slope, 3: Draw Vector Field, 4: Locate Point, \
5: Different Equation, 6: Clear Screen, or 7: Quit? (1,2,3,4,5,6, or 7) ")
        print "--------------------------------------------------------------------------------"
        print
        if choice == 1:
            Equation.solution()
        elif choice == 2:
            Equation.slope()
        elif choice == 3:
            Equation.VecField()
        elif choice == 4:
            Equation.point()
        elif choice == 5:
            main()
        elif choice == 6:
            clr_screen()
        else:
            print "Goodbye!"
            time.sleep(1.2)
            win.close()
            return

main()

    
        
