# 5 4
# 1 2
# 3 4
# 1 4
# 2 2
import sys

if __name__ == '__main__':

    M, N = map(int, sys.stdin.readline().split(" "))

    basket = [0] * M
    for i in range(0, M):
        basket[i] = i + 1

    for i in range(0, N):
        a, b = map(int, sys.stdin.readline().split(" "))
        newA, newB = basket[b - 1], basket[a - 1]
        basket[a - 1] = newA
        basket[b - 1] = newB

    answer = ''
    for j in range(0, len(basket)):
        answer += str(basket[j]) + " "

    print(answer.rstrip())
