import pandas as pd

locations = pd.read_csv('locations.csv')

covid_df = pd.read_csv('italy-covid-daywise.csv')

locations_copy = locations.copy()

#print(locations[locations.location == 'Italy'])

covid_df['location'] = 'Italy'

#print(covid_df)







# to merge df's in order to be able to analyse them better, we need to use the .merge() and the 2 df's need to 
# have atleast 1 common column

merged_df = covid_df.merge(locations, on='location')

merged_df['total_cases'] = merged_df.new_cases.sum()
merged_df['total_deaths'] = merged_df.new_deaths.sum()
merged_df['total_tests'] = merged_df.new_tests.sum()

merged_df['cases_per_million'] = merged_df.total_cases * 1e6 / merged_df.population
merged_df['deaths_per_million'] = merged_df.total_deaths * 1e6 / merged_df.population
merged_df['tests_per_million'] = merged_df.total_tests * 1e6 / merged_df.population

#print(merged_df)

result_df = merged_df[['date', 'new_cases', 'total_cases', 'new_deaths', 'total_deaths', 'new_tests', 'total_tests',
'cases_per_million', 'deaths_per_million', 'tests_per_million']]

#result_df.to_csv("results_df.csv", index=None)











# BASIC PLOTTING WITH PANDAS

#result_df.new_cases.plot()  # if this was a conda environment and a ipynb (which there is a way to do so with VSC, opened the tutorial)
# will output a plot with the data specified






# to set a particular columns values as an index:
result_df.set_index('date', inplace=True)

# this means that we can now access values by passing the index value, aka date

#print(result_df.loc['2020-09-01'])




death_rate = result_df.total_deaths / result_df.total_cases

#death_rate.plot(title="DEATH RATE")

#covid_month_df.new_cases.plot(kind='bar')  # this will output a bar graph in conda environment


# this is all the material from this lesson and the assigment is the following thing I will have to do before proceeding to lesson 5

# assigment done, proceeded with lesson 5
































































































