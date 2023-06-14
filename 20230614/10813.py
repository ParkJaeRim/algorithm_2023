# 5 4
# 1 2
# 3 4
# 1 4
# 2 2
import sys


M, N = map(int, sys.stdin.readline().split(" "))

basket = [0] * M
for i in range(0, M):
    basket[i] = i + 1


def swap(a, b):
    tmp = a
    a = b
    b = tmp
    return a, b


for i in range(0, N):
    a, b = map(int, sys.stdin.readline().split(" "))
    newa, newb = basket[b - 1], basket[a - 1]
    basket[a - 1] = newa
    basket[b - 1] = newb

answer = ''
for j in range(0, len(basket)):
    answer += str(basket[j]) + " "

print(answer.rstrip())