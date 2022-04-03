country_name = ["Bangladesh", "India", "Japan", "Vhutan", "Tokio", "USA", "UK", "Jarmany", "Canada"]

with open("file.txt", "w") as fp:
    for name in country_name:
        fp.write(name+"\n")

with open("file.txt", "r") as fp:
    for name in country_name:
        print(name)