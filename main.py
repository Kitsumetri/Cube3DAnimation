from math import cos, sin, tan

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

    x_0 = round(HEIGHT/2)  # 17
    y_0 = round(WIDTH/2)   # 85
    aspect = (11*WIDTH)/(24*HEIGHT)

    for t in range(100000):
        screen = make_resolution()
        for i in range(-2*x_0, x_0):
            for j in range(-2*y_0, y_0):
                default_x = (x_0 + i) * aspect
                x = (default_x * cos(t*0.01) - (y_0 + j) * sin(t*0.01))
                y = (default_x * sin(t*0.01) + (y_0 + j) * cos(t*0.01))
                if abs(x) + abs(y) <= 20:
                    screen[i][j] = '@'
        print_drawing(screen)


def main():
    drawing()


if __name__ == '__main__':
    main()
