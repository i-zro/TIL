### 인텔리제이가 이클립스에 비해 갖는 장점
- 강력한 추천 기능
- 훨씬 더 다양한 리팩토링 및 디버깅 기능
- 이클립스의 git에 비해 훨씬 높은 자유도
- 프로젝트 시작할 때 인덱싱을 하여 파일을 비롯한 자원들에 대한 빠른 검색 속도
- HTML, CSS, JS, XML 강력한 지원 기능
- 자바, 스프링 부트 버전업에 맞춘 빠른 업데이트

> 17 ~ 28p : 인텔리제이 설치 방법

### 인텔리제이로 프로젝트 생성
- Gradle - Java 선택
![Image](https://i.imgur.com/bmFgFBr.png)

- ArtifactId가 프로젝트 이름
![Image](https://i.imgur.com/9XDrZYa.png)

## 그레이들 프로젝트를 스프링 부트 프로젝트로 변경하기
- 초기 build.gradle 파일
```gradle
plugins {
    id 'java'
}

group 'com.izero'
version '1.0-SNAPSHOT'

repositories {
    mavenCentral()
}

dependencies {
    testImplementation 'org.junit.jupiter:junit-jupiter-api:5.8.1'
    testRuntimeOnly 'org.junit.jupiter:junit-jupiter-engine:5.8.1'
}

test {
    useJUnitPlatform()
}
```

- ext: build.gradle에서 사용하는 전역변수를 설정하겠다.
- repositories는 각종 의존성 (라이브러리) 들을 어떤 원격 저장소에서 받을 지 정함. 책에서는 jcenter도 사용하나, 현 시점 (22.07.07) 에 중지 되어, mavenCentral만 사용 가능
- dependencies : 프로젝트 개발에 필요한 의존성들을 선언
```gradle
buildscript {
    ext{    // ext: build.gradle에서 사용하는 전역변수를 설정하겠다.
        springBootVersion = '2.1.7.RELEASE'
    }
    repositories {
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

plugins {
    id 'java'
}

group 'com.izero'
version '1.0-SNAPSHOT'
sourceCompatibility = 1.8

repositories {
    mavenCentral()ㅅ
}

dependencies {
    compile('org.springframework.boot:spring-boot-starter-web')
    testCompile('org.springframework.boot:spring-boot-starter-test')
}

//test {
//    useJUnitPlatform()
//}
```

### 최종 build.gradle
- 앞의 dependencies의 compile과 testCompile이 작동하지 않아서 compile은 A가 수정이 되면, B, C와 같이 의존하고 있는 오브젝트들이 모두 다시 빌드, 반면 implementation은 A수정 시, 직접 의존하는 B만 다시 빌드.
공식문서에서, gradle 3.0 이상부터는 compile을 사용을 권장하지 않는다. (https://compogetters.tistory.com/64) : compile은 연결된 API 모두가 프로젝트에 의해 노출이 되고 implementation은 노출되지 않는다. api가 노출이 되면, API로직에서 유효성 검사 및 기타 원하지 않는 형태의 데이터가 들어와 보안의 위협이 돼서 골치 아파진다.
```gradle
buildscript {
    ext{    // ext: build.gradle에서 사용하는 전역변수를 설정하겠다.
        springBootVersion = '2.1.7.RELEASE'
    }
    repositories {
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

//test {
//    useJUnitPlatform()
//}
```

# gitignore 설정
- 프로젝트에서 오른쪽 마우스 누르고 ignore File 누르기
![Image](https://i.imgur.com/gVoxHyY.png)

- 화면 나오면 generate
![Image](https://i.imgur.com/AAuY9Vh.png)

- 인텔리제이에서 자동으로 생성되는 파일들은 모두 ignore 처리하기
    - .gradle
    - .idea

# TDD
## 개요
TDD는 테스트가 주도하는 개발.

테스트 코드를 먼저 작성하는 것부터 시작.

### 레드 그린 사이클
![Image](https://i.imgur.com/nJUeFqA.png)
1. 항상 실패하는 테스트 코드를 먼저 작성하고 (Red)
2. 테스트가 통과하는 프로덕션 코드를 작성하고 (Green)
3. 테스트가 통과하면 프로덕션 코드를 리팩토링 (Refactor)

## 필요성
1. 빠른 피드백 (톰캣을 재시작하면 1분 이상 소요되지만 테스트 코드 작성하면 바로 볼 수 있다.)
2. 자동 검증 가능 (System.out.println() 사용 불필요)
3. 개발자가 만든 기능 보호 (서비스의 모든 기증을 테스트 할 수 없기에, 이후 수정에서 기존 기능 보호하도록)

## 테스트 코드 작성 프레임워크 ( == xUnit : 개발환경(x)에 따라 Unit 테스트를 도와준다.)
~~오마이 옛날 정처기 문제...xUnit...😥~~
- JUnit - Java
- DBUnit - DB
- CppUnit - C++
- NUnit - .net

# 테스트 코드 작성하기 [Spring / 스프링 부트와 AWS로 혼자 구현하는 웹 서비스]
- src > main > java 에서 오른쪽 클릭해서 springboot 패키지 생성
![Image](https://i.imgur.com/ljf69Uy.png)
![Image](https://i.imgur.com/t6Jg2rI.png)

- 그 아래에 Application 클래스 생성
![Image](https://i.imgur.com/l7xshLi.png)

- Application 클래스에 코드 작성
  - @SpringBootApplication 위치부터 설정을 읽어가는 것
  - SpringApplication.run()으로 내장 WAS 실행.
  
    ```java
    package com.izero.springboot;

    import org.springframework.boot.SpringApplication;
    import org.springframework.boot.autoconfigure.SpringBootApplication;

    //  SpringBootApplication 어노테이션이 있는 위치부터 설정을 읽어가므로, 클래스는 항상 프로젝트의 최상단에 위치하여야 함
    @SpringBootApplication
    public class Application {
        public static void main(String[] args){
            //  해당 run 함수로 내장 WAS를 실행. 내장 WAS란 별도로 외부에 WAS를 두지 않고 앱 실행 시 내부에서 WAS를 실행하는 것
            //  이러면 항상 서버에 Tomcat을 설치할 필요가 없어짐.
            //  내장 WAS를 사용해야 '언제 어디서나 같은 환경에서 스프링 부트 배포' 가능. 외장 WAS 사용시 실수할 여지도 많고 시간도 많이 필요함.
            SpringApplication.run(Application.class, args);
        }
    }
    ```

- 마찬가지로, web 폴더 하위에 HelloController 만들어주기
![Image](https://i.imgur.com/CXC6Tgc.png)

- Hello Controller 코드
    ```java
    package com.izero.springboot.web;


    import org.springframework.web.bind.annotation.GetMapping;
    import org.springframework.web.bind.annotation.RestController;

    @RestController // 컨트롤러를 JSON을 반환하는 컨트롤러로 만들어 줌.
    public class HelloController {

        @GetMapping("/hello")   //  HTTP Method인 Get의 요청을 받을 수 있는 API 만들어 줌.
        public String hello(){
            return "hello";
        }

    }
    ```

    ~~🦾 바보같이 저 GetMapping 쓰고 중괄호로 막아놓고 왜 안되는지 헤맸는데 수프님😎이 도와주셨당~~

- HelloControllerTest 
  - @RunWith(SpringRunner.class) : JUnit에 내장된 실행자 외에 다른 실행자(SpringRunner)를 실행시킴.
  - @Autowired : 스프링이 관리하는 빈(Bean)을 주입 받음
  - 

    ```java
    package com.izero.springboot;

    import com.izero.springboot.web.HelloController;
    import org.junit.Test;
    import org.junit.runner.RunWith;
    import org.springframework.beans.factory.annotation.Autowired;
    import org.springframework.boot.test.autoconfigure.web.servlet.WebMvcTest;
    import org.springframework.test.context.junit4.SpringRunner;
    import org.springframework.test.web.servlet.MockMvc;

    import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.get;
    import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.content;
    import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.status;

    // RunWith: 테스트를 진행할 때 JUnit에 내장된 실행자 외에 다른 실행자를 실행시킴.
    // 여기서는 SpringRunner라는 실행자를 사용한 것.
    // 스프링 부트 테스트와 JUnit 사이에 연결자 역할.
    @RunWith(SpringRunner.class)
    //  선언할 경우 @Service, @Component, @Repository를 사용 못함. 여기서는 컨트롤러만 사용해서 사용한 것.
    @WebMvcTest(controllers = HelloController.class)
    public class HelloControllerTest {

        @Autowired  //  스프링이 관리하는 빈(Bean)을 주입 받음
        private MockMvc mvc;    //  웹 API를 테스트 할 때 사용, 스프링 MVC 테스트의 시작점, 이 클래스로 HTTP GET, POST 등에 대한 API 테스트 가능

        @Test
        public void hello가_리턴된다() throws Exception{
            String hello = "hello";

            mvc.perform(get("/hello"))  //  MockMvc를 통해 /hello 주소로 HTTP GET 요청
                    .andExpect(status().isOk()) //  mvc.perform 결과 검증 : HTTP Header 상태 검증 (200, 404, 500 등)
                    .andExpect(content().string(hello));    //  mvc.perform 결과 검증 : 본문 내용 검증 ("hello" return 맞는지)
        }
    }
    ```

- 메소드 왼쪽의 화살표 클릭 - Run
![Image](https://i.imgur.com/ucrmoPU.png)

- 메소드 통과  
![Image](https://i.imgur.com/oLYeCjp.png)

# 롬복 소개 및 설치하기 [Spring / 스프링 부트와 AWS로 혼자 구현하는 웹 서비스]
- 롬복은 자바 개발 시 자주 사용하는 코드 Getter, Setter, 기본 생성자, toString 등을 어노테이션으로 자동 생성해 줌.

- 인텔리제이에서 플러그인으로 설치 가능, 
  - Ctrl + Shift + A > plugins > lombok 검색 후 설치 (이미 설치 된 경우 체크 누르기) 
    ![Image](https://i.imgur.com/j8V2aSS.png)
    ![Image](https://i.imgur.com/b7sb2LX.png)

- Settings > Annotation Processor > Enable annotation processing 체크
![Image](https://i.imgur.com/ahS5P0o.png)

# Hello Controller 코드를 롬복으로 전환하기
### DTO
계층 간 데이터 교환을 하기 위해 사용하는 객체.

DTO는 setter가 있고 VO는 없음.

- 유저가 입력한 데이터를 DB에 넣는 과정
    - 유저가 자신의 브라우저에서 데이터를 입력하여 form에 있는 데이터를 DTO에 넣어서 전송
    - 해당 DTO를 받은 서버가 DAO를 이용하여 데이터베이스로 데이터를 집어넣음.

- HelloDto 코드 작성
  - dto class 생성
    ![Image](https://i.imgur.com/7Cp0SeX.png)

    - Getter : 선언된 모든 필드의 get 메소드를 생성
    - RequiredArgsConstructor : 선언된 모든 final 필드가 포함된 생성자 생성

    ```java
    package com.izero.springboot.web.dto;

    import lombok.Getter;
    import lombok.RequiredArgsConstructor;

    @Getter //  선언된 모든 필드의 get 메소드를 생성
    @RequiredArgsConstructor    //  선언된 모든 final 필드가 포함된 생성자 생성, final이 없는 필드는 생성자에 포함 되지 않음
    public class HelloResponseDto {

        private final String name;
        private final int amount;

    }

    ```

- HelloDtoTest 클래스 작성
  - 롬복 프로젝트 추가 후 테스트 코드 실행 시 error: variable name not initialized in the default constructor 오류 : https://naa0.tistory.com/172

  - assertThat : assertj의 동등 비교 메소드, **assertThat**에 있는 값과 **isEqualTo** 값을 비교해서 같을 때만 성공

  - Jnit의 assertThat과 assertj의 assertThat 차이 : assertj는 1. is()와 같이 CoreMatchers 라이브러리가 필요없고 2. 자동완성이 조금 더 확실하게 지원

    ```java
    package com.izero.springboot.web.dto;

    import org.junit.Test;

    import static org.assertj.core.api.Assertions.assertThat;

    public class HelloResponseDtoTest {

        @Test
        public void 롬복_기능_테스트(){
            // given
            String name = "test";
            int amount = 1000;

            // when
            HelloResponseDto dto = new HelloResponseDto(name, amount);

            // then
            assertThat(dto.getName()).isEqualTo(name);  //  assertj의 동등 비교 메소드, assertThat에 있는 값과 isEqualTo 값을 비교해서 같을 때만 성공
            assertThat(dto.getAmount()).isEqualTo(amount);
        }
    }
    ```

    ![Image](https://i.imgur.com/mhKAHO6.png)

- Dto 컨트롤러 및 테스트 코드 작성
    - Controller에 다음 코드 추가
      - RequestParam : 외부에서 API로 넘긴 파라미터 가져오는 어노테이션
    ```java
        @GetMapping("/hello/dto")   //  HTTP Method인 Get의 요청을 받을 수 있는 API 만들어 줌.
        public HelloResponseDto helloDto(@RequestParam("name") String name, // RequestParam : 외부에서 API로 넘긴 파라미터 가져오는 어노테이션
                                        @RequestParam("amount") int amount){
            return new HelloResponseDto(name, amount);
        }
    ```

    - 테스트 코드 추가
      - jsonPath : JSON 응답값을 필드별로 검증할 수 있는 메소드, $를 기준으로 필드명 명시.
    ```java
        @Test
        public void helloDto가_리턴된다() throws Exception{
            String name = "hello";
            int amount = 1000;

            mvc.perform(
                    get("/hello/dto")
                            .param("name", name)
                            .param("amount", String.valueOf(amount)))
                            .andExpect(status().isOk())
                            .andExpect(jsonPath("$.name", is(name)))
                            .andExpect(jsonPath("$.amount", is(amount)));
        }
    ```

# 롬복 프로젝트 추가 후 테스트 코드 실행 시 error: variable name not initialized in the default constructor 오류 [Spring / 트러블 슈팅]

## 🔑 원인 추론

gradle 버전이 5로 올라가면서 lombok 을 프로젝트에 추가하는 방법이 달라졌기 때문

## 🎆 조치 및 방안 검토
- build.gradle
```
dependencies {
    implementation('org.springframework.boot:spring-boot-starter-web')
    implementation('org.projectlombok:lombok')
    testImplementation('org.springframework.boot:spring-boot-starter-test')
    annotationProcessor('org.projectlombok:lombok') //  추가
}
```

