## **규제가 있는 선형회귀모델 (Ridge, Lasso, Elastic Net)**

### 선형회귀모델의 규제

- 모형의 과대적합을 막기 위한 규제 방법(regularization)으로 선형회귀모형에서는 보통 모델의 가중치를 제한하는 방법을 사용함.
    - 선형회귀모델의 비용함수
    $J(\beta) = \dfrac 1 n \displaystyle \sum_{i=1}^n (y_i - \beta_0 - \beta_1x_{1i} - \beta_2x_{2i} - ... - \beta_kx_{ki})^2$
    - 규제가 있는 경우 비용함수
    $J(\beta) = \dfrac 1 n \displaystyle \sum_{i=1}^n (y_i - \beta_0 - \beta_1x_{1i} - \beta_2x_{2i} - ... - \beta_kx_{ki})^2 + \lambda \cdot penalty(\beta_1, ..., \beta_k)$
    수직거리 제곱합의 평균을 최소로 만들되 패널티의 추가로 인해 $\hat \beta$의 크기도 커지지 않도록 하는 것
        
        수직거리 제곱합을 줄이는 것에 비중을 둘 것인지, 아니면 $\beta$ 들의 패널티를 줄이는 것에 더 비중을 두는지 결정하는게 $\lambda$이다.
        
        - $\lambda$가 작으면 수직거리 제곱합을 줄이는데에 비중을 둠
        - $\lambda$가 크면 $\beta$ 들의 패널티를 줄이는 것에 비중을 둠
        - 0이면 수직거리 제곱합의 비용과 동일

- 가중치를 제한하는 방법에 따른 규제 선형회귀모델의 종류
    - 릿지회귀(Ridge Regression)
    - 라소회귀(Lasso Regression)
    - 엘라스틱넷(Elastic Net)
    
    <aside>
    💡 $L_p \ norm = \bigg( \sum_{j = 1}^k |\beta_j|^p\bigg)^{1/p}$
    릿지 : p = 2
    라쏘 : p = 1
    엘라스틱넷 : 릿지와 라쏘의 장점을 둘 다 취하기 위해 만들어진 것
    
    </aside>
    

### 릿지회귀(Ridge Regression)와 L2 규제

- 릿지회귀의 비용함수
    - 비용함수 $J(\beta)$에 규제항 $\lambda \cdot \sum_{j=1}^k \beta_j^2$이 추가된 선형모형
        
        $J(\beta) = \dfrac 1 n \displaystyle \sum_{i=1}^n (y_i - \beta_0 - \beta_1x_{1i} - \beta_2x_{2i} - ... - \beta_kx_{ki})^2 + \lambda \cdot \sum_{j=1}^k \beta_j^2$
        
    - $\lambda$(규제 정도를 결정하는 하이퍼 파라미터)
        - $\lambda$가 크면 규제 많음. 회귀 계수 추정치가 작아짐.
        - $\lambda$가 0이면 일반 선형회귀 모델과 동일한 결과
        - 적절한 $\lambda$는 교차검증(cross-validation)등으로 최적화

- 릿지회귀의 훈련
    - 비용함수 $J(\beta)$를 최소로하는 회귀계수 $\hat \beta^R = (\hat \beta_0^R, \hat \beta_1^R, …, \hat \beta_k^R)$를 찾는 문제.
    $\hat \beta^R = arg \ \underset {\beta} {min} \ J(\beta)$
- Alternative Fomulation
    - 어떤 임의의 \lambda에 대해 이에 대응하는 하나의 t가 존재하여 아래 식으로 동일한 해 $\hat \beta^R$를 얻게 됨.
        
        $\hat \beta^R = arg \ \underset {\beta} {min} \ \bigg\{ \dfrac 1 n \displaystyle \sum_{i=1}^n (y_i - \beta_0 - \beta_1x_{1i} - \beta_2x_{2i} - ... - \beta_kx_{ki})^2 + \lambda \cdot \sum_{j=1}^k \beta_j^2\bigg\} \ subject \ to \ \sum_{j=1}^k \beta_j^2 \le t$
        
        - $\beta$에 대해 범위를 한정시킴. 원이나 구 그런 범위로 제한됨.
            
            ![Untitled](img/Untitled%2015.png)
            
            - 사진 속 $\hat \beta$는 일반 선형회귀모형의 비용 최소점
            - 하지만 $\beta$에 노란색 범위가 걸려있음

