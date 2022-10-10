# Execution failed for task ':test'. [Spring / 트러블 슈팅]
## 🎈 개요
![Image](https://i.imgur.com/EHlB3u7.png)

```
Execution failed for task ':test'.
> There were failing tests. See the report at: 
```

대충 이런 에러가 나오면서 TDD 코드의 빌드가 안되었다.

## 🔑 원인 추론
- 테스트버튼 누를때, 테스트메서드명이 한글일 경우 표시안됨

## 🎆 조치 및 방안 검토
ctrl+alt+s를 눌러 settings에 들어가서
아래와 같이 테스트구동을  Gradle -> intellij로 바꿔주면 된다

- File > Settings
![Image](https://i.imgur.com/QkpHaUz.png)

- Build 쪽에 Gradle 탭의 'Run tests using' 부분이 gradle로 되어있을텐데, 이를 IntelliJ IDEA로 바꾼다.
![Image](https://i.imgur.com/LUkGvKZ.png)

- 깔끔히 통과
![Image](https://i.imgur.com/H7GkRPM.png)