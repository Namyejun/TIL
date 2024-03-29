## 간단하면서 기본적인 정렬 알고리즘: 선택 정렬과 삽입 정렬

### 정렬 알고리즘
- 정렬(Sorting)이란 **데이터를 특정한 기준에 따라 순서대로 나열**하는 것이다.
- 일반적으로 **문제 상황에 따라서 적절한 정렬 알고리즘**이 공식처럼 사용한다.

### 선택 정렬(selection sort)
- 처리되지 않은 데이터 중에서 **가장 작은 데이터를 선택해 맨 앞에 있는 데이터와 바꾸는 것을 반복**한다.

### 선택 정렬의 시간 복잡도
- 선택 정렬은 N번 만큼 가장 작은 수를 찾아서 맨 앞으로 보내야 한다.
- 구현 방식에 따라서 사소한 오차는 있을 수 있지만 전체 연산 횟수는 다음과 같다
    - `N + (N - 1) + ... + 2`
- 이는 등차수열 공식에 따라 `(N^2 + N -2) / 2`로 표현할 수 있다.
- Big O notation에 따라 `O(N^2)`이 된다.

### 삽입 정렬(insertion sort)
- **처리되지 않은 데이터를 하나씩 골라 적절한 위치에 삽입**한다.
- 선택 정렬에 비해 구현 난이도가 높은 편이지만, 일반적으로 **더 효율적으로 동작**한다.

### 삽입 정렬의 시간 복잡도
- 삽입 정렬의 시간 복잡도는 `O(N^2)`이며, 선택 정렬과 마찬가지로 반복문이 두 번 중첩되어 사용된다.
- 삽입 정렬은 현재 리스트의 데이터가 거의 정렬되어 있는 상태라면 매우 빠르게 동작한다.
    - 최선의 경우 `O(N)`의 시간복잡도를 가진다.

---

## 더 빠른 정렬 알고리즘: 퀵 정렬과 계수 정렬

### 퀵 정렬(quick sort)
- **기준 데이터를 설정**하고 **그 기준보다 큰 데이터와 작은 데이터의 위치를 바꾸는 방법**이다.
- **일반적인 상황에서 가장 많이 사용**되는 정렬 알고리즘 중 하나이다.
- 병합 정렬과 더불어 대부분의 프로그래밍 언어의 정렬 라이브러리의 근간이 되는 알고리즘이다.
- 가장 기본적인 퀵 정렬은 **첫 번쨰 데이터를 기준 데이터(pivot)로 설정**한다.

### 퀵 정렬이 빠른 이유
- 이상적인 경우 분할이 절반씩 일어난다면 전체 연산 횟수로 `O(NlogN)`을 기대할 수 있다.
- 너비 * 높이 = N * logN = NlogN

### 퀵 정렬의 시간 복잡도
- 퀵 정렬은 평균의 경우 `O(NlogN)`의 시간 복잡도를 가진다.
- 하지만 최악의 경우 `O(N^2)`의 시간 복잡도를 가진다.
    - 이미 정렬되어 있는 경우 최악의 시간 복잡도를 가진다.

### 구현
- 일반적인 반복문을 사용할 수 있다.
- 재귀 함수를 이용해 퀵 정렬을 이용할 수 있다.

### 계수 정렬(counting sort)
- 특정한 조건이 부합할 때만 사용할 수 있지만 매우 빠르게 동작하는 정렬 알고리즘이다.
    - 계수 정렬은 데이터의 크기 범위가 제한되어 정수 형태로 표현할 수 있을 때 사용 가능하다.
- 데이터의 개수가 N, 범위의 크기가 K일 때 최악의 경우에도 `O(N + K)`를 보장한다.

### 동작 방식
1. 제시된 숫자 배열 길이를 가지는 배열을 새로 만들어준다.
2. 숫자 배열의 처음 기록된 수를 인덱스로 하여 새로 만들어준 배열에 값을 1 더해준다.
    - 값의 개수를 세어준다라는 뜻
3. 2의 과정을 배열이 끝날 때 까지 반복한다.
4. 3이 끝나면 새로운 배열을 첫 인덱스부터 개수만큼 출력해주면 끝난다.

### 계수 정렬의 복잡도 분석
- 계수 정렬의 시간 복잡도와 공간 복잡도는 모두 `O(N + K)`이다.
- 계수 정렬은 때에 따라서 심각한 비효율성을 초래할 수 있다.
    - 데이터가 0과 999,999로 단 2개만 존재하는 경우
    - 공간 복잡도와 출력 면에서 손해를 본다.
- 계수 정렬은 동일한 값을 가지는 데이터가 여러 개 등장할 때 효과적으로 사용할 수 있다.

--- 