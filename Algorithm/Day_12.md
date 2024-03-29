## 소수 여부를 빠르게 처리하는 알고리즘들

### 소수(prime number)
- 소수란 1보다 큰 자연수 중에서 1과 자기 자신을 제외한 자연수로는 나누어떨어지지 않는 자연수이다.
- 코딩 테스트에서는 어떠한 자연수가 소수인지 아닌지 판별해야 하는 문제가 자주 출제된다.

### 소수의 판별: 기본적인 알고리즘
- 2부터 x - 1까지의 수를 전부 다 확인해보는 방법이다.
- 성능 분석
    - 모든 수를 다 확인해본다는 점에서 `O(X)`이다.

### 약수의 성질
- 모든 약수가 가운데 약수를 기준으로 곱셈 연산에 대해 대칭을 이룬다.
- 따라서 우리는 특정한 자연수의 약수를 찾을 때 가운데 약수까지만 확인하면 된다는 것이다.

### 소수의 판별: 개선된 알고리즘
- 2부터 x^(1/2)까지의 수를 전부 다 확인해보는 방법이다.
-  성능 분석
    - 2부터 X의 제곱근까지의 모든 자연수에 대해 연산을 수행한다.
    - 따라서 시간 복잡도는 `O(X^(1/2))`이다.

### 다수의 소수 판별
- 특정한 수의 범위 안에 존재하는 모든 수를 찾아야 할 때는 시간 복잡도가 굉장히 뛴다.
- 에라토스테네스의 체 알고리즘을 사용하면 시간 복잡도를 줄일 수 있다.

### 에라토스테네스의 체 알고리즘
- 다수의 자연수에 대하여 소수 여부를 판별할 때 사용하는 대표적인 알고리즘
- 에라토스테네스의 체는 N보다 작거나 같은 모든 소수를 찾을 때 활용한다.
- 동작 과정
    1. 2부터 N까지의 모든 자연수를 나열한다.
    2. 남은 수 중에서 아직 처리하지 않은 가장 작은 수 i를 찾는다.
    3. 남은 수 중에서 i의 배수를 모두 제거한다. (i는 제거하지않는다.)
    4. 더 이상 반복할 수 없을 때 까지 2번과 3번의 과정을 반복한다.

- 성능 분석
    - 에라토스테네스의 체 알고리즘의 시간 복잡도는 사실상 선형 시간에 가까울 정도로 매우 빠르다.
        - 시간 복잡도는 O(NloglogN)이다.
    - 에라토스테네스의 체 알고리즘은 다수의 소수를 찾아야하는 문제에서 효과적으로 사용될 수 있다.
        - 하지만 소수 여부를 저장해야하므로 메모리가 많이 필요하다.
        - 단일 값의 소수 여부를 판별할 때는 에라토스테네스의 체를 활용하기는 비용 측면에서 어렵다고 볼 수 있다.

---