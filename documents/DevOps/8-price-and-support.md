# 8. 요금 및 지원

# 8_1. AWS 프리티어

- 상시 무료
    - 만료 없음
    - AWS Lambda에서는 매월 무료 요청 1백만 건과 최대 320만 초의 컴퓨팅 시간 제공
    - Amazon DynamoDB에서는 매월 25GB의 무료 스토리지
- 12개월 무료
    - AWS에 처음 가입한 날로부터 12개월 동안 무료
    - 일정량의 Amazon S3 Standard 스토리지, 월별 Amazon EC2 컴퓨팅 시간 한도, Amazon CloudFront 데이터 전송량
- 평가판
    - Amazon Inspector는 90일 무료 평가판을 제공
    - Amazon Lightsail(가상 프라이빗 서버를 실행할 수 있는 서비스)은 30일 동안 750시간의 무료 사용 시간을 제공

Q. AWS 프리 티어에는 신규 AWS 고객에게 AWS 가입 날짜 이후 일정 기간 동안 제공되는 제품이 포함되어 있습니다. 이 기간은 얼마입니까?

A. 12개월

# 8_2. AWS 요금 개념

## AWS 요금 적용 방식

- 종량제 요금
    - 실제 사용한 만큼만 지불
    - 예약하는 경우 비용 감소 (Amazon EC2 Instance Savings Plans 최대 72%)
    - 많이 사용할수록 볼륨 기반 할인으로 비용 감소 (Amazon S3 스토리지 공간을 많이 사용할수록 GB당 비용을 낮출 수 있음)

## AWS 요금 계산기

- https://calculator.aws/#/

- AWS 비용 추정을 정의된 그룹별로 구성 가능
- 필요한 운영 체제, 메모리 요구 사항, 입/출력(I/O) 요구 사항 등 세부 정보를 입력 후 AWS 리전 및 EC2 인스턴스 유형별로 예상 비용을 비교 가능

### 요금 청구 항목

- Lambda : 함수 요청 수 및 기간
- EC2
    - 사용된 각 Amazon EC2 인스턴스 유형
    - 프로비저닝된 Amazon EBS 스토리지 공간
    - Elastic Load Balancing이 사용된 기간

- S3
    - 버킷에 객체를 추가 또는 복사하기 위한 요청 수
    - 버킷에서 객체를 검색하기 위한 요청 수
    - 사용된 스토리지 공간


# 8_3. 결제 대시보드

## 결제 대시보드

- AWS 청구서를 결제하고, 사용량을 모니터링하고, 비용을 분석 및 제어
    - 이번 달 누계 금액을 지난 달과 비교하고 현재 사용량을 기준으로 내달 사용량을 예측합니다.
    - 서비스별 월 누계 지출을 확인합니다.
    - 서비스별 프리 티어 사용량을 확인합니다.
    - Cost Explorer에 액세스하여 예산을 생성합니다.
    - Savings Plans를 구매하고 관리합니다.
    - AWS 비용 및 사용 보고서를 게시합니다.


# 8_4. 통합 결제

## 통합 결제

- AWS Organizations는 통합 결제 옵션을 제공
    - 조직의 모든 AWS 계정에 대한 단일 청구서를 받을 수 있음
- 기본적으로 조직에 허용되는 최대 계정 수는 4개이지만, 필요한 경우 AWS Support에 문의하여 할당량을 늘릴 수 있음


# 8_5. AWS 예산

## AWS 예산

- https://aws.amazon.com/ko/aws-cost-management/aws-budgets/
- 예산을 생성하여 서비스 사용, 서비스 비용 및 인스턴스 예약을 계획
- 정보가 하루에 세 번 업데이트
- 예산 금액을 초과하거나 초과할 것으로 예상되면 알려주는 사용자 지정 알림을 설정 가능

# 8_6. AWS Cost Explorer

## AWS Cost Explorer

- https://aws.amazon.com/ko/aws-cost-management/aws-cost-explorer/
- 시간 경과에 따라 AWS 비용 및 사용량을 시각화, 이해, 관리할 수 있는 도구
- 발생 비용 기준 상위 5개 AWS 서비스의 비용 및 사용량에 대한 기본 보고서가 포함
- 사용자 지정 필터 및 그룹을 적용하여 데이터를 분석 가능

