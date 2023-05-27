## **다중회귀분석(Multiple Linear Regression)**

### 다중선형회귀모형

- 독립변수가 두 개 이상인 선형회귀모형
- 여러 개의 독립변수를 이용하면 종속변수의 변화를 더 잘 설명할 수 있을 것임
- 자료$((x_{1i}, x_{2i}, …,x_{ki}), Y_i)$, i= 1, …, n에 다음의 관계식이 성립한다고 가정함.

$Y_i = \alpha + \beta_1x_{1i} + … +  \beta_kx_{ki} + \epsilon_i$      (i = 1,2,…,n)
- 오차항인 $\epsilon_1, …, \epsilon_n$ 서로 독립인 확률변수로 $\epsilon_i \sim N[0,\sigma^2]$ : 정규, 등분산, 독립
- 회귀계수 $\alpha, \beta_1, … , \beta_k$와 $\sigma^2$은 미지수인 모수로 상수임
    - $\beta_j$의 해석 : $x_j$를 제외한 나머지 모든 예측변수들을 상수로 고정시킨 상태에서 $x_j$의 한 단위 증가에 따른 E[Y]의 증분을 의미 (j = 1,…,k)

### 회귀계수 $\alpha, \beta_1, … , \beta_k$의 추정

- 수직거리 제곱합
$SS(\alpha, \beta_1, … , \beta_k) = \displaystyle \sum_{i=1}^n (y_i -\alpha -\beta_1x_{1i} - … - \beta_kx_{ki})^2$이 최소가 되도록 $\alpha, \beta_1, … , \beta_k$를 추정
- 최소제곱 추정량 $\hat \alpha,\hat \beta_1, … ,\hat \beta_k$

### 범주형 독립변수가 포함된 회귀모형

- 범주형 독립변수를 회귀모형에 포함하기 위해서는 더미변수(dummy variable) 기법을 사용
- 더미변수는 0또는 1의 값을 갖는 변수로 아래와 같이 정의됨
    - 더미 변수의 개수 = 범주의 개수 - 1