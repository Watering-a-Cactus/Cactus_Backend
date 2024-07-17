import requests
from openai import OpenAI

from app.core.config import settings


class GPT():
  def __init__(self):
    self.__API_Key = settings.GPT_API_KEY

  def test_GPT(self, message: str):
    client = OpenAI(api_key=self.__API_Key)

    completion = client.chat.completions.create(
      model="gpt-4o",
      messages=[
        {"role": "system", "content": "You are a helper who helps me write a novel."},
        {"role": "user", "content": message}
      ]
    )

    print(completion.choices[0].message)
  
  