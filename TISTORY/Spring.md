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
    mavenCentral()
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

