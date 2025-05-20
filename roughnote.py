class CaptainAmerica:
    def __int__(self, name, power):
        self.name = name
        self.power = power

    def usePower(self):
        print(self.name + " used " + self.power)


if __name__ == "__main__":
    classy = CaptainAmerica("Hasan", "Time waste")
    classy.usePower()