### 2. 데이터(베이스) 정규화
- **정규화란**
  - **정규화의 정의** <br>
    관계형 데이터베이스의 설계에서 **불필요한 데이터(중복 등)을 최소화**하고 **데이터 정확성(accuracy)과 일관성(consistency)을 향상** 시키도록 **데이터를 구조화하는 과정 또는 그 결과**를 정규화라고 한다.
    **비정상적인 것을 찾아서 정상화**(normalize)하는 과정으로 진행한다.
  - **정규화 단계** <br>
    정상화 하는 정도(비정상적인 것의 규정과 그것의 교정)에 따라서 **제 1정규화, 2정규화, 3정규화..** 식으로 단계가 진화한다. 다음 링크에서 표로 잘 정리해놓았다.

    E.F. Codd 박사에 따르면 **정규화의 목표**는 다음과 같다.
    1. **To free** the collection of relations from **undesirable insertion, update and deletion dependencies**.
    2. **To reduce the need for restructuring the collection of relations**, as new types of data are introduced, and thus increase the life span of application programs.
    3. To make the relational model **more informative to users**.
    4. To make the collection of relations **neutral to the query statistics, where these statistics are liable** to change as time goes by.

    하지만, 정말 이 방식으로 정규화를 할 수 있을까? 그리고 그렇게 하면 과연 좋은 시스템일까?
    > 본 강의에서는 요구사항 분석을 기반으로한 실천적인 방법을 사용한다. 실제로 **실무에서 1~5까지 차례로 정규화하면서 최대로 정규화를 할 수 있는 경우는 많지 않다**. 고려해야할 **여러가지 요구사항과 tradeoff** 가 있기 때문이다. 정규화를 **섬세하게 할 수록 성능이 좋아지는 것이 아니다**. 정규화를 섬세하게 할수록 **프로그래밍하기 좋아지는 것 또한 아니다**.
    정규화의 목적과 효과를 잘 이해하고 자신의 서비스/시스템에 맞게 의사결정하고 결과를 낼 수 있는 능력이 더 중요하다.

