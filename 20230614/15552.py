import sys

if __name__ == '__main__':

    T = int(sys.stdin.readline())

    for T in range(0, T):
        a, b = map(int, sys.stdin.readline().split(" "))
        print(a + b)
