# Feedback for Problem 2

## Loading Data 

* The standard csv way to read a file is to use the reader class in the csv module, but if you observe the data, it's almost like a text file, just that it's structured column-wise as well.
* So a nice way to read this (especially since it has no header, which csv files usually have) is to treat it like a text file and read it line by line into a list, and then split the string with the ',' character, and you get what you want.
* Since you haven't used both of them, I'd suggest that you also try out reading from a csv file and from a text file, even though you'll have libraries like sklearn to help you out with this in the future, you'll need to know how to load assignments from these in the future.

Do try out the grouping data part when you get time, that's the most interesting part of the assignment, feel free to ask doubts as well if you're not able to do it
