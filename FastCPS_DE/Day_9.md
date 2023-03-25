### 2. SQL 기초 - DML

SQL은 RDBMS 종류의 데이터베이스 뿐만 아니라, NoSQL, 빅데이터용 도구들에서도 지원하기 때문에 기본적인 사용법은 알고 있어야 한다.

```
💡 SQL 문법의 표준

ANSI SQL을 표준 SQL이라고 한다. DB의 종류마다 ANSI의 규칙의 일부를 지키지 않는 것도 있지만, 사실상 ANSI SQL에 있는 것은 최소한을 지키고 구현해야하는 것으로 자리잡았다.

```

- Create(Insert)
    
    INSERT 문을 이용해서 테이블에 새로운 row 를 추가할 수 있다. 입력하고 싶은 데이터를 column 과 column별로 들어갈 값을 각각 명시 해야한다.
    
    ```markdown
    INSERT INTO table_name (column1, column2, column3, ...)
    VALUES (value1, value2, value3, ...);
    
    INSERT INTO table_name VALUES (value1, value2, value3, ...);
    ```
    
    column의 선언 순서와 동일하고, 모든 column의 값을 명시한다면 column을 명시하지 않아도 되지만, 휴먼에러 또는 DDL을 통해서 테이블 스키마가 변경되었을 수도 있으므로 이 방법은 권장하지 않는다. column을 항상 명시하는 습관을 들이자.
    
- Read(Select)
    
    SELECT 문을 이용해서 테이블에서 원하는 row와 column을 가져올 수 있다. *표시로 모든 컬럼을 가져올 수 있고, 원하는 컬럼을 직접 명시해서 필요한 컬럼만 가져올 수 있다. row 는 조건절(where, limit 등)로 구분한다.
    
    ```markdown
    SELECT * from table_name;
    
    -- 2022.08.01 00시~01시 사이
    SELECT * from product where updated_at between 1659279600 and 1659283200;
    ```
    
- Update
    
    테이블에 이미 존재하는 row를 조건절로 찾아서, column의 값을 변경할 수 있다. Where 조건절에 해당하는 row가 모두 변경되니, 원하지 않는 row의 데이터가 바뀌지 않도록 조건절을 잘 사용해야한다.
    
    ```markdown
    UPDATE table_name
    SET column1 = value1, column2 = value2, ...
    WHERE condition;
    -- 실습
    UPDATE product SET `price` = `price`-1000 where `name` like 'shoes%'
    ```
    
    Workbench에서는 **unique 한 key 가 where 절에 오지 않는 경우 업데이트를 막고 있다**. 다음 명령어로 제한을 해제할 수 있다.
    
    ```markdown
    SET SQL_SAFE_UPDATES=0;
    ```
    
- Delete
    
    테이블에 이미 존재하는 row를 조건절로 찾아서 삭제한다. Where 조건절에 해당하는 row가 모두 삭제되니, 원하지 않는 row의 데이터가 삭제되지 않도록 조건절을 잘 사용해야한다.
    
    ```markdown
    DELETE FROM table_name WHERE condition;
    -- 실습
    DELETE FROM product WHERE `price` > 200000;
    ```
    

### 3. SQL 기초 - DDL

- **Create Table**
    
    테이블을 생성할 수 있는 명령어이다. 테이블은 이름이 해당 데이터베이스 내에서 유일해야한다.
    
    ```markdown
    CREATE TABLE table_name (
    column1 datatype,
    column2 datatype,
    column3 datatype,
    ....
    );
    -- Constraint로 단일 컬럼을 PK 지정
    CREATE TABLE table_name (
    column1 datatype not null,
    column2 datatype,
    column3 datatype,
    PRIMARY KEY (column1)
    );
    -- Constraint로 컬럼의 조합을 PK 지정
    CREATE TABLE table_name (
    column1 datatype not null,
    column2 datatype not null,
    column3 datatype,
    Constraint PK_table PRIMARY KEY (column1, column2)
    );
    -- Constraint로 FK 지정
    CREATE TABLE other_table (
    other_id datatype not null primary key,
    )
    CREATE TABLE table_name (
    column1 datatype not null,
    column2 datatype not null,
    this_column datatype,
    Foreign Key (this_column) references other_table(other_id)
    );
    
    -- 실습
    CREATE TABLE `review` (
    `id` int NOT NULL,
    `content` varchar(2048) DEFAULT NULL,
    `user_id` int DEFAULT NULL,
    `product_id` int unsigned NOT NULL,
    PRIMARY KEY (`id`),
    FOREIGN KEY (`product_id`) REFERENCES `product` (`id`)
    );
    ```
    
