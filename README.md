# 인턴 코드 테스트의 목적

본 레파지토리는 인턴 지원자 분들의 코딩 실력을 테스트하기 위한 테스트 레파지토리입니다.

# 목표

fastapi와 redis를 활용하여, 특정 테스크의 비동기 작업 큐 구조를 만들어 보세요.

## 구현 기능 조건

fastapi의 엔드포인트로 다음을 구현하세요.

1. uuid v4를 key로, 생성 시간을 value로 가지는 객체를 10초동안 랜덤 시간 간격으로 50개 생성해서 redis에 삽입하는 함수
2. redis에 저장된 객체를 0~10개 사이로 랜덤하게 삭제하는 함수
3. redis에 저장된 객체가 몇 개인지 리턴하는 함수
4. redis에 저장된 객체를 입력한 값 수 만큼 리턴하는 함수

## 구현 제약사항

본 프로젝트를 fork해서 자신의 개인 레파지토리에서 진행해 주세요. private으로 만들고 @lectom-dd 계정을 contributor로 추가해 주시면 됩니다.
docker compose up 명령어로 해당 환경이 구동되게 만들어 주세요.

# 평가 항목

- 2024년 2월 23일 금요일에 해당 코드를 가지고 방문하고, 시연 및 코드에 대한 설명 그리고 질의응답과 간략한 기능 추가를 짝 프로그래밍(XP)형태로 진행합니다.
- 동작의 완성도 보다 구현의 방향성과 의도의 선명함. 그리고 문제를 해결해 나갔던 과정을 볼 예정입니다. 코딩 경험과 배경에 따라 쉬울 수도 어려울 수도 있는 과제라고 생각합니다. 감안해 평가할께요.
- Milestone을 정하고 해당 Milestone의 단계를 이슈로 나누어 등록하세요. 또한 해당 이슈를 해결하기 위한 커밋도 연결 주세요. 커밋 메시지에는 이슈 번호가 포함되어 있어야 하고, 적절한 메시지를 지정해야 합니다.

## 추가 평가항목(옵션)

- fast-api의 redoc 혹은 swagger ui에서 데이터 구조를 보기 좋게 표현해 보세요.
- 이런 구조를 왜 비동기 패턴이라고 하고, 왜 대용량 처리에서 비동기 방식을 선호하는지 설명할 수 있으면 좋습니다.
- redis queue의 워커로 pytorch inference 모듈이 연결되어 있다면, 배치 구성은 어떻게 하는 것이 좋을지 제안해 주세요.
- 운영 및 테스트 환경에 배포를 위해서는 환경의 Freeze와 제약이 필요합니다. 구동 가능한 상태로 requirements.txt를 유지하고, 각각 패키지가 python 3.11에서 동작하지 않는다면, 적정한 버전으로 fix하거나 유사한 기능을 수행할 수 있는 다른 패키지로 변경해 주세요.

## 참고

초기 보일러 플레이팅은 커밋해 놓았습니다. 익숙하다면 바로 코드에 집중할 수 있을겁니다.
노트북이 없다면, 미리 말씀해 주세요. 내부에 해당 코드 클론해서 구동해 놓을께요.

## notion, linear

https://www.notion.so/789f2fe92e40421e8a3fdee6f48f3519?pvs=4
https://linear.app/ohhoho/project/intern-code-test-497f45c0e7ab
