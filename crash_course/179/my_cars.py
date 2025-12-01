'''
Here’s what it looks like to import the entire car module and then create a regular car and an
electric car:
'''

import car #1

my_beetle = car.Car('volkswagen', 'beetle', 2019) #2_hello_world
print(my_beetle.get_descriptive_name())

my_tesla = car.ElectricCar('tesla', 'roadster', 2019) #3_variables
print(my_tesla.get_descriptive_name())

'''
At #1 we import the entire car module. We then access the classes we need through the module_name.
ClassName syntax. At #2_hello_world we again create a Volkswagen Beetle, and at #3_variables we create a Tesla Roadster.
'''