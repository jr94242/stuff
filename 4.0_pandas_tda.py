import pandas as pd

covid_df = pd.read_csv("italy-covid-daywise.csv")

#print(type(covid_df))

#print(covid_df)

#print(covid_df.describe())   # ---> this will display some more additional information about the dataset from .info() method





# other methods for gathering info about the dataset:
# df.columns ; df.shape ; df.info()




# how a pandas df is structured: a dict where all the keys are the column names and all the values are 
# lists of values from the rows within the corresponding column



# therefore in order to retrieve specific info from the df:



#print(covid_df['new_cases'])






# and then to take a specific value

#print(covid_df['new_cases'][242])




# this is similar to this:

#print(covid_df.at[222, 'new_tests'])





# pandas allows to access columns directly as if they are properties of the df:

#print(covid_df.new_deaths)

cases_df = covid_df[['date', 'new_cases']]

#print(cases_df)







# NB -- if you modify the data from cases_df, data will also be modified in the original df







# to make sure you can analyse the data and make transformations to it without losing the original data --- df.copy()

covid_df_copy = covid_df.copy()  # this will create a separate set of data that will not be affected by the changes made in 
#the other instance






# to access a specific row --> .loc[]

#print(covid_df_copy.loc[222])  # this will output the entire row with values from all the columns







# if there are a lot of NaN values, there is a method to show where the first valid value appears

pls_tellme = covid_df.new_tests.first_valid_index()
#print(pls_tellme)

#print(covid_df.loc[108:113])  # ---> to verify its true



# df.sample(20)   ---> get a random sample of 20 rows from the data to get a feel for it (will also show the rows index)








# ANALYSING DATA FROM THE DATAFRAME


total_cases = covid_df.new_cases.sum()
total_deaths = covid_df.new_deaths.sum()
death_rate = total_deaths/total_cases

#print(f"Total cases for the period are {total_cases}, with total deaths: {total_deaths}, death rate is {death_rate:.2f}")

initial_tests = 935310
total_tests = initial_tests + covid_df.new_tests.sum()

#print(total_tests)

positive_rate = total_cases/total_tests

#print(f"{positive_rate:.2f} % ")   # --> for some reason I am using the same syntax as him, but his output is 5.2% and mine is 0.05%






high_new_cases = covid_df.new_cases > 1000


lethal_df = covid_df[high_new_cases]  # wherever it was true, it will add this to the new df

#print(lethal_df)

# all this could have been written in 1 line

# high_cases_df = covid_df[covid_df.new_cases > 1000]








# in order to display the full df, it needs to be done via a context manager

#from IPython.display import display

# with pd.option_context('display.max_rows', 100):
#     display(lethal_df)








# more complex queries

high_ratio_df = covid_df[covid_df.new_cases / covid_df.new_tests > positive_rate]
#print(high_ratio_df)





# this is the way to add a new column to the df
covid_df['positive_rate'] = covid_df.new_cases / covid_df.new_tests

#print(covid_df)

# and then to remove a column, the syntax is:
covid_df.drop(columns=['positive_rate'], inplace=True)

#print(covid_df)








# sorting rows via column values  -- this will sort the df with the biggest number of new cases in a descending fashion
most_infectious_days = covid_df.sort_values('new_cases', ascending=False).head(10)

#print(most_infectious_days)




least_infectious_days = covid_df.sort_values('new_cases').head(10)

#print(least_infectious_days)

# as we can see from the data, there is a discrepancy in the new_cases column, -148 new cases which is unlikely for the 
# nature of our data, may be an entry error ; couple of ways to fix this:
# replace with 0 ; replace with avg for entire col ; replace with avg from previous and next record ; discard row entirely

# values can be modified through .at[] method
covid_df.at[172, 'new_cases'] = (covid_df.at[171, 'new_cases'] + covid_df.at[173, 'new_cases']) / 2

#print(covid_df.at[172, 'new_cases'])





# it seems that pandas does not really know it is a datetime format, so lets convert it

#print(covid_df.date)

covid_df['date'] = pd.to_datetime(covid_df.date)

#print(covid_df.date)




# and now to add specific time-period columns

covid_df['month'] = pd.DatetimeIndex(covid_df.date).month  # can also be done for year, month, day, weekday
covid_df['weekday'] = pd.DatetimeIndex(covid_df.date).weekday

#print(covid_df)






covid_df_may = covid_df[covid_df.month == 5]

may_metrics = covid_df_may[['new_cases', 'new_deaths', 'new_tests']]

may_totals = may_metrics.sum()

#print(may_totals)   # ----> this will output the totals for all three values for may


# and to do all that in a single line, the syntax is the following:

#print(covid_df[covid_df.month == 5][['new_cases', 'new_deaths', 'new_tests']].sum())







# to find the overall average ---> covid_df.new_cases.mean()

# and now to find it for Sundays

sunday_funday = covid_df[covid_df.weekday == 6]['new_cases'].mean()
# sunday_funday = covid_df[covid_df.weekday == 6].new_cases.mean()  --> can also be like that

# print(sunday_funday)









# GRANULARITY OF DATA - the subsections of data comprising the entire dataset -- in this case can be monthly, weekly, daily, etc

covid_by_month_df = covid_df.groupby('month')[['new_cases', 'new_deaths', 'new_tests']].sum()

#print(covid_by_month_df)

# this is also called aggregation, with pandas you can aggregate in a lot of ways. read documentation








covid_df['total_cases'] = covid_df.new_cases.cumsum()   # ---> this is to report the cumulative sum of an element

print(covid_df)


# and I will continue in the next python file as this one is getting long enough
