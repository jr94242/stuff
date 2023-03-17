# so this is basically him doing the exact same thing I will have to do in the assigment before this lecture

# he is going to be doing that assigment on a dataset containing Stackoverflow's 2020 annual developer survey

# data analysis libraries
import pandas as pd
import numpy as np

# visualization libraries
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt
#%matplotlib inline

# visualisation configurations
sns.set_style('darkgrid')
matplotlib.rcParams['font.size'] = 14
matplotlib.rcParams['figure.figsize'] = (9, 5)
matplotlib.rcParams['figure.facecolor'] = '#00000000'











# DATA LOADING AND INITIAL FORMATTING

survey_raw = pd.read_csv('stackoverflow_survey/survey_results_public.csv')

schema_raw = pd.read_csv('stackoverflow_survey/survey_results_schema.csv', index_col='Column').QuestionText
# the following syntax will allow me to directly take the full questions by indexing the name of the column from schema_df

#print(survey_raw_df.columns)

#print(schema_raw['Age1stCode'])













# DATA PREPARATION AND CLEANING

# there is a lot of data, so limiting the dataset to be more insightful: 
# in the following areas: demographics ; distribution of programming skills ; employment-related info

selected_columns = [
    # Demographics
    'Country',
    'Age',
    'Gender',
    'EdLevel',
    'UndergradMajor',
    # Programming experience
    'Hobbyist',
    'Age1stCode',
    'YearsCode',
    'YearsCodePro',
    'LanguageWorkedWith',
    'LanguageDesireNextYear',
    'NEWLearn',
    'NEWStuck',
    # Employment
    'Employment',
    'DevType',
    'WorkWeekHrs',
    'JobSat',
    'JobFactors',
    'NEWOvertime',
    'NEWEdImpt'
]

# and now, to extract copy of the data in a new df:
survey_df = survey_raw[selected_columns].copy()
schema = schema_raw[selected_columns]

#print(survey_df.shape)
#print(survey_df.info())

# this shows that we need to manually take care of the NaN values, as well as converting some columns to numbers 
# as they are primarily numeric values in the rows



survey_df['Age1stCode'] = pd.to_numeric(survey_df.Age1stCode, errors='coerce')
survey_df['YearsCode'] = pd.to_numeric(survey_df.YearsCode, errors='coerce')
survey_df['YearsCodePro'] = pd.to_numeric(survey_df.YearsCodePro, errors='coerce')

# this will convert the values to numeric ones, in case it finds sth that it cannot convert, it will convert it to NaN

#print(survey_df.describe())   # ---> we can now see that there are 5 columns in total with numeric values


# as there are some weird values in some of the columns, like in age, the age is 1 or 279, we need to filter the dataset by directly 
# dropping all invalid rows

survey_df.drop(survey_df[survey_df.Age < 10].index, inplace=True)
survey_df.drop(survey_df[survey_df.Age > 100].index, inplace=True)

survey_df.drop(survey_df[survey_df.WorkWeekHrs > 140].index, inplace=True)

survey_df.where(~(survey_df.Gender.str.contains(';', na=False)), np.nan, inplace=True)
# this is to filter all the places, where idiots have selected more than 1 option, degenerates
# what is this syntax though? np.where/pd.where   ?????

















# EXPLORATORY ANALYSIS AND VISUALISATIONS

# as with any real-world data, there is some bias in this data, therefore we should aim to categorize certain groups of 
# people and other dependencies where the biased data can be represented more objectively

# we can do that by answering generalising question like those:





# COUNTRY

# print(schema.Country)
# print(survey_df.Country.unique())
# print(survey_df.Country.nunique())


# how do I find out how many people from each country took the survey
countries_representation = survey_df.Country.value_counts()
# print(countries_representation.head(20))   # this will output the 20 coutries with most surveyed


# visualising this conclusion:
# plt.figure(figsize=(12,6))
# plt.xticks(rotation=75)
# plt.title(schema.Country)
# sns.barplot(x=top_countries.index, y=top_countries);








# AGE

# visualisation for age via a histogram:
# plt.figure(figsize=(12, 6))
# plt.title(schema.Age)
# plt.xlabel('Age')
# plt.ylabel('Number of respondents')

# plt.hist(survey_df.Age, bins=np.arange(10,80,5), color='yellow');







# GENDER:

#print(schema.Gender)

# and now to find out how many of responders pertain to one or the other sex:
gender_counts = survey_df.Gender.value_counts(dropna=False)  # the dropna will also display the nan values, where people rejected answering
#print(gender_counts)

# and now to visualise this:
# plt.figure(figsize=(12,6))
# plt.title(schema.Gender)
# plt.pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%', startangle=180);

