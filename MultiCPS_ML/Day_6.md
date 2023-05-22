## 특성 공학: 개요, 특성 선택(Feature Selection) 방법론

### 특성공간 차원축소의 필요성

- 모델의 해석력 향상
- 모델 훈련시간의 단축
- 차원의 저주 방지
- 과적합에 의한 일반화 오차를 줄여 성능 향상

특성공학의 방법론은 크게 특성 선택(feature selection) 방법과 특성 추출(feature extraction) 방법으로 구분할 수 있다.

### 특성 선택(feature selection)

- 주어진 특성 변수들 가운데 가장 좋은 특성 변수의 조합만 선택함.
- 불필요한 특성 변수를 제거함.
- Filtering, Wrapper, Embedded 방식으로 분류할 수 있음.
    
    ![Untitled](img/Untitled%203.png)
    
    - Filtering : 특성변수 중 y를 설명하는데, 중요한 순서대로 순위를 매겨 top n개만 뽑는다.
    - Wrapper : 전체의 특성변수 중에서 일부 set을 후보로 가져와 모델에 적합을 해본다.
    여러 번 반복 후에 평가 기준을 통해 어떤 변수의 조합이 최고인지를 판단한다.
    - Embedded : 모델이 직접적으로 특성변수를 선택하는 모델을 사용한다.
    변수선택의 기능의 알고리즘이 탑재된 모델을 사용한다.

### Filter 방식 : 각 특성변수를 독립적인 평가함수로 평가

- 각 특성변수 $X_i$와 목표변수($Y$)와의 연관성을 측정한 뒤, 목표변수를 잘 설명할 수 있는 특성 변수만을 선택하는 방식.
- $X_i$와 $Y$의 1:1 관계로만 연관성을 판단.
- 연관성 파악을 위해 t-test, chi-square test, information gain 등의 지표가 활용됨.

### Wrapper 방식 : 학습 알고리즘을 이용

- 다양한 특성변수의 조합에 대해 목표변수를 예측하기 위한 알고리즘을 훈련하고, cross-validation 등의 방법으로 훈련된 모델의 예측력을 평가함. 그 결과를 비교하여 최적화된 특성변수의 조합을 찾는 방법.
- 특성변수의 조합이 바뀔 때마다 모델을 학습함.
- 특성변수에 중복된 정보가 많은 경우 이를 효과적으로 제거함.
- 대표적인 방법으로는 순차탐색법인 forward selection, backward selection, stepwise selection 등이 있음.
    - forward selection : 중요한 애들부터 모형에 포함
    - backward selection : 안 중요한 애들부터 모형에서 제거
    - stepwise selection : 포함과 제거를 번갈아 가면서 진행

### Filter와 Wrapper의 장단점 비교

![Untitled](img/Untitled%204.png)

### Embedded 방식 : 학습 알고리즘 자체에 feature selection을 포함하는 경우

- Wrapper 방식은 모든 특성변수 조합에 대해 학습을 마친 결과를 비교하는데 비해, Embedded 방식은 학습 과정에서 최적화된 변수를 선택한다는 점에서 차이가 있음.
- 대표적인 방법으로는 특성변수에 규제를 가하는 방식인 Ridge, Lasso, Elastic net 등이 있음.