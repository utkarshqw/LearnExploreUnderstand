from car  import Car 

car_1 = Car("Chevy","Corvette", 2021, "blue")
car_2 = Car("Ford", "Mustang",2022, "red")

car_1.wheels = 2 

print(car_1.wheels)
print(car_2.wheels) 


# We can directly get the number of whells 
print(Car.wheels) # effect all instances

# suppose we change the wheels count from Car class then every cars wheels would chane 
Car.wheels = 2
print("after change in Car class wheels" ,car_1.wheels)
print("after change in Car class wheels" ,car_2.wheels) 
