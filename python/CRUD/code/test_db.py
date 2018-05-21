from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine
DBSesstion = sessionmaker(bind = engine)
session = DBSesstion()

# myFirstRestaurant = Restaurant(name = "Pizza Palace")
# session.add(myFirstRestaurant)
# session.commit()

# #print(session.query(Restaurant).all())

# cheesepizza = MenuItem(name = "Cheese Pizze", course = "Pizza", price = "$6.99", description = "sone discriptions", restaurant= Restaurant(name = "myFirstRestaurant"))
# session.add(cheesepizza)
# session.commit()
# print(session.query(MenuItem).all())

print('Start --- ...')
cheese_pizza = session.query(MenuItem).filter_by(name = 'Cheese Pizze').one()


print(cheese_pizza.name)
print(cheese_pizza.id)
print(cheese_pizza.price)
print(cheese_pizza.restaurant.name)
print("\n")
# cheese_pizza.price = "$2.99"
# session.add(cheese_pizza)
# session.commit()

print(cheese_pizza.name)
print(cheese_pizza.id)
print(cheese_pizza.price)
print(cheese_pizza.restaurant.name)
print("\n")