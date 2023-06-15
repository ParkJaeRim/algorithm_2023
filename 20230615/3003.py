import sys

if __name__ == '__main__':
    wrongChess = list(map(int, sys.stdin.readline().split(" ")))
    rightChess = [1, 1, 2, 2, 2, 8]

    for i in range(0, len(wrongChess)):
        wrongChess[i] = rightChess[i] - wrongChess[i]

    print(*wrongChess)
