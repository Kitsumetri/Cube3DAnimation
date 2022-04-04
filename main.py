from math import cos, sin, sqrt
import numpy as np

# Resolution (WIDTH/HEIGHT = 5/1)
WIDTH = 300
HEIGHT = 60

RTX = tuple(" .:!/)(l1Z4H9W8$@")


def get_color(vector):
    color = round(sqrt(vector[0] ** 2 + vector[1] ** 2) / 2)
    if color < 0:
        color = 0
    if color > len(RTX):
        color = len(RTX)
    return color


def rotation(default_vector, t):
    matrix_rotate = np.array([[cos(t), sin(t)], [-sin(t), cos(t)]])
    return default_vector.dot(matrix_rotate)


def make_resolution():
    resolution = [[' '] * WIDTH for i in range(HEIGHT)]
    return resolution


def print_drawing(screen):
    for i in screen:
        print(''.join(list(map(str, i))))


def drawing():
    x_0 = round(HEIGHT/2)
    y_0 = round(WIDTH/2)

    for t in range(10000):
        screen = make_resolution()
        for i in range(-2*x_0, x_0):
            for j in range(-2*y_0, y_0):

                default_vector = np.array([(x_0 + i) * (11*WIDTH)/(24*HEIGHT), (y_0 + j) + 70])

                vector = rotation(default_vector, t)

                # Square
                if abs(vector[0]) + abs(vector[1]) <= 38:
                    color = get_color(vector)
                    if color == 0:
                        screen[i][j] = '0'
                    else:
                        screen[i][j] = RTX[-color]

        print_drawing(screen)


def main():
    drawing()


if __name__ == '__main__':
    main()