### 라쏘회귀(Lasso Regression)와 L1 규제

- 라쏘회귀의 비용함수
    - 비용함수 $J(\beta)$에 규제항 $\lambda \cdot \sum_{j=1}^k |\beta_j|$이 추가된 선형모형
        
        $J(\beta) = \dfrac 1 n \displaystyle \sum_{i=1}^n (y_i - \beta_0 - \beta_1x_{1i} - \beta_2x_{2i} - ... - \beta_kx_{ki})^2 + \lambda \cdot \sum_{j=1}^k |\beta_j|$
        
    - $\lambda$(규제 정도를 결정하는 하이퍼 파라미터), 교차검증 등으로 최적화

- 릿지회귀의 훈련
    - 비용함수 $J(\beta)$를 최소로하는 회귀계수 $\hat \beta^L = (\hat \beta_0^L, \hat \beta_1^L, …, \hat \beta_k^L)$를 찾는 문제.
    $\hat \beta^L = arg \ \underset {\beta} {min} \ J(\beta)$
    - Alternative Fomulation
        - 어떤 임의의 \lambda에 대해 이에 대응하는 하나의 t가 존재하여 아래 식으로 동일한 해 $\hat \beta^L$를 얻게 됨.
            
            $\hat \beta^L = arg \ \underset {\beta} {min} \ \bigg\{ \dfrac 1 n \displaystyle \sum_{i=1}^n (y_i - \beta_0 - \beta_1x_{1i} - \beta_2x_{2i} - ... - \beta_kx_{ki})^2 + \lambda \cdot \sum_{j=1}^k |\beta_j|\bigg\} \ subject \ to \ \sum_{j=1}^k |\beta_j| \le t$
            
            - $\beta$에 대해 범위를 한정시킴. 범위 제한됨.
                
                ![Untitled](img/Untitled%2016.png)
                
                - 사진 속 $\hat \beta$는 일반 선형회귀모형의 비용 최소점
                - 하지만 $\beta$에 노란색 범위가 걸려있음
                - 라쏘 회귀는 저 범위를 지켜야하므로 자주 회귀계수의 값이 0이 되는 경우를 볼 수 있다.

### 릿지회귀와 라쏘회귀의 특징

- 두 방식 모두 추정치는 일반선형회귀모형과는 달리 편의가 발생하지만 분산은 더 작아지게 됨
    - 추정치가 0 부근에서만 추정되도록 범위를 한정지어 놓았기 때문에 아무리 변동해도 선형회귀 모델의 크기자체가 별로 변하지않음
    
    → $\lambda$에 따라 일반화오차가 더 작아질 수 있음
    
- 라쏘 회귀의 경우 제약 범위가 각진 형태
    
    → 파라미터의 일부가 0이 되는 경향이 있음. (sparse model)
    
- 릿지 회귀의 경우 제약 범위가 원의 형태
    
    → 파라미터가 0이 되지 않고 전반적으로 줄어드는 경향이 있음
    

### 엘라스틱 넷(Elastic Net)

- L1과 L2 규제를 혼합한 방식
- 엘라스틱 넷의 비용함수
$J(\beta) = \dfrac 1 n \displaystyle \sum_{i=1}^n (y_i - \beta_0 - \beta_1x_{1i} - \beta_2x_{2i} - ... - \beta_kx_{ki})^2 + \lambda_1 \cdot \sum_{j=1}^k \beta_j^2 + \lambda_2 \cdot \sum_{j=1}^k |\beta_j|$
- 릿지회귀와 라쏘회귀의 장점을 모두 가짐
    - 라쏘를 쓰면 변수선택을 하는데 중복되는 정보가 존재하면 걔네들을 대부분 탈락시키고 한 두 개만 남기는게 단점인데, 정말 중요한 독립변수에 대해서는 일정한 계수 수준으로 남길 수 있도록 해 두 모델의 장점을 취함.