#######################################################
#######################################################
############    COPYRIGHT - DATA SOCIETY   ############
#######################################################
#######################################################

## DAY 3 DATA WRANGLING WITH PYTHON/DAY 3 DATA WRANGLING WITH PYTHON ##

## NOTE: To run individual pieces of code, select the line of code and
##       press ctrl + enter for PCs or command + enter for Macs


#=================================================-
#### Slide 4: Import Pandas and os  ####

import pandas as pd
import numpy as np
import os


#=================================================-
#### Slide 5: Series  ####

num_series = pd.Series([45, 89, 67, 33])
print(num_series)
print(num_series.values)


#=================================================-
#### Slide 6: Date series: ranges by month  ####

# Go in intervals of month.
print(pd.date_range(start = '20170101', end = '20170331', freq = 'M'))
# Not specifying end, but instead the start, freq, and how many periods.
print(pd.date_range(start = '20170101', freq = 'M', periods = 4))


#=================================================-
#### Slide 7: Date series: ranges by hour  ####

print(pd.date_range(start = '20170101', end = '20170102', freq = 'H'))


#=================================================-
#### Slide 8: Series methods  ####

norm_series = pd.Series(np.arange(5, 20, 5))
print(norm_series)


#=================================================-
#### Slide 9: Series - functions  ####

print(norm_series.shape)    #<- number of rows and columns

print(norm_series.mean())   #<- series mean

print(norm_series.median()) #<- series median

print(norm_series.std())    #<- series std deviation


#=================================================-
#### Slide 10: Series - functions  ####

# Show number of unique values.
print(norm_series.nunique())      
# Position of the max value.
print(norm_series.idxmax())       


#=================================================-
#### Slide 12: Series - sort and cumulative sum  ####

# Returns a series that is the cumulative sum of `norm_series`. 
print(norm_series.cumsum())       


#=================================================-
#### Slide 14: Exercise 1  ####




#=================================================-
#### Slide 17: Series to dataframe  ####

# Series 1 - times:
times = pd.date_range(start = '20170101', end = '20170630', freq = 'M')

# Series 2 - days out of the office:
days = pd.Series([2, 2, 6, 6, 2, 3])
            


#=================================================-
#### Slide 18: Generate dataframe from series  ####

# Create a dataframe from the two series we just created, as a dictionary.
average_ooo = pd.DataFrame({'Timestamp': times, 'OOO': days})

# View the first few rows of the dataframe, using the pandas function `.head()`.
print(average_ooo.head())


#=================================================-
#### Slide 19: Look-up dataframe information  ####

# Look up the type of object.
print(type(average_ooo))  
# Look up its shape.
print(average_ooo.shape) 


#=================================================-
#### Slide 21: Dataframe description metrics   ####

print(average_ooo.columns)
print(average_ooo.info())
print(average_ooo.describe())


#=================================================-
#### Slide 22: Extracting a single column   ####

print(average_ooo['Timestamp'])


#=================================================-
#### Slide 23: Extracting multiple columns   ####

print(average_ooo[['Timestamp', 'OOO']])


#=================================================-
#### Slide 24: Extracting a single row  ####

june_ooo = average_ooo.iloc[5, :]
print(june_ooo)

june_ooo = average_ooo.iloc[5] #<- equivalent without the colon
print(june_ooo)


#=================================================-
#### Slide 26: Index for our dataset  ####

# Let's use the `Timestamp` column as our new index.
average_ooo = average_ooo.set_index('Timestamp')
print(average_ooo)


#=================================================-
#### Slide 27: Looking up by the new index  ####

print(average_ooo.index)
# Look up a specific row by index.
print(average_ooo.loc['2017-02-28'])


#=================================================-
#### Slide 28: Loc vs. iloc  ####

print(average_ooo.iloc[1])


#=================================================-
#### Slide 29: Reset the index  ####

average_ooo = average_ooo.reset_index()
print(average_ooo.index)
# You can see that now `Timestamp` is once again a column vs. what it looked like when it was an index.
print(average_ooo) 


#=================================================-
#### Slide 37: Directory settings  ####

# Set `main_dir` to the location of your `skill-soft` folder (for Linux).
main_dir = "/home/[username]/Desktop/skill-soft"
# Set `main_dir` to the location of your `skill-soft` folder (for Mac).
main_dir = '/Users/[username]/Desktop/skill-soft'
# Set `main_dir` to the location of your `skill-soft` folder (for Windows).
main_dir = "C:\\Users\\[username]\\Desktop\\skill-soft"
# Make `data_dir` from the `main_dir` and 
# remainder of the path to data directory.
data_dir = main_dir + "/data"

# Create a plot directory to save our plots
plot_dir = main_dir + "/plots"



#=================================================-
#### Slide 38: Setting working directory  ####

# Set working directory.
os.chdir(data_dir)
# Check working directory.
print(os.getcwd())


#=================================================-
#### Slide 39: Read data from csv file  ####

household_poverty = pd.read_csv('household_poverty.csv')
print(household_poverty.head())


#=================================================-
#### Slide 40: Exercise 2  ####




#######################################################
####  CONGRATULATIONS ON COMPLETING THIS MODULE!   ####
#######################################################
