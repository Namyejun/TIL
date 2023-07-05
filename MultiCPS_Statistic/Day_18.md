## **모분산 비교에 관한 가설검정(F-test of equality of variances)**

### 두 모집단의 모분산$(\sigma_1^2/ \sigma_2^2)$ 차이

- 독립인 두 표본
    
    ![Untitled](img/Untitled%2016.png)
    
    $\theta = \sigma_1^2/\sigma_2^2$에 관한 추론
    → 추정량($\hat \theta = S_1^2/S_2^2$)의 표본 분포를 이용
    
    $X = \bigg(\dfrac {\sigma_2^2} {\sigma_1^2}\bigg) \cdot \bigg(\dfrac {S_1^2} {S_2^2}\bigg) \sim F[n_1 - 1, n_2 - 1]$
    

### 모분산 비교에 관한 가설검정(F test of Equality of variances)

- 가설 유형
    - 관심 모수가 $\sigma_1^2/ \sigma_2^2$이고 검정하고자 하는 모수의 경계값은 1가 되므로,
        
        ![Untitled](img/Untitled%2017.png)
        
- 검정통계량
    - 두 모집단이 모두 정규분포인 경우
    다음의 검정통계량 X는 귀무가설 $H_0 : \sigma_1^2/ \sigma_2^2 = 1$이 사실일 때,
    $X = 1 \cdot \bigg(\dfrac {S_1^2} {S_2^2}\bigg) \sim F[n_1 - 1, n_2 - 1]$
- 유의확률(p-value)의 계산
    - 귀무가설 H_0가 사실일 때,
    검정통계량 X의 분포 $X = \bigg(\dfrac {S_1^2} {S_2^2}\bigg) \sim F[n_1 - 1, n_2 - 1]$에서,
    $x_0$(= 표본 자료로부터 계산된 검정통계량의 값) 보다 대립가설 방향으로 더 극단적
    - 귀무가설 H_0가 사실일 때,
    검정통계량 X의 분포 $X = \bigg(\dfrac {S_1^2} {S_2^2}\bigg) \sim F[n_1 - 1, n_2 - 1]$에서,
    $x_0$(= 표본 자료로부터 계산된 검정통계량의 값) 보다 대립가설 방향으로 더 극단적인 값이 나올 확률
- 유의수준(significance level) $100 \alpha \%$의 검정법
    - 자료로부터 계산된 유의확률(p-value)이 주어진 유의수준 $\alpha$보다 작은 경우에 귀무가설 $H_0$를 기각함.
    $p-value ≤ \alpha$면 $H_0$를 기각함

### Bartlett 검정과 Levene 검정

- k(≥2) 개의 모집단에 대한 등분산 검정
- 가설
    - $H_0 : \sigma_1^2 = … = \sigma_k^2$
    - $H_1 :$  적어도 하나 이상의 $\sigma_i^2$은 나머지와 다르다.
- Bartlett 검정
    - 모집단이 모두 정규분포를 따르는 경우 적용함
    - k = 2인 경우 등분산 F검정, k > 3인 경우는 Bartlett 검정
- Levene 검정
    - 모집단에 대한 정규성 가정이 필요하지 않음
