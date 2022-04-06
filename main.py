# PycCharm console animation

from vectors import *
from screen_draw import *


'''
   vector example:
       [[x],
        [y],
        [z],
        [w = 1]]
'''


def drawing():
    x_0 = round(HEIGHT/2)
    y_0 = round(WIDTH/2)

    for t in range(10000):
        screen = make_resolution()
        for i in range(-2*x_0, x_0):
            for j in range(-2*y_0, y_0):

                default_vector = np.array([(x_0 + i) * (11*WIDTH)/(24*HEIGHT), (y_0 + j) + 70, 0, 1])
                vector = rotation(default_vector, pi/4)

                vector = rotation(vector, t)
                # vector = scale(vector, t)

                # Square
                if abs(vector[0]) + abs(vector[1] + abs(2)) <= 38:
                    color = get_color(vector)
                    if color == 0:
                        screen[i][j] = '0'
                    else:
                        screen[i][j] = RTX[-color]

        print_drawing(screen)
        screen.clear()


def main():
    drawing()


if __name__ == '__main__':
    main()
