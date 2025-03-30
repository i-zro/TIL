## Which of the following best describes Kafka as a Distributed Streaming Platform?

- [x] Kafka is primarily a **messaging system** with **real-time streaming** capabilities
- [ ] Kafka is a **batch processing** system for large data analytics

---

## 해설

- Kafka는 **분산 스트리밍 플랫폼**으로 설계 되었고, **Messaging(메시지 발행 및 구독), Storage(데이터 저장), Streaming(실시간 데이터 처리)**를 수행
- Kafka는 실시간 스트리밍에 특화되어 있으며, **배치 분석은 Hadoop/Spark와 같은 도구**가 더 적합함.

---

## When commissioning a new Kafka broker, which of the following is most critical to maintain cluster availability?

- [ ]Replicate the broker logs to new brokers
- [ ] Stop and restart the cluster
- [ ] Assign the broker a higher partition count
- [x] Ensure the broker joins the Zookeeper quorum

---

## 해설

Replicate the broker logs to new brokers
→ 로그 복제는 broker 간 자동으로 처리됨. 수동 복제는 필요 없음.

Stop and restart the cluster
→ Kafka는 무중단 운영을 전제로 설계되었음. 클러스터를 정지할 필요는 없으며, 오히려 위험함.

- partition 개수는 topic 생성 시 결정되며, broker마다 수동으로 설정하지 않음.
- Kafka는 Zookeeper 기반 모드 (KRaft 이전 버전) 에서 클러스터 메타데이터와 브로커 상태 관리를 위해 **Zookeeper**를 사용함. 따라서 새로운 **broker를 클러스터에 추가(commission)**할 때는, 그 **broker가 Zookeeper와 정상적으로 연결되어 클러스터 메타데이터에 등록되는 것이 핵심**이다.