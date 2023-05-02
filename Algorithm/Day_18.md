## 자주 사용되는 기타 알고리즘: 투 퍼인터와 구간 합

### 투 포인터(Two pointer)
- 투 포인터 알고리즘은 리스트에 순차적으로 접근해야 할 때 두 개의 점 위치를 기록하면서 처리하는 알고리즘을 의미한다.
- 흔히 2, 3, 4, 5, 6, 7번 학생을 지목해야 할 때 간단히 '2번부터 7번까지의 학생' 이라고 부른다.
- 리스트에 담긷 데이터에 순차적으로 접근해야 할 때는 시작점과 끝점 2개의 점으로 접근할 데이터의 범위를 표현할 수 있다.
  
### 특정한 합을 가지는 부분 연속 수열 찾기
``` python
N, M = map(int, input().split())
lst = list(map(int, input().split()))
cnt = 0
i = 0
j = 1
while i < N:
    while j < N or i < N:
        if sum(lst[i:j]) == M:
            cnt += 1
        if sum(lst[i:j]) < M:
            j += 1
        elif sum(lst[i:j]) >= M:
            i += 1
print(cnt)
```

### 구간 합(Interval Sum)
- 구간 합 문제: 연속적으로 나열된 N개의 수가 있을 때 특정 구간의 모든 수를 합한 값을 계산하는 문제

### 구간 합 빠르게 계산하기
```python
N = int(input())
lst = [0] + list(map(int, input().split()))
for i in range(1, len(lst)):
    lst[i] += lst[i - 1]
M = int(input())
for _ in range(M):
    left, right = map(int, input().split())
    print(lst[right] - lst[left - 1])
```