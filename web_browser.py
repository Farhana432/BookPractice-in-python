import requests
import os
import webbrowser as wb
url = "http://subeen.com/allposts"
response = requests.get(url)
with open("dimik.html", "w", encoding=response.encoding) as f:
    f.write(response.text)
file_path = os.path.realpath("shubeen.html")
print(file_path)
wb.open("file://" + file_path)