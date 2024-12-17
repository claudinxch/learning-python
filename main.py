from models import Restaurant # RestaurantBuilder
restaurant_chinese = Restaurant('Yin Yang', 'Chinesa' )
restaurant_french = Restaurant('Joseph Gusteau', 'French' )

# print(restaurant)
# print(restaurant2)

# restaurant.list_restaurants()
# Restaurant.list_restaurants()

print('\n--------------\n')

restaurant_chinese.set_active()
restaurant_chinese.receive_rating('Clau', 10)
restaurant_chinese.receive_rating('Lorry', 4)
# Restaurant.list_restaurants()

def main():
    print()
    restaurant_chinese.show_name()
    print()
    restaurant_french.show_name()
    print()
    Restaurant.list_restaurants()

'''
builder desing pattern

restaurant = RestaurantBuilder() \
                .addName('Joseph Gusteau') \
                .addCategory('French') \
                .addActivation(False)

restaurant.restaurant.show_name()

'''     

# class Person:
#     def __init__(self, name, age, profession = ''):
#         self.name = name
#         self.age = age
#         self.profession = profession

#     def __str__(self):
#         return f'{self.name} is {self.age} years old and works as a {self.profession}.'
    
#     def anniversary(self):
#         self.age += 1
   
#     @property
#     def greet(self):
#         if self.profession:
#             return f'I am {self.name} and I am a {self.profession}!'
#         return f'I am {self.name}!'

# person1 = Person(name='Alice', age=25, profession='Software Developer')
# person2 = Person('Joseph', 22)
# print(person1)
# print(person2)
# print(person1.greet)
# print(person2.greet)

# class BankAccount:
#     def __init__(self, title, amount):
#         self._title = title
#         self._amount = amount
#         self._active = False

#     def __str__(self):
#         return f'Owner: {self._title}, amount: {self._amount}'
    
#     @classmethod
#     def activate_account(cls, account):
#         account._active = not account._active

#     @property
#     def title(self):
#         return self._title
    
#     @property
#     def amount(self):
#         return self.amount
    
#     @property
#     def active(self):
#         return self._active
    
# account1 = BankAccount('Joseph', 98392)
# print(account1._active)
# account1.activate_account(account1)
# print(account1._active)

if __name__ == '__main__':
    main()