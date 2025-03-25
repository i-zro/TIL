# ✅ Kafka Broker 이해하기

Kafka broker는 Apache Kafka 클러스터 내에서 데이터를 수신, 저장, 전송하는 서버이다. Kafka 생태계의 핵심 컴퓨팅 노드이며, 메시지를 불변한 순서로 저장하는 **topic partition (로그 파일)** 을 갖고 있음.

---

## 📌 Broker의 기본

- **Broker**: 여러 개의 partition에 데이터를 저장하며, producer와 consumer 간 메시지 전달을 중계하는 서버임.  
- **Broker ID**: 각 Kafka broker는 고유한 정수형 ID로 식별됨.  
- **Bootstrap Server**: 모든 Kafka broker는 bootstrap server로 동작함. 클러스터 전체에 접근하기 위해서는 하나의 broker에만 연결하면 됨.  
- **Cluster**: 여러 Kafka broker가 함께 동작하며 데이터와 처리 부하를 분산하는 집합체임.

---

## 🔹 데이터 분산

- **Topic Partitions**: broker는 topic의 일부인 partition을 저장함. partition은 클러스터 전체 broker에 분산되어 저장되며, 부하를 균형 있게 분산함.  
- **Horizontal Scaling**: broker를 추가하면 Kafka는 수평적으로 확장됨. 데이터가 클러스터 전체에 더 고르게 분산됨.  
- **Broker Discovery**: 각 broker는 클러스터 내 모든 broker, topic, partition 정보를 알고 있음.

---

## 🔹 핵심 설정 파라미터

### ⚙️ 주요 설정

- **broker.id**: 클러스터 내 각 broker를 고유하게 식별하는 ID.  
- **broker.id.generation.enable**: true로 설정하면 broker ID를 자동으로 생성함.  
- **broker.rack**: broker의 rack 위치를 지정하는 설정. rack-aware replication에 사용됨 (예: `"RACK1"`, `"us-east-1d"`).  
- **bootstrap.servers**: 클라이언트가 Kafka 클러스터에 연결할 때 사용하는 `host:port` 목록.

### ❤️‍🔥 Heartbeat 및 세션 관리 (KRaft 모드 기준)

- **broker.heartbeat.interval.ms**: broker 간 heartbeat를 보내는 주기. 기본값은 2000ms (2초).  
- **broker.session.timeout.ms**: heartbeat 없이 broker가 유지될 수 있는 시간. 기본값은 9000ms (9초).  
- **heartbeat.interval.ms**: consumer가 broker에 heartbeat를 보내는 주기. consumer와 broker 간 세션 유지를 위해 사용됨.

---

## 🔹 Broker의 기능

### ✉️ 메시지 관리

- broker는 producer가 지정한 key 또는 라운드로빈 방식에 따라 메시지를 저장할 partition을 결정함.  
- offset을 추적하여 어떤 메시지가 소비되었고, 어떤 메시지가 아직 남아 있는지 관리함.

### 🔁 복제 관리

- broker는 partition을 여러 서버에 복제하여 장애에 대비함.  
- 각 partition에는 하나의 **leader broker**가 존재하며, 모든 읽기 및 쓰기 요청을 처리함.  
- 나머지 broker는 **follower replica**로 동작하며, leader의 데이터를 복제함. leader 장애 시 새로운 leader로 승격될 수 있음.

### 📚 메타데이터 관리

- broker는 Kafka 클러스터 운영에 필요한 메타데이터를 관리함.  
- topic 생성, partition 수, partition 위치 등의 정보를 추적함.  
- **KRaft 모드**에서는 broker가 **controller** 역할을 수행할 수 있으며, 클러스터 메타데이터를 포함한 이벤트 레코드를 처리함