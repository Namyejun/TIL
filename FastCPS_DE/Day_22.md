### 4. Indexing

- **데이터베이스 처리 단위 - page**
    
    ![Untitled](/FastCPS_DE/img/Untitled%2021.png)
    
    MySQL에서 조회하는 **데이터는 InnoDB Buffer pool에 있어야 한다**. 이미 **있지 않은 데이터라면, Disk에서 읽어서 메모리에 올려놓은 뒤에 응답**한다.
    
    Disk에서 데이터를 읽을 때는 **원하는 데이터만 읽어서 메모리에 올리지 않는다**. 내가 **원하는 데이터가 속한 page 단위로 읽어서 메모리에 로드** 한다.
    
    위 예제에서 `select * from EMP where id = 1` 로 조회했다고 하더라도, 1과 2가 같은 페이지에 속한다면, 1,2가 모두 메모리에 올라가게 된다.
    
    **메모리는 Disk보다 공간의 제약**이 있다. **사용하지 않는 데이터는 메모리에서 삭제**해야하는데, 이때도 **page 단위로 삭제**된다.
    
    따라서 **page의 크기가 데이터베이스의 성능에 큰 영향**을 미친다. 다음과 같은 상황은 어떤 결과를 낳을까?
    
    1. page의 크기가 너무 크다면?
    2. page의 크기가 너무 작다면?
    
    <aside>
    ℹ️ MySQL의 page 는 **16KB 단위로 관리**한다.
    
    </aside>
    
    <aside>
    ℹ️ Oracle 은 block 이라는 단위로 관리하는데, 그 크기를 조정할 수 있다. 2^N으로 최대 64KB까지 가능하다.
    
    </aside>
    
    - **Page의 크기와 record의 관계**
        
        각 테이블의 row 사이즈에 따라서 **1개의 page 에 있는 row의 수가 다르다**. 만약, **하나의 row가 16KB 이상이라면 2개의 page에 나눠서 저장**된다.
        
        ![Untitled](/FastCPS_DE/img/Untitled%2022.png)
        
        - 테이블 설정이 다음과 같다면 어떻게 될까?
            
            ```sql
            NAME: varchar(100),
            DEPT: char(10),
            DESC1: varchar(4000),
            DESC2: varchar(4000),
            DESC3: varchar(4000),
            DESC4: varchar(4000),
            BINARY1: BLOB,
            BINARY2: BLOB
            ```
            
            따라서 **page 가 너무 크다면**, **필요한 데이터에 비해서 Memory에 많은 데이터**가 올라오므로 **cache hit가 떨어진다**. 그리고 **메모리를 불필요하게 많이 점유**하게 된다.
            
            **단편화**도 어떤 관점에서 많이 생길 수 있다.
            
            반대로 **page 가 너무 작다면**, 데이터마다 **page 를 너무 빈번하게 메모리에 로드하고 삭제**하게 된다. 이 과정에서 **cache hit 또한 떨어지고, 추가삭제 작업 때문에 cpu 자원을 많이 소모**하게 된다.
            
- **Index 의 구조와 동작방식(B-Tree)**
    - **B-Tree 의 검색 방식**
        
        ![Untitled](/FastCPS_DE/img/Untitled%2023.png)
        
        위 tree 에서 Joey 를 찾는다고 해보자 어떤 과정으로 찾을까?
        
        - Root 블록에서 검색하려는 단어의 앞자부터 일치하는 범위를 찾는다.
            - [Anna, Janna) 범위의 알파벳은 BB_1 부터 다음 검색
            - [Janna, ) 범위의 알파벳은 BB_2 부터 다음 검색
        - Branch Block에서 같은 방식으로 찾는 대상이 속한 범위의 leaf block을 찾는다.
        - Leaf Block 안에서 해당하는 문자열을 찾는다.
        
        Leaf block까지 도달하는 과정을 `수직적 탐색` 이라고 한다.
        Leaf block에서 레코드를 찾는 과정을 `수평적 탐색` 이라고 한다
        
    - **B-Tree index가 비효율적일 때**
        
        **B-Tree는 수직 탐색의 비용이 크다**. Leaf block을 찾는다면, 해당 블록내에서 찾는 **수평적 탐색은 블록내의 크기 자체가 작기 때문에 비용이 크지 않다**.
        
        수직적 탐색은 **depth가 깊을수록 시간이 오래걸린다**. 그렇다면 언제 depth가 깊어질까?
        
        - **데이터의 양 자체가 많을 때** Tree 의 깊이 자체가 깊어진다.
        
        기본적으로 **인덱스를 구성하는 데이터도 페이지 단위로 관리**된다. **데이터의 길이가 길다면 더 많은 페이지가 필요**하다. 데이터의 길이가 길다면, depth가 깊어질 뿐만 아니라 **메모리에 로드되는 페이지도 더 많아진다**.
        
