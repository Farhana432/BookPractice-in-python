from BookPractice1.parent import Vehicle

class Car(Vehicle):
    """Car class"""
    """Method for add new feature and change gear"""
    def change_gear(self,gear_name):
        print(self.name, " is changing gear to", gear_name)

    def turnn(self, direction):
        print(self.name, " is now ", "to", direction)

if __name__ == "__main__":
    c = Car("thhukkoiX4", "toyota", "Right", "red")

    c.drive()
    c.change_gear("P")