- **정규화 - 데이터 라이프 사이클에 의한 방법**
    - **원리**

        **서비스의 특징, UX의 설계에 따라서 결정**하는 방식이다. **RDBMS는 Update 가 가능하지만, 데이터 관리 차원에서는 update가 없는 것이 좋다**. 또한 **optional(nullable)한 필드가 많다면 비즈니스 로직과 데이터에 버그를 많이 유발**한다. 따라서 **idempotent한 아키텍처의 구성**, 데이터 관리의 용이성, 비즈니스 로직의 버그 방지를 위해서 한 번에 확정되는 데이터의 기준으로 테이블을 분리하는 방식을 사용할 수 있다.
    - **예제 - 요구사항**

        쇼핑몰을 구축한다. 유저는 상품을 장바구니에 담는다. 주문서를 작성한다. 유저의 결제를 기다린다. 결제가 완료되면 배송정보가 생성된다. 배송이 완료되면 최종 주문이 완료된다. 유저의 구매내역을 하나의 테이블로만들었다.

        Table: order
        |order_no|items|payment|delivery|status|review|
        |:---|:---|:---|:---|:---|:---|
        |1|[1029,2910,3829]|null|null|ordered|null|

    - **문제 1 - nullable column**

        nullable column 은 **개발자들이 항상 null 처리를 해야하는 불편함**을 발생시킨다. 또한 null 의 의미가 무엇인지 - 잘못 된 값인지, 유저의 상태가 이상한 것인지, 없어도 되는건지 등- 오해를 발생시키고 커뮤니케이션이 늘어나게 만든다.
        게다가 기본 테이블은 null인 컬럼이 많기 때문에 **null에 대한 복잡도도 기하급수적으로 증가**한다.

        Table: order
        |order_no|items|amount|payment|delivery|status|review|
        |:---|:---|:---|:---|:---|:---|:---|
        |1|[1029,2910,3829]|1000|1000|not_yet|ordered|not_yet|
    
        **필드를 non null로 선언**하고, **default 값**을 테이블에 선언, **프로그램에서는 enum으로 상태 값을 관리**하도록 해서 문제를 해결했다.
    - **문제 2 - 데이터 누락**

        |order_no|items|amount|payment|delivery|status|review|
        |:---|:---|:---|:---|:---|:---|:---|
        |1|[1029,2910,3829]|1000|100|not_yet|ordered|not_yet|

        결제정보가 도착해서 유저의 구매정보를 업데이트 한다. 유저가 결제 취소 후 재결제를 했는데, 첫 번째에 입금된 금액으로만 남아있고 두 번째 입금 금액이 없었다. 유저는 자신의 입금 내역이 다르다는데 확인할 길이 없다.

        Table: payment
        |payment_no|datetime|pay_method|pay_vendor|status|cost|
        |:---|:---|:---|:---|:---|:---|
        |1|2020.01.01 10:00:00|card|samsungcard|confirmed|100|
        |2|2020.01.01 10:00:01|card|samsungcard|cancelled|100|
        |3|2020.01.01 10:00:02|card|samsungcard|confirmed|1,000|

        Table: order
        |order_no|items|amount|FK_payment|delivery|status|review|
        |:---|:---|:---|:---|:---|:---|:---|
        |1|[1029,2910,3829]|1000|3|not_yet|ordered|not_yet|

        **입금 내역을 기록하는 테이블(payment)을 따로** 만들었다. order 테이블은 **payment 의 마지막 유효한 결제 내역을 FK**로 가진다.
    - **문제 3 - 데이터 정확성**

        배송도 택배사의 데이터를 연동해서 값을 채워넣었는데, 배송이 완료 이벤트가 배송출발 이벤트보다 먼저 들어와서 배송중인 상태로 잘못 업데이트가 되었다. 판매자에게서 완료가 처리 안된다는 CS가 들어왔다.

        Table: order
        |order_no|items|amount|FK_payment|delivery|status|review|
        |:---|:---|:---|:---|:---|:---|:---|
        |1|[1029,2910,3829]|1000|3|배송 출발|ordered|not_yet|

        Table: delivery
        |delivery_no|datetime|partner|delivery_vendor|status|
        |:---|:---|:---|:---|:---|
        |1|2020.01.01 10:00:00|Nancy|Logen|입고|
        |2|2020.01.02 12:00:02|Paul|Logen|배송완료|
        |3|2020.01.02 10:00:01|Paul|Logen|배송출발|

        Table: order
        |order_no|items|amount|FK_payment|FK_delivery|status|review|
        |:---|:---|:---|:---|:---|:---|:---|
        |1|[1029,2910,3829]|1000|3|2|ordered|not_yet|

    - **문제 4 - race condition**

        결제정보의 업데이트와 배송정보 업데이트에 순서가 보장되지 않았다. 거의 동시에 요청이 오면 **race condition에 의해서 업데이트가 무시**될 수 있었다.

        ![Untitled](/FastCPS_DE/img/Untitled%2031.png)
        **lock을 걸어 해결**했다.
        그런데 lock을 걸어보니 **반복해서 조회하고 업데이트가 일어나는 테이블**이라 **lock에 의한 조회 지연시간**이 늘어났다.

    - **해결**

        유저의 **구매과정에서 생기는 이벤트 별로 테이블을 분리(정규화)**했다. 배송 이벤트 테이블, 결제 이벤트 테이블이 order 테이블을 참조하고, 주문 내역의 상태의 판단과 통합 조회는 join 쿼리로 해결하기로 했다.

        Table: payment
        |payment_no|datetime|pay_method|pay_vendor|status|cost|FK_order|
        |:---|:---|:---|:---|:---|:---|:---|
        |1|2020.01.01 10:00:00|card|samsungcard|confirmed|100|1|
        |2|2020.01.02 10:00:01|card|samsungcard|cancelled|100|1|
        |3|2020.01.02 10:00:02|card|samsungcard|confirmed|1000|1|

        Table: delivery
        |delivery_no|datetime|partner|delivery_vendor|status|FK_order|
        |:---|:---|:---|:---|:---|:---|
        |1|2020.01.01 10:00:00|Nancy|Logen|입고|1|
        |2|2020.01.02 10:00:01|Paul|Logen|배송출발|1|
        |3|2020.01.02 12:00:02|Paul|Logen|배송완료|1|

        |order_no|items|amount|
        |:---|:---|:---|
        |1|[1029,2910.3829]|1000|

        **상태의 판단은 join 쿼리안에서 로직으로 column을 추가하거나, 서버에서 로직으로 추가**하는 것으로 했다. 다음과 같은 정규화 목표를 달성했다.
        1. 데이터의 **중복이 없다**.
        2. 하나의 이벤트가 **하나의 null이 없는 데이터셋(row)으로 완결성**이 있다.
        3. update가 없어서 **race condition이 발생하지 않는다**.
        4. **데이터의 누락이 없어 데이터가 정확**하다.
        5. **모든 데이터가 남아서 문제 상황시 CS를 정확히 대응**할 수 있다.

        과연 이 모델은 완벽할까?
- **정규화에서 고려해야할 side effect**

    정규화 과정에서 정규화 조건은 만족하지만, 의도하지 않은 side effect가 발생할 수 있다. 다음 세 가지 상황이 발생하지 않도록 정규화를 해야한다.
    - **Insertion anomaly**. There are circumstances in which certain facts cannot be recorded at all.

        ![Untitled](/FastCPS_DE/img/Untitled%2032.png)
    - **Update anomaly**. The same information can be expressed on multiple rows; therefore updates to the relation may result in logical inconsistencies.

        ![Untitled](/FastCPS_DE/img/Untitled%2033.png)
    - **Deletion anomaly**. Under certain circumstances, deletion of data representing certain facts necessitates deletion of data representing completely different facts.

        ![Untitled](/FastCPS_DE/img/Untitled%2034.png)