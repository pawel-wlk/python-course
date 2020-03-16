import os
import sys


def rename(directory):
    for filename in os.listdir(directory):
        newpath = directory + '/' + filename.lower()
        os.rename(directory + '/' + filename, newpath)
        if os.path.isdir(newpath):
            rename(newpath)


if __name__ == "__main__":
    rename(sys.argv[1])
