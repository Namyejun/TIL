## 단순회귀분석(Simple Linear Regression)

### 회귀분석

- 독립변수와 종속변수 간의 함수적인 관련성을 규명하기 위하여 어떤 수학적 모형을 가정하고. 이 모형을 측정된 자료로부터 통계적으로 추정하는 분석방법.
- $y = f(x)$의 함수 관계가 있을 때
    - x를 설명변수(explanatory variable) 또는 독립변수(independent variable)
        - 단순 회귀 : 독립변수가 1개
        - 다중 회귀 : 독립변수가 2개 이상
    - y를 반응변수(response variable) 또는 종속변수(dependent variable)

### 모형 정의 및 가정

- 자료$(x_i, Y_i)$, i = 1, …, n에 다음의 관계식이 성립한다고 가정함.
$Y_i  = \alpha + \beta x_i + \epsilon_i$, i = 1,2,…,n
    - 오차항인 $\epsilon_1, \epsilon_2, …, \epsilon_n$는 서로 독립인 확률변수로, $\epsilon_i \sim N[0,\sigma^2]$ : 정규, 등분산, 독립 가정
    - $\alpha, \beta$는 회귀 계수라 부르며 $\alpha$는 절편 $\beta$는 기울기를 나타냄
    - $\alpha, \beta, \sigma^2$은 미지의 모수로 상수임
- 자료$(x_i, Y_i),$ i = 1, …, n에 다음의 관계식이 성립한다고 가정함.
$Y_i \sim N[\alpha + \beta x_i, \sigma^2]$ ⇒ $E[Y_i] = \alpha + \beta x_i$

### 모수 추정

- 모형이 포함한 미지의 모수 $\alpha, \beta$를 추정하기 위하여 각 독립변수 $x_i$에 대응하는 종속변수 $y_i$로 짝지어진 n개의 표본인 관측치 $(x_i, y_i)$가 주어짐

### 최소제곱법

