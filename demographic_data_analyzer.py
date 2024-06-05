import pandas as pd

def calculate_race_counts(df):
    return df['race'].value_counts()

def calculate_average_age_men(df):
    return round(df[df['sex'] == 'Male']['age'].mean(), 1)

def calculate_percentage_bachelors(df):
    return round((df[df['education'] == 'Bachelors'].shape[0] / df.shape[0]) * 100, 1)

def calculate_percentage_high_education(df):
    higher_education = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    return round((higher_education[higher_education['salary'] == '>50K'].shape[0] / higher_education.shape[0]) * 100, 1)

def calculate_percentage_low_education(df):
    lower_education = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    return round((lower_education[lower_education['salary'] == '>50K'].shape[0] / lower_education.shape[0]) * 100, 1)

def calculate_min_work_hours(df):
    return df['hours-per-week'].min()

def calculate_percentage_min_workers(df):
    min_hours = df['hours-per-week'].min()
    min_workers = df[df['hours-per-week'] == min_hours]
    return round((min_workers[min_workers['salary'] == '>50K'].shape[0] / min_workers.shape[0]) * 100, 1)

def calculate_highest_earning_country(df):
    countries = df['native-country'].unique()
    highest_percentage = 0
    highest_country = None
    for country in countries:
        country_df = df[df['native-country'] == country]
        percentage = (country_df[country_df['salary'] == '>50K'].shape[0] / country_df.shape[0]) * 100
        if percentage > highest_percentage:
            highest_percentage = percentage
            highest_country = country
    return highest_country, round(highest_percentage, 1)

def calculate_top_IN_occupation(df):
    india_df = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
    if not india_df.empty:
        top_occupation = india_df['occupation'].value_counts().idxmax()
    else:
        top_occupation = "No data for India in the DataFrame"
    return top_occupation

if __name__ == "__main__":
    # Load dataset
    df = pd.read_csv('your_dataset.csv')

    # Call functions and print results
    race_counts = calculate_race_counts(df)
    print("Count of Each Race:")
    print(race_counts)

    average_age_men = calculate_average_age_men(df)
    print("\nAverage Age of Men:", average_age_men)

    percentage_bachelors = calculate_percentage_bachelors(df)
    print("\nPercentage with Bachelor's Degree:", percentage_bachelors)

    percentage_high_education = calculate_percentage_high_education(df)
    print("\nPercentage with Advanced Education Earning >50K:", percentage_high_education)

    percentage_low_education = calculate_percentage_low_education(df)
    print("\nPercentage without Advanced Education Earning >50K:", percentage_low_education)

    min_work_hours = calculate_min_work_hours(df)
    print("\nMinimum Number of Hours Worked per Week:", min_work_hours)

    percentage_min_workers = calculate_percentage_min_workers(df)
    print("\nPercentage of Minimum Hour Workers Earning >50K:", percentage_min_workers)

    highest_earning_country, highest_percentage = calculate_highest_earning_country(df)
    print("\nCountry with Highest Percentage Earning >50K:", highest_earning_country, "({}%)".format(highest_percentage))

    top_IN_occupation = calculate_top_IN_occupation(df)
    print("\nTop occupations in India:", top_IN_occupation)
