class car:
    name = ""
    color = ""

    @staticmethod
    def start():
        print("starting the engine")


my_car = car()
my_car.name = "tokio"
my_car.color = "blue"
print("name of  the car: ", my_car.name)
print("color of  the car: ", my_car.color)
my_car.start()