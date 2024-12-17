from .rating import Rating

class Restaurant:
    restaurants = []

    def __init__(self, name, category):
        self._name = name.title()
        self._category = category
        self._active = False # o _ é pra colocar o metódo como privado
        self._rating = []
        Restaurant.restaurants.append(self)

    def __str__(self):
        return f'Restaurant {self._name.ljust(15)} | Category {self._category.ljust(15)} | Active {self.active}'
  
    def set_name(self, name):
        self._name = name
    
    def set_category(self, category):
        self._category = category

    def set_active(self):
        self._active = not self._active

    def show_name(self):
        print(self._name)
        print(self._category)
        print(self.active)

    # def list_restaurants(self):
    #     print('***** Listando Restaurantes *****')
    #     print(f'{'Restaurant'.ljust(18)} | Categoria')
    #     for restaurant in self.restaurants:
    #         print(f'- {restaurant.name.ljust(16)} | {restaurant.category}')

    @classmethod
    def list_restaurants(cls):
        print('***** Listando Restaurantes *****')
        print(f'{'Restaurant'.ljust(18)} | {'Category'.ljust(10)} | {'Rating'.ljust(10)} | Activation')
        for restaurant in cls.restaurants:
            print(f'- {restaurant._name.ljust(16)} | {restaurant._category.ljust(10)} | {str(restaurant.get_average_rating).ljust(10)} | {restaurant.active}')

    @property
    def active(self):
        return 'Active' if self._active else 'Inactive'   
    
    def receive_rating(self, client, rate):
        if 0 <= rate <= 5:
            rating = Rating(client, rate)
            self._rating.append(rating)

    @property
    def get_average_rating(self):
        if not self._rating:
            return '-' 
        
        total = sum(rating._rate for rating in self._rating)
        #or
        # total = 0

        # for rating in self._rating:
        #     total += rating._rate

        
        return total / len(self._rating) 
    
        # or try except
        # try:
        #     total = 0

        #     for rating in self._rating:
        #         total += rating._rate
    
        #     return total / len(self._rating) 
        
        # except ZeroDivisionError:
        #     return 0




'''
# this is builder desing pattern

class Restaurant:

    def __init__(self):
        self.name = None
        self.category = None
        self.active = None
    
    def set_name(self, name):
        self.name = name
    
    def set_category(self, category):
        self.category = category

    def set_active(self, active):
        self.active = active

    def show_name(self):
        print(self.name)
        print(self.category)
        print(self.active)

class RestaurantBuilder:
    def __init__(self):
        self.restaurant = Restaurant()

    def add_name(self, name):
        self.restaurant.set_name(name)
        return self

    def add_category(self, category):
        self.restaurant.set_category(category)
        return self
    
    def add_activation(self, active):
        self.restaurant.set_active(active)
        return self
    
    def build(self):
        return self.restaurant

'''