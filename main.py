# Resolution
WIDTH = 170
HEIGHT = 34

RTX = tuple()


def make_resolution():
    resolution = [['!'] * WIDTH for i in range(HEIGHT)]
    return resolution


def print_drawing(screen):
    for i in screen:
        print(''.join(list(map(str, i))))


def drawing():
    screen = make_resolution()
    x_0 = 17
    y_0 = 85
    for i in range(HEIGHT):
        for j in range(WIDTH):

            if i > 85:
                x = x_0 - i
            else:
                x = x_0 + i

            if j > 17:
                y = y_0 - j
            else:
                y = y_0 + j

            if abs(x) + abs(y) <= 50:
                screen[i][j] = '@'
    print_drawing(screen)


def main():
    drawing()


if __name__ == '__main__':
    main()
