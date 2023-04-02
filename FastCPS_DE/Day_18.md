### 3. MongoDB Operations

- 실습 세팅
    - **의존성 추가**
        
        프로젝트를 새로 만들고, build.gradle 에 다음 의존성을 추가해준다.
        
        ```
        dependencies {
        	implementation 'org.mongodb:mongodb-driver-sync:4.7.1'
        	compileOnly 'org.projectlombok:lombok:1.18.24'
        	annotationProcessor 'org.projectlombok:lombok:1.18.24'
        }
        ```
        
    - **Connection 연결**
        
        다음과 같이 try-with-resource 구문으로 MongoClient 객체를 생성한다
        
        ```
        String uri = "mongodb://localhost:27017" // type your uri with configurations
        try (MongoClient mongoClient = MongoClients.create(uri)) {
        }
        ```
        
    - **기본 클래스들**
        
        ```
        try (MongoClient mongoClient = MongoClients.create(uri)) {
        	MongoDatabase database = mongoClient.getDatabase("test");
        	MongoCollection<Document> collection = database.getCollection("movies");
        	Document doc = collection.find(eq("title", "The Favourite")).first();
        	System.out.println(doc.toJson());
        }
        ```
        
        - `MongoDatabase` : 데이터베이스를 가리키는 객체
        - `MongoCollection<T>` : T의 타입의 Document를 가지는 Collection
        - Document : 모든 Document를 담을 수 있는 기본 클래스, Map 인터페이스를 구현하므로 key-value에 대해서 Map처럼 활용할 수 있다.
        
        **MongoDB와 operation은 주로 기본 함수와 JSON 형식의 메세지**로 한다. 하지만 Java 언어의 특성상 **타입시스템을 이용해서 더 안전하게 프로그래밍**을 할 수 있다. 본 실습에서는 **Java의 타입시스템을 적극 활용**하는 방식을 사용한다.
        

- **POJO Model**
    
    MongoDB를 쓰는 가장 큰 이유는 **객체지향 프로그래밍 모델을 Document에 그대로 사용할 수 있다는 장점** 때문이다. JDBC에서 ORM 을 따로 쓰는 것처럼 복잡한 설정 필요 없이 간단하게 **POJO class를 Collection의 Document에 매핑**할 수 있다.
    
    ```java
    import java.time.LocalDateTime;
    import org.bson.codecs.pojo.annotations.BsonId;
    import org.bson.codecs.pojo.annotations.BsonProperty;
    import org.bson.types.ObjectId;
    import lombok.AllArgsConstructor;
    import lombok.Getter;
    import lombok.NoArgsConstructor;
    import lombok.Setter;
    import lombok.ToString;
    @AllArgsConstructor
    @NoArgsConstructor
    @Getter
    @Setter
    @ToString
    public class Product {
    	@BsonId
    	ObjectId id;
    	String name;
    	@BsonProperty("updated_at")
    	LocalDateTime updatedAt;
    	String contents;
    	int price;
    }
    ```
    
    - `@BsonId` : **_id 에 매핑되는 필드**에 달아준다.
    - `@BsonProperty` : MongoDB에 **저장되는 field 이름과 실제 Java 의 변수 이름이 다른 경우**에 **DB에서 사용하는 이름을 따로 명시**해준다.
    - MongoDB의 client에서 POJO Mapping을 자동으로 해주기 위해서 다음 annotation 설정이 필요하다. 실제로 코드를 짜려면 복잡하지만, lombok annotation으로 자동으로 코드가 생성되도록 한다.
        
        ```java
        @AllArgsConstructor // 모든 인자를 가지는 생성자 자동생성 annotation
        @NoArgsConstructor  // 아무 인자도 가지지 않는 생성자 자동생성 annotation
        @Getter             // 각 인자별 get메소드 자동 생성 annotation
        @Setter             // 각 인자별 set메소드 자동 생성 annotation
        @ToString           // 각 인자들을 출력해주는 메소드 자동 생성 annotation
        ```
        
