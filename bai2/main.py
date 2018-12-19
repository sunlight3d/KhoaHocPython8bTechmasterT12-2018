"""File nay buoi so 2 """
# width = 200
# height = 100
# area = width * height
# """String interpolation kieu moi"""
# output = "w = {}, height = {}".format(width,height)
# print(output)
import math
# def calculate_f(x):
#     # sohang1 = x**100
#     # sohang2 = 2*x**2 
#     # return sohang1 + sohang2 + 9    
#     sohang1 = 3*x + 7
#     sohang2 = x + 2
#     return sohang1 / sohang2
# result = round(calculate_f(12.344), 2) 
# print("result = {}".format(result))
def create_list_of_persons():
    guests = []
    guests.append("Hoang")
    guests.append("Minh")
    guests.append("John")
    guests.append("Jerry")
    print(guests)
    """Bat tay chao hoi"""
    guests.sort(reverse = True)
    for guest in guests:
        print("Hello mr {}".format(guest))
    """Moi ra ve sau khi phat hien ko du cho"""
    number_of_guests = len(guests)
    print("Co {} khach moi".format(number_of_guests))
    while(number_of_guests > 2):
        guest = guests.pop()
        print("Moi ban {} ra ve".format(guest))
        number_of_guests = len(guests)
    print("Co {} khach moi".format(number_of_guests))
# create_list_of_persons()
def use_dictionary():
    dict = {"name": "Hoang", "age": 30}
    """Mutable"""
    dict["name"] = "Hoang 123"
    dict["profession"] = "software developer"
    del dict["name"]
    print(dict)
# use_dictionary()
from person import Person
mrHoang = Person("Hoang", "hoang@gmail.com",30,["an choi","day hoc"])
mrHuy = Person("Huy", "huy@gmail.com",40,["day hoc"])
# print(mrHoang.to_string())
# print(mrHuy.to_string())
# print(str(mrHoang))
# mrHoang.login()
# mrHoang.login()
# mrHoang.login()
# mrHoang.login()
# mrHoang.login()
# mrHoang.login()
# mrHoang.login()
# print(mrHoang.to_string())
# mrHoang.reset_login()
# print(mrHoang.to_string())
Person.base_salary = 20
print(mrHoang.to_string())
print(mrHuy.to_string())

