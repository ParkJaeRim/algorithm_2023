import sys

if __name__ == '__main__':

    given = sys.stdin.readline().strip()
    if given == "":
        print(0)
    else:
        print(len(given.split(" ")))