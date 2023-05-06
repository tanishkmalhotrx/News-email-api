import requests
from send_email import send_email

api_key = "76964584e15e4952bb481b8f78d20c2e"
url = "https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=76964584e15e4952bb481b8f78d20c2e"

request = requests.get(url)
content = request.json()
body = ""
for article in content["articles"]:
    body = body + article["title"] + "\n" + article["description"] + 2*"\n"

body = body.encode("utf-8")
 
send_email(message=body)