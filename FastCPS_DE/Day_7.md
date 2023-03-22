# 데이터 엔지니어링(패스트 캠퍼스)

# Part4. Server(Backend) Engineering 기초

## Ch 01. 백엔드 엔지니어 되어보기 - 강의소개

### 1. MySQL 설치, MySQL CLI

- MySQL은 윈도우, 리눅스, 맥 모든 버전을 지원한다. 간단한 실습의 경우에는 개인 컴퓨터
에 설치하고 사용하는 것이 비용이나 편의성에서 더 좋다. 로컬이 아니어도 cloud에서 제공
하는 MySQL을 써도 되고, AWS상의 Linux 서버에 설치해도 된다.

- MySQL을 접속해서 활용하는 가장 간단한 방법은 CLI를 이용하는 것이다.
MySQL Client 프로그램을 통해서 MySQL 서버에 접속할 수 있다.
기본 mysql 명령어로 접근할 수 있다.

```markdown
mysql --host=localhost --user=myname --password=password mydb
```

- mysql에서 table, column, schema 같은 유니크한 대상을 지칭할 때 `~`로 묶어서 사용하곤 한다. Backquote 백쿼트라고 부른다.

### 2. MySQL Workbench

RDBMS의 데이터는 테이블 형태로 보는것이 가장 좋다. 이를 위한 GUI 툴이 있다.
Workbench 는 무료로 쓸 수 있는 대표적인 MySQL GUI Client이다. 단순히 visualize 용
도 뿐만 아니라 SQL 추출, 성능 분석, ERD diagram 등 데이터 모델링, RDBMS 관리 등에
편한 기능들을 제공한다

1. DB 서버를 연결해준다.
2. 스키마를 만들어준다.
3. 테이블들을 만든다.
4. row를 추가한다.

### 3. MongoDB 실습 세팅

- **MongoDB**
- **MongoDB Shell**
    
    Command Line Interface 로 MongoDB 와의 상호작용할 수 있는 도구이다. Javascript로 만들어졌다.
    
    - mongosh로 **MongoDB 접속**하기
        
        아래 명령어에 자신이 띄운 MongoDB 서버의 host 주소, port 를 입력하면 된다. 자신의 local에 기본 설정으로 설치한 경우는 mongosh 명령어만 수행해도 접속이 된다.
        
        ```
        mongosh "mongodb://$host:$port"
        ```
        
        그 외의 connection 옵션들
        
        - -username: 접속하는 user name을 입력
        - -authenticationDatabase: 해당 user 가 권한을 가지고 있는 데이터베이스로 접속
        - —password: user 의 password 를 parameter로 입력
        
        접속한 뒤 db.getMongo() 명령어로 접속이 제대로 되었는지 확인한다.
        
        연결을 끊는 방법은 아래 방법들이 있다
        
        - `.exit` , `exit` , or `exit()` .
        - Type `quit` or `quit()` .
        - Press `Ctrl + D` .
        - Press `Ctrl + C` .
    - mongosh로 **DB 생성**하기
        
        `use` 명령어로 이미 존재하는 database에 접속할 수도, 새로운 이름의 database를 생성할
        수도 있다.
        
        ```
        use $databasename
        ```
        
    - mongosh로 **Collection 생성**하기
        
        같은 종류의 데이터(document)의 묶음을 collection 이라고 한다. 보통 scheme 가 같은 document를 지칭하기 위해서 사용한다. RDBMS에서 테이블과 유사하다고 생각하면 된다.
        
        Collection을 생성하는 방법은 원하는 collection 이름에 데이터를 하나 입력하면 자동으로 생성된다.
        
        ```
        db.myCollection.insertOne( { x: 1 } );
        ```
        
    - mongosh로 **query하기**
        
        mongosh는 javascript로 만들어졌기 때문에 사실상 MongoDB의 javascript client driver에 있는 함수로 query를 한다
        
        대표적인 CRUD는 MongoDB의 드라이버의 함수로 수행할 수 있다. query 함수에 대한 자세한 내용은 MongoDB 강의에서 다룬다.
        
        - 데이터 생성하기
            
            ```
            db.movies.insertOne(
            	{
            		title: "The Favourite",
            		genres: [ "Drama", "History" ],
            		runtime: 121,
            		rated: "R",
            		year: 2018,
            		directors: [ "Yorgos Lanthimos" ],
            		cast: [ "Olivia Colman", "Emma Stone", "Rachel Weisz" ],
            		type: "movie"
            	}
            )
            
            db.movies.insertMany([
            	{
            		title: "Jurassic World: Fallen Kingdom",
            		genres: [ "Action", "Sci-Fi" ],
            		runtime: 130,
            		rated: "PG-13",
            		year: 2018,
            		directors: [ "J. A. Bayona" ],
            		cast: [ "Chris Pratt", "Bryce Dallas Howard", "Rafe Spall" ],
            		type: "movie"
            	},
            	{
            		title: "Tag",
            		genres: [ "Comedy", "Action" ],
            		runtime: 105,
            		rated: "R",
            		year: 2018,
            		directors: [ "Jeff Tomsic" ],
            		cast: [ "Annabelle Wallis", "Jeremy Renner", "Jon Hamm" ],
            		type: "movie"
            	}
            ])
            ```
            
        - 데이터 가져오기
            
            ```
            db.movies.find()
            ```
            
        - 데이터 업데이트 하기
            
            ```
            db.movies.updateOne( { title: "Tag" },
            {
            	$set: {
            		plot: "One month every year, five highly competitive friends" +
            					"hit the ground running for a no-holds-barred game of tag"
            	},
            	$currentDate: { lastUpdated: true }
            })
            ```
            
        - 데이터 삭제하기
            
            ```
            db.movies.deleteMany({})
            ```
            

