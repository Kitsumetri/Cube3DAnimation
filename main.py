from math import cos, sin, pi

# Resolution
WIDTH = 170
HEIGHT = 34


RTX = tuple(" .:!/r(l1Z4H9W8$@")


def make_resolution():
    resolution = [[' '] * WIDTH for i in range(HEIGHT)]
    return resolution


def print_drawing(screen):
    for i in screen:
        print(''.join(list(map(str, i))))


def drawing():

    screen = make_resolution()
    x_0 = round(HEIGHT/2)  # 17
    y_0 = round(WIDTH/2)   # 85
    aspect = (11*WIDTH)/(24*HEIGHT)

    for t in range(0, 10):
        for i in range(-2*x_0, x_0):
            for j in range(-2*y_0, y_0):
                default_x = (x_0 + i) * aspect + sin(t)
                x = (default_x * cos(pi/4) - (y_0 + j) * sin(pi/4))
                y = (default_x * sin(pi/4) + (y_0 + j) * cos(pi/4))
                if abs(x) + abs(y) <= 20:
                    screen[i][j] = '@'
        print_drawing(screen)


def main():
    drawing()


if __name__ == '__main__':
    main()
