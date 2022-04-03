import requests
import sys

img_url = sys.argv
file_name = sys.argv[0]
r = requests.get(img_url)

with open(file_name, "wb") as f:
    f.write(r.content)
