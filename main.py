import requests

api_key = "76964584e15e4952bb481b8f78d20c2e"
url = "https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=76964584e15e4952bb481b8f78d20c2e"

request = requests.get(url)
content = request.text