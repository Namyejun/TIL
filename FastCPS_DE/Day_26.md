### 3. 데이터(베이스) 비정규화

- **비정규화란**

    **정규화로 잘 구조화되어 나누어져 있는 데이터를 다시 합치는 것**을 말한다. 데이터가 나누어져 있으면 **복잡도가 높아진다**. 또한 활용할 때마다 Join을 해야하는 불편함이나 성능의 손해가 발생한다. 전체적으로 데이터 활용에 있어서 생산성의 저하가 나타나기 때문에, 활용 목적에 따라 데이터를 비정규화 하는 경우가 필요하다.
    **빅데이터 데이터베이스에서는 비정규화를 이용해서 데이터를 저장하고 조회**하는 방식을 사용한다.

- **비정규화 - 데이터 활용 방식에 의한 방법**

    시스템 전체에서 데이터를 어떻게 활용할지에 대한 예상과 계획을 가지고 모델링 하는 것이다. **저장하는 쪽 보다는 가공하고 활용하는 쪽의 요구사항을 기반으로 모델링**을 한다. **키를 기준으로 테이블을 합치는 의사결정**을 한다. **빅데이터용 데이터베이스에 적합**하다.

    - **예제 - 요구사항**

        이 앱은 슈퍼앱이다. 유저의 일상 생활에 파고들어서 없는 서비스가 없다. 메신저, 쇼핑, 검색, 콘텐츠 등의 서비스가 연계된다. 최근에 ML을 이용해서 경계를 가리지 않고 자동화된 추천기반의 서비스를 제공한다. 여기서 학습된 내용은 광고 타게팅 효율에 큰 영향을 미쳐서 기하급수적인 매출 성장을 이룰 수 있다. 그런데 데이터가 정규화로 너무 잘게 나눠져 있다. ML서비스는 다음과 같은 영향이 있다. 데이터를 활용하기 위해서는 매번 권한을 따로 받아야 하는 것이 불편하다. 데이터를 여러군데서 읽어야 하므로 **I/O 비용때문에 모델 학습비용이 커진다**. **모델의 종류가 많아지고 관리 파일이 커진다**.

    - **해결**

        유저 정보를 중심으로 유저의 활동 정보를 비정규화해서 하나의 join된 테이블로 만들었다. 데이터 조회 속도가 빨라지고, 모델 학습 속도 또한 빨라져서 online ML을 할 수 있게 되었다. 관리포인트가 적어지니 **기술부채와 불필요한 리소스 사용량이 모두 감소**했다.

    -  **또 다른 요구사항**

        이 앱은 슈퍼앱이다. 하나의 유저에 대해서 여러 종류의 데이터가 있고, 각 부서에서 관심있는 데이터는 제각기 다르고, 강한 개인정보보호 규약때문에 **데이터 접근 권한에 대해서 엄격히 관리**된다고 하자. 이 경우 **정규화를 하는 것이 데이터 관리 측면**에서 좋다. 회사 전체의 생산성을 높이는 것이 top priority이다. 만약 비정규화 되어있다고 해보자, 모든 부서에서 **불필요한 유저의 속성을 데이터 조회할 때마다 읽을 수 밖에** 없다. **불필요하게 낭비되는 디스크 용량, I/O 비용, 데이터 유출에 의한 보안사고 우려까지 비용과 리스크가 크다**.

### 4. 파티셔닝
  
- **파티셔닝이란**
    - **파티셔닝의 정의**

        데이터의 사이즈가 큰 테이블을 두 개 이상의 작은 테이블로 나누는 것을 파티셔닝이라고 한다. 쿼리가 스캔할 데이터의 범위를 좁혀서 응답 시간을 빠르게 하기 위한 목적으로 사용한다.
        이 설명은 RDBMS 기준의 설명이다. NoSQL의 파티셔닝은 의미는 같지만 실제 구현방식은 다르다.
        - 예: Hadoop 기반의 빅데이터 도구들(Hive 등)은 수평적 파티셔닝을 위해서 별도 테이블 지정이 필요없다. 파티셔닝 설정으로 저장하는 파일 경로만 달라진다. 즉 테이블이 나누어지 지지않고, 경로가 나누어진다.
    - **파티셔닝의 종류**
        1. **Horizontal Partitioning (수평적 파티셔닝)**

            데이터를 **row 단위로 나눈다**. 컬럼의 종류와 수는 기존과 동일.

        2. **Vertical Partitioning (수직적 파티셔닝)**

            **컬럼의 수를 줄여서 두 개 이상의 테이블**로 나누는 방법.

