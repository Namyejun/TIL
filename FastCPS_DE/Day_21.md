### 3. InnoDB 스토리지 엔진 아키텍처

![Untitled](/FastCPS_DE/img/Untitled%2018.png)

InnoDB는 가장 많이 사용되는 Storage Engine이다. MySQL의 스토리지 엔진 중 거의 **유일하게 레코드 기반 Lock을 제공**하고, 이 때문에 **높은 동시성 처리가 가능**하기 때문이다.

- **Clustering by Primary Key**
    
    InnoDB의 모든 테이블은 기본으로 **PK를 기준으로 클러스터링 되어 저장**된다. **PK값의 순서대로 디스크에 존재**한다고 이해하면 된다. **PK이외의 인덱스는 레코드의 주소 대신 PK값을 논리적인 주소로 사용**한다. 따라서 **PK를 기준으로 하는 Range Scan의 속도가 빠르다**. 따라서 쿼리 실행 계획에서 PK는 다른 인덱스에 비해 비중이 높게 설정된다.
    **MyISAM 스토리지 엔진은 클러스터링 키를 지원하지 않는다**. 따라서 **MyISAM에서는 PK와 다른 인덱스 사이의 차이가 없다**.
    
- **Foreign Key**
    
    InnoDB에서 외래 키(Foreign Key)는 **부모 테이블과 자식 테이블 모두 해당 칼럼에 대해 인덱스 생성이 필요**하다. 또한 변경 시 반드시 부모 테이블, 자식 테이블에 데이터가 있는지 체크하기 때문에 **Lock이 여러 테이블로 전파**된다. 이 때문에 **데드락이 발생할 위험**이 있다.
    
    - `SET foreign_key_check=OFF;` 설정하면 체크 작업을 멈출 수 있다.
- **MVCC(Multi Version Concurrency Control)**
    
    **레코드 레벨의 트랜잭션을 지원하는 DB에서 지원하는 기능**이다. MVCC의 목적은 **일관된 읽기를 제공**하는 데 있다. **InnoDB는 undo log를 이용해서 이 기능을 구현**한다.
    
    ![Untitled](/FastCPS_DE/img/Untitled%2019.png)
    
    다음 상태에서 `UPDATE member SET m_area='경기' WHERE m_id=12;` 를 수행하면 다음과 같은 상태로 변경된다.
    
    ![Untitled](/FastCPS_DE/img/Untitled%2020.png)
    
    이 상태에서 만약 **Isolation Level**이
    
    - **READ_UNCOMMITTED** 라면, **InnoDB 버퍼풀의 내용을 전달**한다.
    - **READ_COMMITTED 이상(REPEATABLE_READ, SERIALIZABLE)**이라면, **아직 커밋되지 않았으므로 undo log의 내용을 반환**한다.
    
    즉, **undo 영역으로 응답할 수 있기 때문에 동시에 두개의 버전이 존재**할 수 있는데, 이것을 **MVCC**라고 한다.
    다만, 사**용이 복잡해질수록, undo space의 공간이 많이 필요**할 수 있다.
    
    - 여기서 commit이 일어나면 **undo log는 없어지고, 버퍼풀의 내용이 디스크에 쓰인다**. 다만, **디스크에 쓰이는 시점은 background thread에 의해 결정**된다.
    - 여기서 rollback이 일어나면 **buffer cache에 undo log가 적용되고, undo log는 지워**진다.
- **잠금 없는 일관된 읽기(non-locking consistent read)**
    
    위의 MVCC에 의해서 **Lock을 걸지 않고 읽기 작업을 수행**한다.
    
    - **Serializable이 아니면서, 순수한 select문의 경우** (insert등과 연결되지 않은 트랜잭션)
    
    단, **Transaction이 시작되고 commit,rollback없이 오랜시간이 지나면 해당 트랜잭션으로 인해 undo log를 지우지 못하게 된다**.
    이것 때문에 **서버가 느려지거나 undo log 공간부족으로 문제**가 생길 수도 있다.
    
