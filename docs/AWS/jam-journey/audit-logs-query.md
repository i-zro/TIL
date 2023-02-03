# [AWS JAM - DB] DML(update) 작동시키는 사람 cloud insights로 찾기 (AUDIT USER ACTIVITY)

# log_output 파라미터 값 변경

이 단계를 안 거쳤어서 계속 로그가 cloud watch 로그 그룹에 안 들어 왔었음. output 형태를 FILE로 고치니 들어옴.

**참고: **이 단계는 **log_output** 파라미터 값이 수동으로 **TABLE**로 수정되지 않는 경우 MySQL 5.7을 실행하는 Aurora 클러스터에 대해 필요하지 않습니다. MySQL 5.7을 실행하는 Aurora 클러스터에 대해 **log_output**파라미터의 기본 값은 **FILE**입니다.

1.  [<u>Amazon RDS 콘솔</u>](https://console.aws.amazon.com/rds)을 엽니다.

2.  탐색 창에서 [**파라미터 그룹**]을 선택합니다.

3.  로그를 게시하려는 인스턴스와 연결된 파라미터 그룹을 선택합니다.

4.  **파라미터 그룹 작업(Parameter group actions)**을 선택한 다음, **편집(Edit)**을 선택합니다.

5.  **Filter 파라미터** 필드를 사용하여 **log_output** 파라미터를 검색합니다.

6.  **log_output** 파라미터 값을 **FILE**로 설정합니다.

7.  **변경 사항 저장**을 선택합니다.  
    **참고: **이것은 동적 파라미터이므로 이 수정 작업은 재시작이 필요하지 않습니다. 자세한 내용은 [<u>파라미터 그룹 작업</u>](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithParamGroups.html)을 참조하세요

![](https://lgu-cto.atlassian.net/wiki/download/attachments/37684215899/image-20230203-054444.png?version=1&modificationDate=1675403087386&cacheVersion=1&api=v2 "권나영 > [RDS Monitoring] Who messed up the data in my DB Cluster? > image-20230203-054444.png")

# Log Insights 쿼리 작성

쿼리 시간 얼마 안남아서 거지같이 짜긴 했는데 하여튼 전체 message 항목에서 쉼표 단위로 parse해서 username과 query 추출하여 사용함.

사실상 그냥 눈으로 봐도 나오긴 함.

![](https://lgu-cto.atlassian.net/wiki/download/attachments/37684215899/image-20230203-061421.png?version=1&modificationDate=1675404865147&cacheVersion=1&api=v2 "권나영 > [RDS Monitoring] Who messed up the data in my DB Cluster? > image-20230203-061421.png")

*   @message : 20230203 06:12:01,ip-172-31-3-29,dev,10.2.10.78,45,1569,QUERY,,'update audit.revenue set amount=300000 where year=202001',0,,


```
@timestamp, @message, @logStream, @log
| parse @message "*,*,*,*,*,*,*" as a, b, userName, d, e, f, query
| filter query like "update"
| sort @timestamp desc
| limit 20 | fields @log, @logStream, @message, @t
    
```





<!--stackedit_data:
eyJoaXN0b3J5IjpbLTIzODg3Njc0MCw3MzA5OTgxMTZdfQ==
-->