# this is some practice code i wrote to implement all the functions i learnt from the 
# developer.google.com machine learning crash course in it the first intro to pandas collaboratory 
# notebook.the original notebook is also there alongside this in the same repo.


#imported the pandas library
import pandas as pd

#populates a series which can be asssumed as a column of a table
names=pd.Series(['shaunak','saudamini','adarsh','jatin','kamdar','samruddhi','manthan'])

#building up data ;)
pointer=pd.Series([7.93,7.07,7.65,7.1,8.4,9.1,7.7])

#using the above built 2 series to constuct a two column data frame by passing column as the string key to the dictionary
data=pd.DataFrame({'names':names,'pointer':pointer})

#gives us some statistics about the data like the mean median etc
data.describe()

#displays on ly the first 5 entries in the data
data.head()

#returns a histogram object
data.hist('pointer')

#prints the names series from the dataframe named data
data['names']

#same
data['pointer']

#prints the first entry from the names series
data['names'][0]

#prints the max values in the data frame for all the series present in it.
data.max()

#if it is a string then it returns the lexicographically smallest string while with an integer the smallest integer
data.min()

indian_pointers=data['pointer']

#performing some mathematical operations on the dataframe.can be complex ones as well using the numpy library
pointer5=(indian_pointer*5)/10

pointer4=(indian_pointers*4)/10

#can apply any lambda equation(function) to a particular series similar to the map function we regularly use to convert all the data in a list
pointer.apply(lambda pointer: pointer>7.5)

#returns the indices of the series passed as an arguement but returns only the start stop and the interval values
pointer.index

#import numpy for the np.rnadom.permutations used in the next step
import numpy as np

#this shuffles the data in a dataframe.it can be done manually using a list.but here to gt random shuflfing we used the np.random.permutation from numpy to achieve random permutations from the pointer.indices descirbed before
data.reindex(np.random.permutation(pointer.index))


















