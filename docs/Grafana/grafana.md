# EKS 상 grafana deployment proxy 설정하기 (slack alert 보내기)  

인터넷이 없는 환경에서 grafana에서 외부의 슬랙으로 슬랙 alert를 보내려하면 proxy server를 타고 가야하는데, 이 proxy 설정에서 막혀서 다소 막막했다.

proxy 설정만 하면 grafana 화면에서 prometheus 데이터가 전혀 불러와지지 않는 문제가 있었다.

https://repost.aws/ko/knowledge-center/eks-http-proxy-configuration-automation

위 게시글 포맷에 맞춰, 프로메테우스 관련된 서비스들의 ip들 및 localhost 등 몽땅 넣어서 no_proxy를 구성하니 죽어도 안되었다.

혹시나 하고 그라파나에 등록된 그냥 서비스 형태대로 no_proxy를 잡자 그제서야 데이터는 정상적으로 불러와지고, slack alert도 정상적으로 갔다. 그렇게 deployment에 설정한 구성은 아래와 같다.

```
 37     spec:
 38       containers:
 39       - env:
 40         - name: HTTP_PROXY
 41           value: [프록시서버:포트]
 42         - name: HTTPS_PROXY
 43           value: [프록시서버:포트]
 44         - name: NO_PROXY
 45           value: influxdb.influxdb.svc,prometheus-server.prometheus.svc
 ```

끄앙 너무 미묘한 차이로 안되는 게 킹 받는다. 어디서 안되는 건지 뭐라도 알려주라고...

확인해보니 대시보드도 잘 나오고,

아래와 같이 그라파나 대시보드에서 토큰 등을 이용해서 이미 슬랙 채널과 연결은 해놓은 상태였기 때문에 (이 부분은 인터넷에 쳐보면 매우매우 많이 나온다.) 테스트 메시지를 보내보면

![Image](https://i.imgur.com/r6vLqdS.png)

![Image](https://i.imgur.com/MJUhhg4.png)

이렇게 매우 잘 오는 것을 확인할 수 있었다.