## ADHD 응답에 TTS 엔진.

REST을 사용하여 `/synthesize` 경로에 질문 텍스트를 음성으로 변환 엔진.

Setup:
```
docker build -t DOCKER_NAME
```

Running method:
```
docker run -d  -p PORT:PORT --gpus all DOCKER_NAME
```

Frond calling method can be obtained in `textList0/templates/ttsdemo-comp.html`.
