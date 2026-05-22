class Car:
    #Define a class named Car with attributes: make, model, year
    #Initialize these attributes in the __init__ method
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    ##Add a method named describe_car() that prints information about the car as "Year Make Model"
    def describe_car(self):
        print(self.make,self.model,self.year)

#Create an instance of the Car class with the following attributes
print_car = Car("Toyota", "Corolla", "2020")
#call describe_car method
print_car.describe_car()


















