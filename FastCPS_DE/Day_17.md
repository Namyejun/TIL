### 2. MongoDB의 기본 개념과 기능들

- **Document**
    
    MongoDB에서 **데이터를 저장하는 단위**는 Document이다. 각 Document의 형식은 미리 지정되어있지 않고, 생성 시점에 어떤 형식의 내용이 와도 된다. **같은 Collection에 속한 Document라고해서 모두 같은 형식을 따를 필요는 없다**. **하나의 Document가 자신의 데이터에 대해서 완결성을 가진다.** Document에 가지는 필드나 값은 **BSON Type**을 따른다. 단, `**_id` 필드는 각 document의 Primary Key**로서 반드시 가져야 한다. 직접 지정할 수도 있고, 지정하지 않으면 **ObjectId 형식**의 데이터가 자동 생성되어 데이터 생성(삽입) 시점에 할당된다.
    
    - **_id 필드와 ObjectId**
        
        **모든 Document는 고유값을 뜻하는 _id 필드를 반드시 가진다**. _id는 직접 지정할 수도 있고, 지정하지 않으면 **ObjectId 형식의 데이터가 자동 생성**되어 **데이터 생성(삽입) 시점에 할당**된다. 
        
        ObjectId는 **12bytes**로 다음의 **데이터의 조합**이다.
        
        - A 4-byte timestamp: 데이터 생성 시점의 **unix epoch timestamp 값**
        - A 5-byte random value: 프로세스당 **unique함을 보장하는 random 값**.
        - A 3-byte incrementing counter: **1씩 증가해서 할당되는 counter**. 앞의 random value에 의해 초기화 된다.
        
        직접 _id를 지정하지 않고, ObjectId를 쓴다면 다음과 같은 장점이 있다.
        
        - **ObjectId.getTimestamp()** 를 통해서 별도의 필드 없이 **생성 시점을 가져올 수 있다.**
        - ObjectID 의 맨 앞이 timestamp로 되어있어서, 그 **ObjectId로 정렬하면 (대략적인) 시간순 정렬**이 된다.
    - **Bson**
        
        JSON style의 binary 포맷이라고 생각하면 된다. 하지만 BSON이 가질 수 있는 데이터 타입은 좀 더 상세하다. 다음 링크를 참고하면 어떤 타입을 어떤 정의로 사용할 수 있는지 알 수 있다. [https://www.mongodb.com/docs/manual/reference/bson-types/](https://www.mongodb.com/docs/manual/reference/bson-types/)
        

- **Collection**
    
    **Document를 저장하기 위한 논리적인 묶음을 Collection**이라고 한다. **RDBMS의 Table과 유사**하다고 생각하면 된다.
    
    MongoDB는 Document Store로서 **Document의 형식에 제약이 없지만**, **Collection 단위에서 같은 형식(필드 이름, 값의 데이터 타입 등)를 가지도록 제약을 걸 수 있다**. 시스템의 요구사항으로 형식이 **다른 데이터가 들어가면 안되는 경우에는 Schema Validation 기능을 사용**한다.
    
    Schema Validation을 사용하지 않더라도, **스키마 규칙을 프로그래밍 모델로라도 가지고 사용하는 것을 추천**한다. 이 경우 optional field가 많아도 상관이 없다. 다만, **optional이 많으면 정적타입 언어를 쓰는 경우 null-check를 신경**써야하는 불편함이 있다.
    

- **Database**
    
    하나의 MongoDB **서버 혹은 클러스터에서 논리적으로 Database를 구분**할 수 있다. 주로 사용하는 **서비스, client user 등을 구분**하고, **접속에 제한**을 두기 위해서 사용한다.
    

- **Schema와 성능**
    
    MongoDB는 **BSON의 형식에 따라서 하나의 필드가 BSON Object(Json object)를 가질 수 있다.** 즉, **필드 안에 또 필드**가 있을 수 있다. 그리고 이 오프젝트에 대해서 검색도 가능하다.
    
    다만, 이렇게 계속 **inner field**를 가지는 식으로 데이터를 저장하면 **검색, 집계 연산에서 그만큼 속도가 느려진다**. 따라서 데이터를 저장에서의 편의성만 생각하는 것이 아니라, **검색에서의 효율성도 고려해서 Document의 형식을 정하는 것**이 좋다.
    
    다만, **데이터가 많지 않으면 큰 차이가 나지 않는다**. **시스템이나 서비스의 규모가 작다면** 아직 발생하지 않는 성능 문제에 이것저것 고려하지 않고 객체지향 모델에 맞게 Document를 저장하고 사용할 수 있는 장점을 살려서 **개발 속도를 끌어올리는 방법**도 좋다. **나중에 문제가 되면 그때 튜닝이나 리팩토링**을 하는 것도 늦지 않다.
    
- **Database-References**
    
    참고: [https://www.mongodb.com/docs/manual/reference/database-references/](https://www.mongodb.com/docs/manual/reference/database-references/)
    MongoDB에서 RDBMS에서 **Foreign Key를 지정하는 것처럼 다른 DB나 Collection의 특정 Document를 참조**할 수 있을까? MongoDB는 이를 위해 **두가지 기능을 제공**한다.
    어떤 기능을 사용하던지 **RDBMS처럼 Cascading을 제공하지 않기 때문에 Atomicity를 완벽하게 제공할 수 없다.**
    
    - **Manual References**
        
        [https://www.mongodb.com/docs/manual/reference/database-references/#std-label-document-references](https://www.mongodb.com/docs/manual/reference/database-references/#std-label-document-references)
        **참조하고 싶은 Document의 _id 필드에 해당하는 값**을, **다른 Document의 특정 필드의 값에 놓고, 직접 찾는 것**이다. 결국 참조하고 싶은 데이터를 가져오려면 두 번 쿼리를 날려야 한다.
        
    - **DB Refs**
        
        Document를 **참조할 수 있는 convention을 제공**한다. 참조하고 싶은 Document의 **Collection, _id, database, another fields와 기타 정보를 객체로 담는다**.
        
        단, 각 언어의 클라이언트마다 지원 여부와 기능의 정도가 다르니 확인하고 사용해야한다.
        
- **Transaction**
    
    MongoDB에서 기본적으로 **하나의 Document에 대해서 하나의 operation만 Atomic operation을 제공**한다. Transaction을 이용하면 **하나 이상의 document에 대해서, 두 번 이상을 operation에 대해서 Atomicity를 제공**할 수 있다.
    
    다만, 모든 **Collection, Document에서 Transaction 을 제공하지는 못하고 일부 제약사항**이 있다. **production level로 Transaction을 사용하려면 문서에서 한정하는 범위나 기능을 정확하게 파악**하고 사용해야한다.
    문서: [https://www.mongodb.com/docs/manual/core/transactions/](https://www.mongodb.com/docs/manual/core/transactions/)
    