from fastapi import FastAPI, Request, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse, StreamingResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import io
# import gradio as gr
from melo.api import TTS
import json

from fastapi.responses import Response
from gtts import gTTS
from io import BytesIO


speed = 1.0
device = 'auto'
language='KR'
models = {
    'KR': TTS(language='KR', device=device),
}
speaker = list(models[language].hps.data.spk2id.keys())[0]

app = FastAPI()
origins = [
    "http://localhost:5981",    "http://localhost:6081",
    "https://localhost:5981",    "https://localhost:6081",
    "http://127.0.0.1:5981",    "http://127.0.0.1:6081",
    "https://127.0.0.1:5981",    "https://127.0.0.1:6081",
    "http://192.168.3.19:5981",    "http://192.168.3.19:6081",
    "https://192.168.3.19:5981",    "https://192.168.3.19:6081",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

# Dummy values — replace with real data
# texts = [
#     "안녕하세요?",
#     "팀A.",
#     "날씨 종다.",
#     # "Click to hear this sentence."
# ]
inputs = json.load(open('static/questions_list.js', encoding="utf-8"))
texts = [i['text'] for i in inputs]

# Dummy synthesize() — replace this with your actual function
def synthesize(speaker, text, speed, language): #, progress=gr.Progress()):
    bio = io.BytesIO()
    models[language].tts_to_file(
        text, 
        models[language].hps.data.spk2id[speaker], 
        bio, 
        speed=speed, 
        # pbar=progress.tqdm, 
        format='wav'
    )
    return bio.getvalue()

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "texts": texts})

@app.post("/synthesize")
async def synthesize_audio(text: str= Form(...)):
    audio_data = synthesize(speaker, text, 1.0, "KR")
    return StreamingResponse(io.BytesIO(audio_data), media_type="audio/wav")

@app.get("/demo", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("ttsdemo-comp.html", {"request": request, "texts": texts})


@app.get("/demo4", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("ttsdemo4.html", {"request": request, "texts": texts})

@app.post("/gtts")
async def tts_korean(text: str = Form(...)):
    tts = gTTS(text=text, lang="ko")
    mp3_fp = BytesIO()
    tts.write_to_fp(mp3_fp)
    mp3_fp.seek(0)
    return Response(content=mp3_fp.read(), media_type="audio/mpeg")
    # StreamingResponse(mp3_fp, media_type="audio/mpeg")