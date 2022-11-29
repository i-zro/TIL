# 2. 클라우드 컴퓨팅

## 2_4. ELB
- ALB에는 탄력적 IP 주소 할당 불가

## 2_5. 메시징 및 대기열
- SNS는 DB로 메시지를 바로 전송 할 수 없음.

# 4. 네트워킹
- Systems Manager 세션 관리자를 통한 콘솔 액세스는 인터넷 연결이므로 VPN보다 안전하지 않음.

## 4_2. 서브넷 및 네트워크 액세스 제어 목록
- 보안그룹은 

# 5. 스토리지 및 데이터베이스
- EFS는 내구성에 대한 공식적 보장은 없음, S3는 99.999999999% 내구성 보장
- SMB 프로토콜(-> FSx)은 윈도우 OS 인스턴스 지원, NFS 프로토콜(->EFS)은 리눅스 OS 인스턴스 지원

## 5_1. 인스턴스 스토어
- 인스턴스 스토어가 IOPS 성능이 가장 높음.

## 5_2. S3
- Glacier은 아카이브용 스토리지 클래스
- S3 Transfer Acceleration은 <bucket>.s3-accelerate.amazonaws.com를 사용하여 업로드 해야 함.

## 5_4. RDS
- 다중 AZ RDS는 재해 복구용 예비 복제본으로, Read Replica처럼 읽기 트래픽 처리 불가.
- RDS는 자동 백업이 활성화 되어 있어야 DB 인스턴스를 특정 시점으로 복구 가능

<!--stackedit_data:
eyJoaXN0b3J5IjpbLTgxNzA2ODQzLC0yMTQ3MzQ1NTIzLDE5Mz
Q4NzQ4NDksNzM3MzY1NzgsMTUxMTg3ODUyOCwzMTkxNjUxNjAs
MTY1Mzg1ODE0OCwxNDg5NzQzNzQwLC0xMTI0MTAxOTM3LC01MD
M4MDEyOTAsLTE1MjQzNTMxNzksLTc5MDgyNDA2OF19
-->