- **Studio-3T**
    
    MongoDB 전용 GUI Client 이다. 30일 체험 후에 무료버전의 제한된 기능으로 계속해서 쓸 수 있다. 시각화 용도로는 무료로도 충분하다.
    
    - Studio-3T로 **MongoDB 접속하기**
        
        기능을 이용하기 위해서는 먼저 MongoDB에 접속할 접속 정보를 입력해야한다. Manually configure를 선택하고, 다음 선택 창에서 접속 정보를 입력한다.
        
        **Connection name, server, port 정보를 가장 기본으로 입력**한다. **원격 서버인 경우, Authentification, SSL, SSH 등의 설정에서 해당하는 항목을 입력하고 접속**한다.
        
        Test Connection의 결과가 성공이면, 접속할 준비가 되었다. Save를 누르고 다음부터는 저장된 접속 정보로 접속한다.
        
    - Studio-3T에서 **DB 생성하기**
        
        좌측 네비게이터에서 Connection 에 오른쪽 마우스를 누르고 Add Database를 누르고 원하는 이름을 입력하면 생성된다. 데이터베이스는 collection, view 의 묶음 단위, user의 접속 인증의 기본 단위이다.
        
    - Studio-3T에서 **Collection 생성하기**
        
        원하는 DB의 Collections 폴더에 오른쪽 마우스를 누르고 Add Collection을 누른다.
        
        Collection의 이름을 가장 기본으로 설정한다.
        이름외에도 원하는 옵션을 각 설정에 맞게 선택해서 설정할 수 있다. 한국어 지원을 위해서는 Collation > Locale > ko - Korean 옵션을 선택해준다.
        
        생성된 Collection에 오른쪽 마우스를 누르면, collection의 이름 변경, 복사, 데이터 삭제, collection 삭제 등을 할 수 있다.
        
    - Studio-3T에서 **Query 하기**
        
        Collection 을 선택한 뒤, Visual Builder 를 선택하면, Visual Builder를 통해서 조회 쿼리를 작성할 수 있다. GUI를 통해서 직관적으로 작성할 수 있다. MongoDB의 query가 익숙하지 않다면, visual builder를 이용해서 query가 작성되는 방식을 익히면 도움이 된다.
        
        이미 MongoDB 의 함수와 쿼리에 익숙한 사람은 바로 IntelliShell 을 통해서 자동완성 기능을 이용해서 query를 작성하는 것이 더 편할 수 있다.