- **Horizontal Partitioning (수평적 파티셔닝)**

    데이터를 row 로 나누는 것이다. 컬럼의 종류와 수는 기존과 동일하다.
    - **데이터를 나누는 방법**

        데이터를 나누는 방법은 대표적으로 두가지 use case 가 있다.
        1. Timeline 성격의 데이터는 데이터의 **기간별로 나눈다**.
            1. 예) 년/월/주/일 등의 단위로 나눈다.
        2. 특정 **컬럼의 분류 별**로 나눈다.
            1. 예) 국가별, 상품 category별
            2. 단, 데이터의 편차가 큰 컬럼에 대해서 파티셔닝 기준을 삼는다면, 데이터 편중(Skew)가 생길 수 있다. <br>
                1. 특정 테이블의 공간이 부족할수도, 특정 테이블의 공간이 너무 많이 남아 비효율적일 수도 있다.

    - **수평적 파티셔닝 구현 방법 1 - 기간**

        정해진 기간별로 테이블 이름의 규칙을 만든다.
        3. 장점
            1. **로직이 복잡하지 않다**. 시간 조건에 따라 테이블 이름을 결정하는 로직만 추가한다.
        4. 단점
            1. 기간별로 데이터가 **다르게 들어오면(skew), 특정 기간 테이블에만 부하**가 생길 수 있다.
            2. **현재를 가리키는 테이블이 항상 바뀐다**.
            3. 해당 기간의 **첫번째 시간인 경우 데이터가 없을 수 있다**.

    - **수평적 파티셔닝 구현 방법 2 - alias + 기간**

        Current Table(현재 시간 ~ window)을 두고, 일정 기간이 되면 파티셔닝 테이블로 복사하고, Current Table에서 데이터를 삭제하는 방법
        5. 장점
            1. **최근 데이터에 대해서는 항상 같은 테이블**에 접근하면 된다.
        6. 단점
            1. Current Table 이전의 데이터는 어떤 테이블인지 **이름을 찾거나 결정하는 로직이 추가**되어야 한다.
            2. 배치로 데이터 복사와, 삭제가 이뤄지기 때문에, **배치가 일어나는 시간에는 DB의 부하**가 크다.

    - **수평적 파티셔닝 구현 방법 3 - alias + 사이즈**

        Current Table(현재 시간 ~ window)을 두고, 일정 사이즈가 되면 파티셔닝 테이블로 복사하고, Current Table에서 데이터를 삭제하는 방법
        7. 장점
            1. 2번의 장점과 동일
            2. 테이블별 데이터 사이즈가 균일하다.
        8. 단점
            1. 2번의 단점과 동일
            2. 테이블을 찾는 로직이 더 복잡하다.

    - **수평적 파티셔닝 구현 방법 4 - alias + rename**

        Current Table(현재 시간 ~ window)을 두고, 일정 조건이 되면 파티셔닝 테이블로 이름을 바꾸고, Current Table은 새로운 빈 테이블로 새로 생성하는 방법
        9. 장점
           1. 2번의 장점과 동일
        10. 2번, 3번과 같은 부하가 없다.
           1. 단점
           2. 이름을 바꾸는 동안 client에서 문제가 발생할 수 있다.

    - **Vertical Partitioning (수직적 파티셔닝)**
        컬럼의 수를 줄여서 두 개 이상의 테이블로 나누는 것이다. 주로 B**LOB/CLOB(바이너리) 데이터로 저장된 컬럼이 복수개 있는 경우에 수직적 파티셔닝**을 고려한다. 이미 저장된 데이터의 **컬럼별 데이터 사이즈를 estimation 한 뒤에 저장**해야한다.
        - **수직적 파티셔닝의 단점**
            
            어플리케이션 **로직이 복잡해지는 단점**이 있다.
            - **단일 로우를 조회한다면 Join 을 추가**로 해야한다.
            - 집계 결과를 구한다면 **테이블 별 집계 결과를 다시 합쳐야 한다**.
            - **마이그레이션 단계에서 데이터를 복사**해야한다.
            
            특정 몇개의 컬럼만 데이터가 지나치게 크다면, 해당 컬럼에 대해서 또 수평적 파티셔닝이 필요할 수 있다. **단일 컬럼으로는 수직적 파티셔닝을 할 수 없으므로**.
            - 따라서 데이터가 지속적으로 쌓일 것을 고려한다면, **결국엔 수평적 파티셔닝이 필요**하다.

        - Vertical Partitioning vs Normalization

            Vertical Paritioning은 정규화(Normalization)랑 무엇이 다른가요?
            파티셔닝은 용량의 문제 때문에 물리적인 최적화를 하기위해서 나누는 것이다. 반면에 정규화는 개념적/추상적 수준에서 데이터의 성격 때문에 테이블을 나누는 것이다. 따라서 컬럼을 분리하는 것이라도 정규화에서 필요한 개념적인 수준에서의 요구가 아니라 단순히 용량 때문이라면 Vertical Partitioning 이라고 할 수 있다.

- **MySQL에서의 파티셔닝**
    DB에서 파티셔닝 기능을 지원하는 경우, 내가 직접 원하는 row가 어느 테이블 이름에 있는지 찾는 로직을 직접 짜지 않고 SQL로파티션된 데이터를 다룰 수 있다.
    - **제약 사항**

        MySQL에서 **InnoDB, NDB** 만 파티셔닝을 지원한다.

    - **파티셔닝 방법**
        - **RANGE partitioning**
        - **LIST partitioning**
        - **HASH partitioning**
        - **KEY partitioning**

    - **파티셔닝 정보**
        `INFORMATION_SCHEMA` 데이터베이스의 `PARTITIONS` 테이블에 파티셔닝 정보가 저장되어있다. `PARITIONS` 테이블에는 다음과 같은 정보들이 있다.
        - `TABLE_ROWS`
        - `DATA_LENGTH`
        - ...