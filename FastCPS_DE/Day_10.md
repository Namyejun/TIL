### 5. JDBC

- 표준 인터페이스가 없을 때
    ![Untitled](/FastCPS_DE/img/Untitled%208.png)
    
- 표준 인터페이스가 있을 때
    
    ![Untitled](/FastCPS_DE/img/Untitled%209.png)
    
- **JDBC**
    - Java Database Connectivity
        
        Java application이 client로서 어떻게 데이터베이스에 접근하는지 정의해놓은 표준 인터페이스이다. Java Standard Edition (Java SE)에서 지원하는 스펙이다.
        
        Database에 접속하고 데이터를 업데이트하거나 쿼리(질의)할 수 있는 메소드를 제공한다. 기본적으로 RDBMS(관계형 데이터베이스)를 상정하고 만들어졌다.
        
- **ODBC**
    - Open Database Connectivity
        
        JDBC를 통해서 Java Application에서는 DBMS의 종류를 바꾸어도 인터페이스(코드)는 변경하지 않아도 되는 장점을 얻었다. DBMS를 사용하는 많은 시스템들이 자바로 작성된 어플리케이션인 것에는 JDBC의 영향이 꽤 크다.
        여기서 착안해서, 프로그래밍 언어나 운영체제에 상관없이, DBMS에 독립적으로 사용할 수 있는 전송계층을 만들려는 노력으로 ODBC drvier가 만들어졌다.
        
        ![Untitled](/FastCPS_DE/img/Untitled%2010.png)
        

### 6. JDBC 실습 - 세팅

gradle 프로젝트에 디펜던시 추가

```markdown
implementation 'mysql:mysql-connector-java:8.0.30'
```

4개를 임포트 해줘야함.

1. Connection
2. DriverManager
3. ResultSet
4. Statement

### 7. JDBC 실습 - Driver Manager, Connection

- **DriverManager**
    
    User와 Driver 사이의 인터페이스를 담당. Driver의 이용가능 여부, Database와 Driver사이의 Connection을 관리한다. Driver의 등록/해제, Connection의 연결/해제를 관리한다. Driver의 Register가 반드시 성공해야 DB와 상호작용을 할 수 있다.
    
    - DriverManager 로 MySQL 접속하기
        
        과거에는 클래스로딩을 위해서 `Class.forName()` 으로 해당 클래스를 클래스패스에서 찾아서 클래스로더가 로딩할 수 있도록 한다. 이렇게 클래스 로딩이 되어야 DriverManager가 표준 인터페이스로 메소드를 호출할 때, 해당 JDBC드라이버의 구현체로 연결될 수 있었다.
        하지만 **최신 버전에서는 Java SPI를 이용해서 자동으로 MySQL Driver 클래스를 표준 Driver 인터페이스에 등록** 해줄 수 있게되었다. **Connection url에 mysql 정보가 있고, mysql connector library 가 클래스패스에 있다면, get connection 단계에서 자동으로 찾아준다.**
        
    - DriverManager 로 Connection 연결하기
        
        ```markdown
        Connection con = DriverManager.getConnection(
        "jdbc:mysql://localhost:3306/de-jdbc", "root", null);
        ```
        
        DB와의 모든 동작은 getConnection 을 통해서 JDBC Driver 클래스를 찾고, 연결까지 성공한 뒤에 할 수 있다.
        
- **Connection**
    
    **Connection 객체 하나**는, **DB와 Java Client 사이의 하나의 물리적인 연결**을 의미한다
    
    이 연결은 DB입장에서는 하나의 Session을 의미한다. Session은 변경사항의 묶음을 관리하는 하나의 단위라고 이해하면 된다. Session에 대해 자세한 내용은 이후 Transaction, RDBMS이해하기 부분에서 더 다룬다.
    
    해당 연결에서 사용할 **Statement, PreparedStatement,** and **DatabaseMetaData** 객체들을 얻어올 수 있다
    
    - 주요 메소드
        - `Statement createStatement()`
            
            Statement 객체를 생성한다.
            
        - `PreparedStatement prepareStatement(String sql)`
            
            Parameterized된 sql과 함께 PreparedStatement 객체를 생성한다.
            
        - `DatabaseMetaData getMetaData()`
            
            DB의 여러가지 메타정보를 제공하는 DatbaseMetaData 객체를 제공한다.
            
            DatbaseMetaData 객체를 통해서 DB vendor 가 명시하는 DB의 스펙이나 설명을 프로그래밍으로 얻을 수있다.
            
        
        **Session이기 때문에 Session단위에서 이루어지는 동작을 메소드로 제공**한다. 이 메소드들은 Transaction 실습에서 구체적으로 다룬다.
        
        - `setAutoCommit(boolean status)`
            
            autocommit 을 사용할지 여부. 기본 값은 true . Auto Commit을 사용한다면, **executeXXX 종류의 함수를 실행하면 바로 commit이 발생**해서 변경사항이 최종 테이블에 반영이 된다.
            
        - `commit()`
            
            지금까지 해당 Connection(Session)에서 수행한 변경사항들을 Database의 원본 테이블에 반영한다. **commit이 성공하면 해당 connection(session)을 가지지 않은 client들도 해당 commit에 의해 변경된 데이터를 볼 수 있다.**
            
        - `rollback()`
            
            지금까지 **해당 Connection에서 수행한 변경사항들을 Database의 원본 테이블에 반영하지 않고, 해당 Connection(Session)에서 바라보는 상태도 원래대로 돌린다.**
            
        - `void setTransactionIsolation(int level)`
            
            **transaction isolation level** 을 직접 지정할 수 있다. parameter는 int를 받도록 되어있지만, **Connection에 미리 정의된 상수(constant)를 사용**한다.
            
            - `Connection.TRANSACTION_READ_UNCOMMITTED`
            - `Connection.TRANSACTION_READ_COMMITTED`
            - `Connection.TRANSACTION_REPEATABLE_READ`
            - `Connection.TRANSACTION_SERIALIZABLE`
        - `close()`
            
            **연결을 즉시 끊는다**. 실행중인 자원의 처리여부는 상관 없다.