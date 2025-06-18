## ADHD 응답에 TTS 엔진.

REST을 사용하여 `/synthesize` 경로에 질문 텍스트를 음성으로 변환 엔진.

Setup:
```
docker build -t DOCKER_NAME
```

Backend running method:
```
docker run -d  -p PORT:PORT --gpus all DOCKER_NAME
```

Frond calling method can be obtained in `textList0/templates/ttsdemo-comp.html`. Runnind demo:
```
cd textList0
uvicorn main:app --reload --host 0.0.0.0 --port PORT --ssl-keyfile=key.pem --ssl-certfile=cert.pem
# Then open in browser:   https://localhost:PORT/demo

```

Build Secure backend communication ports with SSL certificate:
```
cd nginx-reverse-proxy
docker compose
docker run -d --network=host nginx-reverse-proxy-nginx-proxy

```