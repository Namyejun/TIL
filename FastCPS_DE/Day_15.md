### 14. JDBC 실습 - ORM

- **ORM**
    
    **Object Relation Mapping**. 앞서 살펴본 JDBC에서 ResultSet과 POJO class 를 매핑하는 코드를 매번 짜는 것이 불편해서 만들어진 기술(Library)을 ORM(Object-Relational Mapping)이다. 이름에서 추론할 수 있는 바와 같이, **객체와 Relational Model(관계형 데이터베이스 모델)을 매핑할 수 있는 기능**을 가지고 있다. **하나의 테이블이 하나의 Java Class에 해당**하고, FK와 같은 부가적인 기능은 함수로 제공한다.
    
- **JPA**
    
    ORM의 유용성이 입증되고 나니 Hibernate, MyBatis, TopLink, CoCobase 등 ORM을 구현하는 라이브러리 또는 프레임워크가 많아졌다. 이 ORM 기술에 대한 표준화를 시도한 것이 JPA이다.
    
    DB에 query를 날릴때 각 DB 제품별 전용 함수를 사용하는 것이 아니라 JDBC를 사용했던 것과 마찬가지로, ORM과 관련해서 각 구현체의 함수를 따로 사용하는 것이 아니라 JPA의 인터페이스를 통해서 작성하면, ORM 구현체를 무엇을 사용하던지, 코드를 변경할 일이 없게 된다.
    
    - 추천 JPA
        
        빠르게 개발해야한다면, **SpringBoot의 spring-data-jpa**가 data object와 repository interface 만 선언하고 바로 사용할 수 있으므로 좋습니다.
        하지만 **Spring Framework가 필요 없다면, Hibernate jpa 를 이용해서 구현**하는 것을 추천합니다. spring-data-jpa를 쓰기 위해서는 jpa를 위한 기능 뿐만 아니라 spring framework를 위한 다양한 의존성이 생기고, 런타임 동작이 생기는데 이것 때문에 어플리케이션이 불필요하게 리소스를 많이 사용하거나, 라이브러리 의존성 해결에 너무 많은 시간을 쏟게 되기 때문입니다.