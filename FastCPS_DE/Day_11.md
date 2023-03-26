### 8. JDBC 실습 - Statement

Statement를 이용해서 실제 수행할 쿼리를 작성할 수 있다. 수행 결과를 ResultSet 객체로 받아온다. 정적인 쿼리를 작성한다.

- 주요 메소드
    - `ResultSet executeQuery(String sql)`
        
        SQL을 수행하고 ResultSet 을 받아온다. **결과를 받아오므로 SELECT 문을 쓸 때 사용**한다.
        
    - `int executeUpdate(String sql)`
        
        INSERT, UPDATE, DELETE 또는 DDL 등 **결과를 받아오지 않는 SQL을 작성**한다.
        
        **return 값은 변경사항이 적용된 row 의 수**이다. 결과가 없으면 0이다.
        
    - `boolean execute(String sql)`
        
        여러 개의 결과를 얻는 SQL을 수행한다.
        
        **첫 번째 결과가 ResultSet 이면 true**
        
        - getResultSet() 함수를 호출해서 결과를 얻는다.
        
        첫 번째 결과가 **ResultSet이 아니면**(결과가 없거나, 결과가 업데이트 count인 경우) **false를 리턴한다.**
        
        - getUpdateCount() 를 호출해서 결과를 얻는다. -1 은 현재 값이 없거나, ResultSet 인 경우이다.
        
        첫 번째 결과를 후속 함수로 얻었으면, 그 다음 결과는 **getMoreResults() 함수**로 execute()의 리턴값과 같은 방식으로 해석한다.
        
        더 이상 가져올 결과가 없다는 것은 다음과 같이 확인한다.
        
        ```markdown
        **((stmt.getMoreResults() == false) && (stmt.getUpdateCount() == -1))**
        ```
        
    - `int[] executeBatch()`
        
        **addBatch(String sql)** 로 쌓인 **SQL을 배치로 수행한다.** 모든 커맨드가 성공하면 **update된 count 를 배열로 리턴**한다
        
    - `void addBatch(String sql)`
        
        현재 Statement 객체에 배치로 **실행할 SQL 명령어를 추가**한다. 추가만 할 뿐, 실행하지는 않는다.
        
    
    [Statement 클래스의 Javadoc](https://docs.oracle.com/javase/8/docs/api/java/sql/Statement.html)에서 다양한 메소드를 확인할 수 있다.
    

### 9. JDBC 실습 - ResultSet

- **ResultSet**
    
    ResultSet은 쿼리의 결과를 **cursor를 이용해서 다룰 수 있도록 하는 객체**이다.
    
    ResultSet은 **쿼리의 결과를 테이블 형태로 상정**하고, 특정 row(행)을 가리키고 있는 cursor를 가진다. 쿼리의 결과가 단건일수도, 여러 건일수도 있다. 결과 전체를 리스트나 배열로 주면 되지 않냐고 생각할 수도 있다. 하지만, **쿼리 결과가 많다면 그 결과를 한 번에 어플리케이션의 메모리에 모두 로드할 수 없을 수도 있기 때문**에 cursor를 사용한다.
    
    - ResultSet의 **Cursor의 사용**
        
        **cursor는 방향성이 있다.** 시작은 첫 번째 row의 이전을 가리키고 있다. **커서가 가리키는 내용은 업데이트가 불가능**하다.
        
        - 단, 설정으로 **방향을 반대**로 바꿀 수도 있고, **내용이 업데이트 가능**하게 만들 수도 있다.
            
            ```markdown
            Statement stmt = con.createStatement(**ResultSet.TYPE_SCROLL_INSENSITIVE, 
            																			ResultSet.CONCUR_UPDATABLE**);
            ```
            
    - 주요 메소드
        - `public boolean next()`
            
            cursor 를 현재보다 한 row 다음으로 보낸다.
            
        - `public boolean previous()`
            
            cursor 를 현재보다 한 row 이전으로 보낸다.
            
        - `public boolean first()`
            
            result set 의 첫번째로 cursor를 이동한다.
            
        - `public boolean last()`
            
            result set 의 마지막으로 cursor를 이동한다.
            
        - `public boolean absolute(int row)`
            
            result set 의 특정 row로 cursor를 이동한다.
            
        - `public boolean relative(int row)`
            
            현재 cursor 위치로부터 정해진 순번의 row로 cursor를 이동한다. 양,음 모두 가능
            
        - `public int getInt(int columnIndex)`
            
            현재 cursor 가 가리키고 있는 데이터 행의 주어진 column index에 해당하는 컬럼의 값을 int로 가져온다.
            
        - `public int getInt(String columnName)`
            
            현재 cursor 가 가리키고 있는 데이터 행의 주어진 column 이름에 해당하는 컬럼의 값을 int로 가져온다.
            
        - `public String getString(int columnIndex)`
            
            현재 cursor 가 가리키고 있는 데이터 행의 주어진 column index에 해당하는 컬럼의 값을 String으로 가져온다.
            
        - `public String getString(String columnName)`
            
            현재 cursor 가 가리키고 있는 데이터 행의 주어진 column 이름에 해당하는 컬럼의 값을 String으로 가져온다.
            
        - `public Blob getBlob(int columnIndex)`
            
            BLOB 은 binary (이진수) 형태의 대형 객체를 저장할 때 쓴다. 이미지, 동영상, 파일 등
            
            현재 cursor 가 가리키고 있는 데이터 행의 주어진 column index에 해당하는 컬럼의 값을 Blob으로 가져온다.
            
        - `public Blob getBlob(String columnName)`
            
            현재 cursor 가 가리키고 있는 데이터 행의 주어진 column name에 해당하는 컬럼의 값을 Blob으로 가져온다.
            
        - `public Clob getClob(int columnIndex)`
            
            CLOB 은 character (문자) 형태의 대형 객체를 저장할 때 쓴다. 대용량 텍스트/문서 파일, 대용량 파일
            
            현재 cursor 가 가리키고 있는 데이터 행의 주어진 column index에 해당하는 컬럼의 값을 Clob으로 가져온다.
            
        - `public Clob getClob(String columnName)`
            
            현재 cursor 가 가리키고 있는 데이터 행의 주어진 column name에 해당하는 컬럼의 값을 Clob으로 가져온다.
            
        
        [ResultSet 클래스의 Javadoc](https://docs.oracle.com/javase/8/docs/api/java/sql/ResultSet.html)에서 다양한 메소드를 확인할 수 있다.