"""
Robert Matthews
CS 1400
Section 002
Exercise 8

8.3
Chapter 8, Programming Exercises #2, pg. 279
"""

# for t is temperature (F) and v is wind speed (mph) windchill = 35.74 + 0.6215t - 35.75(v**0.16) + 0.4275t(v**0.16)
# write a program that prints a nicely formatted table of windchill values. rows should represent wind speed for 0 - 50
# in 5 mph increments., and the columns represent temperatures from -20 to +60 in 10 degree increments.
# note: the formula only applies for wind speeds in excess of 3 mph


def windchill_calc(a_temperature, a_wind_speed):
    windchill = 35.74 + (0.6215 * a_temperature) - (35.75 * (a_wind_speed ** 0.16)) + \
                (0.4275 * a_temperature * (a_wind_speed ** 0.16))
    return windchill

# create table

# for each box in table use the temperature and wind speed values in the row and column to do the windchill calc
