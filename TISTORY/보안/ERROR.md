```
INFO  07-13 10:36:33 [ERROR] org.mybatis.spring.MyBatisSystemException: nested exception is org.apache.ibatis.exceptions.PersistenceException: 
### Error querying database.  Cause: java.lang.IllegalArgumentException: Mapped Statements collection already contains value for login.selectInquiry
### The error may exist in file [C:\Users\ETNERS\Documents\etnersBidding_new\target\ROOT\WEB-INF\classes\mappings\login-mapping.xml]
### Cause: java.lang.IllegalArgumentException: Mapped Statements collection already contains value for login.selectInquiry 
```






# Error resolving class ~VO [Spring / 트러블 슈팅]
## 🎈 개요
VO 새로 만들어서 매퍼 함수 만드는데 다음과 같은 에러가 떴다.
```
[ERROR] org.mybatis.spring.MyBatisSystemException: nested exception is org.apache.ibatis.builder.BuilderException: Error resolving class . Cause: org.apache.ibatis.type.TypeException: Could not resolve type alias 'UserLoginSecureVO'.  Cause: java.lang.ClassNotFoundException: Cannot find class: UserLoginSecureVO 
```
## 🔑 원인 추론
새로 만든 VO를 못 잡는다.
## 🎆 조치 및 방안 검토
- mybatis-config.xml에 alias 추가
![Image](https://i.imgur.com/Kd6izTd.png)

    ```
    <typeAlias alias="UserLoginSecureVO" type="com.etners.bidding.biz.VO.UserLoginSecureVO"/>
    ```