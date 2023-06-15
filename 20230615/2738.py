
import sys

if __name__ == '__main__':
    N, M = map(int, sys.stdin.readline().split())
    firstMap = [[0] * M] * N
    secondMap = [[0] * M] * N

    for i in range(0, N):
        firstMap[i] = list(map(int, sys.stdin.readline().split()))

    for i in range(0, N):
        secondMap[i] = list(map(int, sys.stdin.readline().split()))

    for a in range(0, N):
        for b in range(0, M):
            print(firstMap[a][b] + secondMap[a][b], end=" ")
        print()
