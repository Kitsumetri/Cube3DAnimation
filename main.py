
# Resolution
WIDTH = 170
HEIGHT = 34


def make_resolution():
    resolution = [['#'] * WIDTH for i in range(HEIGHT)]
    for i in resolution:
        print(''.join(list(map(str, i))))


##def drawing():



def main():
    make_resolution()


if __name__ == '__main__':
    main()
