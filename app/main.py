from fastapi import FastAPI # type: ignore
from pydantic import BaseModel

from app.api.external.intent import Intent
from app.api.external.gpt import GPT

# Request Body 타입 설정
class IntentMessage(BaseModel):
    message: str
class GptMessage(IntentMessage):
   pass

# 서버 인스턴스 생성
app = FastAPI()

# 기타 인스턴스 생성
intent = Intent()
gpt = GPT()


@app.get("/")
async def root():
  return {"message": "Hello World"}

# intent 기능을 테스트하기 위함
@app.post("/test/intent")
async def get_intent(intentMessage: IntentMessage):
  res = intent.get_intent(intentMessage.message)
  return res

# gpt api 기능을 테스트하기 위함
@app.post("/test/gpt")
async def text_gpt(gptMessage: GptMessage):
  res = gpt.test_GPT(gptMessage.message)
  return res