import requests
resp = requests.get("http://en.wikipedia.org/w/api.php?action=query&prop=info&format=json&titles=Hello")
print(resp.status_code)
print(resp.json())