class Vehicle:
    """Base class for all vehicles"""
    def __init__(self,n,m,t,c):
        self.name = n
        self.menufractur = m
        self.turn = t
        self.color = c

    def drive(self):
        print(self.name,",",self.menufractur,"is driving now.")

    def turnn(self, direction):
        print(self.name," is now ", "to", direction)

    def brake(self):
        print(self.name,",",self.menufractur,"is stopping now.")

if __name__ == "__main__":
    v1 = Vehicle("'Toyota.X07'", "walton", "'right'", "black")
    v2 = Vehicle("'FarefoxEX9'", "Ford", "left", "white")
    v3 = Vehicle("'ThhhuopX'","harlewy devideson", "front", "gray")

    v2.drive()

    v1.drive()

    v1.brake()

    v1.turnn("left")