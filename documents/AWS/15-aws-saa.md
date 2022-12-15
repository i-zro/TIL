### 고민하다가 맞은 문제
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

A. (D)

계속 고민하다가 D가 가장 적합해 보여서 골랐다. RDS 시간 지정해놓고 끄는 게 Lambda 쓰는 거 밖에 없다는 게 신기하다.

- EventBridge : 거의 실시간으로 이벤트 자동 전송. 이벤트 패턴 / 일정에 따라 설정 가능

### 고민하다가 틀린 문제

Q. 회사에서 AWS에 새로운 공개 웹 애플리케이션을 배포하고 있습니다. 애플리케이션은 ALB(Application Load Balancer) 뒤에서 실행됩니다. 애 플리케이션은 외부 CA(인증 기관)에서 발급한 SSL/TLS 인증서를 사용하여 에지(Edge)에서 암호화해야 합니다. 인증서가 만료되기 전에 매년 인증서를 교체해야 합니다. 솔루션 설계자는 이러한 요구 사항을 충족하기 위해 무엇을 해야 합니까?

(A). AWS Certificate Manager(ACM)를 사용하여 SSL/TLS 인증서를 발급합니다. 인증서를 ALB에 적용합니다.관리형 갱신 기능을 사용하여 인증서를 자동으로 교체합니다. 

(B). AWS Certificate Manager(ACM)를 사용하여 SSL/TLS 인증서를 발급합니다. 인증서에서 키 구성요소를 가져옵니다. 인증서를 ALB에 적용합  
니다. 관리형 갱신 기능(managed renewal feature)을 사용하여 인증서를 자동으로 교체합니다.  

(C). AWS Certificate Manager(ACM) 사설 인증 기관을 사용하여 루트 CA에서 SSL/TLS 인증서를 발급합니다. 인증서를 ALB에 적용합니다. 관리  
형 갱신 기능을 사용하여 인증서를 자동으로 교체합니다.  

(D). AWS Certificate Manager(ACM)를 사용하여 SSL/TLS 인증서를 가져옵니다. 인증서를 ALB에 적용합니다. Amazon EventBridge(Amazon CloudWatch Events)를 사용하여 인증서가 만료될 때 알림을 보냅니다. 인증서를 수동으로 교체합니다.

A. (D)

완전히 같은 문제는 아니었고 비슷했는데 A와 비슷한 답을 골랐던 것 같다. 외부 인증서는 무조건 ACM 자동교체 기능 미제공이라서 만료될 때 알림받고 수동 교체가 최선이다 ㅠㅠㅠ

---

Q. 회사가 Amazon S3 버킷에 민감한 사용자 정보를 저장하고 있습니다. 회사는 VPC 내부의 Amazon EC2 인스턴스에서 실행되는 애플리케이션  계층에서 이 버킷에 대한 보안 액세스를 제공하려고 합니다.  
작업 수행을 위해 솔루션 설계자는 어떤 조합의 단계를 취해야 하나요? (2개를 선택하십시오.)

(A). VPC 내 Amazon S3용 VPC 게이트웨이 엔드포인트 구성  

(B). S3 버킷에 대한 객체를 퍼블릭으로 만들기 위한 버킷 정책 생성  

(C). VPC에서 실행되는 애플리케이션 계층으로만 액세스를 제한하는 버킷 정책 생성  

(D). S3 액세스 정책으로 IAM 사용자를 생성하고 IAM 자격 증명을 EC2 인스턴스에 복사  

(E). NAT 인스턴스를 생성하고 EC2 인스턴스가 NAT 인스턴스를 사용하여 S3 버킷에 액세스하도록 구성

A. (A), (C)

이거 끝까지 고민하다가 VPC에서 실행되는 애플리케이션 계층으로만 액세스를 제한하는 버킷 정책을 어떻게 만들지? 싶어서 D 골랐던 것 같다 ㅠㅠ 현실은 
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE4NTU0ODE5MjMsLTE5Nzk0NTgzNTAsLT
EyNjI2NTU0MDUsLTI2MTY5NDhdfQ==
-->