echo docker run -d  -p 10081:10081 --gpus all backend0
echo docker run -d  -p 10081:10081 --gpus all --restart unless-stopped backend0
echo docker run -d  --network=host --restart unless-stopped nginx-reverse-proxy-nginx-proxy