## **다중회귀분석(잔차분석, 다중공선성)**

### 다중회귀모형의 가정 위반 검토 및 해결

- 잔차분석
    - 회귀모형에서의 가정이 적절한 것인가에 대한 평가
        1. 오차의 정규성
        2. 오차의 등분산성
        3. 오차의 독립성
    - 오차는 확률변수로 관찰되지 않는 값이므로 각 오차에 대응되는 잔차를 관찰한 뒤 잔차들의 분포를 통해 오차에 대한 가정의 적정성을 확인할 수 있음
- 잔차분석 방법
    - 각 가정 별로, 검정을 통한 방법과 그래프를 통한 시각적인 확인 방법이 가능
    - 시각적 방법을 이용할 경우
        - 오차의 정규성 위반 : 히스토그램, QQ플롯
            
            ![Untitled](img/Untitled%2011.png)
            
        - 오차의 등분산성 : 잔차산점도
        - 오차의 독립성 : 잔차산점도
            
            ![Untitled](img/Untitled%2012.png)
            
            - a : 등분산, 독립 가정 만족
            - b : 등분산성 가정 깨짐
            - c : 등분산성 가정 깨짐
            - d : 독립 가정 깨짐 → x축이 i인 경우에 그렇게 판단, x축이 x_i면 x와 y가 선형관계가 아니었을 확률 존재
- 가정 위반 시 해결방안
    - 오차의 정규성 위반 : 변수변환
        - 로그변환이나 제곱근변환, 지수 변환 etc
    - 오차의 등분산성 : 가중최소제곱회귀
        - 수직거리의 제곱으로 하는게 아닌 각 자료값이 가지는 분산의 역수로 가중치를 두고 최소제곱법을 적용시킴
        → 변동성이 큰(분산이 큰) 자료는 보다 적게 계수추정을 하는데 반영
        - $\sum \Big(\dfrac {1} {\sigma^2}\Big) (y_i - \alpha - \beta x_i)^2$
    - 오차의 독립성 : 시계열 분석
        - 상관관계의 구조에 대해서 파악을 한다, 정상성 조건을 만족하는지 만족한다면 어떤 모델을 적용하면 좋을지 적절한 모델을 선택해서 분석해본다
    

### 다중공선성

- 다중공선성이란
    - 독립변수들 간에 강한 선형관계가 존재하는 경우
    - 다중회귀모형 분석 시 자주 발생하는 문제 중 하나임
    - 다중회귀모형에서 회귀계수 추정에 부정적인 영향을 미침
        - 회귀계수($\beta_i$)의 변동성이 커짐 → $x_i$의 값에 따라 바뀌는 정도가 커짐
    1. **개별적인 회귀계수 추정의 신뢰성이 떨어져** 추정치를 믿을 수 없게 만듦
    2. 전반적인 **모형의 적합성이나 정확도는 크게 변하지 않음 → $\beta_i$**만 이상하게 추정됨
- 진단방법
    - 추정량의 분산
        
        <aside>
        💡 $V[\hat \beta_j] = \dfrac {\sigma^2} {x_j의 변동성} \times \dfrac {1} {1- R_j^2}$
        다중공선성이 존재하면 $\dfrac {1} {1- R_j^2}$이 커져서 결국 $V[\hat \beta_j]$가 커짐.
        따라서 추정치를 믿지 못함
        
        </aside>
        
    - VIF 계수 도출
    $VIF = \dfrac {1} {1- R_j^2}$
        1. $R_j^2$ : $x_j$를  종속변수로 두고 **나머지 독립변수로 설명하는 다중선형회귀모델에서의 결정계수**
            - j번째를 제외한 나머지를 독립변수로 놓고 다시 다중회귀를 돌린 후 다시 계산한 결정계수
    - VIF 계수가 5 또는 10 이상인 경우 다중 공선성이 심각한 것으로 봄
        - 5라는 뜻은 $R_j^2$ = 0.8이라는 뜻 → 해당 독립 변수를 제외한 나머지로 80%가 설명이 됨
        - 10라는 뜻은 $R_j^2$ = 0.9이라는 뜻 → 해당 독립 변수를 제외한 나머지로 90%가 설명이 됨
- 해결책
    - 변수선택으로 중복된 변수를 제거
    - 주성분 분석 등을 이용하여 중복된 변수를 변환하여 새로운 변수 생성
        - PCA → 중복된 변수가 축이 됨 → 새로운 변수 축들을 만들고 그 축을 사용한다.
            
            ![Untitled](img/Untitled%2013.png)
            
    - 릿지, 라쏘 등으로 중복된 변수의 영향력을 일부만 사용
        
        ![Untitled](img/Untitled%2014.png)
        
        - 라쏘는 일부 변수를 강제로 0으로 만들어버림, 자동으로 변수선택과 다중공선성 문제를 해결할 수 있다.