# **Ch 10**. **데이터베이스(RDBMS) 구조와 동작방식 (MySQL을 기초로)**

### 1. RDBMS Architecture

- overview
    
    [https://dsf.berkeley.edu/papers/fntdb07-architecture.pdf](https://dsf.berkeley.edu/papers/fntdb07-architecture.pdf)
    
    ![Untitled](/FastCPS_DE/img/Untitled%2011.png)
    
    1. **Client Communication Manager**
        
        **외부의 Client 에서 접속**하고, **명령을 전달할 수 있는 통로**. 그리고 그 **자원의 관리**.
        
        - Client 로부터의 연결을 받는다.
            - **연결을 맺기 위한 인증, 보안 등의 프로세스를 처리**한다.
        - Client의 연결의 상태를 관리한다. (**session**)
        - SQL의 **실행 결과를 응답**한다.
        
    2. **Process Manager**
        
        **RDBMS에서 필요한 자원을 관리**, 주로 **프로세스/스레드의 전용, 스케줄링, 할당 등을 관리**.
        
        - Client에서 요청이 와서 연결을 맺으면 스레드에 할당된다. 이 때 Process Manager 는 **Client connection pool 에서 유휴 스레드를 꺼내서 할당**한다.
        - 뿐만 아니라 r**ead, write 등의 전용 스레드 풀도 따로 관리**해서, **특정 작업의 부하나 병목 때문에 다른 작업을 할 자원이 부족한 일이 없게 한다**.
        - **실행을 즉시 할지, 지연해서 할지 등의 결정**도 할 수 있다.
        
    3. **Relational Query Processor**
        
        Client 로부터 전달된 **쿼리의 해석과 실행 계획을 담당**.
        
        - Query **Parser가 Query 를 파싱**한다.
        - 접속한 유저가 해당 **Query를 실행할 권한이 있는지 확인**한다.
        - **Query optimizer가 적은 비용으로 쿼리를 실행 할 수 있도록, Query의 실행계획을 짠다**.이때 **DBMS의 카탈로그 정보를 참고**한다.
        - Query Excecutor는 **Query Plan 이 나오면 실제 물리적인 자원에 어떻게 할당할 것인지 결정**한다.
        - 그 외에도 부가적인 처리를 할 수 있다.
        
        **Query Parser의 동작**
        
        ![Untitled](/FastCPS_DE/img/Untitled%2012.png)
        
        - **문법을 확인**한다.
        - 구문의 내용의 **의미를 확인**한다.
            - table 의 존재여부
            - column 의 존재여부
        - 자원을 많이 소모하는 작업을 피하기 위한 **shared pool check를 한다.** 이미 있는 내용이라면, 이후 자원을 많이 소모하면서 실행계획을 짜거나 실행할 필요가 없다.
        
        **Query Optimizer 의 동작방식**
        
        ![Untitled](/FastCPS_DE/img/Untitled%2013.png)
        
        - SQL의 기능은 똑같지만, **SQL문의 내용의 순서나 형식 등을 바꿔서 성능상 더 나은 쿼리가 나온다면, Query Transformer에서 query를 rewrite** 한다.
        - **Estimator 는 실행 계획에 대한 비용을 계산**한다. 이때 **Data dictionary를 참고**한다.
            - (Oracle 의 경우)다음 지표들을 수집/계산한다.
            - **Selectivity**: scan한 row중에 몇 퍼센트만큼 최종결과에 선택되는지 비율을 계산한다.
            - **Cardinality**: 각 플랜이 리턴한 결과의 row수.
            - **Cost**: 해당 작업이 얼마만큼의 리소스를 사용할지예 대한 추정치. 통계를 활용하고, 통계는 지속적으로 조정된다.
            
    4. **Transactional Storage Manager**
        
        **Transaction 처리와 관련된 기능**들을 담당.
        
        - 실제 데이터에 접근
        - **Access method**는 query 실행 오퍼레이터에 의해 **원본데이터에서 뽑아낸 result tuple 을 리턴**한다.
        - **Result tuple 은 만들어지면 buffer 에 위치**한다. **Client Manager는 이 버퍼에서 데이터를 가져와서 응답**한다.
        - **Transaction 의 상태 기록, 라이프사이클 관리**.
    
    1. **Shared Components and Utilities**
        
        그 외에도 시스템의 각 기능이 잘 동작하기위해서 필요한 컴포넌트나, 유틸들이 있다.