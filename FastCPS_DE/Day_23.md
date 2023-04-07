### 5.MySQL High Availability

- **HA란**
    
    일반적인 의미로는 서비스 또는 시스템이 **약속한 수준의 서비스를 이용가능한 상태를 유지하는 것**을 말한다.
    Database의 경우 **SPOF 없이 비정기적인 HW 장애에도 불구하고 항상 이용할 수 있는 상태(ACID)를 유지**할 수 있는 아키텍처, 시스템의 구성을 말한다.
    **replication**: **데이터의 유실을 방지**하기 위한 목적으로 **복제 기능만을 말하는 국소적인 의미**.
    
    - **HA의 필요성**
        
        Database는 데이터의 중앙 저장소이다. **데이터를 활용할 수 없다면 서비스를 이용할 수 없다는 것이나 마찬가지**이다.
        Database 는 **대량의 데이터 처리 작업**을 할 수 있다. 데이터베이스에 **장애가 나면 대량의 워크로드를 처리할 수 없는 상태**가 된다.
        따라서 데이터베이스는 **사실상 무중단 운영이 필요**하다. 하지만 데이터베이스의 용도 자체가 대량의 데이터를 저장하고, 고성능이 필요한 워크로드를 처리하다보니 **장애에 취약**하다. 클라이언트의 잘못된 사용으로 장애가 날 수도 있고, 데이터나 메모리 용량을 관리하지 못해 장애가 나기도 한다. 예상치 못한 HW장비의 문제로 장애가 나는 것은 예측을 할 수도 없다.
        **Data를 언제나 두벌 저장**하면 되지 않을까? 이것은 **Application 개발자에게 Database의 책임을 떠넘기는 것**이다. 여기서 발생하는 코스트, 복잡도, 장애는 예측이 불가능하고, 관리되지 않는다. 따라서 **Database 자체에서 장애에도 무중단 운영을 위한 기능이 필요**하다. 이것을 **Database HA**라고 한다.
        
    - **HA의 목표**
        1. **SPOF(single point of failure)의 제거**
        2. **Detection of failure**: **장애 인지를 실시간으로 확인**할 수 있어야 한다.
        3. **Reliable crossover**: **장애 방지를 위해 자동으로 전환하는 시스템**이 필요.
        
- **MMM**
    
    **Multi-Master replication Manager** 의 줄임말.
    **Perl 기반의 auto failover 기능**을 하는 **오픈소스**이다.
    
    - **MMM 구조**
        
        ![Untitled](/FastCPS_DE/img/Untitled%2027.png)
        
        **MMM Monitor**와의 관계
        
        - **DB 서버에서 agent를 실행**시키고, **별도로 구성한 MMM monitor 서버와 통신**을 하면서 **MMM monitor 서버에 의해 상태 판단(health check)과, failover 전략을 수행**한다.
        
        **master**(active, standby), **slave**
        
        - **active master**와 **standby master** 가 있다.
        - **VIP는 active master** 에만 연결한다.
        - **active master 는 사용하는 서버**, **standby master는 active. master 와 연결해서 양방향 복제**를 한다.
        - Slave 를 추가하면, **단방향 복제를 하는 slave 가 하나씩 추가**된다.
        - **slave는 언제나 read only mode**이다.
    - MMM failover
        
        ![Untitled](/FastCPS_DE/img/Untitled%2028.png)
        
        active **master 에 장애**가 나면
        
        1. active master 는 **master 의 역할을 잃는다**.
        a. **read only 로 변경**
        b. **존재하는 session kill**
        c. **VIP 회수**
        2. master **standby 또는 slave로 복제를 재구성**한다.
        a. **복제지연이 있는지 확인**한다.
        b. **standby master 를 기준으로 복제**를 맞춘다.
        3. **master standby 에 대한 readonly 모드를 해제하고 VIP를 할당**한다.
    - **MMM 의 한계**
        
        Multi slave 환경에서 복제 Crash 가능성이 존재한다.
        
        - insert 도중 active master 에서 장애 발생
        - slave는 복제를 받았는데, standby master 가 복제를 못받음.
        - standby master 가 active master 로 전환
        - 다시 active master 에 insert를 하면 slave 에서 복제 에러
- **MHA**
    
    **Perl 기반의 Auto failover opensource**이다. **MMM과는 다르게 agentless 방식**이다.
    
    - **MHA 구성**
        
        ![Untitled](/FastCPS_DE/img/Untitled%2029.png)
        
        **하나의 master** 와 **다수의 slave 로 구성**된다.
        
        **master와 slave 사이에 서로의 연결을 구성**하고 **상태를 확인**한다.
        
        **모두 단방향 복제**이다.
        
    - **MHA 의 failover**
        
        ![Untitled](/FastCPS_DE/img/Untitled%2030.png)
        
        **master 에 장애**가 나면
        
        1. master 와 **slave 의 복제 연결을 끊는다.**
        2. **나머지 slave DB들로 복제 연결을 재구성**한다.
        3. **가장 최신의 데이터를 가지고 있는 DB를 마스터로 전환**한다.
        
        MHA는 **MMM의 복제 crash를 방지**하기위해
        
        - **복제 대상을 구분**한다: **바이너리 로그, 릴레이 로그 파일**을 읽는다.
        - 바이너리 로그 , 릴레이 로그를 **비교한 후 diff 를 추출**한다.
        - **diff 가 반영이 안된 slave 노드에 해당 diff를 적용**한다.
- **Cloud, Third party solution**
    
    MMM 또는 **MHA 아키텍처를 직접 구성하고, 유지보수하는 일은 쉽지 않다**
    
    AWS, Azure 등 **대형 Cloud 업체에서는 서비스 형태로 간단한 설정만으로도 HA를 구성**할 수 있도록 한다. 당연히 **HA를 구성하기 위한 추가 인프라에 서비스 비용이 추가되어 비용은 커진다.** 하지만, 숙련되지 않은 엔지니어 또는 전문 DBA가 아닌 다른 데이터 업무를 하면서 DB를 production level로 관리하는 것은 쉬운 일이 아니다.
    
    따라서 기회비용을 고려해서 **빠르고 안전하게 솔루션을 사용하는 것도 하나의 방법**이다.
    
    **설치형 솔루션도 존재**하는데, 이 경우 **인프라에 대한 관리와 솔루션에 대한 사용이 분리된다는 점이 단점**이다.
    
    - **AWS의 multi master MySQL Aurora**
        
        [Build highly available MySQL applications using Amazon Aurora Multi-Master | AWS Database Blog](https://aws.amazon.com/ko/blogs/database/building-highly-available-mysql-applications-using-amazon-aurora-mmsr/)
        
    - **Azure 의 MySQL HA**
        
        [High availability - Azure Database for MySQL | Microsoft Learn](https://learn.microsoft.com/en-us/azure/mysql/single-server/concepts-high-availability)
        
        [Zone-redundant HA with Azure Database for MySQL - Flexible Server | Microsoft Learn](https://learn.microsoft.com/en-us/azure/mysql/flexible-server/concepts-high-availability)