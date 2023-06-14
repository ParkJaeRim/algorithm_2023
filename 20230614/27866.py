import sys

if __name__ == '__main__':
    myString = sys.stdin.readline()
    idx = int(sys.stdin.readline())

    print(myString[idx - 1])
