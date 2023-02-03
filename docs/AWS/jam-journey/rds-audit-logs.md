
# RDS 설정하기

다음은 AWS 기본 매뉴얼에 나와있는 항목이었다.

* * *

*   참고 : [https://aws.amazon.com/ko/premiumsupport/knowledge-center/advanced-audit-rds-mysql-cloudwatch/](https://aws.amazon.com/ko/premiumsupport/knowledge-center/advanced-audit-rds-mysql-cloudwatch/)

* * *

*   Amazon RDS 콘솔을 엽니다.

*   탐색 창에서 데이터베이스(Databases)를 선택합니다.

*   로그 데이터를 CloudWatch로 내보낼 때 사용할 DB 인스턴스를 선택합니다.

*   [수정]을 선택합니다.

*   로그 내보내기(Log exports) 섹션에서 감사 로그(Audit log)를 선택합니다.

*   [계속]을 선택합니다.

*   수정 요약(Summary of modifications)을 검토하고 인스턴스 수정(Modify instance)을 선택합니다.

![](https://i.imgur.com/jY6urNI.png)


**단순히 위 매뉴얼대로 프로세스를 따라갔는데, 감사 로그 활성화가 안되고 있어서, 다른 매뉴얼들을 읽다보니 옵션 그룹을 생성하라는 힌트들이 있어서 아래와 같이 생성해줬다.**

## 옵션 그룹 생성하기

옵션 그룹을 생성하는 것은 아래의 블로그를 참고했다.

* * *

*   참고 : [https://hoing.io/archives/6132](https://hoing.io/archives/6132)

* * *

![](https://i.imgur.com/1hvFKs5.png)


*   옵션 그룹 추가 (MARIADB_AUDIT_PLUGIN)

![](https://i.imgur.com/A7GPQcR.png)


*   RDS 설정에서 해당 옵션 그룹 추가하고 수정 완료하기

![](https://i.imgur.com/mPBB4EA.png)

<!--stackedit_data:
eyJoaXN0b3J5IjpbMTA5MTkwODY5Myw2NzA4Mjk3NDddfQ==
-->