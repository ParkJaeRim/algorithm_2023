import sys

if __name__ == '__main__':
    N = int(sys.stdin.readline())
    score = list(map(int, sys.stdin.readline().split(" ")))

    maxScore = max(score)
    totalScore = 0
    for i in range(0, N):
        totalScore += score[i] / maxScore * 100

    print(totalScore / N)
