import sys

#
# 11
# 1 4 1 2 4 2 4 2 3 4 4
# 2

if __name__ == '__main__':
    # T = int(sys.stdin.readline())
    # arr = [0] * T
    #
    # arrs = sys.stdin.readline().split(" ")
    # findOne = int(sys.stdin.readline())
    #
    # answer = 0
    # for i in range(0, T):
    #     if int(arrs[i]) == findOne:
    #         answer += 1
    #
    # print(answer)

    input = sys.stdin.readline

    T = int(input())
    numList = list(map(int, input().split(" ")))
    findOne = int(input())

    print(numList.count(findOne))
