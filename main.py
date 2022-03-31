from math import cos, sin, sqrt, pi

# Resolution (WIDTH/HEIGHT = 5/1)
WIDTH = 300
HEIGHT = 60

RTX = tuple(" .:!/r(l1Z4H9W8$@")


def make_resolution():
    resolution = [[' '] * WIDTH for i in range(HEIGHT)]
    return resolution


def print_drawing(screen):
    for i in screen:
        print(''.join(list(map(str, i))))


def drawing():

    x_0 = round(HEIGHT/2)
    y_0 = round(WIDTH/2)

    for t in range(100000):
        screen = make_resolution()
        for i in range(-2*x_0, x_0):
            for j in range(-2*y_0, y_0):

                default_x = (x_0 + i) * (11*WIDTH)/(24*HEIGHT)
                default_y = (y_0 + j) + 60

                # Rotation
                rotation_speed = t * 0.01
                x = (default_x * cos(rotation_speed) - default_y * sin(rotation_speed))
                y = (default_x * sin(rotation_speed) + default_y * cos(rotation_speed))

                # X-axis movement
                '''
                x = (default_x * cos(pi/4) - (default_y + sin(t*0.003)*50) * sin(pi/4))
                y = (default_x * cos(pi/4) + (default_y + sin(t*0.003)*50) * sin(pi/4))
                '''

                # Y-axis movement
                '''
                x = ((default_x + sin(t * 0.003) * 20) * cos(pi / 4) - default_y * sin(pi / 4))
                y = ((default_x + sin(t * 0.003) * 20) * cos(pi / 4) + default_y * sin(pi / 4))
                '''

                # Lights and shadows
                color = round(sqrt(x**2 + y**2)/2)
                if color < 0:
                    color = 0
                if color > len(RTX):
                    color = len(RTX)

                # Square
                if abs(x) + abs(y) <= 38:
                    screen[i][j] = RTX[-color]
                    # Core color
                    if color == 0:
                        screen[i][j] = '0'

        print_drawing(screen)


def main():
    drawing()


if __name__ == '__main__':
    main()
