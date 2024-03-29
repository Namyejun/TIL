## 그래프에 의한 기술 통계

### 그래프를 이용한 자료의 정리

자료의 유형에 맞는 그래프를 이용하여 한 눈에 알아볼 수 있게 자료를 시각화할 수 있음

### 질적 자료인 경우

- 1개 변수 : 바차트, 파이차트
- 2개 변수 : 히트맵, 스택드컬럼차트

### 양적 자료인 경우

- 1개 변수 : 히스토그램, 박스플롯 (상자그림), 라인차트, QQ플롯
- 2개 변수 : 산점도

### 바차트와 파이차트

![Untitled](img/Untitled%203.png)

### 스택트컬럼차트

![Untitled](img/Untitled%204.png)

### 히트맵

![Untitled](img/Untitled%205.png)

### 히스토그램

![Untitled](img/Untitled%206.png)

### 박스플롯

![Untitled](img/Untitled%207.png)

### 정규 QQ 플롯

![Untitled](img/Untitled%208.png)

![Untitled](img/Untitled%209.png)

양적 변수 하나가 주어졌을 때 이 변수의 분포가 정규분포를 따르는가를 확인하는 그림

- 가지는 자료값들을 쭉 오름차순을 해준다.
- 값들이 관찰되는 경험누적 확률이라는 것을 계산한다.
    - 그 값보다 작거나 같은애가 관찰될 확률의 추정치
- 경험누적 확률을 기준으로 값들을 표본의 분위수(quantiles)라고 부름
- 이런 누적 확률을 가지는 이론 quantiles을 구한다.
    - ex) 1/30의 면적을 가지는 quantiles
- 그리고 표본 quantile과 이론 quantiles이 선형관계를 따르는지 확인한다.
    - 선형관계면 정규를 따르고 아니면 안따른다

- 이론 분위수보다 표본 분위수의 값이 큰 형태면 오른꼬리가 긴 양의 왜도 분포를 가진다.
- 이론 분위수보다 표본 분위수의 값이 작은 형태면 왼꼬리가 긴 음의 왜도 분포를 가진다.

### 산점도

![Untitled](img/Untitled%2010.png)
