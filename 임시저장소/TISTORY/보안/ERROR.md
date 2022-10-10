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


# Oracle 쿼리중 (+) 의 의미 - where절 더하기 표시
Secure Coding 작업을 하다가

`WHERE A.ID_COMP = B.ID_COMP(+)`

이런 신기한 쿼리가 있는 걸 봤다.
생소해서 확인해 보니 해당 쿼리가 OUTER JOIN을 위한 표현이라고 한다.
 
```sql

SELECT * FROM a, b WHERE b.id(+)  = a.id  -- Oracle OUTER JOIN
SELECT * FROM a LEFT OUTER JOIN b ON b.id = a.id -- 동일한 표현
 
a.id = b.id (+) -- LEFT OUTER
A.id(+) = b.id  -- RIGHT OUTER

```

즉, '(+)' 기호 위치의 반대쪽 테이블이 OUTER JOIN의 기준이 되는 테이블이다.

![Image](https://i.imgur.com/xr4aCZ0.png)

테이블이 3개일 때

```sql
SELECT A.ID_USER
FROM TB_USER_M A
        ,TB_COMP_M B
        ,TB_USER_SOL C
WHERE A.ID_COMP = B.ID_COMP(+)
    AND A.ID_USER = C.ID_USER(+)
    AND C.CD_SECS ='N'
```

위의 쿼리는

```sql
SELECT A.ID_USER
FROM TB_USER_M A
LEFT JOIN TB_COMP_M B
ON A.ID_COMP = B.ID_COMP
LEFT JOIN TB_USER_SOL C
ON A.ID_USER = C.ID_USER
AND C.CD_SECS = 'N'
```

이렇게 풀어진다.

## 참고
https://blog.edit.kr/entry/Oracle-%EC%BF%BC%EB%A6%AC%EC%A4%91%EC%97%90-%EC%9D%98-%EC%9D%98%EB%AF%B8
