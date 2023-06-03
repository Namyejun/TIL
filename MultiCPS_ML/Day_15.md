## **분류: 로지스틱 회귀(Logistic Regression)**

### 로지스틱 회귀모형

- 로지스틱 회귀분석은 선형 회귀분석과 달리 반응변수가 범주형 데이터인 경우에 사용되는 기법.
- 새로운 설명변수의 값이 주어질 때 반응변수의 각 범주에 속할 확률이 얼마인지를 추정하고, 추정 확률을 분류기준값에 따라 분류하는  목적으로 사용됨.

### 이항 로지스틱 회귀모형

- 이항 로지스틱 회귀모형 : 이진(0/1)형 값을 가지는 반응변수를 여러 설명변수를 이용하여 회귀식의 형태로 예측하는 모형
    - 다항 로지스틱은 Y의 범주가 둘 이상인 경우
- 반응변수 Y는 1또는 0의 값을 가지는 이진변수,
설명변수는 $x_1, …, x_k$로 k개인 경우에,
$p = P(Y = 1|x_1, …, x_k)$라고 하면,
    
    $log\Big(\dfrac {p} {1-p}\Big) = \beta_0 + \beta_1x_1 + … + \beta_kx_k$  → $log\Big(\dfrac {p} {1-p}\Big)$ : 로그 오즈비
    
    - 오즈
        - 가능성의 척도로 내가 관심있는 사건의 확률이 나머지 사건의 확률에 비해 몇 배인지
        - 확률이 커지면 오즈도 커진다.
        - 확률은 0~1의 스케일을 가지지만 0~$\infin$의 스케일을 가짐
        - 로그 오즈는 $(-\infin, \infin)$의 범위를 가짐
- 위 모형은 다음과 같이 p에 관한 식으로 표현할 수 있음.
$p = \dfrac {exp(\beta_0 + \beta_1x_1 + … + \beta_kx_k)} {1 + exp(\beta_0 + \beta_1x_1 + … + \beta_kx_k)} = \dfrac {1} {1 + exp(-(\beta_0 + \beta_1x_1 + … + \beta_kx_k))}$
→ 시그모이드 함수
- 범주형 반응변수의 범주가 두 개일 때, 관심 범주를 1, 다른 범주를 0으로 정의하면, 반응변수 Y는 관심범주에 속할 확률이 p인 베르누이 확률분포를 따르는 것으로 볼 수 있음.
$Pr(Y = 1) = p, Pr(Y = 0) = 1 - p$
- 여기서 확률 p를 독립변수의 함수로 설명하고자 함.
- **확률 p은 0과 1 사이의 값이므로 $(-\infin, \infin)$의 범위를 가지는 독립변수의 선형함수로 나타낼 수 없음**
    - 모형 $\beta_0 + \beta_1x_1 + … + \beta_kx_k$으로 p를 예측하고 싶다. 그런데 p는 0~1의 값이고 모형은 $(-\infin, \infin)$의 범위를 가진다. 따라서 p를 오즈로 표현해 $(0, \infin)$까지 표현할 수 있게하고, 추가로 log를 취해 $(-\infin, \infin)$의 범위까지 가지게 만들어 준다.

### 로지스틱 모형식의 이해

- 확률 p 대신 로그오즈$(log(\dfrac {p} {1-p}))$를
독립변수의 선형함수로 나타낸 것임.
    
    $logit(p) = log(\dfrac {p} {1-p}) = \beta_0 + \beta_1x_1 + … + \beta_kx_k$
    
- 설명변수가 1개인 경우 (k = 1), $p = \dfrac {exp(\beta_0 + \beta_1x_1)} {1 + exp(\beta_0 + \beta_1x_1)}$  ($\beta_1 > 0$)는 아래와 같은 비스듬한 S 곡선형태를 가짐
    
    ![Untitled](img/Untitled%2017.png)
    
    - p는 언제나 0~1 사이의 값이 됨
    - x가 $-\infin$일 때, p는 0
    - x가 $\infin$일 때, p는 1

### 추정 및 예측

- $(x_i, y_i)$의 표본 자료가 n개 주어지면 최대우도추정법, 경사하강법 등을 이용하여 가장 적합한 곡선함수 $(\hat \beta_0, \hat \beta_1)$를 추정.
- 새로운 자료 $x_{new}$가 주어졌을 때,
$P(Y_{new} = 1)$는 $\hat p_{new} = \dfrac {exp(\hat \beta_0 + \hat \beta_1x_1)} {1 + exp(\hat \beta_0 + \hat \beta_1x_1)}$로 추정됨.
- $\hat p_{new} \ge threshold$면, $\hat Y_{new} = 1$
- $\hat p_{new} \lt threshold$면, $\hat Y_{new} = 0$

### 로지스틱 회귀모형의 분리경계면

- 로지스틱 회귀모형은 선형의 결정경계를 가짐
- 독립변수가 2개인 로지스틱 회귀모형과 threshold = 0.5일 때의 초평면(Hyperplane)
$p = \dfrac {e^{\beta_0 + \beta_1x_1 + \beta_2x_2}} {1 + e^{\beta_0 + \beta_1x_1 + \beta_2x_2}}$
    
    ![Untitled](img/Untitled%2018.png)
    

### 로지스틱 회귀와 오즈비(odds ratio)

$p = \dfrac {e^{\beta_0 + \beta_1x_1 + \beta_2x_2}} {1 + e^{\beta_0 + \beta_1x_1 + \beta_2x_2}} \Leftrightarrow \dfrac {p} {1-p}(odds) = e^{\beta_0 + \beta_1x_1 + \beta_2x_2}$

- 1나머지 변수는 모두 고정시킨 상태에서 한 변수 $X_1$만 1만큼 증가시켰을 때, 변화하는 odds의 비율(오즈비)는 $e^\beta_1$임을 알 수 있음
$\dfrac {odds(x_1 + 1, x_2)} {x_1, x_2} = \dfrac {e^{\beta_0 + \beta_1(x_1 + 1) + \beta_2x_2}} {e^{\beta_0 + \beta_1x_1 + \beta_2x_2}} = e^{\beta_1}$
- $x_1$만 1만큼 증가하면, 성공(관심범주, Y = 1)에 대한 오즈가 $exp(\beta_1)$배 변화함
    - $\beta_1 > 0$ : 관심범주에 속할 확률이 증가함
    $X_1$ 변수와 관심범주 간에는 양의 상관관계
    - $\beta_1 < 0$ : 관심범주에 속할 확률이 감소함
    $X_1$ 변수와 관심범주 간에는 음의 상관관계
