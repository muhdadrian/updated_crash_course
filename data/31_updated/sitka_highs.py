# The datetime Module

# Let’s add dates to our graph to make it more useful. The first date from the weather data file is in the second row of the file:

# "USW00025333","SITKA AIRPORT, AK US","2021-07-01",,"61","53"

# The data will be read in as a string, so we need a way to convert the string "2021-07-01" to an object representing this date. We can construct an object representing July 1, 2021, using the strptime() method from the datetime module. Let’s see how strptime() works in a terminal session:
# >>> from datetime import datetime
# >>> first_date = datetime.strptime('2021-07-01', '%Y-%m-%d')
# >>> print(first_date)
# 2021-07-01 00:00:00

# We first import the datetime class from the datetime module. Then we call the method strptime() with the string containing the date we want to process as its first
# argument.
# The second argument tells Python how the date is formatted. In this example, '%Y-' tells Python to look for a four-digit year before the first dash; '%m-' indicates a two- digit month before the second dash; and '%d' means the last part of the string is the day of the month, from 1 to 31.

# The strptime() method can take a variety of arguments to determine how to interpret the date. Table below shows some of these arguments.

# Argument  Meaning
# %A        Weekday name, such as Monday
# %B        Month name, such as January
# %m        Month, as a number (01 to 12)
# %d        Day of the month, as a number (01 to 31) %Y Four-digit year, such as 2019
# %y        Two-digit year, such as 19
# %H        Hour, in 24-hour format (00 to 23)
# %I        Hour, in 12-hour format (01 to 12)
# %p        AM or PM
# %M        Minutes (00 to 59) %S Seconds (00 to 61)
