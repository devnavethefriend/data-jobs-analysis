# Import the pandas and numpy packages
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
data_jobs = pd.read_csv('data_jobs.csv')

# Display basic information about the DataFrame
#print("\nDataFrame Info:")
#print(data_jobs.info())

# Display summary statistics of the DataFrame
#print("\nSummary Statistics:")
#print(data_jobs.describe())

# Check for missing values
# Add an if statement to print there are no missing values
if data_jobs.isnull().sum().sum() == 0:
    print("\nThere are no missing values in the DataFrame.")
else:
    print("\nThere are missing values in the DataFrame.")

# Find the number of different job titles from the job_title column
job_titles = data_jobs["job_title"].nunique()
print(f"\nThe total number of unique job titles in the database is {job_titles}.")

# Check the most and least entered job title
job_title_count = data_jobs["job_title"].value_counts()
print(f"The most occuring job is {job_title_count.idxmax()} with {job_title_count[0]} entries.")
print(f"There are multiple jobs with a single entry such as {job_title_count.idxmin()} being an example.")

# Visualize the distribution of the job titles to see the most occuring job
job_title_count = data_jobs["job_title"].value_counts()

# Display the top N most common job titles
top_n = 10
top_job_titles = job_title_count.head(top_n)

'''
# Plot the distribution of the top N job titles
plt.figure(figsize=(8, 4))
top_job_titles.plot(kind='bar')
plt.title(f"Top {top_n} Most Common Job Titles")
plt.xlabel("Job Title")
plt.ylabel("Count")
plt.xticks(rotation=45, ha='right')
plt.show()
'''

# Check for the highest salary in usd from the salary_in_usd column
# Fill missing values in the column with the mean value
highest_salary = data_jobs.loc[data_jobs["salary"].idxmax()]
print(f"\nThe highest salary from the different jobs available is ${highest_salary['salary_in_usd']} which is paid for a {highest_salary['job_title']} job.")

'''
More analysis on a Research Engineer job title
'''
# Subset for the job titles with Research engineer as value
research_jobs = data_jobs[data_jobs["job_title"] == 'Research Engineer']
#print(research_jobs)
 
# What is the lowest salary for a research engineer job
lowest_salary = research_jobs["salary_in_usd"].min()
lowest_research_salary = research_jobs[research_jobs["salary_in_usd"] == lowest_salary]
lowest_research_salary_location = lowest_research_salary["company_location"].values[0]
print(f"The lowest salary paid for a Research Engineer job is ${lowest_salary} in {lowest_research_salary_location}.")

# Which company location hires the most reserch engineer
# Count the occurrences of each company location for research engineers
research_location_counts = research_jobs["company_location"].value_counts()

# Identify the company location with the highest count
top_research_location = research_location_counts.idxmax()
top_research_location_count = research_location_counts.max()
print(f"The company location that hires the most research engineers is {top_research_location} with {top_research_location_count} entries.")

# Visualize the spread of experience level for a research engineer job title
# Count the occurrences of each experience level for research engineers
research_job_experience = research_jobs["experience_level"].value_counts()

'''
# Plot the distribution using a bar plot
plt.figure(figsize=(10, 6))
sns.barplot(x=research_job_experience.index, y=research_job_experience.values, palette='viridis')
plt.title("Distribution of Experience Levels for Research Engineer Job Title")
plt.xlabel("Experience Level")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.show() 
'''

'''
 Analysis on Remote work settings
'''

# Subset for the work_setting columns with 'Remote' as value
remote_settings = data_jobs[data_jobs["work_setting"] == 'Remote']
remote_settings_count = remote_settings["work_setting"].value_counts().sum()
print(f"\nThere are a total of {remote_settings_count} remote jobs present.")

# Find and compare the highest and lowest salary under a remote work setting
highest_salary = remote_settings["salary_in_usd"].max()
lowest_salary = remote_settings["salary_in_usd"].min()
highest_salary_details = remote_settings[remote_settings["salary_in_usd"] == highest_salary]
highest_salary_details_job = highest_salary_details["job_title"].values[0]
highest_salary_details_location = highest_salary_details["company_location"].values[0]

