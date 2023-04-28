## 다양한 동적 계획법 문제 풀이

### 개미 전사
``` python
N = int(input())
lst = list(map(int, input().split()))
dp = [0 for i in range(N)]
dp[0] = lst[0]
dp[1] = max(lst[:2])
for i in range(2, N):
    dp[i] = max(dp[i - 2] + lst[i], dp[i - 1])
print(dp[N-1])
```

### 1로 만들기
``` python
X = int(input())
dp = [0 for i in range(30001)]
dp[1] = 0
for i in range(2, 30001):
    lst = [dp[i - 1] + 1]
    if i % 2 == 0:
        lst.append(dp[i//2] + 1)
    if i % 3 == 0:
        lst.append(dp[i//3] + 1)
    if i % 5 == 0:
        lst.append(dp[i//5] + 1)
    dp[i] = min(lst)
print(dp[X])
```

### 효율적인 화폐 구성
``` python
N, M = map(int, input().split())
coin_list = []
for i in range(N):
    coin_list.append(int(input()))

dp = [-1 for i in range(M + 1)]
for i in coin_list:
    if i <= M:
        dp[i] = 1
for i in range(1, M + 1):
    lst = []
    if dp[i] != -1:
        continue
    for j in coin_list:
        if 0 <= i - j <= M and dp[i - j] != -1:
            lst.append(dp[i - j] + 1)
    if lst:
        dp[i] = min(lst)
print(dp[M])
```

### 금광
``` python
T = int(input())
for _ in range(T):
    n, m = map(int, input().split())
    lst = list(map(int, input().split()))
    lst = [lst[i*m:(i+1)*m] for i in range(n)]

    dp = [[0 for j in range(m)] for i in range(n)]
    for i in range(n):
        dp[i][0] = lst[i][0]
    
    for i in range(1, m):
        for j in range(n):
            temp = []
            if j == 0:
                temp.append(dp[j][i - 1] + lst[j][i])
                temp.append(dp[j + 1][i - 1] + lst[j][i])
            elif j == n - 1:
                temp.append(dp[j - 1][i - 1] + lst[j][i])
                temp.append(dp[j][i - 1] + lst[j][i])
            else:
                temp.append(dp[j - 1][i - 1] + lst[j][i])
                temp.append(dp[j][i - 1] + lst[j][i])
                temp.append(dp[j + 1][i - 1] + lst[j][i])
            dp[j][i] = max(temp)
    print(max(dp[i][m - 1] for i in range(n)))
```

### 병사 배치하기
- LIS(Longest increasing Subsequence) 문제 : 가장 긴 증가하는 부분 수열
``` python
N = int(input())
lst = list(map(int, input().split()))
dp = [1 for i in range(N)]
for i in range(1, N):
    for j in range(i):
        if lst[j] >= lst[i]:
            dp[i] = max(dp[i], dp[j] + 1)
print(N - max(dp))
```
---