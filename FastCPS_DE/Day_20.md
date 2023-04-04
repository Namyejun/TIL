### 2. MySQL Architecture

- **MySQL Basic Architecture**
    
    ![Untitled](/FastCPS_DE/img/Untitled%2014.png)
    
    - **MySQL Engine**
        
        MySQL Engine은 **클라언트로부터의 요청**을 받고, **SQL을 분석하고 최적화**하는 역할을 수행한다.
        
        **Connection Handler** : 클라이언트로부터의 접속, 쿼리요청 처리
        
        **SQL interface** : SQL을 받아준다.
        
        **SQL Parser** : SQL을 파싱하고, 전처리를 한다.
        
        **SQL Optimizer** : 쿼리 최적화와 실행계획을 짠다.
        
    - **Storage Engine**
        
        MySQL Storage Engine은 **실제 데이터를 디스크에 저장**하거나, **디스크로부터 데이터를 읽는 처리**를 담당한다.
        Storage Engine 은 **Plugin 방식으로 원하는 구현체를 선택**할 수 있다. 즉, **하나의 DB 서버에서 논리적으로 Storage Engine을 선택**할 수 있다. **선택은 database , table 마다 할 수 있다.** **create database, table 선언시에** `ENGINE=$ENGINE_NAME` **으로 설정**한다.
        `SHOW ENGINES;` 커맨드로 확인할 수 있다.
        
        <aside>
        ℹ️ MySQL 은 storage engine 뿐만 아니라 다양한 기능들도 플러그인 형태로 지원한다. 인증 관련 기능, 검색용 파서, 쿼리 rewrite 플러그인 등이 있다. 기본적으로 MySQL의 표준 API 가 열려있기 때문에 가능하다.
        
        </aside>
        
    - **Handler API**
- **MySQL 스레드 구조**
    
    ![Untitled](/FastCPS_DE/img/Untitled%2015.png)
    
    MySQL 은 멀티 프로세스가 아니라 멀티 스레드 기반으로 동작한다. 동작 방식에 따라 Foreground, Backgound 스레드로 구분한다. 실행중인 스레드는 performance_schema 데이터베이스 > threads 테이블에 기록된다.
    
    - **Foreground Thread(Client connection)**
        
        foreground thread 는 **최소한 현재 연결된 클라이언트의 수만큼 존재**한다. 클라이언트의 **커넥션이 종료되면, 다시 스레드 캐시로 돌아간다**. 스레드 캐시에 **일정 개수 이상의 스레드가 대기중이라면, 스레드 캐시에 돌아가지 않고, 스레드를 종료**한다. 최대 대기 스레드수는 `thread_cache_size` 로 설정한다.
        foreground thread 는 **데이터를 데이터 버퍼나 캐시로부터 가져오고, 버퍼나 캐시에 없다면 디스크에서 읽어서 가져온다**.
        **InnoDB는 foreground thread 는 cache, buffer 까지만 접근하고 디스크에는 접근하지 않는다**.
        
    - **Background Thread**
        
        InnoDB 기준으로 background thread 는 다음 일을 한다.
        
        - insert buffer 를 merge
        - Log 를 disk에 기록
        - InnoDB buffer pool의 데이터를 disk에 기록
        - 데이터를 버퍼로 read
        - Lock monitoring thread
        
        원하는 읽기 쓰기 성능이 안나오거나, 주 사용용도를 예측해서 스레드 수를 조정할 수 있다
        
        - `innodb_write_io_threads`
        - `innodb_read_io_threads`
        
        <aside>
        ℹ️ innodb 의 경우 읽기는 대부분 포그라운드 스레드에서 처리되기 때문에 innodb의 read 스레드를 늘릴일은 많지 않다. **쓰기 작업이 많거나, 지연되는 경우**에 `innodb_write_io_threads` 를 **2 이상으로 세팅**한다.
        
        </aside>
        
        innodb는 **지연된 쓰기 작업을 지원**한다. 쓰기 작업을 **버퍼에 넣고 아직 디스크에 쓰이기 전에 클라이언트에 응답**할 수 있다. 버퍼에 쌓인것은 **내부적으로 배치처리로 적용**한다.
        
- **메모리 구조**
    
    ![Untitled](/FastCPS_DE/img/Untitled%2016.png)
    
    - **글로벌 메모리 영역**
        
        **MySQL이 시작되면서 운영체제로 부터 할당** 된다. **클라이언트 스레드 수와 상관없이 하나**(또는 N개)의 공간이다. **모든 스레드가 공유하는 자원**이다.
        
        다음과 같은 내용들이 있다.
        
        - InnoDB buffer pool
        - InnoDB adaptive hash index
        - InnoDB redo log buffer
        - table cache
    - **세션(로컬) 메모리 영역**
        
        클라이언트 스레드가 쿼리를 처리하는데 사용하는 메모리 영역. 각 클라이언트 스레드별로 독립적으로 할당 되고 공유되지 않는다. 각 쿼리별로 필요한 용량을 할당한다. 할당하지 않는 경우도 있다.
        
        - **Sort buffer** : Sort 쿼리가 있을 때만 할당되고 해제된다. 아예 할당이 안될수도 있다.
        - **Join buffer** : Join 쿼리가 있을 때만 할당되고 해제된다. 아예 할당이 안될수도 있다.
        - **Binary Log Cache**
        - **Network buffer** : Connection buffer는 항상 할당되어있다.
