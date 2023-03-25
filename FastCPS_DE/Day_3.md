# Part2. 유틸리티 강의

## Ch 01. 개발환경 세팅

### 1. 개발환경 세팅 강의 수강 방법

Python은 Airflow 강의 수강 전에 하는 것 추천

Scala는 Spark 강의 수강 전에 하는 것 추천

### 2. Git 설치하기 - Windows

Git은 컴퓨터 파일의 변경사항을 추적하고 여러 명의 사용자들 간에 파일들의 작업을 조율 하기위한 분산 버전 관리 시스템이다.

소프트웨어 개발에서 소스코드 관리에 주로 사용된다.

### 3. Git 기본 사용방법 - CLI

HTTPS : 개발할 때 사용

SSH : 깃허브 소스 기반으로 배포할 때 사용

우리의 컴퓨터를 local이라고 부름

그리고 git의 레파지토리는 remote 또는 원격이라고 부름 그리고 origin이라는 별명을 붙여줌

`git status` : 현재 로컬 상태 확인

`commit` : 원격 레파지토리에 올리기 전에 변경한 것에 대해 도장을 찍는 것, 다수도 가능

커밋할 것들을 stage에 올린다고 함

- `git add <file>` : 파일을 stage에 commit할 대상으로 추가하는 것
    - —all, .  : 폴더 내 전체 파일들 추가
    - regular expression도 적용 가능 (ex. git add newfile*)
- `git restore —staged <file>` : 파일을 stage에서 없애는 것
    - . : stage 내 전체 파일 내리기
- `git commit -m “~”` : 메시지와 함께 stage에 올라온 대상들을 커밋하는 것

`push` : local commit을 원격 레포지토리에 배포하는 것

- `git push origin main`
- 어떤 브랜치에 푸쉬하는지 중요

linux 명령어

mv <file> <new object> : 이름 바꾸기 or 위치 이동

### 4. Git 기본 사용방법 - Source Tree

`pull` : 원격에 있는걸 내 로컬에 가져오는 것. 브랜치 설정 잘 해줘야함

`branch` : 새로운 분기를 만들어내서 변경사항을 기록함

브랜치를 만들어서 푸시하면 그건 원 분기랑 다른 것이다.

그래서 그 두 개를 병합 merge해줘야한다.

`checkout` : 브랜치를 떠나 새로운 브랜치로 이동하는 것

`merge` : 브랜치 간에 변경사항을 병합해준다. 이후에 푸시를 해줘야 적용됨

### 5. Java 개발환경 세팅하기 - Windows

자바는 객체지향 프로그래밍이 가능한 프로그래밍 언어이다.

자바의 장점은 코드를 한 번 작성하면 운영체제에 상관없이 JVM 위에서 실행할 수 있다는 것이다.

환경변수 : 어떤 명령어를 쳤을 때 그 명령어가 어디있는지 찾는 장소

### 6. Java 개발환경 세팅하기 - IntelliJ maven 프로젝트 생성하기

내 코드를 사용할 수 있는 형태로 만들어주는게 빌드 시스템임

거기에 Maven Gradle IntelliJ 가 존재

Maven project

- xml을 이용해 빌드한다.
- 자바용 프로젝트 관리도구
- pom.xml : 메이븐 빌드시스템 기본 빌드 설정 파일
- groupId : 팀 이름
- artifactId : 프로젝트 이름
- main : 실제 배포할 프로그램들의 소스
- test : 테스트 스텝에서만 사용될 파일, main + alpha
- resources : 프로그램의 실행에 필요한 여러 파일
- target : 빌드가 수행된 결과물이 저장되는 디렉토리

### 7. Java 개발환경 세팅하기 - IntelliJ gradle 프로젝트 생성하기

gradle project

- 빌드 자동화 및 다국어 개발 지원에 중점을 둔 빌드 도구
- android os 빌드도구 채택
- DSL(Domain Specific Languages) : 도메인 특화 언어 - 관력 특정 분야에 최적화된 언어
- groovy와 kotlin이 있다.
- build.gradle과 settings.gradle이 pom.xml의 역할을 수행한다.
- gradle/wrapper/gradle-wrapper.properties에 gradle 버전등의 정보가 담김
- gradle-wrapper : gradle에 관한게 pc에 설치가 안돼도 실행가능하게 해주는 것
- .gradle : gradle을 돌리는 데 필요한 중간 파일들
- gradlew(mac, unix), gradle.bet(windows)을 이용해 gradle을 다운로드 없이 사용
- src는 maven과 동일
- build라는 디렉토리는 maven의 target 디렉토리와 비슷하다.