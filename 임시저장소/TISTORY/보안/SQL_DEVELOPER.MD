# SQL Developer에서 Oracle 칼럼 추가

- SQL 편집기 켜주기
![Image](https://i.imgur.com/gzqWrGb.png)

## TABLE에 칼럼 추가
- 기본
```sql
ALTER TABLE 테이블명 ADD(컬럼명 타입(사이즈));
```

- 예시
- TB_USER_M 테이블에 칼럼, 타입(사이즈), DEFAULT값 / NOT NULL 조건 추가
    ```sql
    ALTER TABLE TB_USER_M ADD
    (LOGIN_FAIL_CNT NUMBER(10) DEFAULT 0,
    LOCK_RSN VARCHAR(20),
    LOCK_YN VARCHAR(20) DEFAULT 'N' NOT NULL);
    ```
- 실행
![Image](https://i.imgur.com/if4Nl5B.png)

## 칼럼에 코멘트 추가
- 기본
```SQL
COMMENT ON COLUMN 테이블명.컬럼명 IS '코멘트';
```

- 예시
```SQL
COMMENT ON COLUMN TB_USER_M.LOGIN_FAIL_CNT IS '로그인 실패 횟수(최대 10회)';
\
COMMENT ON COLUMN TB_USER_M.LOCK_RSN IS '계정잠금 사유(10회 로그인실패, 6개월 미접속, 퇴사)';
\
COMMENT ON COLUMN TB_USER_M.LOCK_YN IS '계정잠금 여부(Y/N)';
```

- 실행
![Image](https://i.imgur.com/vMBFsJ2.png)