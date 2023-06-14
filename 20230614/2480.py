if __name__ == '__main__':

    firstNoon, secondNoon, thirdNoon = map(int, input().split(" "))

    if firstNoon == secondNoon == thirdNoon:
        print(10000 + (firstNoon * 1000))

    elif firstNoon == secondNoon:
        print(1000 + (firstNoon * 100))
    elif secondNoon == thirdNoon:
        print(1000 + (secondNoon * 100))
    elif thirdNoon == firstNoon:
        print(1000 + (thirdNoon * 100))

    else:
        print(max(firstNoon, secondNoon, thirdNoon) * 100)