- **결합 인덱스**
    - 결합 인덱스란
        
        **두 개 이상의 컬럼으로 index를 구성**하는 경우를 말한다.
        
        - 순서에 따라 **선행 컬럼, 후행 컬럼으로 구분**한다.
        - 선행 컬럼에서 같은 값을 가진 경우, 후행 컬럼으로 정렬한다.
        - 따라서 선행, 후행의 순서가 성능에 큰 영향을 미친다.
        
        ![Untitled](/FastCPS_DE/img/Untitled%2024.png)
        
    - **결합인덱스의 원리 - 순서의 중요성**
        
        위의 INDEX_2 에서
        
        - Q: 서울에 사는 김기사를 찾는다면 어떻게 될까?
        - Q: 김기사를 찾는다면 어떻게 될까?
        
        서울에 사는 김기사
        
        - `WHERE location = ‘Seoul’ and name = ‘김기사’`
            - **location먼저 찾고, seoul 안에서 정렬된 이름으로 검색**
        
        김기사
        
        - `WHERE name = ‘김기사’`
            - location을 알 수 없으므로, **모든 location에 대해 김기사를 검색**
            - **정렬이 안된 것**이랑 같음
                - **TABLE FULL SCAN**
        
        Q: 같은 검색조건을 **INDEX[ name + location ] 으로 구성된 테이블에 검색**한다면, 결과는 어떻게 달라질까?
        
        - Q: 서울에 사는 김기사를 찾는다면 어떻게 될까? → 김기사를 찾고 서울사람을 찾는다.
        - Q: 김기사를 찾는다면 어떻게 될까? → name으로 정렬되어 문제없이 찾는다.
    - **결합인덱스의 원리 - 정렬**
        
        ![Untitled](/FastCPS_DE/img/Untitled%2025.png)
        
        `SELECT location, name, register_date FROM driver WHERE location='Seoul' and name = '김기사' ORDER BY register_date;`
        
        Q: INDEX2 로 구성된 테이블에 위 쿼리를 수행하면 어떻게 될까?
        
        Q: INDEX3 으로 구성된 테이블에 위 쿼리를 수행하면 어떻게 될까?
        
        INDEX2
        
        - register_date 가 정렬되어있지 않으므로, **client 의 sort buffer 에 해당 내용을 적재 후, 정렬**을 ****한 뒤 내보내게 된다. **메모리나 cpu 자원 소모**
        
        INDEX3
        
        - **reigster_date 로 이미 정렬**되어있으므로, 그 **인덱스에서 조회된 그 상태로 client 에게 전달**된다.
    - **Covering Index**
        
        ![Untitled](/FastCPS_DE/img/Untitled%2026.png)
        
        `SELECT location, register_date, name FROM driver WHERE location='Busan' and register_date > '20120101';`
        
        Q: 위 쿼리를 INDEX4 에 수행하면 어떤 동작을 할까?
        
        Q: 위 쿼리를 INDEX 5에 수행하면 어떤 동작을 할까?
        
        INDEX4의 경우, name 정보가 index에 없으므로 테이블에서 name정보를 추가로 가져와야 한다.
        INDEX5의 경우, name정보가 index에 있으므로 바로 응답이 가능하다.
        
        Q: 그렇다면 INDEX를 가능한한 많이 거는 것이 좋을까?
        
    - **결합 인덱스 가이드**
        1. 조건절에 자주 사용되는 컬럼들을 선정한다.
        2. 선정된 컬럼 중 equals 조건(=, in)으로 조회되는 컬럼을 선행 컬럼으로 한다.
        3. Sort 작업이 생략되도록 sort 기준이 있다면 해당 컬럼을 인덱스에 추가한다.
        4. Covering Index로 해결할 수 있다면 해당 컬럼을 인덱스에 추가한다.
            1. 실행 계획에 Using index 로 마킹된다.
- **Index Scan의 종류**
    - **Index Range Scan**
        - INDEX 루트 블록에서 리프 블록까지 **수직적으로 탐색한 후에 리프 블록을 필요한 범위만 스캔**하는 방식
        - Single Block I/O
    - **Index Range Scan Descending**
        - INDEX **Range Scan과 기본적으로 동일하지만, INDEX를 뒤에서부터 앞쪽**으로 스캔
        - Single Block I/O
    - **Index Unique Scan**
        - **수직적 탐색만으로 데이터를 찾음 (리프노드가 하나의 데이터로 구성)**
        - **Unique INDEX를 ‘=‘ 조건으로 탐색하는 경우**에 작동
        - Single Block I/O
    - **INDEX Skip Scan**
        - 루트 또는 브랜치 블록에서 읽은 칼럼값 정보를 보고 조건에 부합하는 레**코드를 포함 할가능성이 있는 하위 블록만 골라서 액세스**
        - **결합 칼럼 index 구성**에서 **선행 컬럼에 조건이 없는 경우 →** 후행컬럼만 보고 해야함 어차피 풀스캔 돌아야함
        - **선행 컬럼의 cardinality가 작을 때 효과적**
    - **INDEX Full Scan**
        - **INDEX 리프 블록을 처음부터 끝까지 수평적으로 탐색**하는 방식
        - Single Block I/O
        - Index **Leaf Node Entry의 정렬된 결과**를 받음
    - **INDEX Fast Full Scan**
        - INDEX **세그먼트 전체를 Multiblock Read 방식**으로 스캔
        - INDEX의 논리 구조가 아니라, **물리적인 저장순서대로 INDEX블록**을 읽음
        - **Multiblock I/O** 발생
            - `db_file_multiblock_read_count` 로 설정
        - 결과의 **정렬 순서가 보장되지 않는다.**