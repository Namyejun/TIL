## **모평균 비교에 관한 가설검정(paired t test)**

### 대응표본

- 대응 표본과 독립인 두 표본의 차이 비교
    
    
    |  | 대응표본 | 독립인 두 표본 |
    | --- | --- | --- |
    | 표본 추출 | 두 모집단으로부터 추출된 서로 짝을 이루는 표본 | 두 모집단으로부터 각각 독립적으로 추출된 표본 |
    | 예시 | 체중, 나이 등이 유사한 2명씩 짝을 지어 한 명은 A약 다른 한 명은 B약을 투여한 뒤 혈압을 측정 | A약을 투여한 그룹과 B약을 투여한 그룹에 대하여 혈압을 측정 |

### 대응 표본에 대한 모평균 차이($\mu_d$)

![Untitled](img/Untitled%2011.png)

### 대응 표본에서 모평균 비교에 관한 쌍체 t-검정(paired t-test)

- 가설유형
    - 관심 모수가 \mu_d이고 검정하고자 하는 모수의 경계값은 0가 되므로,
        
        
        | 단측(한쪽 꼬리) 검정 | 단측(한쪽 꼬리) 검정 | 양측(양쪽 꼬리) 검정 |
        | --- | --- | --- |
        | 왼 꼬리 검정 | 오른 꼬리 검정 | 양측(양쪽 꼬리) 검정 |
        | $H_0 : \mu_d = 0$
        $H_1 : \mu_d < 0$ | $H_0 : \mu_d = 0$
        $H_1 : \mu_d > 0$ | $H_0 : \mu_d = 0$
        $H_1 : \mu_d \ne 0$ |
- 검정통계량과 표본분포
    - 대응표본간 차이 $d_1, …, d_n$이 분산이 알려지지 않은 정규분포를 따른다고 가정.
    - 검정통계량 T는 귀무가설 $H_0 : \mu_d = 0$이 사실일 때,
    $T = \dfrac {d} {S_d/\sqrt {n}} \sim t[n-1]$를 만족함.
    단, $\bar d = \dfrac {\sum_{i=1}^n d_i} {n}$이고, $S_d = \sqrt {\dfrac {\sum_{i=1}^n (d_i - \bar d_i)^2} {n-1}}$임.
- 유의확률(p-value)의 계산
    - 귀무가설 H_0가 사실일 때,
    검정통계량 T의 분포 $T = \dfrac {\bar d} {S_d/\sqrt {n}} \sim t[n-1]$에서,
    $t_0$(=표본 자료로부터 게산된 검정통계량의 값)보다 대립가설 방향으로 더 극단적인 값이 나올 확률
- 유의수준(significance level) $100 \alpha \%$의 검정법
    - 자료로부터 계산된 유의확률(p-value)이 주어진 유의수준 $\alpha$보다 작은 경우에 귀무가설 $H_0$를 기각함.
    $p-value ≤ \alpha$면, $H_0$를 기각
    