- **InnoDB 버퍼 풀**
    
    디스크의 **데이터 파일이나 인덱스 정보를 메모리에 캐시하는 공간**이다. 또한 **쓰기 작업을 지연**시키고 **배치로 disk에 write 할 수 있도록 하는 버퍼 역할**도 한다.
    예를 들어, **insert, update, delete 요청을 다양하게 날린다면, 디스크에 random access를 높여 성능이 떨어**진다. buffer pool이 **이 작업들을 모아서 처리하면 random access 횟수를 줄일** 수 있다.
    
    - **버퍼풀 크기 설정**
        
        버퍼풀의 크기를 운영중 동적으로 조정할 수 있다.
        
        - `innodb_buffer_pool_size` 로 조정
        
        InnoDB의 버퍼풀은 해당 머신의 **50%이하부터 시작해서 모니터링 하면서 늘려가는 방법을 추천**한다. 쿼리의 결과가 대량의 레코드인 경우가 거의 없다면 (client가 사용하는 record buffer 사이즈를 고려), **수정 없이 80%로 운영하는 것도 하나의 방법**이다
        
        단, 버퍼풀의 **메모리를 늘리는 것은 큰 문제가 없지만, 줄이는 것은 영향이 크므로** 가능하면 **줄이는 일이 없도록 운영**해야한다.
        버퍼풀은 **내부적으로 세마포어로 잠근 경합**이 있는데, 이 경합을 줄이기 위해 **쪼개서 관리할 수 있다**.
        `innodb_buffer_pool_instances`로 조정할 수 있다. 1GB 미만에 대해서는 1개만 가능하다. **버퍼풀 인스턴스당 5GB 정도**가 되도록 유지하는 것이 적절하다.
        
    - **InnoDB 버퍼풀 구조**
        
        InnoDB 스토리지 엔진은 **버퍼풀을 page 조각 단위로 관리**한다. ( `innodb_page_size` , 보통 **4K**)
        페이지 관리를 위해 **LRU(least recently used), Flush, Free 세 개의 자료구조로 관리**한다.
        
        - **LRU list**: **한 번 읽어온 페이지를 최대한 오래 버퍼풀에 유지**해서 hit를 높이고 disk access를 줄이기 위해 사용.
            - 내부적으로 두개의 리스트가 있는데, **old 영역은 LRU**(least recently used)로 관리, **new 영역은 MRU**(Most recently used)로 관리.
        - **Flush list**: 디스크로 동기화되지 않은 데이터를 가진 페이지**(dirty page)의 변경 시점 기준의 페이지 목록을 관리**한다. 디스크에서 **읽은 상태에서 변경이 가해지면 flush list에 의해 관리**. **특정 시점이 되면 disk에 기록**된다.
        - **Free list**: 비어있는 페이지 목록
    - **InnoDB에서 데이터를 찾는 과정**
        1. 필요한 레코드가 **버퍼 풀에 있는지 검사**
            1. **InnoDB adaptive hash index**를 통해 검색
            2. 해당 테이블의 **인덱스(B-Tree)로 버퍼풀에서 페이지 검색**
            3. 조회하려는 데이터의 페이지가 **이미 버퍼 풀에 있었다면, 해당 페이지의 포인터를 MRU 방향으로 승급**
        2. (1에서 조회가 안되면) **디스크에서 필요한 데이터 페이지를 찾아 버퍼풀에 적재**, 적재된 페이지에 대한 **포인터를 LRU head에 추가**.
        3. 버퍼풀의 **LRU 헤더에 적재된 데이터 페이지가 읽히면, MRU 헤더로 이동**.
        4. 버퍼 풀에 상주하는 데이터 페이지는 사용자 쿼리가 얼**마나 최근에 access 했는지에 따라 age가 부여**됨. **aging 이 오래되면 버퍼풀에서 제거**된다. 버퍼 풀의 데이터 페이지가 **access되면 age가 초기화되고, MRU의 헤더**로 옮겨진다.
        5. 필요한 데이터가 **자주 접근된 데이터**라면, 해당 페이지의 **인덱스 키를 adaptive hash index에 추가**
    - **Change Buffer**
        
        **변경해야할 인덱스 페이지가 버퍼풀에 있으면 바로 업데이트를 수행**한다. 만약 **디스크에서 읽어와서 업데이트를 해야한다면, 즉시 실행하지 않고 임시공간에 저장**해두고 **바로 사용자에게 결과를 반환해서 성능 향상**을 시킨다 이 때 사용하는 임시 메모리 공간이다.
        
        단, **응답 전에 중복여부가 확인되어야 하는 unique index는 change buffer를 사용할 수 없다**.
        Change Buffer 에 기록된 **인덱스 레코드 조각은 background 스레드에 의해 병합**된다. 이 때 스레드를 **change buffer merge thread**라고 한다.
        `innodb_change_buffering` 변수로 어떤 작업에 대해 change buffer 를 쓰게 할 것인지 결정할 수 있다.
        
    - **Adaptive Hash Index**
        
        일반적으로 MySQL에서의 인덱스는 모두 B- Tree 자료구조로 관리된다.
        Adaptive Hash Index는 **b-Tree의 검색 시간을 줄여주기 위해 도입**되었다. 자주 읽히는 데이터 페이지의 **키값을 통해 해시 인덱스를 만들고, 필요할 때마다 Adaptive Hash Index를 통해 페이지에 즉시 접근 가능**하도록 한다. 이 방식은 **Hash table이기 때문에 O(1)으로 수행**되므로, **B-Tree의 Log2(N)보다 빠르고 그만큼 Cpu자원을 아낄 수 있다**.
        
        단, 다음과 같은 경우 Adaptive Hash Index는 성능 향상이 크지 않다.
        
        - 디스크 읽기가 많은 경우
        - 패턴 쿼리가 많은경우 (LIKE문)
        - 큰 테이블에 대해 스캔 범위가 넓은 경우
        
        다음 경우에는 큰 이득을 볼 수 있다.
        
        - 디스크의 데이터가 InnoDB 버퍼 풀 크기와 비슷할 때
        - equals 검색이 많은 경우(==, in절)
        - 쿼리의 데이터가 일부 데이터만 조회하는 것이 대부분인 경우