# 9. 마이그레이션 및 혁신

# 9_1. AWS Cloud Adoption Framework(AWS CAF)

## Cloud Adoption Framework의 6가지 주요 관점

- 비즈니스 기능에 중점
    - 비즈니스
        -  IT가 비즈니스 요구 사항을 반영하고 IT 투자가 주요 비즈니스 결과와 연계되도록 보장
    - 인력
        - 클라우드 채택을 성공하기 위한 조직 전반의 변화 관리 전략 개발을 지원
    - 거버넌스
        - IT 전략이 비즈니스 전략에 부합하도록 조정하는 기술 및 프로세스에 중점
- 기술 역량에 중점
    - 플랫폼
        - 클라우드로 마이그레이션하기 위한 원칙과 패턴이 포함
        - 다양한 아키텍처 모델을 사용하여 IT 시스템의 구조와 그 관계를 이해하고 전달
    - 보안
        - 가시성, 감사 가능성, 제어 및 민첩성에 대한 보안 목표를 충족하도록 보장
        - 조직의 요구 사항에 맞춰 보안 제어의 선택 및 구현을 구성
    - 운영
        - 비즈니스 이해당사자와 합의된 수준까지 IT 워크로드를 구현, 실행, 사용, 운영 및 복구하는 데 도움

**<span style="color:red">Q. AWS Cloud Adoption Framework에서 비즈니스 목표 및 관점에 따라 AWS 인프라를 설계, 구현 및 최적화하는 데 도움이 되는 관점은 무엇입니까?</span>**

A. 플랫폼 관점

# 9_2. 마이그레이션 전략

## 6가지 마이그레이션 전략

- 리호스팅(Rehosting)
    - lift-and-shift, 애플리케이션 변경 없이 이전
- 리플랫포밍(Replatforming)
    - lift, tinker, and shift
    - 몇 가지 클라우드 최적화 수행 필요 (핵심 아키텍처 변경 없이 달성)
- 리팩터링(Refactoring)/아키텍처 재설계(Re-architecting)
    - 아키텍처 재설계라고도 함
    - 기존 환경의 애플리케이션에서 실행하기 까다로운 기능 추가, 확장 또는 성능 개선의 필요성이 클 때 활용
- 재구매(Repurchasing)
    - 기존 라이선스를 Software-as-a-Service 모델로 전환
- 유지(Retaining)
    - 비즈니스에 중요한 애플리케이션을 소스 환경에 유지
- 폐기(Retiring)
    - 더 이상 필요하지 않은 애플리케이션 제거


**Q. 다음 중 다른 제품으로 전환하는 마이그레이션 전략은 무엇입니까?**

A. 재구매

# 9_3. AWS Snow 패밀리

## AWS Snow 패밀리 멤버

- AWS와 고객 간에 최대 엑사바이트 규모의 데이터를 물리적으로 이동할 수 있는 물리적 디바이스 모음
- 모든 데이터는 자동으로 암호화
- AWS Snowcone, AWS Snowball 및 AWS Snowmobile로 구성