- 단순회귀모형 $Y_i = \alpha + \beta x_i + \epsilon_i$에서 자료점과 회귀선 간의 수직거리 제곱합
$SSE(\alpha, \beta) = \displaystyle \sum_{i=1}^n (y_i - \alpha - \beta x_i)^2$이 최소가 되도록 $\alpha$와 $\beta$를 추정하는 방법
- $\alpha$에 대한 최소제곱 추정량 : $\hat \alpha = \bar y - \hat \beta \bar x$
    - 마찬가지로 $\alpha$에 대해 미분하고 계산
    
    ![[https://datalabbit.tistory.com/49](https://datalabbit.tistory.com/49)](%5BProDS%5D%20%E1%84%86%E1%85%A5%E1%84%89%E1%85%B5%E1%86%AB%E1%84%85%E1%85%A5%E1%84%82%E1%85%B5%E1%86%BC%20%E1%84%8B%E1%85%B5%E1%84%85%E1%85%A9%E1%86%AB%20%E1%84%86%E1%85%B5%E1%86%BE%20%E1%84%83%E1%85%A6%E1%84%8B%E1%85%B5%E1%84%90%E1%85%A5%20%E1%84%8E%E1%85%A5%E1%84%85%E1%85%B5%200fd2bfc90cad4606942dfafe60f5a110/Untitled%207.png)
    
    [https://datalabbit.tistory.com/49](https://datalabbit.tistory.com/49)
    
- $\beta$에 대한 최소제곱 추정량 : $\hat \beta = \dfrac {\sum_{i=1}^n (x_i - \bar x)(y_i - \bar y)} {\sum_{i=1}^n (x_i - \bar x)^2}$(단, $\bar x$는 $x_i$의 평균, $\bar y$는 $y_i$의 평균)
    - SSE를 \alpha, \beta에 대해서 미분하고 미분한 식이 각각 0일 때의 beta값을 계산한다.
    
    ![[https://datalabbit.tistory.com/49](https://datalabbit.tistory.com/49) 여기서 퍼왔습니다.](%5BProDS%5D%20%E1%84%86%E1%85%A5%E1%84%89%E1%85%B5%E1%86%AB%E1%84%85%E1%85%A5%E1%84%82%E1%85%B5%E1%86%BC%20%E1%84%8B%E1%85%B5%E1%84%85%E1%85%A9%E1%86%AB%20%E1%84%86%E1%85%B5%E1%86%BE%20%E1%84%83%E1%85%A6%E1%84%8B%E1%85%B5%E1%84%90%E1%85%A5%20%E1%84%8E%E1%85%A5%E1%84%85%E1%85%B5%200fd2bfc90cad4606942dfafe60f5a110/Untitled%208.png)
    
    [https://datalabbit.tistory.com/49](https://datalabbit.tistory.com/49) 여기서 퍼왔습니다.
    
    $\hat \beta = \dfrac {\sum_{i=1}^n (x_i - \bar x)(y_i - \bar y)} {\sum_{i=1}^n (x_i - \bar x)^2}= \dfrac {S_{xy}/N} {S_{xx}/N}$  : 분모는 x의 분산, 분자는 x,y의 공분산
    
- $y_i$의 추정치 : $\hat y_i = \hat \alpha + \hat \beta x_i$
- 잔차 : $e_i = y_i - \hat y_i = y_i - \hat \alpha - \hat \beta x_i$, i = 1,…, n

<aside>
💡 결정계수로 회귀모델의 성능을 측정할 수 있다.

</aside>

### 모형의 유의성 t검정

- 독립변수 x가 종속변수 Y를 설명하기에 유용한 변수인가에 대한 통계적 추론은 회귀계수 $\beta$에 대한 검정을 통해 파악할 수 있음
- $\beta$는 표본을 통해서 나온 값이기 때문에 표본에서는 X를 의미있는 변수라고 할 수는 있어도 모집단에서도 의미있다는 것을 의미하지는 않는다. 따라서 t 검정을 하는듯
- 가설
    - $H_0 : \beta = 0$ → X는 의미 없는 변수다.
    - $H_1 : \beta \ne 0$ → X는 의미 있는 변수이다.
- 검정통계량과 표본분포
    - 귀무가설 $H_0$가 사실일 때,
    $T = \dfrac {\hat \beta} {\hat {S.E.[\hat \beta]}} \sim t[n-2]$: $\hat \beta$를 추정량의 표준오차로 나눠주면 t분포를 따름
        
        $|T| = \bigg|\dfrac {\hat \beta} {\hat {S.E.[\hat \beta]}}\bigg| > t_{\alpha/2,n-2}$ : 대립가설의 방향이 양쪽 꼬리, 귀무가설은 가운데
        
        또는 $p-value(= P[T > |t_0|] \times 2) <\alpha$면 귀무가설을 기각, 검정통계량의 관찰값 $t_0$
        → 독립변수 x가 종속변수 Y를 설명하기에 유용한 변수라고 해석할 수 있음
        
        ![Untitled](img/Untitled%209.png)
        

### Y의 변동성 분해

- 제곱합 :
    - SST : $y_i$의 변동
    $\displaystyle \sum_{i=1}^n (y_i - \bar y)^2$
    - SSR : 모형으로 설명되는 변동
    $\displaystyle \sum_{i=1}^n (\hat y_i - \bar y)^2$
    - SSE : 모형으로 설명되지 않는 변동 
    $\displaystyle \sum_{i=1}^n (y_i - \hat y)^2$

![Untitled](img/Untitled%2010.png)

### 모형의 적합성

- 결정계수 $R^2$
$R^2 = \dfrac {SSR} {SST} = 1- \dfrac {SSE} {SST}$
    - SST = SSR + SSE 이므로 항상 0과 1 사이의 값을 가짐 $(0 \le R^2 \le 1)$
    - $y_i$의 변동 가운데 추정된 회귀모형으로 통해 설명되는 변동의 비중을 의미함
    - 0에 가까울수록 추정된 모형의 설명력이 떨어진다
    1에 가까울수록 추정된 모형 $y_i$의 변동을 완벽하게 설명하는 것으로 해석할 수 있음
    - $R^2$는 두 변수 간의 상관계수 r의 제곱과 같음 → $R^2$로 상관관계의 방향성은 따질 수 없음
