import sys

if __name__ == '__main__':
    myString = sys.stdin.readline().rstrip()

    arr = [-1] * (ord("z") - ord("a") + 1)


    for i in range(0, len(myString)):
        if(arr[ord(myString[i])-97] == -1):
            arr[ord(myString[i])-97] = i

    print(*arr)