![](https://i.imgur.com/YBb1V5J.png)

### AWS Snowone
- 작고 견고하며 안전한 엣지 컴퓨팅 및 데이터 전송 디바이스
- CPU 2개, 4GB 메모리 및 **8TB**의 가용 스토리지

### AWS Snowball
- 두 가지 유형의 디바이스 제공
- 클러스터링 가능
    - **Snowball Edge Storage Optimized**
        -  대규모 데이터 마이그레이션 및 반복 전송 워크플로뿐 아니라 큰 용량이 필요한 로컬 컴퓨팅에 적합
        -  스토리지: 블록 볼륨 및 Amazon S3 호환 객체 스토리지를 위한 80TB의 하드 디스크 드라이브(HDD) 용량, 블록 볼륨을 위한 1TB의 SATA 솔리드 스테이트 드라이브(SSD) 용량
        - 컴퓨팅: Amazon EC2 sbe1 인스턴스(C5와 동등)를 지원하기 위한 40개의 vCPU와 80GiB의 메모리
    - **Snowball Edge Compute Optimized**
        - 기계 학습, 풀 모션 비디오 분석, 분석 및 로컬 컴퓨팅 스택과 같은 사용 사례를 위한 강력한 컴퓨팅 리소스를 제공
        - 스토리지: Amazon S3 호환 객체 스토리지 또는 Amazon EBS 호환 블록 볼륨을 위한 42TB의 가용 HDD 용량과 Amazon EBS 호환 블록 볼륨을 위한 7.68TB의 가용 NVMe SSD 용량
        - 컴퓨팅: 52개의 vCPU, 208GiB 메모리 및 NVIDIA Tesla V100 GPU 옵션. 디바이스는 C5, M5a, G3 및 P3 인스턴스와 동등한 Amazon EC2 sbe-c 및 sbe-g 인스턴스를 실행합니다.

### AWS Snowmobile
- 대용량 데이터를 AWS로 이동하는 데 사용하는 엑사바이트 규모의 데이터 전송 서비스
- 세미 트레일러 트럭으로 견인되는 45피트 길이의 견고한 운반 컨테이너인 Snowmobile 1대당 최대 100페타바이트의 데이터를 전송

---

Q. Snowball Edge Storage Optimized의 스토리지 용량은 얼마입니까?

A. 80TB

---

# 9_4. AWS를 통한 혁신

## AWS 서비스를 통한 혁신

- VMware Cloud on AWS
    - 온프레미스에서 사용하는 동일한 VMware 기반 인프라는 많은 경우에 이를 통해 AWS에 그대로 옮기기 가능
- 서버리스 애플리케이션
- 인공지능
    - Amazon Transcribe를 사용하여 음성을 텍스트로 변환
    - Amazon Comprehend를 사용하여 텍스트에서 패턴을 검색
    - Amazon Fraud Detector를 사용하여 잠재적인 온라인 사기 행위를 식별
    - Amazon Lex를 사용하여 음성 및 텍스트 챗봇 빌드
- 기계학습
    - 어려운 작업을 제거하여 ML 모델을 신속하게 빌드, 훈련, 배포하는 데 사용할 수 있는 Amazon SageMaker를 제공
    - Amazon Textract는 스캔한 문서에서 텍스트 및 데이터를 자동으로 추출하는 기계 학습 서비스
    - AWS DeepRacer는 강화 학습 모델을 테스트하는 데 사용할 수 있는 1/18 크기의 자율 주행 경주용 자동차
- MongoDB 워크로드를 지원하는 문서 데이터베이스 서비스는 Amazon DocumentDB

---
Q. 다음 중 기계 학습 모델을 신속하게 빌드, 훈련, 배포할 수 있는 서비스는 무엇입니까?

A. Amazon SageMaker

---

**<span style="color:red">Q. AWS Cloud Adoption Framework에서 권한의 선택 및 구현을 구성하는 데 도움이 되는 관점은 무엇입니까?</span>**

A. 보안 관점

---

**<span style="color:red">Q. 다음 중 6가지 애플리케이션 마이그레이션 전략에 포함되는 전략은 무엇입니까? (2개 선택)</span>**

- 재방문(Revisiting)

- [x] 유지(Retaining)

- 기억하기(Remembering)

- 재개발(Redeveloping)

- [x] 리호스팅(Rehosting)

---

Q. AWS Snowmobile의 스토리지 용량은 얼마입니까?

A. 100PB

---

Q. 다음 중 Amazon Lex를 가장 잘 설명한 것은 무엇입니까?


A. 
음성 및 텍스트를 사용하여 대화형 인터페이스를 빌드할 수 있는 서비스

---

---

참고 : AWS Cloud Practitioner Essentials

---
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTE2MjA3OTczM119
-->