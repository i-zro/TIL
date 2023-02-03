# RDS 설정하기

다음은 AWS 기본 매뉴얼에 나와있는 항목이었다.

* * *

*   참고 : [https://aws.amazon.com/ko/premiumsupport/knowledge-center/advanced-audit-rds-mysql-cloudwatch/](https://aws.amazon.com/ko/premiumsupport/knowledge-center/advanced-audit-rds-mysql-cloudwatch/)

* * *

*   Amazon RDS 콘솔을 엽니다.

*   탐색 창에서 데이터베이스(Databases)를 선택합니다.

*   로그 데이터를 CloudWatch로 내보낼 때 사용할 DB 인스턴스를 선택합니다.

*   [수정]을 선택합니다.

*   로그 내보내기(Log exports) 섹션에서 감사 로그(Audit log)를 선택합니다.

*   [계속]을 선택합니다.

*   수정 요약(Summary of modifications)을 검토하고 인스턴스 수정(Modify instance)을 선택합니다.

![](https://lgu-cto.atlassian.net/wiki/download/thumbnails/37684215899/image-20230202-075224.png?version=1&modificationDate=1675324347315&cacheVersion=1&api=v2&width=680 "권나영 > [RDS Monitoring] Who messed up the data in my DB Cluster? > image-20230202-075224.png")

**단순히 위 매뉴얼대로 프로세스를 따라갔는데, 감사 로그 활성화가 안되고 있어서, 다른 매뉴얼들을 읽다보니 옵션 그룹을 생성하라는 힌트들이 있어서 아래와 같이 생성해줬다.**

## 옵션 그룹 생성하기

옵션 그룹을 생성하는 것은 아래의 블로그를 참고했다.

* * *

*   참고 : [https://hoing.io/archives/6132](https://hoing.io/archives/6132)

* * *

![](https://lgu-cto.atlassian.net/wiki/download/attachments/37684215899/image-20230202-083436.png?version=1&modificationDate=1675326879531&cacheVersion=1&api=v2 "권나영 > [RDS Monitoring] Who messed up the data in my DB Cluster? > image-20230202-083436.png")

*   옵션 그룹 추가 (MARIADB_AUDIT_PLUGIN)

![](https://lgu-cto.atlassian.net/wiki/download/thumbnails/37684215899/image-20230202-083655.png?version=1&modificationDate=1675327018004&cacheVersion=1&api=v2&width=680 "권나영 > [RDS Monitoring] Who messed up the data in my DB Cluster? > image-20230202-083655.png")

*   RDS 설정에서 해당 옵션 그룹 추가하고 수정 완료하기

![](https://lgu-cto.atlassian.net/wiki/download/attachments/37684215899/image-20230202-083913.png?version=1&modificationDate=1675327156251&cacheVersion=1&api=v2 "권나영 > [RDS Monitoring] Who messed up the data in my DB Cluster? > image-20230202-083913.png")
<!--stackedit_data:
eyJoaXN0b3J5IjpbNjcwODI5NzQ3XX0=
-->