lowest_salary_details = remote_settings[remote_settings["salary_in_usd"] == lowest_salary]
lowest_salary_details_job = lowest_salary_details["job_title"].values[0]
lowest_salary_details_location = lowest_salary_details["company_location"].values[0]
print(f"\nThe highest salary for a remote job is ${highest_salary} for a {highest_salary_details_job} job available in {highest_salary_details_location}.")
print(f"The lowest salary for a remote job is ${lowest_salary} for a {lowest_salary_details_job} in {lowest_salary_details_location}.")

# Find the country with more remote work setting entries
# Group by 'company_location' and count the number of job entries for each location
country_counts = remote_settings.groupby("company_location").size().reset_index(name="count")

# Sort the results by count in descending order
sorted_country_counts = country_counts.sort_values(by="count", ascending=False)

# Get the country with the highest and lowest count
top_country = sorted_country_counts.iloc[0]["company_location"]
top_country_count = sorted_country_counts.iloc[0]["count"]
least_country = sorted_country_counts.iloc[-1]["company_location"]
least_country_count = sorted_country_counts.iloc[-1]["count"]
print(f"\nThe country with the most remote jobs is {top_country} with {top_country_count} entries.")
print(f"While {least_country} has the lowest available remote job with {least_country_count} entries.")

# Visualise the spread of jobs under remote work settings
# Group by 'job_title' and count the number of job entries for each job title
job_counts = remote_settings.groupby("job_title").size().reset_index(name="count")

# Sort the results by count in descending order
sorted_job_counts = job_counts.sort_values(by="count", ascending=False)
top_n = 20
top_sorted_job_counts = sorted_job_counts.head(top_n)

'''
# Visualize the spread of top N jobs under remote work settings
plt.figure(figsize=(14, 7))
sns.barplot(x="count", y="job_title", data=top_sorted_job_counts, palette="viridis")
plt.title("Number of Remote Jobs by Job Title")
plt.xlabel("Number of Jobs")
plt.ylabel("Job Title")
plt.show()
'''

# Find the most occuring job_title in the subset
remote_job_titles = remote_settings["job_title"].value_counts()

# Get the top most occuring remote job title
most_occuring_remote = remote_job_titles.idxmax()

# Filter the DataFrame for the most common remote job title
most_common_remote_job = remote_settings[remote_settings["job_title"] == most_occuring_remote]
print(f"\nThe most available job for remote work setting is {most_occuring_remote} with a total of {remote_job_titles[0]} entriess.")

# Check the highest and lowest salary paid for the most occuring remote job position
highest_salary = most_common_remote_job["salary_in_usd"].max()
lowest_salary = most_common_remote_job["salary_in_usd"].min()
print(f"The highest salary for a {most_occuring_remote} is ${highest_salary}")
print(f"With a lowest salary of ${lowest_salary}")

# Find the company_location and experience level
remote_job_location = most_common_remote_job["company_location"].value_counts()
remote_experience_level = most_common_remote_job["experience_level"].value_counts()
print(f"The {remote_job_location.idxmax()} offers more remote work setting for a {most_occuring_remote} with a total of {remote_job_location[0]} entries.")

# Visualize the distribution of most occuring remote job with experience level


# Compare the stats of remote work to In_person work settings, using groupby
# Subset for the work_setting columns with 'Remote' as value
in_person_settings = data_jobs[data_jobs["work_setting"] == 'In-person']
in_person_jobs = in_person_settings["job_title"].value_counts()
#print(in_person_jobs.head())

# Get the top most occuring In-person job title
most_occuring_in_person = in_person_jobs.idxmax()

# Filter the DataFrame for the most common remote job title
common_in_person_job = in_person_settings[in_person_settings["job_title"] == most_occuring_in_person]
print(f"\nThe most available job for on site work setting is {most_occuring_in_person} with a total of {in_person_jobs[0]} entries.")
print(f"Followed by a Data Scientist and Data Analyst job with {in_person_jobs[1]} and {in_person_jobs[2]} entries respectively.")

# Find the company_location and experience level
in_person_job_location = common_in_person_job["company_location"].value_counts()
in_person_experience_level = common_in_person_job["experience_level"].value_counts()
print(f"The {in_person_job_location.idxmax()} offers more on site work setting for a {most_occuring_in_person} with a total of {in_person_job_location[0]} entries.")

# Visualize the spread of experience level for in person work settings
# Visualise the distribution of salaries in this subset