![](https://i.imgur.com/qmftaQe.png)


# 8_7. AWS Support 플랜

## AWS Support

AWS는 문제를 해결하고 비용을 절감하며 AWS 서비스를 효율적으로 사용하는 데 도움이 되는 네 가지 Support 플랜을 제공

- Basic
- Developer
- Business
- Enterprise

### Basic Support
- 모든 AWS 고객에게 무료
- 백서, 설명서 및 지원 커뮤니티에 대한 액세스가 포함
- 제한된 AWS Trusted Advisor 검사에 액세스 가능
- AWS에 결제 관련 질문 및 서비스 한도 증가에 대해 문의 가능
- 사용자에게 영향을 줄 수 있는 이벤트가 발생할 때 알림 및 수정 지침을 제공하는 도구인 **AWS Personal Health Dashboard**를 사용 가능

### Developer, Business 및 Enterprise Support
- 월 단위 비용 지불
- 장기 계약 필요 없음
- 가격의 경우 Developer 플랜이 가장 낮고 Business 플랜은 중간이며 Enterprise 플랜이 가장 높음

#### Developer
- 모범 사례 지침
- 클라이언트 측 진단 도구
- AWS 제품, 기능 및 서비스를 함께 사용하는 방법에 대한 지침으로 구성된 빌딩 블록 아키텍처 지원

```
예를 들어 회사에서 AWS 서비스를 탐색한다고 가정해 보겠습니다. 여러분은 몇 가지 AWS 서비스에 대해 들었습니다. 그러나 이러한 서비스를 함께 사용하여 회사의 요구 사항을 해결할 수 있는 애플리케이션을 빌드하는 방법은 잘 모르겠습니다. 이 시나리오에서는 Developer Support 플랜에 포함된 빌딩 블록 아키텍처 지원을 통해 특정 서비스 및 기능을 결합할 수 있는 기회를 파악할 수 있습니다.
```

#### Business
- 특정 요구 사항을 가장 잘 지원할 수 있는 AWS 제품, 기능 및 서비스를 식별하기 위한 사용 사례 지침
- 모든 AWS Trusted Advisor 검사
- 일반적인 운영 체제 및 애플리케이션 스택 구성 요소와 같은 타사 소프트웨어에 대한 제한된 지원

```
회사가 Business Support 플랜을 보유 중이고 Amazon EC2 인스턴스에 일반적인 타사 운영 체제를 설치하려고 한다고 가정해 보겠습니다. AWS Support에 운영 체제 설치, 구성 및 문제 해결에 대한 지원을 요청할 수 있습니다. 성능 최적화, 사용자 지정 스크립트 사용 또는 보안 문제 해결과 같은 고급 항목의 경우에는 타사 소프트웨어 공급자에게 직접 문의해야 할 수 있습니다.
```

#### Enterprise

- Basic, Developer 및 Business Support 플랜에 포함된 모든 기능 외에도 다음과 같은 기능에 액세스 가능

- 회사의 특정 사용 사례 및 애플리케이션을 지원하기 위한 컨설팅 관계인 애플리케이션 아키텍처 지침
- 인프라 이벤트 관리 지원: 회사가 사용 사례를 더 잘 이해할 수 있도록 돕는 AWS Support와의 단기 계약. 또한 회사에 아키텍처 및 확장 지침도 제공
- 기술 계정 관리자(TAM) 포함

```
회사에 Enterprise Support 플랜이 있는 경우 TAM이 AWS 측 주 연락 창구입니다. 여러분이 애플리케이션을 계획, 배포, 최적화할 때 TAM이 지속적으로 커뮤니케이션하면서 권장 사항, 아키텍처 검토를 제공합니다. 

TAM은 모든 AWS 서비스에 대한 전문 지식을 제공합니다. 통합 접근 방식을 통해 여러 서비스를 함께 효율적으로 사용하는 솔루션을 설계하는 과정을 도울 수 있습니다.
```

Q. 다음 중 최저 비용으로 모든 AWS Trusted Advisor 검사를 포함하는 Support 플랜은 무엇입니까?

A. Business


# 8_8. AWS Marketplace

## AWS Marketplace

![](https://i.imgur.com/8uxpvzM.png)

- Independent Software Vendor(ISV)의 소프트웨어 리스팅 수천 개가 포함된 디지털 카탈로그
- AWS 아키텍처에서 실행되는 타사 소프트웨어를 검색, 배포, 관리하는 단계를 간소화하는 큐레이트된 디지털 카탈로그로서 다양한 결제 옵션을 제공
- 각 리스팅에 대해 요금 옵션, 사용 가능한 지원 및 다른 AWS 고객의 리뷰 등 자세한 정보에 액세스

---

Q. 다음 중 통합 결제에서 수행할 수 있는 작업은 무엇입니까?

- 예상 AWS 사용량을 기준으로 월말 비용을 검토

- AWS 기반 사용 사례에 대한 비용을 추정

- [x] 대량 구매 할인을 적용받기 위해 계정 간 사용량을 결합

- 시간 경과에 따라 AWS 비용 및 사용량을 시각화 및 관리


Q. 다음 중 시간 경과에 따라 AWS 비용 및 사용량을 시각화, 이해, 관리하는 데 사용되는 요금 도구는 무엇입니까?

A. AWS Cost Explorer


---

Q. 다음 중 서비스 사용량이 정의한 임계값을 초과할 때 알림을 받을 수 있는 요금 도구는 무엇입니까?

A. AWS 예산

---

Q. 회사가 AWS 기술 지원 관리자(TAM)로부터 지원을 받으려고 합니다. 다음 중 어떤 Support 플랜을 선택해야 합니까?

A. Enterprise

---

Q. 다음 중 AWS에서 실행되는 타사 소프트웨어를 검색하는 데 사용되는 서비스 또는 리소스는 무엇입니까?

A. AWS Marketplace

---


<!--stackedit_data:
eyJoaXN0b3J5IjpbMTIxMzAyNjI1OF19
-->