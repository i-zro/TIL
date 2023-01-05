# HTTP 요청과 관련된 Annotation

###### tags: `2023.01.04`

---
#### References

- https://www.baeldung.com/spring-mvc-annotations

---

### @RequestMapping



### @RestController

- 주용도는 Json/Xml 형태로 객체 데이터를 반환하는 것이다.

- 주로 RestAPI Control Class에 선언한다.

RestController가 선언된 클래스의 내부 함수들은 return 값이 Json/Xml 형식으로 자동 변환되어 반환된다.
샘플

@RestController
public class HotelController extends AbstractRestHandler {
@RequestMapping
REST API 호출 시 작성된 URL 의 method 값에 따라 맵핑 시켜준다.

RestController이 선언된 클래스의 내부 함수 상단에 선언해준다.
샘플

  @RequestMapping(value = "",
          method = RequestMethod.POST,
          consumes = {"application/json", "application/xml"},
          produces = {"application/json", "application/xml"})
consumes
consumes는 Content-Type이 consumes에 명시한 media-type과 같아야한다.
샘플
curl -XPOST "localhost:8080/test" -H "Content-Type:application/json"
content-type
content-type은 client가 보내는 content의 타입이다.
produces
produces는 Accet Header가 produces에 명시한 Media Type과 같을때에 해당 Type으로 response를 보내준다
accept
accept는 client가 backend 서버에게 어떤 형식(Media Type)으로 달라고 하는 요청의 방식 (ex. JSON 방식으로 주세요 => Accept:application/json)
샘플
curl -XGET "localhost:8080/test" -H "Accept:application/json"
출처 : http://blog.naver.com/PostView.nhn?blogId=writer0713&logNo=221422059349&parentCategoryNo=&categoryNo=83&viewDate=&isShowPopularPosts=false&from=postView

@ResponseStatus
ResponseStatus는 부여된 메소드(함수)의 응답 상태 코드를 지정할 수 있다. (ex. 200 OK, 201 Created, 202 Accepted 등)

아무것도 지정하지 않으면 200 OK가 반환되다.
샘플

@RestController
@RequestMapping("/hello")
public class HelloController {

  @RequestMapping(method=RequestMethod.GET)
  @ResponseStatus(HttpStatus.BAD_REQUEST)
  public void getMethod() {
  }
}
출처 : http://www.devkuma.com/books/pages/474

@RequestBody
HTTP로 받은 Body 데이터를 자바 객체로 받기 위하여 사용
샘플

@RestController
public class LoginWebController 
{

  // HTTP 요청의 내용을 Member 객체에 매핑하기위해 @RequestBody 애너테이션을 설정한다.
  @RequestMapping(value="/member/login", method = RequestMethod.POST)
  public MemberResultDto login(@RequestBody Member member) 
  {
  MemberResultDto memberResultDto = memberService.login(member); 
  return memberResultDto;

  }
}
출처 : https://codelib.tistory.com/24

@ApiParam
ApiParam은 멤버 변수에 대한 설명 및 다양한 설정을 지원합니다.

value
저장되야할 값에 대한 설명을 명시합니다.
required
필수 여부를 지정합니다.
샘플
@ApiParam(value = "member age", required = true)
  private int age;
출처 : https://bamdule.tistory.com/36

@RequestParam
HTTP를 통하여 받아온 데이터를 단일 파라미터 변환 해준다.
샘플

@RequestParam(value = "page", required = true, defaultValue = DEFAULT_PAGE_NUM)
Integer page;
value
HTTP를 통하여 넘어온 쿼리 스트링의 Key값
required
필수로 사용 여부 true=필수사용, false=사용하든 안하든 상관없음
defaultValue
HTTP에서 해당 Key로 넘어온 값이 없다면 들어갈 기본값

# Spring Message 처리

###### tags: `2023.01.04`, `김영한 MVC2`

악덕? 기획자가 화면에 보이는 문구가 마음에 들지 않는다고, `상품명`이라는 단어를 모두 `상품이름`으로 고쳐달라고 하면 어떻게 해야할까?
여러 화면에 보이는 상품명, 가격, 수량 등, label 에 있는 단어를 변경하려면 다음 화면들을 다 찾아가면서 모두 변경해야 한다. 화면 수가 적으면 문제가 되지 않지만 화면이 수십개 이상이라면 수십개의 파일을 모두 고쳐야 한다.

왜냐하면 해당 HTML 파일에 메시지가 `하드코딩` 되어 있기 때문이다.
이런 `다양한 메시지를 한 곳에서 관리`하도록 하는 기능을 메시지 기능이라 한다.

### 국제화

메시지 파일( messages.properties )을 각 나라별로 별도로 관리하면 서비스를 국제화 할 수 있다.

```properties
- messages_en.properties

item=Item
item.id=Item ID
item.itemName=Item Name

- messages_ko.properties

item=상품 
item.id=상품 ID 
item.itemName=상품명
```

### 한국에서 접근한 것인지 영어에서 접근한 것인지는 인식하는 방법
1. HTTP accept-language 헤더 값을
사용하거나 
2. 사용자가 직접 언어를 선택하도록 하고, 쿠키 등을 사용해서 처리하면 된다.


### 스프링 빈 직접 등록

메시지 관리 기능을 사용하려면 스프링이 제공하는 MessageSource 를 스프링 빈으로 등록하면 되는데, MessageSource 는 인터페이스이다. 따라서 구현체인 `ResourceBundleMessageSource` 를 스프링 빈으로 등록하면 된다.

```java
   @Bean
  public MessageSource messageSource() {
      ResourceBundleMessageSource messageSource = new
  ResourceBundleMessageSource();
      messageSource.setBasenames("messages", "errors"); // "messages" => messages.properties 파일 읽어서 사용
      messageSource.setDefaultEncoding("utf-8");
      return messageSource;
}
```


### 스프링 부트 자동 등록

- application.properties에 등록

```properties
spring.messages.basename=messages,config.i18n.messages
```

### MessageSource 인터페이스

- 파라미터로 메시지를 읽어오는 기능

```java
public interface MessageSource {
    String getMessage(String code, @Nullable Object[] args, @Nullable String
  defaultMessage, Locale locale);
    String getMessage(String code, @Nullable Object[] args, Locale locale) throws
  NoSuchMessageException;
```

- 메시지가 없는 경우에는 NoSuchMessageException 이 발생


### Message Source 매개변수

```java
    @Test
    void argumentMessage() {
        String result = ms.getMessage("hello.name", new Object[]{"Spring"}, null); // Spring 단어를 매개변수로 전달
        assertThat(result).isEqualTo("안녕 Spring");
    }
```


### 타임리프 메시지 적용

```html
<!-- label.item을 messages에 저장했을 때 -->
<div th:text="#{label.item}"></h2>
```