# this is a pie chart, values will change depending if T/F in the dropna argument







# EDUCATION LEVEL

# print(schema.EdLevel)



#visualisation:

# sns.countplot(y=survey_df.EdLevel)
# plt.xticks(rotation=75);
# plt.title(schema['EdLevel'])
# plt.ylabel(None);


# now lets dig deeper and find out out of those that have majors and bachelors, what part is in the computer sciences fields:
# print(schema.UndergradMajor)

undergrad_pct = survey_df.UndergradMajor.value_counts() * 100 / survey_df.UndergradMajor.count()


# visualisations for those percentages:
# sns.barplot(x=undergrad_pct, y=undergrad_pct.index)

# plt.title(schema.UndergradMajor)
# plt.ylabel(None);
# plt.xlabel('Percentage');






# EMPLOYMENT

#print(schema.Employment)

# and now to visualise what part of the participant have what type of employment:
# (survey_df.Employment.value_counts(normalize=True, ascending=True)*100).plot(kind='barh', color='g')
# plt.title(schema.Employment)
# plt.xlabel('Percentage');

# how does he do this plot to appear in percentage --> he simply multiplies by 100 the values in the rows/columns and 
# this is how he gets to this answer


#print(schema.DevType)

#print(survey_df.DevType.value_counts())


# Let's define a helper function that turns a column containing lists of values (like `survey_df.DevType`) 
# into a data frame with one column for each possible option:

def split_multicolumn(col_series):
    result_df = col_series.to_frame()
    options = []
    # Iterate over the column
    for idx, value  in col_series[col_series.notnull()].iteritems():
        # Break each value into list of options
        for option in value.split(';'):
            # Add the option as a column to result
            if not option in result_df.columns:
                options.append(option)
                result_df[option] = False
            # Mark the value in the option column as True
            result_df.at[idx, option] = True
    return result_df[options]


dev_type_df = split_multicolumn(survey_df.DevType)

# The `dev_type_df` has one column for each option that can be selected as a response. If a respondent has chosen an 
# option, the corresponding column's value is `True`. Otherwise, it is `False`.
# We can now use the column-wise totals to identify the most common roles.

dev_type_totals = dev_type_df.sum().sort_values(ascending=False)

#print(dev_type_totals)










# ASKING AND ANSWERING QUESTIONS:

# Q: What are the most popular programming languages in 2020? 

# survey_df.LanguageWorkedWith  # ---> this displays multiple options per answer, but we can separate them with the helper function

languages_worked_df = split_multicolumn(survey_df.LanguageWorkedWith)

# # this indicates 25 different languages, now let's see their distribution among the people

languages_worked_percentages = languages_worked_df.mean().sort_values(ascending=False) * 100

#print(languages_worked_percentages)





# Q: Which languages are the most people interested to learn over the next year?:

languages_interested_df = split_multicolumn(survey_df.LanguageDesireNextYear)
languages_interested_percentages = languages_interested_df.mean().sort_values(ascending=False) * 100

#print(languages_interested_percentages)

# and now to visualise those conclusions:
# plt.figure(figsize=(12, 12))
# sns.barplot(x=languages_interested_percentages, y=languages_interested_percentages.index)
# plt.title("Languages people are intersted in learning over the next year");
# plt.xlabel('count');






# Q:  Which are the most loved languages, i.e., a high percentage of people who 
# have used the language want to continue learning & using it over the next year?:

languages_loved_df = languages_worked_df & languages_interested_df

languages_loved_percentages = (languages_loved_df.sum() * 100/ languages_worked_df.sum()).sort_values(ascending=False)

# plt.figure(figsize=(12, 12))
# sns.barplot(x=languages_loved_percentages, y=languages_loved_percentages.index)
# plt.title("Most loved languages");
# plt.xlabel('count');




# Q: In which countries do developers work the highest number of hours per week? 
# Consider countries with more than 250 responses only.

countries_df = survey_df.groupby('Country')[['WorkWeekHrs']].mean().sort_values('WorkWeekHrs', ascending=False)

high_response_countries_df = countries_df.loc[survey_df.Country.value_counts() > 250].head(25)

#print(high_response_countries_df)

# this will output a df where the mean hours for each country represented by more than 250 participants will be calculated




# Q: How important is it to start young to build a career in programming?:

#print(schema.YearsCodePro)

# and to directly visualise that:

# sns.scatterplot(x='Age', y='YearsCodePro', hue='Hobbyist', data=survey_df)
# plt.xlabel("Age")
# plt.ylabel("Years of professional coding experience");


# and another visualisation on the topic:

# plt.title(schema.Age1stCode)
# sns.histplot(x=survey_df.Age1stCode, bins=30, kde=True);




















































































































































































































































































