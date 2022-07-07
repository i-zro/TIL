# DI
## 개요
DI(의존성 주입, Dependency Injection)란, `클래스간의 의존 관계`를 스프링 컨테이너가 자동으로 연결해주는 것
* Dependency 란, 객체가 다른 객체와 상호작용하는 것을 말한다.
클래스 A가 클래스 B,C와 상호작용한다면 객체 A는 객체B,C와 의존관계이다.

## 필요성 : 객체 간 의존성
![Image](https://i.imgur.com/poNrg8E.png)
Factory 인터페이스를 상속받는 ConsoleFactory, UserFactory가 있을 때, 
SW를 사용하는 고객은 Factory 클래스만을 호출해야하며, 그것이 ConsoleFactory인지 UserFactory인지 몰라야한다.

고객마다 전용 Factory를 생성할 경우 1. 코드 생산성이 떨어지며, 2. 고객이 몰라도 되는 코드가 노출되기 때문이다.
때문에 스프링은 Factory가 ConsoleFactory인지 UserFactory인지를 프레임워크가 자동으로 객체간 의존성을 주입해준다.


































# 그레이들 프로젝트를 스프링 부트 프로젝트로 변경하기









# 스프링 부트와 AWS로 혼자 구현하는 웹 서비스 목표 (22.07.07)

## 🎈구매처
편의성을 위해 전자책으로 구매하였다.

https://www.aladin.co.kr/shop/wproduct.aspx?ItemId=256310078

## 🎀 개요
지금까지 회사에서 스프링 프로젝트를 여럿 다뤘지만 정작 Setting 하는 법이나 개념적인 부분에서는 많이 미흡한 것을 느꼈다. 이로 인해 한 번 기초적인 틀을 닦는 게 필요하다는 생각에서 해당 책을 따라해보며, 개념을 꼼꼼하게 잡아보려고 한다.

## 🎆 계획 및 현황
> 7월 말까지 최소한 AWS 까지는 다뤄보고 싶다.

우선, 책의 목차는 다음과 같다.

7월 10일까지 03장까지 끝내보고 이후 진도를 정할 것이다.
---
- 7월 7일까지 (완료 됨 / 최종 소요 시간 : 약 4h)
  
    01장  인텔리제이로 스프링 부트 시작하기  
    _1.1 인텔리제이 소개  
    _1.2 인텔리제이 설치하기  
    _1.3 인텔리제이 커뮤니티에서 프로젝트 생성하기  

    _1.4 그레이들 프로젝트를 스프링 부트 프로젝트로 변경하기 (https://naa0.tistory.com/163?category=1033133 / [그레이들 프로젝트를 스프링 부트 프로젝트로 변경하기](https://naa0.tistory.com/163?category=1033133))

    _1.5 인텔리제이에서 깃과 깃허브 사용하기 ([gitignore 설정](https://naa0.tistory.com/164))


- 7월 9일까지
  
    02장  스프링 부트에서 테스트 코드를 작성하자  
    _2.1 테스트 코드 소개  
    _2.2 Hello Controller 테스트 코드 작성하기  
    _2.3 롬복 소개 및 설치하기  
    _2.4 Hello Controller 코드를 롬복으로 전환하기  

- 7월 10일까지
      
    03장  스프링 부트에서 JPA로 데이터베이스 다뤄보자  
    _3.1 JPA 소개  
    __Spring Data JPA  
    __실무에서 JPA  
    __요구사항 분석   
    _3.2 프로젝트에 Spring Data Jpa 적용하기   
    _3.3 Spring Data JPA 테스트 코드 작성하기   
    _3.4 등록/수정/조회 API 만들기   
    _3.5 JPA Auditing으로 생성시간/수정시간 자동화하기   
    __LocalDate 사용   
    __JPA Auditing 테스트 코드 작성하기   
---


04장  머스테치로 화면 구성하기   
_4.1 서버 템플릿 엔진과 머스테치 소개   
__머스테치란   
__머스테치 플러그인 설치   
_4.2 기본 페이지 만들기   
_4.3 게시글 등록 화면 만들기   
_4.4 전체 조회 화면 만들기   
_4.5 게시글 수정, 삭제 화면 만들기   
__게시글 수정   
__게시글 삭제   

05장  스프링 시큐리티와 OAuth 2.0으로 로그인 기능 구현하기   
_5.1 스프링 시큐리티와 스프링 시큐리티 Oauth2 클라이언트   
_5.2 구글 서비스 등록   
_5.3 구글 로그인 연동하기   
__스프링 시큐리티 설정   
__로그인 테스트   
_5.4 어노테이션 기반으로 개선하기   
_5.5 세션 저장소로 데이터베이스 사용하기   
_5.6 네이버 로그인   
__네이버 API 등록   
__스프링 시큐리티 설정 등록   
_5.7 기존 테스트에 시큐리티 적용하기   

06장  AWS 서버 환경을 만들어보자 - AWS EC2   
_6.1 AWS 회원 가입   
_6.2 EC2 인스턴스 생성하기   
_6.3 EC2 서버에 접속하기   
_6.4 아마존 리눅스 1 서버 생성 시 꼭 해야 할 설정들   

07장  AWS에 데이터베이스 환경을 만들어보자 - AWS RDS   
_7.1 RDS 인스턴스 생성하기   
_7.2 RDS 운영환경에 맞는 파라미터 설정하기   
_7.3 내 PC에서 RDS에서 접속해 보기   
__Database 플러그인 설치   
_7.4 EC2에서 RDS에서 접근 확인   

08장  EC2 서버에 프로젝트를 배포해 보자   
_8.1 EC2에 프로젝트 Clone 받기   
_8.2 배포 스크립트 만들기   
_8.3 외부 Security 파일 등록하기   
_8.4 스프링 부트 프로젝트로 RDS 접근하기   
__RDS 테이블 생성   
__프로젝트 설정   
__EC2 설정   
_8.5 EC2에서 소셜 로그인하기   

09장  코드가 푸시되면 자동으로 배포해 보자 - Travis CI 배포 자동화   
_9.1 CI & CD 소개   
_9.2 Travis CI 연동하기   
__Travis CI 웹 서비스 설정   
__프로젝트 설정   
_9.3 Travis CI와 AWS S3 연동하기   
__AWS Key 발급   
__Travis CI에 키 등록   
__S3 버킷 생성   
__.travis.yml 추가   
_9.4 Travis CI와 AWS S3, CodeDeploy 연동하기   
__EC2에 IAM 역할 추가하기   
__CodeDeploy 에이전트 설치   
__CodeDeploy를 위한 권한 생성   
__CodeDeploy 생성   
__Travis CI, S3, CodeDeploy 연동   
_9.5 배포 자동화 구성   
__deploy.sh 파일 추가   
__.travis.yml 파일 수정   
__appspec.yml 파일 수정   
__실제 배포 과정 체험   
_9.6 CodeDeploy 로그 확인   

10장  24시간 365일 중단 없는 서비스를 만들자   
_10.1 무중단 배포 소개   
_10.2 엔진엑스 설치와 스프링 부트 연동하기   
_10.3 무중단 배포 스크립트 만들기   
__profile API 추가   
__real1, real2 profile 생성   
__엔진엑스 설정 수정   
__배포 스크립트들 작성   
_10.4 무중단 배포 테스트   

11장  1인 개발 시 도움이 될 도구와 조언들   
_11.1 추천 도구 소개   
__댓글   
__외부 서비스 연동   
__방문자 분석   
__CDN   
__이메일 마케팅   
_11.2 1인 개발 팁   
_11.3 마무리   

찾아보기












# build.gradle dependencies의 compile과 testCompile이 작동하지 않는 문제 [Spring / 트러블 슈팅]
## 🎈 문제 정의
build.gradle에서 책에서 쓰라는 대로 따라가면

![Image](https://i.imgur.com/aclgUWq.png)

사진과 같이 아예 인식을 못한다.

## 🔑 원인 추론
1. jdk 버전 문제라고 생각 (X)
2. compile 에서 implementation 과 api 로 변경되었다고 함. (O)

### compile과 implementation 차이
![Image](https://i.imgur.com/MApz3qR.png)
compile은 연결된 API 모두가 프로젝트에 의해 노출이 되고 implementation은 노출되지 않는다.

1. api가 노출이 되면, API로직에서 유효성 검사 및 기타 원하지 않는 형태의 데이터가 들어와 보안의 위협이 돼서 골치 아파진다.

A <- B <- C와 같이 B, C가 A라는 모듈을 의존하고 있다고 가정하자.
 
compile은 A가 수정이 되면, B, C와 같이 의존하고 있는 오브젝트들이 모두 다시 빌드되어야 한다.

2. 반면 implementation은 A수정 시, 직접 의존하는 B만 다시 빌드를 하기 때문에 속도적인 측면에서  더 유리하다.

그리고 이는 프로젝트의 구조가 복잡할수록, 커질수록 더욱 많은 퍼포먼스상 차이를 보인다.

3. 게다가 공식문서에서, gradle 3.0 이상부터는 compile을 사용을 권장하지 않는다.

(출처 : https://compogetters.tistory.com/64)

~~🦾 this is assisted by 관프님😠~~

## 🎆 조치 및 방안 검토
```gradle
dependencies {
    implementation('org.springframework.boot:spring-boot-starter-web')
    implementation('org.springframework.boot:spring-boot-starter-test')
}
```

똑같은 부분을 implementation으로 바꾼다.

## 👀 결과관찰
빌드쓰가 완료쓰

# 그레이들 프로젝트를 스프링 부트 프로젝트로 변경하기 [Spring]

### build.gradle 최종 코드
```gradle
buildscript {
    ext{    // ext: build.gradle에서 사용하는 전역변수를 설정하겠다.
        springBootVersion = '2.1.7.RELEASE'
    }
    repositories {  //  repositories는 각종 의존성 (라이브러리) 들을 어떤 원격 저장소에서 받을 지 정함. 책에서는 jcenter도 사용하나, 현 시점 (22.07.07) 에 중지 되어, mavenCentral만 사용 가능
        mavenCentral()
        jcenter()
    }
    dependencies {
        //  spring-boot-gradle-plugin라는 스프링 부트 그레이들 플러그인의 springBootVersion(2.1.7.RELEASE)를 의존성으로 받겠다.
        classpath("org.springframework.boot:spring-boot-gradle-plugin:${springBootVersion}")
    }
}

apply plugin: 'java'
apply plugin: 'eclipse'
apply plugin: 'org.springframework.boot'
apply plugin: 'io.spring.dependency-management' //  스프링 부트의 의존성들을 관리해주는 플러그인

group 'com.izero'
version '1.0-SNAPSHOT'
sourceCompatibility = 1.8

repositories {
    mavenCentral()
}

dependencies {
    implementation('org.springframework.boot:spring-boot-starter-web')
    implementation('org.springframework.boot:spring-boot-starter-test')
}
```

# gitignore 설정 [Spring / 스프링 부트와 AWS로 혼자 구현하는 웹 서비스]
- 프로젝트에서 오른쪽 마우스 누르고 ignore File 누르기
![Image](https://i.imgur.com/gVoxHyY.png)

- 화면 나오면 generate
![Image](https://i.imgur.com/AAuY9Vh.png)

- 인텔리제이에서 자동으로 생성되는 파일들은 모두 ignore 처리하기
    - .gradle
    - .idea