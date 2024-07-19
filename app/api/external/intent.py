import requests

class Intent:
  base_url = "https://kochatbot.fly.dev/webhooks/rest/webhook"

  def get_intent(self, message: str) -> list[str]:
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }

    body = {
      "sender": "Cactus-back",
      "message": message
    }
    try:
      response = requests.post(self.base_url, json=body, headers=headers)
      response.raise_for_status()
      json = response.json()
      
      return [item["text"] for item in json]
    
    except requests.RequestException as e:
      print(e)
      return ["fail"]
