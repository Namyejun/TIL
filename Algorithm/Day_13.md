## 이진 탐색: 정렬된 데이터에서 빠르게 데이터를 찾아보자

### 이진 탐색 알고리즘
- 순차 탐색: 리스트 안에 있는 특정한 데이터를 찾기 위해 앞에서부터 데이터를 하나씩 확인하는 방법
- 이진 탐색: 정렬되어 있는 리스트에서 탐색 범위를 절반씩 좁혀가며 데이터를 탐색하는 방법
    - 이진 탐색은 시간점, 끝점, 중간점을 이용하여 탐색 범위를 설정한다.
    - 재귀적으로 구현하는 방법과 반복문으로 구현하는 방법이 존재한다.

### 이진 탐색의 시간 복잡도
- 단계마다 탐색 범위를 2로 나누는 것과 동일하므로 연산 횟수는 logN에 비례한다.
    - 다시 말해 이진 탐색은 탐색 범위를 절반씩 줄이며, 시간 복잡도는 `O(logN)`을 보장한다.

### 파이썬 이진 탐색 라이브러리
- 이진 탐색 라이브러리인 bisect가 존재한다.
    - `from bisect import bisect_left, bisect_right`
    - 이것을 활용해 값이 특정 범위에 속하는 데이터의 개수를 구할 수 있다.

### 파라메트릭 서치(Parametric Search)
- 파라메트릭 서치란 최적화 문제를 결정 문제(예 혹은 아니오)로 바꾸어 해결하는 기법이다.
    - ex: 특정한 조건을 만족하는 가장 알맞은 값을 빠르게 찾는 최적화 문제
- 일반적으로 코딩 테스트에서 파라메트릭 서치 문제는 이진 탐색을 이용하여 해결이 가능하다.

### 떡볶이 집 문제
- 시간제한 : 2초
``` python
from bisect import bisect_left, bisect_right
N, M = map(int, input().split())
lst = list(map(int, input().split()))
lo, hi = 0, max(lst)
result = 0
while lo <= hi:
    md = (lo + hi)//2
    total = 0
    for i in lst:
        if i <= md:
            pass
        else:
            total += i - md
    if total >= M:
        result = md
        lo = md + 1
    else:
        hi = md - 1
print(result)
```

### 정렬된 배열에서 특정 수의 개수 구하기
- 시간제한 : 1초
``` python
from bisect import bisect_left, bisect_right
N, x = map(int, input().split())
lst = list(map(int, input().split()))
if x not in lst:
    print(-1)
else:
    print(bisect_right(lst, x) - bisect_left(lst, x))
```

---