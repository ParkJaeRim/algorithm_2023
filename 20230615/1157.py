import sys

if __name__ == '__main__':
    word = sys.stdin.readline().upper()

    alphabetList = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    countAlphabetList = [0] * len(alphabetList)

    for i in range(0, len(alphabetList)):
        countAlphabetList[i] = word.count(alphabetList[i])

    howMany = 0
    answer = ''
    for i in range(0, len(countAlphabetList)):

        if countAlphabetList[i] == max(countAlphabetList):
            howMany += 1
            if howMany >= 2:
                break
            else:
                answer = alphabetList[i]

    if howMany >= 2:
        print("?")
    else:
        print(answer)