- **Create(insert)**
    
    ```java
    public static void main(String[] args) {
    	CodecProvider pojoCodecProvider = PojoCodecProvider.builder().automatic(true).build();
    	CodecRegistry pojoCodecRegistry = fromRegistries(getDefaultCodecRegistry(),
    	fromProviders(pojoCodecProvider));
    	// Replace the uri string with your MongoDB deployment's connection string
    	String uri = "mongodb://localhost:27017";
    	MongoClient mongoClient = MongoClients.create(uri);
    	MongoDatabase database = mongoClient.getDatabase("de-mongodb").withCodecRegistry(pojoCodecRegistry);
    	MongoCollection<Product> productCollection = database.getCollection("product", Product.class);
    	DateTimeFormatter formatter = DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss");
    	List<Product> products = new ArrayList<>();
    	products.add(new Product(null, "shoes1", LocalDateTime.parse("2022-08-01 01:00:00", formatter),
    	"This is shoes1", 10000));
    	products.add(new Product(null, "shoes2", LocalDateTime.parse("2022-08-01 02:00:00", formatter),
    	"This is shoes2", 20000));
    	products.add(new Product(null, "shoes3", LocalDateTime.parse("2022-08-01 03:00:00", formatter),
    	"This is shoes3", 30000));
    	products.add(new Product(null, "shoes4", LocalDateTime.parse("2022-08-01 04:00:00", formatter),
    	"This is shoes4", 40000));
    	products.add(new Product(null, "shoes5", LocalDateTime.parse("2022-08-01 05:00:00", formatter),
    	"This is shoes5", 50000));
    	products.add(new Product(null, "shoes6", LocalDateTime.parse("2022-08-01 06:00:00", formatter),
    	"This is shoes6", 60000));
    	products.add(new Product(null, "backpack", LocalDateTime.parse("2022-08-02 04:00:00", formatter),
    	"This is backpack", 50000));
    	products.add(new Product(null, "shirt", LocalDateTime.parse("2022-08-03 05:00:00", formatter),
    	"This is shirt", 20000));
    	products.add(new Product(null, "glasses", LocalDateTime.parse("2022-08-04 06:00:00", formatter),
    	"This is glasses", 10000));
    	productCollection.insertMany(products);
    }
    ```
    
    collection 객체에 `insertOne` 또는 `insertMany` 함수에 객체를 통채로 넘겨준다.
    
    이것이 가능하려면 먼저 POJO를 해석할 수 있는 Codec이 등록 돼있어야한다.
    
- **Read(find)**
    
    `find()` 함수로 검색을 할 수 있다. 검색 결과는 Mongoiterator인데, JDBC와 유사하게 커서 방식으로 데이터를 확인한다.
    
    ```java
    MongoCursor<Product> cursor = productCollection.find().cursor();
    while (cursor.hasNext()) {
    System.out.println(cursor.next());
    }
    ```
    
    **com.mongodb.client.model.Filters.*** 의 패키지에 있는 필터들을 통해 조회 조건을 타입 안정성과 함께 걸 수 있다.
    
    ```java
    import static com.mongodb.client.model.Filters.eq
    import static com.mongodb.client.model.Filters.regex;
    MongoCursor<Product> cursor = productCollection.find(eq("price", 10000)).cursor();
    MongoCursor<Product> cursor = productCollection.find(regex("name", "shoes")).cursor();
    ```
    
    find 의 결과에 `sort()` 함수를 **chaining 해서 정렬**을 할 수 있다.
    
    정렬의 종류는 **com.mongodb.client.model.Sorts** 클래스에 정적 함수로 있다.
    
    ```java
    import static com.mongodb.client.model.Sorts.descending;
    MongoCursor<Product> cursor = productCollection.find(**regex("name", "shoes"))
    																										.sort(descending("price"))
    																										.cursor();**
    ```
    
    find의 결과에 `projection()` **함수를 chaining** 해서 원하는 필드만 가져올 수 있다.
    
    Projection의 종류는 **import static com.mongodb.client.model.Projections 클래스**에 정적 함수로 있다.
    다만, **POJO mapping을 하는 경우 POJO class에 있는 필드는 exclude가 안된다**. **slice 역시 POJO class 형식과 다르면 안된다.**
    단순히 메타데이터를 가져올 때는 **POJO로 그대로 매핑하는 것이 좋지만**, **aggregation등의 연산을 할 때는 Projection으로 필요한 데이터만 사용해서 연산하는 것이 성능에 좋다**.
    
    ```java
    MongoCursor<Product> cursor = productCollection.find(regex("name", "shoes"))
    																								.**projection(fields(include("name", "price")
    																								))**
    																								.sort(descending("price"))
    																								.cursor();
    ```
    
