class car:

    def __init__(self, n, c):
        self.name = n
        self.color = c

    def start(self):
        print("name : ", self.name)
        print("color : ", self.color)
        print("starting the engine")


my_car1 = car("Ttokio", "White")  #car.start(my_car)
my_car1.start()
my_car2 = car("hdffer", "blue")
my_car2.start()
my_car3 = car("kdfhjsd", "black")
my_car3.start()
my_car3.year = 2017
print(my_car3.name, my_car3.color, my_car3.year)