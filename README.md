# algorithm_2023
파이썬으로 푸는 알고리즘 문제


## 20230614

- 입력 받기
```python
import sys

if __name__ == '__main__':
    givenInt = int(sys.stdin.readline())
    a, b, c = map(int, input().split(" "))
    givenIntArray = list(map(int, sys.stdin.readline().split(" ")))

```

- pyton은 swap 함수 구현이 필요 없음
```python
def swap(a, b):
    tmp = a
    a = b
    b = tmp
    return a, b

대신에...

if __name__ == '__main__':
    a, b = b, a
```