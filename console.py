from models.city import City
from models.user import User
from models.country import Country
from models.destination import Destination

from repositories import user_repository, country_repository, city_repository, destination_repository

user_repository.delete_all()
city_repository.delete_all()
country_repository.delete_all()
destination_repository.delete_all()

user1 = User('Lina', 'Edinburgh', 'Scotland')
user_repository.save(user1)

user2 = User('Oscar Wilde', 'Dublin', 'Ireland')
user_repository.save(user2)

user3 = User('Peter Parker', 'New York', 'USA')
user_repository.save(user3)

country1 = Country('Germany')
country_repository.save(country1)

country2 = Country('France')
country_repository.save(country2)

country3 = Country('Estonia')
country_repository.save(country3)

city1 = City('Berlin', country1)
city_repository.save(city1)

city2 = City('Paris', country2)
city_repository.save(city2)

city3 = City('Tallinn', country3)
city_repository.save(city3)

city4 = City('Frankfurt', country1)
city_repository.save(city4)

destination = Destination(user1, country1, city1, True)
destination_repository.save(destination)

destination = Destination(user2, country2, city2, False)
destination_repository.save(destination)

destination = Destination(user3, country3, city3, False)
destination_repository.save(destination)
