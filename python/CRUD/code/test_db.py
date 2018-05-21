from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine
DBSesstion = sessionmaker(bind = engine)
session = DBSesstion()

myFirstRestaurant = Restaurant(name = "Pizza Palace")
session.add(myFirstRestaurant)
session.commit()

#print(session.query(Restaurant).all())

cheesepizza = MenuItem(name = "Cheese Pizze", course = "some course", price = "price", description = "sone discriptions", restaurant= Restaurant(name = "myFirstRestaurant"))
session.add(cheesepizza)
session.commit()
print(session.query(MenuItem).all())