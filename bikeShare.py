import time
import datetime
import calendar as caldr
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    city,day = '',''
    month = -1
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while city not in CITY_DATA.keys():
        print("Enter name of the city to analyze (chicago, new york city, washington):")
        city = input().lower()

        if city not in CITY_DATA.keys():
            print("Invalid City.")

    # TO DO: get user input for month (all, january, february, ... , june)
    while type(month) != int  or int(month) > 12 or int(month) < 0:
        print("Enter number of the month to filter by, or 0 to apply no month filter: ")
        
        try:
            month = int(input())
            if month > 12 or month < 0:
                print("Invalid number")
        except ValueError:
            print("This is not a number.")
        
        

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    daysList = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    day = ''
    while day not in daysList:
        print("Enter name of the day of week to filter by, or '"'all'"' to apply no day filter:")
        day = input().lower()

        if day not in daysList:
            print("Invalid input")



    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
 

    #Get month and day from Start Time
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    
    #Filter by month
    if month != 0:
        df = df[df['month'] == month]

    #Filter by day 
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...')
    start_time = time.time()

    # TO DO: display the most common month
    commonMonth = caldr.month_name[df['month'].mode()[0]]
    print("The most common month: {}".format(commonMonth))


    # TO DO: display the most common day of week
    commonDay = df['day_of_week'].mode()[0]
    print("The most common day of week: {}".format(commonDay))


    # TO DO: display the most common start hour
    df['hours'] = df['Start Time'].dt.hour
    commonHour = datetime.time(df['hours'].mode()[0]).strftime("%I %p") 
    print("The most common start hour: {}".format(commonHour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...')
    start_time = time.time()

    # TO DO: display most commonly used start station
    commonStartStation = df['Start Station'].mode()[0]
    print("The most commonly used start station: {}".format(commonStartStation))


    # TO DO: display most commonly used end station
    commonEndStation = df['End Station'].mode()[0]
    print("The most commonly used end station: {}".format(commonEndStation))

    # TO DO: display most frequent combination of start station and end station trip
    df['combo'] = df['Start Station'].str.cat(df['End Station'], sep=' to ')
    combo = df['combo'].mode()[0]
    print("The most frequent trips from {}".format(combo))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...')
    start_time = time.time()

    # TO DO: display total travel time
    total_duration = datetime.timedelta(seconds = int(df['Trip Duration'].sum()))
    print("The total trip duration is {}".format(total_duration))

    # TO DO: display mean travel time
    average_duration =  datetime.timedelta(seconds =  round(df['Trip Duration'].mean()))
    print("The average trip durationis {}".format(average_duration))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    userTypes = df['User Type'].value_counts()
    print("Counts by user types:\n{}".format(userTypes))


    # TO DO: Display counts of gender
    try:
        userGender = df['Gender'].value_counts()
        print("Counts by gender:\n{}".format(userGender))
    except:
        print("Gender data is not found")


    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest = int(df['Birth Year'].min())
        recent = int(df['Birth Year'].max())
        commonYear = int(df['Birth Year'].mode()[0])
        print("\nThe earliest year of birth: {}\nThe most recent year of birth: {}\nThe most common year of birth: {}".format(earliest,recent,commonYear))
    except:
        print("There are no birth year details in this file.")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    
    view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no: ')
    start_loc = 0
    view_display = 'yes'
    while view_data != 'no' and view_display == 'yes' :
        print(df.iloc[start_loc:start_loc+5])
        start_loc += 5
        view_display = input("Do you wish to continue? Enter yes or no: ").lower()
    
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
