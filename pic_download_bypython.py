import requests

img_url1 = "https://media.istockphoto.com/photos/the-city-of-london-skyline-at-night-united-kingdom-picture-id1312550959"
r = requests.get(img_url1)

img_url2 = "https://images.unsplash.com/photo-1453728013993-6d66e9c9123a?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8Mnx8dmlld3xlbnwwfHwwfHw%3D&w=1000&q=80"
res = requests.get(img_url2)

with open("pybook1.png", "wb") as f: #make sure that png or jpg location
    f.write(r.content)

with open("pybook2.png", "wb") as f:  # make sure that png or jpg location
    f.write(res.content)