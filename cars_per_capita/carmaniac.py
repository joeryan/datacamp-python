import pandas as pd

# read csv into pandas dataframe, I added the 'country' column to the original csv data
cars = pd.read_csv('cars.csv')

# create series of cars_per_capita (series has an extra column with the row number)
cpc = cars['cars_per_cap']
# print(cars) # just to see the dataframe

# print(cpc) # print the cars_per_capita series

# create a list of the items with many cars using list comprehension
# https://www.pythonforbeginners.com/basics/list-comprehensions-in-python
many_cars = [ item > 500 for item in cpc ]
print(many_cars)

# select only those countries that have many cars (>500)
# https://www.geeksforgeeks.org/selecting-rows-in-pandas-dataframe-based-on-conditions/
#  this is probably better, but they wanted to have a many_cars series
car_maniacs_easy = cars[cars['cars_per_cap'] > 500]
print("car maniacs the easy way:")
print(car_maniacs_easy)


# I had to google a bunch of shit to find a way to do this with the intermediace many_cars and I don't know if it's right
car_high_use = pd.DataFrame()
# https://treyhunner.com/2016/04/how-to-loop-with-indexes-in-python/
for index, value in enumerate(many_cars):
  if value:
      # https://stackoverflow.com/a/41529411
      # https://kite.com/python/answers/how-to-insert-a-row-into-a-pandas-dataframe
      # https://www.geeksforgeeks.org/python-pandas-dataframe-append/
    car_high = pd.Series(cars.iloc[index])
    car_high_use = car_high_use.append(car_high, ignore_index=True)

print("car maniacs the hard way:")
print(car_high_use)