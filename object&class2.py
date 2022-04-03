class car:
    name = ""
    color = ""

    def __init__(self, n, c):
        self.name = n
        self.color = c

    @staticmethod
    def start():
        print("starting the engine")


my_car = car("Ttokio", "White")
print("name of  the car: ", my_car.name)
print("color of  the car: ", my_car.color)

my_car.start()
