FROM python:3.10-slim
WORKDIR /app
COPY . /app

RUN apt-get update && apt-get install -y \
    build-essential libsndfile1 \
    && rm -rf /var/lib/apt/lists/*

RUN cd MeloTTS && pip install -e .
RUN python -m unidic download
RUN cd MeloTTS && python melo/init_downloads.py
RUN pip install fastapi uvicorn jinja2 aiofiles python-multipart gTTS python-mecab-ko

WORKDIR textList0
CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "10081"]
# CMD ["python", "./melo/app.py", "--host", "0.0.0.0", "--port", "8888"]