# 7. 모니터링 및 분석

# 7_1. Amazon CloudWatch

## Amazon CloudWatch
- 다양한 지표를 모니터링 및 관리하고 해당 지표의 데이터를 기반으로 경보 작업을 구성할 수 있는 웹 서비스
- 지표를 사용하여 리소스의 데이터 포인트를 나타냄 -> AWS 서비스는 지표를 CloudWatch로 전송 -> CloudWatch가 이러한 지표를 사용하여 시간 경과에 따라 성능이 어떻게 변화했는지 보여주는 그래프를 자동으로 생성

### CloudWatch 경보
- 지표의 값이 미리 정의된 임계값을 상회 또는 하회할 경우 자동으로 작업을 수행하는 경보를 생성

### Cloudwatch 대시보드

![](https://i.imgur.com/PVyams7.png)

- 대시보드 기능을 사용하면 단일 위치에서 리소스에 대한 모든 지표에 액세스 가능 (CPU 사용률, Amazon S3 버킷에 대해 실행된 총 요청 수 등)

# 7_2. AWS CloudTrail

## AWS CloudTrail

- 계정에 대한 API 호출을 기록
    - API 호출자 ID, API 호출 시간, API 호출자의 소스 IP 주소 등이 포함
- 로그를 안전한 S3 버킷에 무제한으로 저장
    - 변조 방지 기능 사용 가능
- 이벤트는 일반적으로 API 호출 후 15분 이내에 CloudTrail에서 업데이트

```
점주는 Mary라는 이름의 새 IAM 사용자가 생성된 것을 발견하지만 이 사용자를 만든 사람, 시기 또는 방법은 알 수 없습니다.

이러한 의문을 해결하기 위해 AWS CloudTrail로 이동합니다.
```

![](https://i.imgur.com/Ua3ODoE.png)

### CloudTrail Insights

- CloudTrail에서 CloudTrail Insights를 활성화
- 활성화 시 AWS 계정에서 비정상적인 API 활동을 자동으로 감지


**Q. 다음 중 AWS CloudTrail을 사용하여 수행할 수 있는 작업은 무엇입니까? (2개 선택)**

- AWS 인프라 및 리소스 실시간 모니터링

- [x] AWS 인프라 전체에 걸쳐 사용자 활동 및 API 요청 추적

- 지표 및 그래프를 확인하여 리소스 성능 모니터링

- [x] **운영 분석 및 문제 해결을 지원하기 위한 로그 필터링**

- 지표에 대한 응답으로 자동 작업 및 알림 구성

# 7_3. AWS Trusted Advisor

## AWS Trusted Advisor

- AWS 환경을 검사하고 AWS 모범 사례에 따라 실시간 권장 사항을 제시하는 웹 서비스
- **비용 최적화, 성능, 보안, 내결함성, 서비스 한도**라는 5개 범주에서 결과를 AWS 모범 사례와 비교
- 각 범주의 검사에 대해 권장 작업 목록을 제공하고 AWS 모범 사례를 자세히 알아볼 수 있는 추가 자료를 제공

### AWS Trusted Advisor 대시보드

![](https://i.imgur.com/QO56sQ7.png)

- 녹색 체크 표시는 문제가 감지되지 않은 항목 수
- 주황색 삼각형은 권장 조사 항목 수
- 빨간색 원은 권장 조치 수

**Q. 다음 중 Amazon CloudWatch를 사용하여 수행할 수 있는 작업은 무엇입니까? (2개 선택)**

- [x] 리소스 활용도 및 성능 모니터링

- AWS 환경 개선을 위한 실시간 권장 사항 받기

- 5개 범주에서 인프라를 AWS 모범 사례와 비교

- [x] **단일 대시보드에서 지표에 액세스**

- **비정상적인 계정 활동을 자동 감지**


**Q. 다음 중 오픈 액세스 권한을 확인하여 Amazon S3 버킷의 보안을 검토할 수 있는 서비스는 무엇입니까?**

- Amazon CloudWatch

- AWS CloudTrail

- [x] **AWS Trusted Advisor**

- Amazon GuardDuty

```
정답은 AWS Trusted Advisor입니다.



AWS Trusted Advisor는 AWS 환경을 검사하고 AWS 모범 사례에 따라 실시간 권장 사항을 제시하는 웹 서비스입니다. 검사에는 오픈 액세스 권한이 설정된 Amazon S3 버킷과 같은 보안 검사가 포함됩니다.



다른 선택지가 오답인 이유는 다음과 같습니다.

Amazon CloudWatch는 애플리케이션을 실행하는 리소스에 대한 다양한 지표를 모니터링하고 관리할 수 있는 웹 서비스입니다.
AWS CloudTrail은 AWS 환경 내에서 발생한 사용자 활동 및 API 호출에 대한 세부 정보를 검토할 수 있는 웹 서비스입니다.
Amazon GuardDuty는 AWS 환경 및 리소스에 대한 지능형 위협 탐지 기능을 제공하는 서비스입니다. 이 서비스는 AWS 환경 내의 네트워크 활동 및 계정 동작을 지속적으로 모니터링하여 위협을 식별합니다.

```

**Q. 다음 중 AWS Trusted Advisor 대시보드의 범주에 포함되는 항목은 무엇입니까? (2개 선택)**

- 안정성

- [x] **성능**

- 확장성

- 탄력성

- [x] **내결함성**
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTczMTcyMDM5OV19
-->