- **Query 실행 구조**
    
    ![Untitled](/FastCPS_DE/img/Untitled%2017.png)
    
    - **Query Parser**
        
        **쿼리를 토큰(인식할 수 있는 최소단위의 단어, 기호) 단위로 분리**해 **Tree 자료구조를 만든다**. **문법 오류를 이 단계에서 검출**한다
        
    - **Preprocessor**
        
        Parser Tree 를 기반으로 쿼리문 안에 **의미적인 오류가 있는지 확인**한다. **테이블 이름, 칼럼 이름, 내장함수와의 매핑 등을 확인**한다.
        SQL 수행할 **권한이 있는지 확인**한다.
        
    - **Optimizer**
        
        쿼리를 **가장 적은 비용(cost)으로 처리할 수 있도록 의사결정**을 한다.
        
        고려요소(파라미터)
        
        - **테이블, 또는 인덱스 당 page 수**
        - **인덱스의 카디널리티**
        - **Row 길이**
        - **key 길이**
        - **key 분포**
    - **Execution Engine**
        
        실행엔진은 **Optimizer에게 받은 계획**에 따라 **핸들러에게 구체적으로 할 일(read, write)을 알려**준다.
        예 : **group by 를 처리**하기 위해 임시테이블을 만든다.
        
        1. Execution Engine이 핸들러에게 임시 테이블을 만들라고 요청
        2. Execution Engine은 where 에 일치하는 레코드를 읽어오라고 함.
        3. 읽어온 레코드를 1번에서 준비한 임시테이블에 저장하라고 핸들러에 요청
        4. 데이터가 준비된 임시 테이블에서 데이터를 읽으라는 요청을 핸들러에게 요청
        5. Execution Engine은 최종 결과를 사용자나 다른 모듈로 넘긴다.
    - **Handler (Storage Engine)**
        
        Execution Engine의 요청에 따라 데이터를 디스크로 저장, 또는 데이터를 디스크에서 읽어오는 역할을 한다.
        
- **Query Cache**
    
    SQL의 실행 결과를 메모리에 저장하고, **동일한 SQL이 실행되면 디스크에서 읽지 않고 즉시 결과**를 준다. 다만, **테이블의 데이터가 변경**되면 **해당 테이블과 관련된 캐시를 모두 삭제** 해야했는데, 이것 때문에 **오히려 성능저하**가 오는 경우가 많았다. 이 때문에 **MySQL 8.0 에서 Query Cache는 삭제**되었다.
    
- **Thread Pool**
    
    <aside>
    ℹ️ MySQL **Enterprise 버전에서만 Thread Pool을 지원**한다. MySQL Community 버전을 이용하는 경우에는 [**Percona Server for MySQL](https://www.percona.com/software/mysql-database/percona-server)을 이용하면 플러그인 형태로 thread_pool.so 를 설치**해서 사용할 수 있다.
    
    </aside>
    
    Percona Server 의 스레드 풀은 **기본으로 장치의 CPU 코어 수 만큼 스레드 그룹을 생성**한다. `thread_pool_size` 로 조정할 수 있다. 다만, CPU 코어 수와 스레드 수를 맞추는 것이 **Context Switch 가 덜 일어나므로 processor affinity 에 좋다**. 이미 스레드 풀이 모두 일하고 있다면 `thread_pool_oversubscribe` 의 수만큼 추가로 스케줄링 할 수는 있다.
    
    스레드 그룹의 모든 스레드가 할당되어 일하고 있다면, 스레드 풀은 스레드 그룹에 새로운 스레드를 추가할지, 아니면 기존 스레드가 작업을 완료할 때까지 기다릴지를 판단한다. 스레드풀의 타이머 스레드가 주기적으로 스레드 그룹의 상태를 체크해서 `thread_pool_stall_limit` **시스템 변수에 정의된 (milliseconds) 기간동안 작업을 못 끝낸다면, 새로운 worker thread를 추가**한다.
    
    - **client의 동시요청이 많고, 응답시간이 중요한 서비스**라면?
        - `thread_pool_stall_limit`를 감소시킨다.
    
    Percona Server의 스레드풀 플러그인은 선순위 큐와 후순위 큐를 이용해 특정 트랜잭션이나 쿼리를 우선 처리할 수 있는 옵션을 제공한다. **우선순위 큐에 속한 트랜잭션을 빨리 처리**하면, 해당 **transaction에 의한 lock이 빨리 해제**되고, **race condition(경쟁 상태)**을 낮추어서 전체적인 **처리 성능을 높이자는** 아이디어이다.