import requests
url = "http://subeen.com/allposts"
response = requests.get(url)
with open("dimik.html", "w", encoding = response.encoding) as f:
    f.write(response.text)
