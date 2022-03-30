# Resolution
WIDTH = 170
HEIGHT = 34

RTX = tuple()


def make_resolution():
    resolution = [['!'] * WIDTH for i in range(HEIGHT)]
    return resolution


def print_drawing(drawing):
    for i in drawing:
        print(''.join(list(map(str, i))))


def drawing():
    resolution = make_resolution()
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
                resolution[i][j] = '@'
    print_drawing(resolution)


def main():
    drawing()


if __name__ == '__main__':
    main()
