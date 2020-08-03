import os


def main():
    path = "../test-images/"
    for count, filename in enumerate(os.listdir(path)):
        dst = "image" + str(count) + ".jpg"
        src = '../test-images/' + filename
        dst = '../test-images/' + dst

        os.rename(src, dst)


if __name__ == '__main__':
    main()
