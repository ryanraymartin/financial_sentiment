# File name: router_client.py
import requests

article_text = (
    "We are headed for another great depression."
)

response = requests.get("http://127.0.0.1:8000/router?txt=" + article_text).text

print(response)