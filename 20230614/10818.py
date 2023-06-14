import sys

# if __name__ == '__main__':
input = sys.stdin.readline

T = int(input())
numList = list(map(int, input().split(" ")))

print(min(numList), max(numList))
