## 구현: 시뮬레이션과 완전 탐색

### 구현(Implementation)
- 구현이란, 머릿속에 있는 알고리즘을 소스코드로 바꾸는 과정이다.

- 흔히 알고리즘 대회에서 구현 유형의 문제란 풀이를 떠올리는 것은 쉽지만 소스코드로 옮기기 어려운 문제를 지칭한다.
- 예시
    - 알고리즘은 간단한데 코드가 지나칠 만큼 길어지는 문제
    - 실수 연산을 다루고, 특정 소수점 자리까지 출력해야 하는 문제
    - 문자열을 특정한 기준에 따라서 끊어 처리해야 하는 문제
    - 적절한 라이브러리를 찾아서 사용해야 하는 문제

- 일반적으로 알고리즘 문제에서의 2차원 공간은 행렬의 의미로 사용된다.
- 시뮬레이션 및 완전 탐색 문제에서는 2차원 공간에서의 방향 벡터가 자주 활용된다.

### 상하좌우
```python
move = {"L":(0, -1), "U":(-1, 0), "R":(0, 1), "D":(1, 0)}
N = int(input())
lst = list(map(str, input().split()))
x, y = 1, 1
for i in lst:
    nx, ny = x + move[i][0], y + move[i][1]
    if 1 <= nx <= N and 1 <= ny <= N:
        x, y = nx, ny
    else:
        pass
print(x, y)
```

### 시각
```python
N = int(input())
cnt = 0
for i in range(N + 1):
    for j in range(60):
        for k in range(60):
          if '3' in (str(i) + str(j) + str(k)):
             cnt += 1  
print(cnt)
```

### 왕실의 나이트
```python
s = input()
move = [(2,1),(-2,1),(2,-1),(-2,-1),(1,2),(-1,2),(1,-2),(-1,-2)]
x, y = ord(s[1]) - 49, ord(s[0]) - 97
cnt = 0
for m in move:
    nx, ny = x + m[0], y + m[1]
    if 0 <= nx <= 7 and 0 <= ny <= 7:
        cnt += 1
print(cnt)
```

### 문자열 재정렬
```python
import re
S = input()
uppper = re.compile("[A-Z]")
digit = re.compile("[0-9]")
upper_find = re.findall(uppper, S)
digit_find = re.findall(digit, S)
digit_sum = 0
for i in digit_find:
    digit_sum += int(i)
result = sorted(upper_find)
result.append(digit_sum)
print(*result, sep="")
```

---