- **Alter Table**
    
    이미 선언되어있는 테이블의 내용의 스키마를 변경할 때 사용한다. 주로 column을 추가,삭제, 변경할 때 사용한다.
    
    ```markdown
    -- 속성 추가
    ALTER TABLE table_name
    ADD column_name datatype;
    -- 속성 제거
    ALTER TABLE table_name
    DROP COLUMN column_name;
    -- 속성 변경
    ALTER TABLE table_name
    MODIFY COLUMN column_name datatype;
    ```
    
- **Drop Table**
    
    테이블을 삭제할 때 사용한다.
    
    ```markdown
    DROP TABLE table_name;
    ```
    
- **DDL 사용시 주의점**
    
    DDL은 테이블, 데이터베이스의 주요 속성을 변경한다. 영향도를 고려하지 않고 동작시킬 경우, **시스템이나 client 에게 문제**를 일으킬 수 있다. 이 때문에 **DDL은 신중하게 사용**하고, 가능하다면 **시스템적으로 원하지 않거나, 문제를 일으킬만한 DDL이 발생하지 않도록 하는 것이 중요**하다.
    DB를 관리하는 인프라가 구축되어있는 기업이나, managed DB를 서비스하는 업체의 솔루션에는 이런 **DDL을 기능, 권한을 제한**하고, **잘못된경우 되돌릴 수 있는 기능들을 구축**해서 **사고를 방지**한다. 아무튼 DDL은 주의해서 사용해야한다. 걱정 없이 사용할 수 있는 **DDL은 Alter Table > add column 정도**이다.

### 4. Foreign Key에 대한 제약 설정

내가 참조하고 있는 테이블에서 해당 row 가 없어지면, 그것을 참조하고 있던 테이블의 컬럼들은 어떻게 처리해야할까? 프로그래밍 언어를 이용해서 코딩한다면, 이런 처리를 할 수 있을 것이다. 하지만 SQL만 이용한다면 어떻게 할 수 있을까? 이것을 지원하기위한 기능이 있다.

ON UPDATE/ON DELETE constraint는 Foreign Key 로 참조되고 있는 원본 테이블에서 변경(Update)/삭제(Delete)가 일어날 때, 그것을 참조하고 있는 테이블에서 어떤 동작이 일어나도록 하는 설정이다.

SQL 표준에서는 ON UPDATE/ON DELETE 동작에 대한 스펙을 명시하고 있다. 다만, 내가 사용하는 DB에서 어떤 기능들을 지원하는지, 어떤 문법으로 지원하는지는 추가로 확인해야한다. 표준 스펙과 기능이 다를 수 있다.

- **MySQL Referential Action**
    - `ON DELETE/UPDATE CASCADE` : 부모 테이블(참조대상)의 row가 지워지면, 그것을 참조하고 있는 자식 테이블의 row도 **함께 지워진다/업데이트 된다.**
    - `ON DELETE/UPDATE SET NULL` : 부모 테이블(참조대상)의 row가 지워지면/업데이트 되면, 그것을 참조하고 있는 자식 테이블의 **해당 row의 참조 컬럼의 값을 null로 바꿔준다**. **참조 컬럼이nullable 이어야한다.**
    - `ON DELETE/UPDATE SET DEFAULT` : 부모 테이블(참조대상)의 row가 지워지면/업데이트되면, 그것을 참조하고 있는 자식 테이블의 **해당 row의 참조 컬럼의 값을 default 값으로 바꿔준다.** 참조 컬럼에 default 값 설정이 있어야 한다. **MySQL의 InnoDB, NDB에서 사용 불가능**하다. 사실상 못쓴다고 봐야한다.
    - `ON DELETE/UPDATE RESTRICT` : 다른 테이블에 참조하고 있는 곳이 있다면 **부모 테이블(참조대상)의 row를 지울 수 없다/업데이트할 수 없다.** **표준에서는 commit 시점까지의 판단 지연을 명시**하지만, MySQL은 해당 스펙으로는 동작하지않는다. transaction 시작 이전에 자식 테이블의 row들이 지워져있어야 한다.
    - `ON DELETE/UPDATE NO ACTION` (the default): 아무 설정을 하지 않으면, 이 설정으로 동작한다. **MySQL 에서는 Restrict 와 같다**. **표준에서는 RESTRICT와 NO ACTION은 다른 스펙**으로 명시하고 있다.