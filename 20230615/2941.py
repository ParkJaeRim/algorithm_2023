import sys

if __name__ == '__main__':
    croatiaAlphabets = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

    givenWord = sys.stdin.readline()
    count = 0

    for croatia in croatiaAlphabets:
        howMany = givenWord.count(croatia)
        givenWord = givenWord.replace(croatia, "*", -1)
        count += howMany
    print(count + len(givenWord.replace("*", "", -1).strip()))
