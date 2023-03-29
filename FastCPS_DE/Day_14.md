### 13. Transaction이란?

- **Transaction**
    
    Transaction은 데이터베이스에서 하나의 작업 단위를 말한다.
    Transaction 작업 단위는 **ACID** 라는 특징을 반드시 가져야 한다.
    
    - **Atomicity** : **모두 성공하거나, 모두 실패**
        
        예: 하나의 작업의 단위에서 4개의 update가 이루어져야 하는데, 마지막 update가 실패했다면, 4개를 모두 반영하지 않는다.
        
    - **Consistency :** 데이터베이스를 하나의 **유효한 상태로부터 그 다음 유효한 상태로 변경하는 것을 보장**. 데이터(또는 데이터 사이의 관계)가 오류가 있는 상태로 존재하지 않는다.
        
        예: FK가 RESTRICT로 설정되어있는데, 자식테이블의 데이터가 존재하는 상태로 부모테이블의 row가 지워지는 경우는 있을 수 없다. 그런 쿼리는 실패한다.
        
    - **Isolation : 하나의 transaction은 다른 transaction과 독립**되어있다. commit되지 않은 다른 transaction의 변경사항에 영향을 받지 않는다.
    - **Durability :** 한 번 transaction이 **commit되면, 어떤 경우에도 그 데이터 또는 상태는 유지**된다. 심지어는 컴퓨터의 전원이 꺼져도 유지된다.
- **Isolation Level (격리 수준)**
    
    하나의 transaction이 데이터를 변경할 때, 다른 transaction에서 어떤 영향을 받는지에 대해서 다음과 같은 문제가 있다.
    
    - **Dirty Read** : **자신의 transaction에서 처리한 작업이 완료되지 않았음**에도 불구하고 **다른 transaction에서 볼 수 있게 되는 현상**
    - **Non Repeatable Read :** 동일한 SELECT 쿼리를 실행했음에도 다른 transaction의 변경이 반영되어서 **항상 같은 결과를 보장하지 못하는 현상**
        - **Repeatable Read :** 동일한 SELECT 쿼리 수행에 대해서 **항상 같은 결과를 보장한다.**
    - **Phantom Read : 다른 tranaction에서 수행한 변경 작업에 의해 레코드가 보였다가 안보였다** 하는 현상
    
    이 문제들을 해결하기 위해서 4가지가 **격리 수준 설정을 제공**한다.
    
    - **READ UNCOMMITTED(커밋되지 않은 읽기)**
        
        transaction 안에서 커밋하지 않은 데이터를 다른 tranaction이 볼 수 있다.
        
    - **READ COMMITTED(커밋된 읽기)**
        
        transaction 에서 커밋된 데이터만 다른 transaction이 볼 수 있다.
        
    - **REPEATABLE READ(반복 가능한 읽기)**
        
        transaction 내에서 한 번 조회한 **데이터를 반복해서 조회해도 결과가 항상 동일**
        
        **MySQL JDBC의 기본값.**
        
    - **SERIALIZABLE(직렬화 가능)**
        
        **가장 엄격한** 격리 수준. 완벽한 읽기 일관성 모드 제공
        
    
    다음은 격리 수준 별 발생할 수 있는 문제를 표로 정리한 것이다.
    
    |  | Dirty Read | Non Repeatable Read | Phantom Read |
    | --- | --- | --- | --- |
    | READ UNCOMMITTED | O | O | O |
    | READ COMMITTED |  | O | O |
    | REPEATABLE READ |  |  | O (INNO DB X) |
    | SERIALIZABLE |  |  |  |
    
    MySQL은 INNO DB이므로 **REPEATABLE READ만으로 가장 엄격한 격리 수준을 제공**한다.
    

### 14. JDBC 실습 - Transaction

- `con.setAutoCommit(false)`

```sql
Connection con = DriverManager.getConnection(
"jdbc:mysql://localhost:3306/de-jdbc", "root", null);
con.setAutoCommit(false);
```

- `con.commit()` : 변경사항을 실제 DB에 적용시킨다.
- `con.rollback()` : 변경사항을 실제 DB에 적용하지 않는다.
- `Savepoint sp = con.setSavepoint()` : 세이브포인트 객체를 생성한다.
- `con.rollback(Savepoint sp)` : 변경사항을 실제 DB에 적용하지 않으며 파라미터의 위치로 DB를 적용한다.