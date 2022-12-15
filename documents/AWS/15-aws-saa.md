Q. 솔루션 설계자는 회사의 스토리지 비용을 줄이기 위한 솔루션을 구현해야 합니다. 회사의 모든 데이터는 Amazon S3 Standard 스토리지 클래 스에 있습니다. 회사는 모든 데이터를 최소 25년 동안 보관해야 합니다. 최근 2년 동안의 데이터는 가용성이 높고 즉시 검색할 수 있어야 합니다. 어떤 솔루션이 이러한 요구 사항을 충족합니까?

(A). Amazon S3에 로그 저장 AWS Backup을 사용하여 S3 Glacier Deep Archive로 1개월 이상 된 로그 이동 

(B). Amazon S3에 로그 저장 S3 수명 주기 정책을 사용하여 1개월 이상 된 로그를 S3 Glacier Deep Archive로 이동 

(C). Amazon CloudWatch Logs에 로그 저장. AWS Backup을 사용하여 1개월 이상 된 로그를 S3 Glacier Deep Archive로 이동 

(D). Amazon CloudWatch Logs에 로그를 저장. Amazon S3 수명 주기 정책을 사용하여 S3 Glacier Deep Archive로 1개월 이상 된 로그를 이동 합니다.

A. (B)

이 문항 CloudWatch Logs랑 S3 중 헷갈렸는데 `aws backup` 은 애초에 리소스 백업이라 S3에 로그 저장한 후 backup 서비스로 다른 스토리지 서비스로 옮기기 가능

![](https://i.imgur.com/tQY1cqO.png)

---

Q. 회사에서 3계층 웹 응용 프로그램을 사용하여 신입 직원에게 교육을 제공합니다. 애플리케이션은 매일 12시간 동안만 액세스됩니다. 회사는 Amazon RDS for MySQL DB 인스턴스를 사용하여 정보를 저장하고 비용을 최소화하려고 합니다. 솔루션 설계자는 이러한 요구 사항을 충족하기 위해 무엇을 해야 합니까?

(A). AWS Systems Manager Session Manager에 대한 IAM 정책을 구성합니다. 정책에 대한 IAM 역할을 생성합니다. 역할의 신뢰 관계를 업데 이트합니다. DB 인스턴스에 대한 자동 시작 및 중지를 설정합니다. 

(B). DB 인스턴스가 중지될 때 사용자가 캐시의 데이터에 액세스할 수 있는 기능을 제공하는 Redis용 Amazon ElastiCache 캐시 클러스터를 생 성합니다. DB 인스턴스가 시작된 후 캐시를 무효화합니다. 

(C). Amazon EC2 인스턴스를 시작합니다. Amazon RDS에 대한 액세스 권한을 부여하는 IAM 역할을 생성합니다. 역할을 EC2 인스턴스에 연결 합니다. 원하는 일정에 따라 EC2 인스턴스를 시작 및 중지하도록 크론 작업을 구성합니다. 

(D). DB 인스턴스를 시작 및 중지하는 AWS Lambda 함수를 생성합니다. Amazon EventBridge(Amazon CloudWatch Events) 예약 규칙을 생성 하여 Lambda 함수를 호출합니다. 규칙에 대한 이벤트 대상으로 Lambda 함수를 구성 합니다.

---


<!--stackedit_data:
eyJoaXN0b3J5IjpbOTY4MjUyMTU2LC0xMjYyNjU1NDA1LC0yNj
E2OTQ4XX0=
-->