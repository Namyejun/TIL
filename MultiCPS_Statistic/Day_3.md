## 확률변수와 확률분포, 분포의 특성치
### 확률변수

- 확률변수 : 표본공간에서 정의된 실수값 함수
    - 이산형 확률변수 : 확률변수가 취할 수 있는 값이 셀 수 있는 경우
    - 연속형 확률변수 : 주어진 구간에서 모든 실수 값을 취할 수 있어 셀 수 없는 경우

### 확률분포

- 확률질량함수, PMF (probability mass function)
    - 확률변수 X가 이산형인 경우 X가 취할 수 있는 값 $x_1, x_2, …, x_n$의 각각에 대하여 확률 $P[X = x_1], P[X = x_2], …, P[X = x_n]$을 대응시켜 주는 관계를 X의 확률질량함수라고 하며 f(x)로 표기.
- 확률질량함수의 성질
    1. 모든 i = 1,2,…,n에 대해 $0 \le f(x_i) \le 1$
    2. $\Sigma^n_{i=1} f(x_i) = 1$
- 확률밀도함수, PDF (probability density function)
    - 확률변수 X가 연속형인 경우 X가 가질 수 있는 구간 $(-\infin, \infin)$위에서의 함수 f(x)가 다음을 만족할 때, 이를 X의 확률밀도함수라고 함.
- 확률밀도함수의 성질
    1. 모든 a, b에 대해 $0 \le \int_a^b f(x) dx \le 1$
    2. $\int_{-\infin}^{\infin} f(x)dx = 1$
- 누적분포함수, CDF (cumulative density function)
    - X의 확률밀도함수가 f(x)일 때, X의 누적분포함수 F(x)는 $X \le x$인 모든 X에 대한 f(x)의 적분 값이 됨.
    - $F(-\infin) = 0, F(\infin) = 1$
    - x가 증가할 때 F(x)도 증가하며, F(x)는 음의 값을 가질 수 없음.

### 확률분포의 특성치

- 기대값 : 분포의 무게중심, 중심 위치를 나타냄.
    - $E[X] = \mu = \Sigma_{x \in S} xf(x)$ → 이산형
    - $E[X] = \mu = \int_{-\infin}^{\infin} xf(x)dx$ → 연속형
- 분산 : 분포의 산포를 나타냄.
    - $V[X] = \sigma^2 = E[(X-\mu)^2]$
- 표준편차
    - $S[X] = \sigma = \sqrt{V[X]}$
