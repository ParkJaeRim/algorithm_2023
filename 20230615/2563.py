import sys

if __name__ == '__main__':
    maps = [[0] * 100 for _ in range(100)]
    N = int(sys.stdin.readline())

    for i in range(0, N):
        start, end = map(int, sys.stdin.readline().split(" "))

        for a in range(start - 1, start + 9):
            for b in range(end - 1, end + 9):
                maps[a][b] = 1

    count = 0
    for m in range(0, len(maps)):
        for n in range(0, len(maps[m])):
            if maps[m][n] == 1:
                count += 1
    print(count)
