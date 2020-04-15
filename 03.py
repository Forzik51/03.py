# class Person:
#     # __name = "Bill" #__приховує елем
#     # __age = 33

#     def __init__(self, name, age):
#         self.__name = name
#         self.__age = age
#         print("Construktor working")

#     def __del__(self):
#         print("DDEESSConstruktor working")

#     def person_info(self):
#         print(self.__name, "says", self.__age)

#     @property
#     def name(self):
#         return self.__name

#     @property
#     def age(self):
#         return self.__age

#     @age.setter
#     def age(self, new_age):

#         if self.__age == new_age:
#             print("The same age")
#         else:
#             self.__age = new_age

#     @name.setter
#     def name(self, new_name):

#         if self.__name == new_name:
#             print("The same age")
#         else:
#             self.__name = new_name


# bill = Person("Billy", 56)
# print("Before =>",bill.age)
# print("Before =>",bill.name)
# bill.age = 58
# bill.name = "test"
# print("After =>",bill.age)
# print("After =>",bill.name)
# bill.person_info()

# print(bill.get_name())
# print("Before =>",bill.get_age())
# bill.set_age(55)
# print("After =>",bill.get_age())

# stive = Person("Stiven", 26)
# stive.person_info()
# person.name = "Stive"
# person.age = 33
# person.person_info()

# pers = Person()
# pers.person_info()

import random


# class Account:
#     def __init__(self, nomer, money, valuta):
#         self.__nomer = nomer
#         self.__money = money
#         self.__valuta = valuta
#         print("Construktor working")

#     def __del__(self):
#         print("DDEESSConstruktor working")

#     def person_info(self):
#         print("nomer", self.__nomer, " money =>",
#               self.__money, " valuta =>", self.__valuta)

#     @property
#     def put(self):
#         return self.__money

#     @property
#     def withdraw(self):
#         return self.__money

#     @put.setter
#     def put(self, new_money):
#         if self.__money == new_money:
#             print("The same age")
#         else:
#             self.__money = self.__money - new_money

#     @withdraw.setter
#     def withdraw(self, new_money):
#         if self.__money == 0:
#             print("error")
#         else:
#             self.__money = self.__money + new_money

#     def transfer(self, name1, name2, money_tr):
#         name1.put = money_tr
#         name2.withdraw = money_tr


# adam = Account(random.randint(100000, 999999), 555, "$")
# adam.person_info()
# adam.put = 55
# print("After =>", adam.put)
# adam.withdraw = 55
# print("After =>", adam.withdraw)

# Bill = Account(random.randint(100000, 999999), 555, "$")
# Bill.person_info()

# adam.transfer(adam,Bill,55)
# print("After =>", adam.withdraw)
# print("After =>", Bill.withdraw)


class DiscountCard:
    def __init__(self, nomer, money, sale, data):
        self.__nomer = nomer
        self.__money = money
        self.__sale = money // 1000 
        self.__data = data
        print("Construktor working")

    def __del__(self):
        print("DDEESSConstruktor working")

    def person_info(self):
        print("sale =>", self.__sale, " \nmoney =>", 1000 - (self.__money % 1000))

    @property
    def buy(self):
        return self.__sale
        return self.__money

    @buy.setter
    def buy(self, price):
        print(price * (1 - (self.__sale / 100)))
        self.__money += price


Bill = DiscountCard(random.randint(100000, 999999), 1000, 1, "12/07/2020")
Bill.person_info()
Bill.buy = 1000