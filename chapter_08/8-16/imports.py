# import car_function
# output = car_function.car_descriptor(
#     'honda', 'civic', year=1986, color='silver')

# from car_function import car_descriptor
# output = car_descriptor(
#     'honda', 'civic', year=1986, color='silver')

# from car_function import car_descriptor as cd
# output = cd(
#     'honda', 'civic', year=1986, color='silver')

# import car_function as cf
# output = cf.car_descriptor(
#     'honda', 'civic', year=1986, color='silver')

from car_function import *
output = car_descriptor(
    'honda', 'civic', year=1986, color='silver')

print(output)
