### 12. JDBC 실습 - CallableStatement

- **Stored Procedure, Function**
    
    DB에는 SQL 말고도 stored procedure 또는 function이 있다. 이것들은 다음과 같은 경우에 사용한다.
    
    - SQL은 아닌데 **자주 사용하는 여러 동작의 세트**
    - SQL로 한다면 여러번 I/O를 해야하는데, **한 번에 DB에서 모두 처리한 뒤 최종 결과만 빨리 받고 싶을 때**
        - 보통 Application 서버보다 DB 서버의 스펙이 월등히 좋으므로.
    
    Function은 그 **자체로도 호출**할 수 있지만, **SQL문 내에서도 호출**할 수 있다는 점이 Stored procedure와의 차이점이다.
    
    Function의 사례
    
    - **복잡한 수학적 연산을 자동화**하는 것을 Function으로 만들어 놓고 재사용한다.
    - **문자열 변환**, 이미 **입력된 데이터의 인코딩 오류 해결** 등을 Function으로 만들어 놓고 재사용한다.
    
    Stored Procedure의 사례
    
    - 여러 SQL문으로 수행되어야하는 데이터 집계
    - 복제 테이블을 만들거나 유효 기간이 지난 데이터를 삭제하는 등의 작업을 자동화 하고 싶을때
    - DBA가 DB를 관리하기 위한 기능(용량 모니터링, 감사 자료 추출 등)을 의미 단위로 만들어 놓고 재사용하고 싶을 때
    
     JDBC에서는 이런 Stored Procedure 또는 Function은 CallableStatement 클래스를 이용해 다룬다.
    
    - **PROCEDURE 정의하기**
        
        ```sql
        DELIMITER //
        CREATE PROCEDURE discount_price(IN _id int unsigned, IN percent int, OUT discounted_price int)
        BEGIN
        	update product set price = (price - (price * (percent/100))) where `id` = _id;
        	select price into discounted_price from product where `id` = _id;
        END //
        DELIMITER ;
        ```
        
    - **PROCEDURE 호출하기**
        
        ```sql
        call discount_price(1, 10, @discounted_price);
        select @discounted_price;
        ```
        
    - **CallableStatement로 procedure 호출하기**
        1. `Connection.prepareCall(String statement)` : CallableStatement를 만든다. 파라미터는 ?로 처리한다.
        2. `CallalbleStatement` 를 사용하는 방법은 PreparedStatement를 사용하는 방법과 같은 방식으로 index/label 별로 타입에 맞는 값을 세팅할 수 있다.
        3. 단, **out parameter**는 `CallalbleStatement.registerOutParameter(int index 또는 String label, java.sql.Type type)` 로 세팅해야한다.
        4. `execute()` 함수로 실행한다.
        5. 결과는 `excute()` 함수를 해석하는 방식과 같다.
        6. 단, **out parameter**는 CallalbleStatement 객체에 바로 **getXXX 함수**를 통해서 얻을 수 있다.
    
    - **Function 정의하기**
        
        ```sql
        CREATE FUNCTION add_event_prefix (s CHAR(20))
        RETURNS CHAR(50) DETERMINISTIC
        	RETURN CONCAT('[특별 할인 이벤트] , ',s);
        ```
        
    - **FUNCTION 호출하기**
        
        ```sql
        SELECT `id`, add_event_prefix(`name`) as `name`, `price` from product where id = 1;
        ```
        
    - **CallableStatement로 Function 호출하기**
        
        Function은 **CallableStatemnet를 이용해서 호출할 수도 있고**, 다른 query statement 객체의 **SQL 문에서 곧바로 사용할 수도 있다.**
        
        CallableStatement를 이용하는 방식의 위 **Procedure Call 할 때 사용한 방식과 같다.**