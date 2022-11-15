# 5. 스토리지 및 데이터 베이스

# 5_1. 인스턴스 스토어 및 Amazon Elastic Block Store(Amazon EBS)
 
- 블록 수준 스토리지 볼륨은 물리적 하드 드라이브처럼 동작함.

## 인스턴스 스토어

- 인스턴스 스토어는 EC2 인스턴스에 임시 블록 수준 스토리지를 제공
- 물리적으로 EC2 인스턴스의 호스트 컴퓨터에 연결되어 있고, 따라서 인스턴스와 수명이 동일한 디스크 스토리지
- 인스턴스가 종료되면 인스턴스 스토어의 데이터가 손실됨.
- 임시데이터가 포함 됐을 때 사용하는 게 좋음.
 
**※ 볼륨(Volume)이란?**

- 파일 시스템으로 포맷된 디스크상의 저장영역
- 하나의 파일 시스템을 갖춘 하나의 접근 가능한 스토리지 영역
 

## Amazon EBS (Amazon Elastic Block Store)
- 단일 가용 영역에 데이터 저장
- EC2 인스턴스에서 사용할 수 있는 블록 수준 스토리지 볼륨을 제공하는 서비스

- EC2 인스턴스를 `중지 또는 종료하더라도` 연결된 EBS 볼륨의 모든 데이터를 사용할 수 있음.
- EBS 볼륨을 생성하려면 구성(크기&유형)을 정의하고 볼륨을 프로비저닝함. -> 그 다음 EBS 볼륨을 생성하고 EC2 인스턴스에 연결
- 스냅샷을 생성하여 증분 백업 가능 (처음 볼륨을 백업하면 모든 데이터가 복사 -> 이후의 백업에서는 가장 최근의 스냅샷 이후 변경된 데이터 블록만 저장 ↔ 전체 백업은 변경되지 않은 데이터도 포함됨.)

