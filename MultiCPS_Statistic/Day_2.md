## 베이즈 정리

### 표본공간의 분할과 전확률 공식

- 표본공간의 분할
    - $B_1, …, B_k$ 가 다음 조건을 만족하면 표본 공간 S의 분할이라고 함.
        - 서로 다른 i, j 에 대해 $B_i \bigcap B_j = \Phi$ : 상호배반
        - $B_1 \bigcup B_2 \bigcup … \bigcup B_k = S$
- 베이즈 정리
    - 데이터라는 조건이 주어졌을 때의 조건부확률을 구하는 공식
- 전확률 공식
    - 사건 $B_1, …, B_k$는 상호 배반이며, $B_1 \bigcup B_2 \bigcup … \bigcup B_k = S$라고 함.
    - 이 때 S에서 정의되는 임의의 사건 A에 대하여 다음이 성립
        
        $P(A) = P(A \bigcap B_1) + … + P(A \bigcap B_k)
        = P(B_1)P(A|B_1) + … + P(B_k)P(A|B_k)$
        
- 베이즈 정리
    - 사건 $B_1, …, B_k$는 상호 배반이며, $B_1 \bigcup B_2 \bigcup … \bigcup B_k = S$라고 함.
    - 이 때 사건 A가 일어났다는 조건 하에서 사건 $B_i$가 일어날 확률은 다음과 같다.
    - $P(B_i|A) = \dfrac {P(A \bigcap B_i)} {P(A)} = \dfrac {P(B_i)P(A|B_i)} {P(B_1)P(A|B_1) + … + P(B_k)P(A|B_k)}$
    - $B_i$는 원인 $A$는 결과
- 베이즈 정리 활용
    - 원인별 결과의 조건부 확률을 알고 있을 때, 결과를 전제로 각 원인의 조건부 확률을 도출