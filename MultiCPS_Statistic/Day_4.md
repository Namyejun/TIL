## 이항분포, 포아송분포, 지수분포, 감마분포

### 베르누이 시행

- 매 시행 마다
    - 성공 또는 실패의 오직 두 가지 가능한 결과만 가짐
    - 성공의 확률이 p로 일정함
    
    의 조건을 만족하는 실험
    

### 이항 확률변수가 고려되는 실험

- 매 시행 마다
    - 성공 또는 실패의 오직 두 가지 가능한 결과만 가짐
    - 성공의 확률이 p로 일정함
    
    의 조건을 만족하는 베르누이 시행을
    
    - 독립적으로
    - n번 반복하는 실험

### 이항확률변수와 확률질량함수

- X : n번 시행 중 성공의 횟수로 정의
- x = 0,1,2,…,n의 값을 가짐
- $f(x) = P(X=x) = \dbinom{n}{x}p^x(1-p)^{n-x}$
- 이 경우 $X \text{\textasciitilde} Bin[n,p]$라고 함

### 이항분포의 특성치

- $X \text{\textasciitilde} Bin[n,p]$인 경우
    - $E[X] = np$
    - $V[X] = npq$

### 포아송 확률변수와 확률질량함수

- 단위시간에(t=1), 포아송 확률과정을 따르는 사건 A가 발생하는 횟수를 X로 정의하면,
$f(x) = P(X=x) = \dfrac {e^{-\lambda}\lambda^x} {x!}$, x = 0, 1, 2, …
- a이 경우 $X \text{\textasciitilde}Poison[\lambda]$라고 함.

### 포아송분포의 특성치

- $X \text{\textasciitilde} Poison[\lambda]$인 경우
    - $E[X] = V[X] = \lambda$

### 지수확률변수와 확률밀도함수

- 단위구간에서 평균발행횟수가 m인 포아송 확률과정을 따르는 사건 A가 한 번 일어난 뒤 그 다음 또 일어날 때까지 걸리는 시간 W로 정의됨.
$f(x) = \dfrac {1} {\lambda} e^{- {x}/{\lambda}}$, x > 0
- 이 경우 $X \text{\textasciitilde} Exp[\lambda]$라고 함.

### 지수분포의 특성치

- $X \text{\textasciitilde} Exp[\lambda]$인 경우
    - $E[X] = \dfrac {1} {\lambda}$
    - $V[X] = \dfrac {1} {\lambda^2}$

### 감마확률변수와 확률밀도함수

- 감마확률변수 X의 확률밀도함수는 양수인 $\theta$와 $k$에 대하여 다음과 같이 정의됨.
$f(x) = \dfrac {1} {\theta^k \Gamma(k)}x^{k-1}e^{-x/\theta}$, x > 0
- 이 경우 $X \text{\textasciitilde} Gamma[k, \theta]$라고 함.

### 감마분포의 특성치

- $X \text{\textasciitilde} Gamma[k, \theta]$인 경우
    - $E[X] = k\theta$
    - $V[X] = k\theta^2$
