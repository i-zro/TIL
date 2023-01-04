# HTTP 요청과 관련된 Annotation

###### tags: `2023.01.04`

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