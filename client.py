import requests

text = input("Enter text to reverse: ")

url = "http://127.0.0.1:5000/reverse"
response = requests.post(url, json={"text": text})

if response.status_code == 200:
    result = response.json()
    print("Reversed text:", result["reversed"])
else:
    print("Request failed:", response.text)
