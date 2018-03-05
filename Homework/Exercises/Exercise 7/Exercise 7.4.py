from graphics import *
import math
"""
Robert Matthews
CS 1400
Section 002
Exercise 7

7.4
Chapter 7, Programming Exercise #14, pg. 240. Submit your source code as your answer.
"""

# do exercise 7 from chapter 4, but add a decision to handle the case where the line does not intersect the circle

win = GraphWin("Draw a Horizontal Line", 400, 400)
win.setCoords(-10.0, -10.0, 10.0, 10.0)
win.setBackground('Moccasin')


def message(msg):
    message = Text(Point(0, -9), msg)
    message.setFill('blue')
    message.draw(win)


def main():
    instructions = Text(Point(0, 9), 'Click on two points to draw a horizontal line.')
    instructions.setFill('blue')
    instructions.draw(win)

    ball = Circle(Point(0, 0), 5)  # radius is 5 from center 0
    ball.setOutline('black')
    ball.setWidth('2')
    ball.setFill('white')
    ball.draw(win)

    # draw first point
    p = win.getMouse()
    x1 = p.getX()
    y = p.getY()
    c = Circle(Point(x1, y), 0.1)
    c.setFill('blue')
    c.draw(win)
    txt = Text(Point(x1 + 1, y + .5), '')
    txt.setText('%0.2f, %0.2f' % (x1, y))
    txt.draw(win)

    # draw second point
    p2 = win.getMouse()
    x2 = p2.getX()
    c = Circle(Point(x2, y), 0.1)
    c.setFill('blue')
    c.draw(win)
    txt = Text(Point(x2 + 1, y + .5), '')
    txt.setText('%0.2f, %0.2f' % (x2, y))
    txt.draw(win)

    line = Line(Point(x1, y), Point(x2, y))
    line.setOutline('red')
    line.setWidth('3')
    line.draw(win)

    # is the line above or below the ball?
    if y > 5 or y < -5:
        txt = 'Line does not intersect Circle.'
        message(txt)

    else:
        txt = 'Line intersects Circle.'
        message(txt)

        # draw intersect points
        x = math.sqrt(25 - y ** 2)
        for i in range(2):
            pt = Circle(Point(x, y), 0.15)
            pt.setFill('lime')
            pt.draw(win)
            x = -x

    instructions.setText('Click anywhere to quit.')
    win.getMouse()
    win.close()


if __name__ == '__main__':
    main()