- **Update**
    
    업데이트는 **업데이트 대상을 고르는 filter**, 그리고 **업데이트할 내용인 update**, **두 종류의 BSON parameter를 이용**해서 update한다.
    조건은 `fields method` **로 여러개를 이어 붙일 수 있다**.
    **update는 set, unset, set on insert, increment, multiply, rename, min, max, current date** 등 타입 안정성을 제공하는 전용 함수들이 많다. [document](https://www.mongodb.com/docs/drivers/java/sync/v4.3/fundamentals/builders/updates/)를 보고 원하는 함수를 찾아서 사용한다.
    
    ```java
    UpdateResult updateResult =
    	productCollection.updateMany(**fields**(regex("name", "shoes"), // filter shoes
    																			gt("price", 10000)), // filter price > 10000
    																			mul("price", 0.9) // 10% discount
    																			);
    if (updateResult.wasAcknowledged()) {
    	System.out.println("modified: " + updateResult.getModifiedCount());
    }
    ```
    
- **Delete**
    
    삭제는 **filter 조건만 넣으면 삭제**가 된다.
    **연관된 document가 있는 경우 cascading 옵션이 없으므로** 삭제시 **참조하는 데이터를 어떻게 처리할지를 고민**해서 **자동화할 수 있도록 해야한다.**
    
    ```java
    DeleteResult deleteResult =
    	productCollection.deleteMany(fields(regex("name", "shoes"), // filter shoes
    																			gte("price", 10000),
    																			lt("price", 20000)) // filter 10000 <= price < 20000
    	);
    if (deleteResult.wasAcknowledged()) {
    	System.out.println("deleted: " + deleteResult.getDeletedCount());
    }
    ```
    

- **Aggregation**
    
    MongoDB 에서 집계를 위한 연산을 **Aggregation Pipeline 기능**을 통해서 할 수 있다.
    Aggregation 에서 사용하는 대표적인 기능은 다음 3종류이다.
    
    1. `$match` : 원하는 조건에 맞는 document 만 고른다. **SQL의 WHERE 조건절**이라고 생각하면 된다.
    2. `$group` : 어느 단위로 묶어서 집계를 할지 정한다. **SQL의 group by** 라고 생각하면 된다.
    3. `$sort` , `$limit` , `$count` : 집계 결과에 대해서 한정한다.
    
    ```java
    MongoCursor<Document> cursor = productCollection.aggregate(
    	Arrays.asList(
    		Aggregates.match(gt("price", 10000)),
    		Aggregates.group("$name", Accumulators.avg("avg_price", "$price")),
    		Aggregates.sort(descending("avg_price"))
    	)
    ).iterator();
    while (cursor.hasNext()) {
    	System.out.println(cursor.next());
    }
    ```
    
    - 집계를 하면 집계 결과의 **Document 가 새로 생성**이 된다.
        - 이 예제 에서는 **“name”필드를 사용하고, “avg_price” 라는 필드가 추가**되었다.
    - 따라서 Collection의 원래 자료구조를 나타내는 **POJO 클래스를 이용해서 생성한 Generic 타입인 MongoCollection<Product>을 사용하면 집계 결과 Document를 가져올 수 없다.**
    - 따라서 이 경우에는 **원본 Collection의 Generic에 POJO클래스를 매핑할 수 없다**. MongoDB의 **Document 클래스를 이용**해서 **필드 이름을 String으로** 다룰 수 밖에 없다.

- **Tranaction**
    - Transaction을 사용하기 위한 세팅
        
        자신이 설치한 mongodb의 **config 에서 다음 설정을 세팅**하고 **mongodb를 재시작**한다. 
        
        - 운영체제별 config file 위치는 다음과 같다.
        [https://www.mongodb.com/docs/manual/reference/configuration-options/](https://www.mongodb.com/docs/manual/reference/configuration-options/) replication:
            
            ```
            replication:
            	oplogSizeMB: 2000
            	replSetName: rs0
            	enableMajorityReadConcern: true
            ```
            
            - replSetName 은 원하는 이름으로 아무거나 지어도 된다.
        
        프로세스를 재시작 한 뒤, mongosh 에 접속해서 다음 명령어를 실행한다.
        
        ```
        mongosh
        ```
        
        ```
        rs.initiate()
        ```
        
        이후 find 명령어로 데이터가 잘 가져와지는지 확인한다.
        
        ```
        use de-mongodb
        db.products.find()
        ```
        
    - Studio3T 에서는 **Connection 설정을 변경**해야 접속할 수 있다
        - **Connection Type: Replica Se**t
        - **Replicat Set Name** : 위 conf 파일에서 **변경해준 replSetName 값을 입력**한다.
    - J**ava 코드로 Connection 을 맺는 uri**에도 **replicaSet 설정을 query string 형식으로 추가**해야한다.
        
        ```java
        String uri = "mongodb://localhost:27017/?replicaSet=rs0";
        MongoClient mongoClient = MongoClients.create(uri);
        ```
        
    - **Atomic Operation in MongoDB**
        
        MongoDB에서는 기본적으로 **Document 단위의 Atomic Operation을 제공**한다.
        여러 개의 Document를 삽입/수정하는 Operation에 대해서도 **Operation 단위가 아니라Document 단위의 Atomic을 제공**한다.
        
        - 주의! **insertMany , updateMany , deleteMany 등의 Operator 는, Operator는 하나**이지만, **개별 Document 단위로 Atomic operation이 수행**된다.
        
        조회와 수정에 대해서 Atomic 을 제공하기 위해서 **findAndModify operator를 제공**한다.
        
        - **SQL의 select for update** 와 기능이 유사하다.
    
    - **Transaction in MongoDB**
        
        개별 Document 단위의 **Atomic으로 부족하다면, Transaction을 이용**할 수 있다.
        
        Transaction, Session의 개념은 RDBMS와 동일하다.
        
        1. **Client Session 생성 / 종료**
            
            ```java
            ClientSession clientSession = mongoClient.startSession(); // default
            // mongoClient.startSession(ClientSessionOptions.builder().snapshot(false).causallyConsistent(false).build()); // ClientSession option
            clientSession.close();
            ```
            
        2. TransactionOption 을 객체로 생성
            
            ```java
            TransactionOptions transactionOptions = TransactionOptions.builder()
            	.readPreference(ReadPreference.primary())
            	.readConcern(ReadConcern.LOCAL)
            	.writeConcern(WriteConcern.MAJORITY)
            	.build();
            ```
            
        3. Transaction의 명령어를 객체로 생성해서 실행
            
            ```java
            CodecProvider pojoCodecProvider = PojoCodecProvider.builder().automatic(true).build();
            CodecRegistry codecRegistry = fromRegistries(getDefaultCodecRegistry(),
            																						fromProviders(pojoCodecProvider));
            String uri = "mongodb://localhost:27017/?replicaSet=rs0";
            MongoClient mongoClient = MongoClients.create(uri);
            MongoDatabase mongoDatabase = mongoClient.getDatabase("de-mongodb").withCodecRegistry(codecRegistry);
            ClientSession clientSession = mongoClient.startSession();
            TransactionOptions transactionOptions = TransactionOptions.builder()
            																			.readPreference(ReadPreference.primary())
            																			.readConcern(ReadConcern.LOCAL)
            																			.writeConcern(WriteConcern.MAJORITY)
            																			.build();
            TransactionBody transactionBody = () -> {
            	clientSession.startTransaction(transactionOptions);
            	MongoCollection<Document> coll1 = mongoDatabase.getCollection("foo");
            	MongoCollection<Document> coll2 = mongoDatabase.getCollection("bar");
            	Map<String, Object> input1 = new HashMap<>();
            	int id = new Random().nextInt();
            	int value = new Random().nextInt();
            	System.out.println("Test input: " + id + " : " + value);
            	input1.put("_id", id);
            	input1.put("field", value);
            	Map<String, Object> input2 = new HashMap<>();
            	input2.put("_id", id + 1);
            	input2.put("field", value + 1);
            	coll1.insertOne(clientSession, new Document(input1));
            	coll1.insertOne(clientSession, new Document(input2));
            	coll2.insertOne(clientSession, new Document(input1));
            	coll1.insertOne(clientSession, new Document(input1));
            	return "inserted into collection in different databases";
            };
            clientSession.withTransaction(transactionBody, transactionOptions);
            ```
            
            - `ClientSession.withTransaction` 에 transaction의 내용과 option 을 파라미터로 전달.
        4. **Transaction 을 명령어로 시작**
            
            ```java
            CodecProvider pojoCodecProvider = PojoCodecProvider.builder().automatic(true).build();
            CodecRegistry codecRegistry = fromRegistries(getDefaultCodecRegistry(),
            																						fromProviders(pojoCodecProvider));
            String uri = "mongodb://localhost:27017/?replicaSet=rs0";
            MongoClient mongoClient = MongoClients.create(uri);
            MongoDatabase mongoDatabase = mongoClient.getDatabase("de-mongodb").withCodecRegistry(codecRegistry);
            ClientSession clientSession = mongoClient.startSession();
            TransactionOptions transactionOptions = TransactionOptions.builder()
            																				.readPreference(ReadPreference.primary())
            																				.readConcern(ReadConcern.LOCAL)
            																				.writeConcern(WriteConcern.MAJORITY)
            																				.build();
            clientSession.startTransaction(transactionOptions); // start
            MongoCollection<Document> coll1 = mongoDatabase.getCollection("foo");
            MongoCollection<Document> coll2 = mongoDatabase.getCollection("bar");
            Map<String, Object> input1 = new HashMap<>();
            int id = new Random().nextInt();
            int value = new Random().nextInt();
            System.out.println("Test input: " + id + " : " + value);
            input1.put("_id", id);
            input1.put("field", value);
            Map<String, Object> input2 = new HashMap<>();
            input2.put("_id", id + 1);
            input2.put("field", value + 1);
            coll1.insertOne(clientSession, new Document(input1));
            coll1.insertOne(clientSession, new Document(input2));
            coll2.insertOne(clientSession, new Document(input1));
            // clientSession.startTransaction(transactionOptions); // duplicate
            clientSession.commitTransaction(); // commit & end
            ```
            
            1. **4 방법으로 Transaction을 시작한 경우, 명시적으로 rollback(abort)를 할 수 있다.**
            
            ```java
            CodecProvider pojoCodecProvider = PojoCodecProvider.builder().automatic(true).build();
            CodecRegistry codecRegistry = fromRegistries(getDefaultCodecRegistry(),
            																			fromProviders(pojoCodecProvider));
            String uri = "mongodb://localhost:27017/?replicaSet=rs0";
            MongoClient mongoClient = MongoClients.create(uri);
            MongoDatabase mongoDatabase = mongoClient.getDatabase("de-mongodb").withCodecRegistry(codecRegistry);
            ClientSession clientSession = mongoClient.startSession();
            TransactionOptions transactionOptions = TransactionOptions.builder()
            																				.readPreference(ReadPreference.primary())
            																				.readConcern(ReadConcern.LOCAL)
            																				.writeConcern(WriteConcern.MAJORITY)
            																				.build();
            clientSession.startTransaction(transactionOptions); // start
            MongoCollection<Document> coll1 = mongoDatabase.getCollection("foo");
            MongoCollection<Document> coll2 = mongoDatabase.getCollection("bar");
            Map<String, Object> input1 = new HashMap<>();
            int id = new Random().nextInt();
            int value = new Random().nextInt();
            System.out.println("Test input: " + id + " : " + value);
            input1.put("_id", id);
            input1.put("field", value);
            Map<String, Object> input2 = new HashMap<>();
            input2.put("_id", id + 1);
            input2.put("field", value + 1);
            coll1.insertOne(clientSession, new Document(input1));
            coll1.insertOne(clientSession, new Document(input2));
            coll2.insertOne(clientSession, new Document(input1));
            clientSession.abortTransaction(); // rollback & end
            clientSession.startTransaction(transactionOptions); // start
            coll1.insertOne(clientSession, new Document(input1));
            clientSession.commitTransaction(); // commit & end
            ```
            
    - **MongoDB의 Transaction 사용시 주의사항**
        
        다만, MongoDB의 **Transaction이 제대로 기능하기 위해서는 여러 조건의 제약이 따르므로 주의**한다. 조건으로는 다음과 같은 조건들이 있다. **Operator(함수) 별로 사용할 수 있는 조건 또한 다르다**.
        
        - [**ReadConcern**](https://www.mongodb.com/docs/manual/reference/read-concern/)
        - **[WriteConcern](https://www.mongodb.com/docs/manual/reference/write-concern/)**
        - [**ReadPreference**](https://www.mongodb.com/docs/manual/core/read-preference/)
        
        위의 조건을 설정 했더라도, **Transaction 자체에 대한 제약사항 또한 따로 있다**.
        
        - **[Transaction의 가능 불가능 여부](https://www.mongodb.com/docs/manual/core/transactions/#transactions-and-operations)**
        
        MongoDB에서는 **multi-document transaction에 대해서 무분별한 사용시 성능저하**가 있을 수 있으니, 웬만하면 data schema design으로 **transaction 사용을 최소화 하는 것을 권장**하고 있다.
        
        <aside>
        ❗ In most cases, multi-document transaction incurs a greater performance cost over single document writes, and the availability of multi-document transactions should not be a replacement for effective schema design. For many scenarios, the [denormalized data model (embedded documents and arrays)](https://www.mongodb.com/docs/manual/core/data-model-design/#std-label-data-modeling-embedding) will continue to be optimal for your data and use cases. That is, for many scenarios, modeling your data appropriately will minimize the need for multidocument transactions.
        For additional transactions usage considerations (such as runtime limit and oplog size limit), see also [Production Considerations.](https://www.mongodb.com/docs/manual/core/transactions-production-consideration/)
        
        </aside>
        
    - **MongoDB에서 Transaction과 관련한 조언**
        
        실무적으로 조언을 한다면, Transaction(ACID)이 중요하고 서비스나 시스템의 중요도가 크다면 MongoDB보다는 RDBMS를 쓰는 것을 권장한다. MongoDB로 방법을 찾으려면 어떻게든 찾을 수는 있겠지만, 그것에 들어가는 시스템의 구축 비용과 구현 난이도, 디버깅 등 개발에 필요한 여러가지 요소들을 고려해본다면 애초에 목적에 맞게 디자인된 시스템을 필요한 곳에 제대로 사용하는 것이 효과적이고 효율적이다.
        
        시스템/서비스의 ACID 요구사항 수준이 낮거나, MongoDB의 장점이 더욱 중요해서 사용하는 경우 Transaction을 사용하기 보다는 Schema Design(또는 데이터 모델링)을 잘해서 Document 단위의 Atomic Operation 으로 해결할 수 있도록 시스템/서비스/로직을 구성하자