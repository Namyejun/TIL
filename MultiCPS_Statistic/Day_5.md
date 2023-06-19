## 정규분포, 표준정규분포
### 정규분포의 정의

- 확률변수 X가 평균이 $\mu$ 분산이 $\sigma^2$이고 다음의 확률밀도함수를 가질 때, X는 정규분포를 따른다고 함.
    
    $f(x) = \dfrac {1} {\sqrt {2\pi}\sigma}e^{{-(x-\mu)^2} /{2\sigma^2}}$, $-\infin < x < \infin$
    
    - 이 경우 $X \text{\textasciitilde} N[\mu, \sigma^2]$라고 함.

### 정규분포 확률밀도함수의 개형

- $\mu$는 분포의 중심
- $\mu$를 중심으로 대칭이고, $\mu$에서 가장 큰 값이 되는 하나의 봉우리만 가짐
- $\sigma^2$이 크면 분포의 산포가 커지고, $\sigma^2$이 작으면 분포의 산포가 작아짐.

### 정규분포의 특성치

- $X \text{\textasciitilde} N[\mu, \sigma^2]$인 경우
    - $E[x] = \mu$
    - $V[X] = \sigma^2$

### 표준정규분포와 정규확률변수의 표준화

- 표준정규분포
- $X \text{\textasciitilde} N[\mu, \sigma^2]$일 때, 정규분포의 선형불변성에 의해
    
    $Z = \dfrac {X - \mu} {\sigma} \text{\textasciitilde} N[0,1]$이 되며,
    이 때의 평균이 0 분산이 1인 정규분포를 표준정규분포라 정의함
    

### 표준정규 확률변수의 $(1-\alpha)$분위수 : $Z_\alpha$

- $Z \text{\textasciitilde} N[0,1]$일 때, $P[Z < c] = 1 - \alpha$를 만족하는 $Z$의 $(1-\alpha)$분위수 c를 $Z_\alpha$으로 표기.
- $(1-\alpha)$분위수 = $\alpha$보다 작은 애들의 범위
