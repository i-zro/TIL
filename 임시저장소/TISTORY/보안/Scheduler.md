# [Spring] 스프링에서 Scheduler 사용하기
### 스프링에서 scheduler 사용
1. annotation으로 심플하게 제어 ~~(비딩 사용 방법)~~
2. xml로 핸들링

### 스키마 설정
WEB-INT > config > biz-layer.xml이라는 xml에서 작업.

- xmlns:task라는 스키마를 등록하고 스키마 경로를 지정하기
![Image](https://i.imgur.com/CgSELxZ.png)

```
xmlns:task="http://www.springframework.org/schema/task"
xsi:schemaLocation=
http://www.springframework.org/schema/task http://www.springframework.org/schema/task/spring-task.xsd"
```

- `@EnableScheduling` and `@EnableAsync` respectively to replace `<task:annotation-driven>`
    - 출처 : [What is annotation for <task:annotation-driven> in spring 4.3](https://stackoverflow.com/questions/43389047/what-is-annotation-for-taskannotation-driven-in-spring-4-3)

    - 현재 프로젝트에서는 `<task:annotation-driven>`을 biz-layer.xml 파일에서 설정하였다.

    - task:scheduler id에 바딩할 id를 작성 (biddingScheduler)

    - pool-size = "10" : 쓰레드 풀 개수가 10
 
    ```xml
    <!-- pool-size 지정하지 않을 경우 쓰레드 풀의 기본값은 1 -->  
    <task:annotation-driven scheduler="biddingScheduler" />
        <task:scheduler id="biddingScheduler" pool-size="10"/>
    ```

## 어노테이션 설정
크게 fixed 방식과 크론탭 방식이 있다.

Schedule 클래스에 아래 Scheduled annotation을 import 하고 확인해보자.

```java
import org.springframework.scheduling.annotation.Scheduled;
```

### fixed 방식
fixedDelay 
- 실행된 task의 종료 시간으로부터 지정된(ms 단위) 시간이 지난 후 실행
 
fixedRate
- 실행된 시간으로부터 지정된(ms) 시간이 지난 후 실행


```java
	// 3초마다 실행
	@Scheduled(fixedDelay=3000)
	public void test() {
		System.out.println("delay 3000");
	}
```

- 3초에 한 번 찍히는 것 확인
![Image](https://i.imgur.com/YMtRkzS.png)

### Cron 방식

![Image](https://i.imgur.com/7dMvFY2.png)

- 예제
```
"0 0 * * * *" = the top of every hour of every day.
"*/10 * * * * *" = 매 10초마다 실행한다.
"0 0 8-10 * * *" = 매일 8, 9, 10시에 실행한다
"0 0 6,19 * * *" = 매일 오전 6시, 오후 7시에 실행한다.
"0 0/30 8-10 * * *" = 8:00, 8:30, 9:00, 9:30, 10:00 and 10:30 every day.
"0 0 9-17 * * MON-FRI" = 오전 9시부터 오후 5시까지 주중(월~금)에 실행한다.
"0 0 0 25 12 ?" = every Christmas Day at midnight
"0 0 0 * * *" = 매일 자정에 실행한다.
0 */2 * * * * = 매일 2분마다 실행한다.
```
- 5초에 한 번 출력하는 코드 추가
```java
	// 5초마다 실행
	@Scheduled(cron = "*/5 * * * * *")
	public void test2() {
		System.out.println("delay 5000");
	}
```

- 3초 스케쥴링 + 5초 스케쥴링 결과

![Image](https://i.imgur.com/93qxkWu.png)

## 참고
[[Spring] 스프링에서 Scheduler 사용하기](https://needjarvis.tistory.com/652)