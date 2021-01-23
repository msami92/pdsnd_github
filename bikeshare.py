import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input('please enter either chicago or new york city or washington: ')
        if city in ('chicago','new york city','washington'):
            break
        else:
            print('invalid input')
            continue

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input('please enter either: january or february or march or april or may or june or all: ')
        if month in ('january','february','march','april','june','all'):
            break
        else:
            print('invalid input')
            continue
                    
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('please enter either: sunday or monday or tuesday or wednesday or friday or saturday or all: ')
        if day in ('sunday','monday','tuesday','wednesday','friday','saturday','all'):
            break
        else:
            print('invalid input')
            continue          

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load data file into a data frame
    df = pd.read_csv(CITY_DATA[city])
                      
    # convert the Start Time column to datetime   
    df['Start Time'] = pd.to_datetime(df['Start Time'])
                      
    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name                  
    
    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
                      
        # filter by month to create the new dataframe
        df = df[df['month'] == month]  
                      
    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]                 
                      
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month = df['month'].mode()[0]
    print('the most common month is:', most_common_month)                  

    # TO DO: display the most common day of week
    most_common_day = df['day_of_week'].mode()[0]
    print('the most common day is:', most_common_day)                 

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour                  
    most_common_start_hour = df['hour'].mode()[0]
    print('the most common start hour is:', most_common_start_hour)                   

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start_station = df['Start Station'].value_counts().idxmax()
    print('the most common start station is:',most_common_start_station)
                      
    # TO DO: display most commonly used end station
    most_common_end_station = df['End Station'].value_counts().idxmax()
    print('the most common end station is:',most_common_end_station)                  

    # TO DO: display most frequent combination of start station and end station trip
    most_common_stations_comb = df.groupby(['Start Station','End Station']).count()
    print('the most common stations combination is:',most_common_stations_comb)                  

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = sum(df['Trip Duration'])
    print('the total travel time (in days) is:',total_travel_time/86400)
                      
    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('the mean travel time (in minutes) is:',mean_travel_time/60)                  

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types_counts = df['User Type'].value_counts()
    print('the user types counts are:',user_types_counts)                    

    # TO DO: Display counts of gender
    try:
        gender_counts = df['Gender'].value_counts()
        print('the gender counts are:',gender_counts)              
    except KeyError:
        print('Sorry! no data is available')   
                      
    # TO DO: Display earliest, most recent, and most common year of birth
    # earliest year of birth                 
    try:
        earliest_year = df['Year Of birth'].min()
        print('the earliest year of birth is:',earliest_year)              
    except KeyError:
         print('Sorry! no data is available')             
    # most recent year of birth
    try:                 
        most_recent_year = df['Year Of birth'].max()                     
        print('the most recent year is:',most_recent_year)              
    except KeyError:
        print('Sorry! no data is available')
     # most common year of birth                 
    try:
        most_common_year = df['Year Of birth'].value_counts().idxmax()             
        print('the most common year of birth is:',most_common_year)             
    except KeyError:
        print('Sorry! no data is available')                    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def display_data(df):
    view_more = input('would you like to view 5 rows of individual data? Enter yes or no: ')
    start_loc = 0
    while(view_more == 'yes'):
        print(df.iloc[start_loc:start_loc+5])
        start_loc+=5
        view_more = input('would you like to continue? Enter yes or no: ').lower()
    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
