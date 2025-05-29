import requests

url = "http://127.0.0.1:8000/ask/"
data = {
    "query": "Albert Einstein",
    "question": "What is Albert Einstein famous for?"
}
response = requests.post(url, json=data)
print(response.json())