![](https://i.imgur.com/WFLImHY.png)


※ **블록스토리지**에서 파일을 수정하면 변경된 부분만 업데이트 됨. ↔ **객체 스토리지(S3)**는 전체 개체가 업데이트 됨.


# 5_2. Amazon Simple Storage Service (Amazon S3)
 
## 객체 스토리지

![](https://i.imgur.com/Jt74RXT.png)

- 각 객체는 데이터, 메타데이터, 키로 구성
    - 데이터 : 이미지, 동영상, 텍스트 등등
    - 메타데이터 : 데이터의 내용, 사용 방법, 객체 크기 등에 대한 정보가 포함
    - 키 : 고유한 식별자

## Amazon Simple Storage Service(Amazon S3)

- 객체 수준 스토리지를 제공하는 서비스
- 데이터를 버킷에 객체로 저장
- 모든 유형 파일 업로드 가능
- 저장 공간 무제한, 저장할 수 있는 객체 최대 크기 5TB

**※ 객체와 버킷**

하드 드라이브에 있는 
- 파일은 "객체"
- 파일 디렉터리는 "버킷"


## Amazon S3 스토리지 클래스
- S3는 사용한 만큼만 비용 지불, 요구 사항에 맞춰 다양한 스토리지 클래스 중 선택 가능.
- 선택 기준
    - 데이터를 검색할 빈도
    - 필요한 데이터 가용성


### S3 스토리지 클래스 종류 

1. S3 Standard
- 자주 액세스 하는 데이터용으로 설계
- 최소 3개의 가용 영역에 데이터 저장
- 데이터분석, 콘텐츠 배포 등 광범위한 사례에 적합
- 자주 액세스하지 않는 데이터 및 보관 스토리지를 위한 다른 스토리지 클래스보다 비용이 높다!
 

2. S3 Standard-Infrequent Access = S3 Standard-IA
- 자주 액세스하지 않는 데이터에 이상적 
- Standard와 비슷하지만 가격은 더 저렴하고 검색 가격은 더 높음.
- 최소 3개의 가용 영역에 데이터 저장
 

3. S3 One Zone-Infrequent Access = S3 One Zone-IA
- 단일 가용 영역에 데이터 저장
- S3 Standard-IA 보다 낮은 스토리지 가격
 

4. S3 Intelligent-Tiering
- 액세스 페턴을 알 수 없거나 자주 변화하는 데이터에 이상적
- 객체당 소량의 월별 모니터링 및 자동화 요금을 부과함. (객체의 액세스 패턴을 모니터링 -> 30일 연속 객체에 액세스하지 않으면 Amazon S3는 자동으로 해당 객체를 자주 사용하지 않는 액세스 계층인 S3 Standard-IA로 이동, 사용자가 자주 사용하지 않는 액세스 계층에 저장된 객체에 액세스하면 Amazon S3는 자동으로 해당 객체를 자주 사용하는 액세스 계층인 S3 Standard로 이동)

5. S3 Glacier
- 데이터 보관용으로 설계된 이상적인 저비용 스토리지
- 객체를 몇 분에서 몇 시간 이내에 검색
 

6. S3 Glacier Deep Archive
- 보관에 이상적인 가장 저렴한 객체 스토리지 클래스
- 객체를 12시간 이내에 검색

---

Q. 자주 액세스하지 않는 데이터를 저장하려고 하지만 필요한 경우 즉시 사용할 수 있어야 합니다. 다음 중 어떤 Amazon S3 스토리지 클래스를 사용해야 합니까?

A. S3 Standard-IA

---

# 5_3. Amazon Elastic File System(Amazon EFS)


## Amazon EBS와 EFS 비교

### EBS
단일 가용 영역에 데이터 저장. Amazon EC2 인스턴스를 EBS 볼륨에 연결하려면 Amazon EC2 인스턴스와 EBS 볼륨 모두 동일한 가용 영역에 상주해야 함.

### EFS
- 리전별 서비스라 여러 가용 영역에 걸쳐 데이터를 저장. 중복 스토리지를 사용하면 파일 시스템이 위치한 리전의 모든 가용 영역에서 동시에 데이터에 액세스할 수 있음. 또한 온프레미스 서버는 AWS Direct Connect를 사용하여 Amazon EFS에 액세스할 수 있음.
- 파일을 추가 또는 제거하면 EFS가 자동으로 확장하거나 축소됨.


# 5_4. Amazon Relational Database Service(Amazon RDS)

## Amazon Relational Database Service (RDS)

- AWS 클라우드에서 관계형 데이터베이스를 실행할 수 있는 서비스
- 하드웨어 프로비저닝, 데이터베이스 설정, 패치 적용 백업과 같은 작업을 자동화하는 관리형 서비스
- 다양한 보안 옵션 제공
    - 저장 시 암호화(데이터가 저장되는 동안 데이터를 보호) 및 전송 중 암호화(데이터를 전송 및 수신하는 동안 데이터를 보호)를 제공

### 지원되는 데이터베이스 엔진

- Amazon Aurora
- PostgreSQL
- MySQL
- MariaDB
- Oracle Database
- Microsoft SQL Server

### Amazon Aurora

- 엔터프라이즈급 관계형 데이터베이스
- MySQL 및 PostgreSQL 관계형 데이터베이스와 호환
    - 표준 MySQL 데이터베이스보다 최대 5배 빠르며 표준 PostgreSQL 데이터베이스보다 최대 3배 빠름
- 상용 데이터베이스 비용의 10분의 1
- 고가용성
    - 6개의 데이터 복사본을 3개의 가용 영역에 복제하고 지속적으로 Amazon S3에 데이터를 백업


# 5_5. Amazon DynamoDB

## Amazon Dynamo DB

- 비관계형 (NoSQL)
- 서버리스
- 자동 조정
    - 데이터베이스 크기가 축소 또는 확장되면 DynamoDB는 용량 변화에 맞춰 자동으로 크기를 조정하면서도 일관된 성능을 유지

### 관계형 vs 비관계형

- 관계형은 여러 테이블에 있는 데이터의 복잡한 분석에 유리
- 비관계형은 오버헤드를 모두 제거하여 강력하고 응답시간이 매우 바르며 복잡한 조인 기능이 필요 없고 확장성 또한 뛰어남.

Q. 다음 중 Amazon Relational Database Service(Amazon RDS)를 사용해야 하는 시나리오는 무엇입니까? (2개 선택)

- 서버리스 데이터베이스 실행

- [x] SQL을 사용하여 데이터 구성

- 키-값 데이터베이스에 데이터 저장

- 하루 최대 10조 개 요청으로 확장

- [x] Amazon Aurora 데이터베이스에 데이터 저장

# 5_6. Amazon Redshift

## Amazon Redshift
- 데이터 웨어하우징 서비스
    - 여러 원본에서 데이터를 수집하여 데이터 간의 관계 및 추세를 파악하는 데 도움

# 5_7. AWS Database Migration Service

## AWS Database Migration Service(AWS DMS)

- 관계형 데이터베이스, 비관계형 데이터베이스 및 기타 유형의 데이터 저장소를 마이그레이션할 수 있는 서비스

- 애플리케이션 가동 중지 시간 최소화
    - 마이그레이션이 진행되는 동안 소스 데이터베이스의 모든 기능이 정상 작동
    - 라이브 마이그레이션이라고 불리는 연속 데이터베이스 복제도 가능 -> 일회성 마이그레이션을 수행하는 것이 아니라 데이터의 진행 중 복제본을 다른 대상 원본으로 전송
        - 프로덕션 데이터베이스의 복사본을 개발 또는 테스트 환경으로 1회 혹은 연속으로 마이그레이션
- 원본 데이터베이스와 대상 데이터베이스 유형이 동일할 필요 없음.
    -    첫 번째 단계는 원본과 대상의 스키마 구조, 데이터 유형, 데이터베이스 코드가 다르므로 먼저 Amazon Schema Conversion(SCT) 툴 사용하여 변환
    -    DMS를 사용하여 원본 데이터베이스의 데이터를 대상 데이터베이스로 마이그레이션
- 데이터 베이스 통합
    - 여러 데이터베이스를 단일 데이터베이스로 결합


# 5_8. 추가 데이터베이스 서비스

- Amazon DocumentDB

	- MongoDB 워크로드를 지원하는 문서 데이터베이스 서비스
    - 콘텐츠 관리, 카탈로그, 사용자 프로필 등에 적합
 

- Amazon Neptune

그래픽 데이터베이스 서비스
 

- Amazon Quantum Ledger Database (Amazon QLDB)
    - 원장 데이터베이스 서비스
    - 모든 변경 사항 전체 기록 검토 가능
 

- Amazon Managed Blockchain

오픈소스 프레임워크를 사용하여 블록체인 네트워크를 생성하고 관리
 

- Amazon ElastiCashe

    - 자주 사용되는 요청의 읽기 시간을 향상시키기 위해 데이터베이스 위에 캐싱 계층을  추가하는 서비스
    - Redis 및 Memcached를 지원함.
 

- Amazon DynamoDB Accelerator

    - DynamoDB용 인 메모리 캐시
    - 응답 시간을 한 자릿수 밀리초에서 마이크로초까지 향상시킬 수 있음.
 

 ---
 Q. 다음 중 보관 데이터에 최적화된 Amazon S3 스토리지 클래스는 무엇입니까? (2개 선택)

- S3 Standard

- [x] S3 Glacier

- S3 Intelligent-Tiering

- S3 Standard-IA

- [x] S3 Glacier Deep Archive
 
 ---
 
 Q. 다음 중 Amazon EBS 볼륨 및 Amazon EFS 파일 시스템에 대한 설명은 무엇입니까?

A. EBS 볼륨은 단일 가용 영역에 데이터를 저장합니다. Amazon EFS 파일 시스템은 여러 가용 영역에 데이터를 저장합니다.

---

Q. 객체 스토리지 서비스에 데이터를 저장하려고 합니다. 다음 중 이러한 유형의 스토리지에 가장 적합한 AWS 서비스는 무엇입니까?

A. Amazon Simple Storage Service(Amazon S3)

---

Q. 다음 중 Amazon DynamoDB를 가장 잘 설명한 것은 무엇입니까?

A. 서버리스 키-값 데이터베이스 서비스

---

**Q. 다음 중 데이터웨어 하우스에서 데이터를 쿼리하고 분석하는 데 사용되는 서비스는 무엇입니까?**

A. Amazon Redshift

---
---

참고 : AWS Cloud Practitioner Essentials

---
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTM2NzY4ODYyMF19
-->