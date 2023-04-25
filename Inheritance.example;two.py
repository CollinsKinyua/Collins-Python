class Magari:
    def __init__(self, make, model, year):
        self.mymake = make
        self.mymodel = model
        self.myyear = year

    def kuanzisha(self):
        print(f"{self.mymake} {self.mymodel}{self.myyear} started")


class Subaru(Magari):
    def __init__(self, make, model, year, num_doors):
        super().__init__(make, model, year)
        self.mynum_door = num_doors

    def kuanzisha(self):
        print(f"{self.mymake}{self.mymodel}car with {self.mynum_door} doors started")


gari = Subaru("Outback", " Hybrid", 2023, 4)
gari.kuanzisha()

class Motorbike:
    def __init__(self,make,model,year,engine):
        self.mymake = make
        self.mymodel = model
        self.myyear = year
        self.myengine = engine
    def start(self):
        print(f"{self.mymake}{self.mymodel}{self.myyear}{self.myengine} delivered")

class Bmw(Motorbike):
    def __init__(self, make, model ,year, engine):
        super().__init__(make,model,year,engine)
        self.mycc = engine
    def start(self):
        print(f"{self.mymake}{self.mymodel}{self.myyear}{self.mycc}cc single four stroke engine delivered")

bike = Bmw("G310", " RR", 2020 ,1260,)
bike.start()

# class