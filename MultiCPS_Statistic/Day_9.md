## **수치적 기술통계 ② 연관성**

### 표본 공분산(Sample Covariance)

- n쌍의 표본 자료 $(x_1, y_1), …, (x_n, y_n)$이 주어졌을 때
$S_{xy} = \dfrac {\displaystyle\sum_{i=1}^n(x_i - \bar x)(y_i - \bar y)} {n-1}$
- 선형관계의 방향
    - $S_{xy} > 0$ : 양의 선형 관계, 비례관계
    - $S_{xy} < 0$ : 음의 선형 관계, 반비례관계
- 선형관계의 강도
$-S_xS_y \le S_{xy} \le S_xS_y$  → by Cauchy-Schwarz 부등식
- 표본 공분산은 x와 y의 측정 단위에 의존하는 지표임.
$x’ = ax + b$이고 $y’ = cy + d$인 경우에 $S_{x’y’} = ac \cdot S_{xy}$
→ x’이 g이고 x가 kg이라면? a = 1000 $(\therefore S_{x'y'} = 1000^2 S_{xy})$

### 표본 상관계수(Sample Correlation, 피어슨의 상관계수)

- $r_{xy} = \dfrac {S_{xy}} {S_xS_y}$
- $-1 \le r_{xy} \le 1$, by Cauchy-Schwarz 부등식
- 선형관계의 방향
    - $r_{xy} > 0$ : 양의 선형 관계
    - $r_{xy} < 0$ : 음의 선형 관계
- 선형관계의 강도
    - $|r_{xy}| \approx 0$ : 강도가 약함
    - $|r_{xy}| \approx 1$ : 강도가 강함
- 표본 상관계수는 x와 y의 측정 단위에 의존하지 않음
$x’ = ax + b$이고 $y’ = cy + d$이고 $ac > 0$인 경우에 $r_{x’y’} = r_{xy}$

### 순위를 이용한 상관계수

- 서열 척도이거나 정규분포를 심하게 벗어나는 두 숫자형 변수의 연관성 파악
- 스피어만 상관계수(Spearman’s correlation coefficient)
    - 원 자료값의 순위를 구한 뒤 순위에 대하여 피어슨의 상관계수를 구한 것
    - -1에서 1사이의 값을 가지며, 절대값이 클수록 강한 상관관계를 나타냄
- 켄달 상관계수(Kendall rank correlation coefficient)
    - 두 변수 순위의 일치 정도를 측정
    - 한 변수의 순위가 증가할 때 다른 변수의 순위도 함께 증가하는 경우가 그렇지 않은 경우에 비해 얼마나 큰지를 측정하는 방식