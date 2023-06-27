## 점추정과 구간추정

### 통계적 추론 - 추정 개요

- 추정량
    - 모수 $\theta$의 추정에 사용되는 통계량을 $\theta$의 추정량($\hat \theta$으로 표기)이라고 함
    - 관찰된 표본자료로 추정량의 값을 계산한 것을 추정치라고 함

- 점추정과 구간추정
    - 점추정(point estimation) : 하나의 모수를 한 개의 값으로 추정
    - 구간추정(interval estimation) : 모수가 포함되리라 기대되는 구간으로 모수를 추정
    

### 신뢰구간

- 모수 $\theta$에 대한 신뢰구간 도출을 위해서는 다음을 알아야함
    - 추정량 $\hat \theta$
    - 추정량 $\hat \theta$의 표본분포 : 일반적으로 모수 $\theta$에 의존함.
    
- $\theta$의 추정량 $\hat \theta$을 적절하게 변형한 L과 U이 있어 다음을 만족하는 경우
$P[L \le \theta \le U] = 1-\alpha,\ \ \  0 \le \alpha \le 1$
- 구간 $(L, U)$을 $\theta$의 $100(1-\alpha)\%$ 신뢰구간이라고 함
- $100(1-\alpha)\%$ : 신뢰수준

### 모평균 $\mu$에 관한 신뢰구간(신뢰수준: $1 - \alpha$)

- 모수
    - 모평균 $\mu$
- 추정량
    - 표본평균 $\bar X$
- 추정량의 표본분포
    - $X_1, … , X_n$이 모분산  $\sigma^2$이 알려진 정규 모집단 $N[\mu,\sigma^2]$으로부터의 확률표본인 경우$\bar X \sim N\bigg[\mu, \dfrac {\sigma^2} {n}\bigg] \iff Z=\dfrac {\bar X - \mu} {\sigma / \sqrt n} \sim N[0,1]$

### 신뢰구간의 해석

- 신뢰수준은 동일한 구간 추정법을 반복적으로 사용할 때 얻어지는 신뢰구간들이 참값 $\theta$를 품을 확률을 의미한다.
    - $\mu$에 관한 90% 신뢰구간
    $P\bigg[\bar X - 1.645 \dfrac {\sigma} {\sqrt n} \le \mu \le \bar X + 1.645 \dfrac {\sigma} {\sqrt n}\bigg]$ = 0.90
    - $\mu$에 관한 95% 신뢰구간
    $P\bigg[\bar X - 1.96 \dfrac {\sigma} {\sqrt n} \le \mu \le \bar X + 1.96 \dfrac {\sigma} {\sqrt n}\bigg]$ = 0.95
    - $\mu$에 관한 99% 신뢰구간$P\bigg[\bar X - 2.58 \dfrac {\sigma} {\sqrt n} \le \mu \le \bar X + 2.58 \dfrac {\sigma} {\sqrt n}\bigg]$ = 0.99
        - 2.576으로 하기도 함.
