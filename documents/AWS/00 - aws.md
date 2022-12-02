# 2. 클라우드 컴퓨팅

## 2_4. ELB
- ALB에는 탄력적 IP 주소 할당 불가

## 2_5. 메시징 및 대기열
- SNS는 DB로 메시지를 바로 전송 할 수 없음.

# 3. 글로벌 인프라 및 안정성 

## 3_2. 엣지 로케이션
- CloudFront에 가격 등급에 따라 배포하는 엣지 로케이션을 줄일 수 있음 -> 가격 등급 100이 일부 리전에 배포 하며 가장 낮은 비용

# 4. 네트워킹
- Systems Manager 세션 관리자를 통한 콘솔 액세스는 인터넷 연결이므로 VPN보다 안전하지 않음.

## 4_1. AWS와의 연결
- 온프레미스 네트워크와 VPC를 연결하려면 두 가지 방법이 있음. VPN은 저렴. Direct Connect는 비싼 대신 더 큰 네트워크 대역폭 제공해서 트래픽 안정.
- VPC 엔드포인트 : 인터넷을 통하지 않고 AWS 서비스에 프라이빗하게 연결할 수 있는 VPC 진입점

## 4_2. 서브넷 및 네트워크 액세스 제어 목록
- 보안그룹(인스턴스 레벨)은 거부 규칙 지정 못함. NACL(서브넷 레벨)이 허용 및 거부 규칙 지원. 

# 5. 스토리지 및 데이터베이스
- EFS는 내구성에 대한 공식적 보장은 없음, S3는 99.999999999% 내구성 보장
- SMB 프로토콜(-> FSx)은 윈도우 OS 인스턴스 지원, NFS 프로토콜(->EFS)은 리눅스 OS 인스턴스 지원

## 5_1. 인스턴스 스토어 및 Amazon Elastic Block Store(Amazon EBS)
- 인스턴스 스토어가 IOPS 성능이 가장 높음.
- EBS는 파일 공유 스토리지 아님. EFS가 파일 공유 스토리지.

## 5_2. S3
- Glacier은 아카이브용 스토리지 클래스
- S3 Transfer Acceleration은 <bucket>.s3-accelerate.amazonaws.com를 사용하여 업로드 해야 함.
- S3 삭제 방지 : 버전 관리 + MFA Delete 옵션 추가

## 5_4. RDS
- 다중 AZ RDS는 재해 복구용 예비 복제본으로, Read Replica처럼 읽기 트래픽 처리 불가.
- RDS는 자동 백업이 활성화 되어 있어야 DB 인스턴스를 특정 시점으로 복구 가능

## 5_5. Amazon DynamoDB
- DynamoDB 글로벌 테이블 구성을 통해 재해 복구 시 1초 이내로 다른 리전으로 데이터 복제 및 모든 리전에 읽기/쓰기 가능하므로 서비스 중단 없음.
- RDS는 밀리 초 지연 시간 데이터 저장 및 검색에 부적합 -> noSQL인 DynamoDB가 적합

## 5_8. 추가 데이터베이스 서비스
- elastiCache는 인메모리 데이터 스토어, Memcached보다 Redis가 고가용성, 복제기능, 스냅샷 백업 등 지원
- elastiCache는 반복되는 요청을 캐시에 저장하여 응답속도를 빠르게 하기 위한 기능으로 읽기 패턴을 알 수 없는 경우 비적합

## 5_9. 스토리지 - 기타
- Data Sync가 온라인으로 데이터 마이그레이션 솔루션를 AWS로 자동 전송, Snowball Edge는 오프라인!가  

# 10. 기타
- 클릭 스트림 데이터 -> Kinesis
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTIwODcwODM0MzgsOTMyMzM0MjIwLDEwND
g2MDUyNTAsLTIwMTY4MjA0NzEsMTQ3NjU4NTM1Nyw0MDQ3Mzcw
NzEsMTY0Mzg2NDkyOCwxNTUzOTYwMDAwLDEzOTM1Nzk5NDIsMz
U5ODY2NTg3LDc4MzUzMzg5MSwtNTQ0MjUxNjg0LDc4MzUzMzg5
MSw3NDc0MjI0MDQsMTM4MTQ4NDg4NCwtMjE0NzM0NTUyMywxOT
M0ODc0ODQ5LDczNzM2NTc4LDE1MTE4Nzg1MjgsMzE5MTY1MTYw
XX0=
-->