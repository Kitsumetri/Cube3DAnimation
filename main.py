
# Resolution
WIDTH = 170
HEIGHT = 34


class Resolution:

    def make_resolution(self):
        resolution = [['#'] * WIDTH for i in range(HEIGHT)]
        for i in resolution:
            print(''.join(list(map(str, i))))


    def drawing(self, resolution):
        for i in range (WIDTH):
            for j in range(HEIGHT):
                x = (i/WIDTH)*2
                y = (j/HEIGHT)*2
                if abs(x)+abs(y) == 1:
                    resolution[i][j] = '@'
        for i in resolution:
            print(''.join(list(map(str, i))))


def main():

if __name__ == '__main__':
    main()
