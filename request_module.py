import requests
res = requests.get("http://example.com")
res.ok
#True
res.text
type(res.text)
print(res)