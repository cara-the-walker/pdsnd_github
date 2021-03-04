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
    threecities = ['chicago','washington','new york city']
    sixmonths = ['january','february','march','april','may','june']
    sevendays = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']

    # TO DO: get user input for month (all, january, february, ... , june)
    city = input('\n\nWhich city you are interested? Chicago, Washington or New York City?      ').lower().strip()

    while city not in threecities:
        print('\n\nPlease enter a valid city name.')
        city = input('Chicago, Washington or New York City?     ')

    month = input('\n\nDo you want to look into a specific month? Yes or No?      ').lower().strip()

    if month == 'no':
        month = 'all'
    elif month == 'yes':
        month = input('January, February,...,June?      ').lower().strip()
        while month not in sixmonths:
            print('Please enter a valid months.')
            month = input('January, February,...,June?      ').lower().strip()


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input('\n\nDo you want to look into a particular day of the week? Yes or No?    ').lower().strip()

    if day == 'no':
        day = 'all'
    elif day == 'yes':
        day = input('Monday, Tuesday,..., Sunday?       ').title()
        while day not in sevendays:
            print('Please enter a valid dayname.        ')
            day = input('Monday, Tuesday,..., Sunday?'      ).title()


    print('-'*40)
    return city, month, day


def load_data(city, month, day):

    df = pd.read_csv(CITY_DATA[city])

    df['month'] = pd.to_datetime(df['Start Time']).dt.month

    df['day_of_week'] = pd.to_datetime(df['Start Time']).dt.day_name()

    months = {'january':1,
    'february':2,
    'march':3,
    'april':4,
    'may':5,
    'june':6}

    if month != 'all' and day != 'all':

        df = df[df['month'] == months[month]]
        df = df[df['day_of_week'] == day]

    elif month != 'all' and day == 'all':
        df = df[df['month'] == months[month]]

    elif month == 'all' and day != 'all':
        df = df[df['day_of_week'] == day]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    if len(df['month'].unique()) != 1:
        print('Most Common Month: ',df['month'].mode()[0])

    # TO DO: display the most common day of week
    if len(df['day_of_week'].unique()) != 1:
        print('Most Common Day of Week: ',df['day_of_week'].mode()[0])

    # TO DO: display the most common start hour
    df['hour'] = pd.to_datetime(df['Start Time']).dt.hour
    print('Most Common Hour of Day: ',df['hour'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('Most Common Start Station: ',df['Start Station'].mode()[0])

    # TO DO: display most commonly used end station
    print('Most Common End Station: ',df['End Station'].mode()[0])

    # TO DO: display most frequent combination of start station and end station trip
    df['trip'] = df['Start Station'] + df['End Station']
    print('Most Common Trip: ',df['trip'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('Total Travel Time: ',df['Trip Duration'].sum())

    # TO DO: display mean travel time
    print('Average Travel Time: ',df['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('Counts of Subscriber: ',df['User Type'].value_counts().Subscriber)
    print('Counts of Customer: ',df['User Type'].value_counts().Customer)

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        tempdf = pd.DataFrame()
        print('Counts of Male User: ',df['Gender'].value_counts().Male)
        print('Counts of Remale User: ',df['Gender'].value_counts().Female)

    # TO DO: Display earliest, most recent, and most common year of birth
        tempdf['Birth Year'] = df['Birth Year']
        tempdf = tempdf.dropna(axis=0)
        tempdf['Birth Year'] = tempdf['Birth Year'].astype(int)
        print('Earlist Birth Year of User: ',tempdf['Birth Year'].min())
        print('Recent Birth Year of User: ',tempdf['Birth Year'].max())
        print('Most Common Birth Year of User: ',tempdf['Birth Year'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(answer,dataframe):
    start_loc = 0
    while answer == 'yes':
        print(dataframe[start_loc:start_loc+5])
        start_loc += 5
        answer = input('\n\nDo you want to see 5 more lines? Yes or No?'        ).lower().strip()

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        see_details = input('\n\nMaybe you want to see the user data in detail. Perhaps 5 lines. Yes or No?     ').lower().strip()
        display_data(see_details,df)

        another_enquiry = input('Do you want to start another enquiry? Yes or No?     ').lower().strip()

        while another_enquiry not in ('yes','no'):
            print('\n\nPlease enter a valid answer.')
            another_enquiry = input('Yes/No?     ').lower().strip()

        if another_enquiry == 'no':
            print('\n\nI am happy to help you. Have a nice day!')
            break


if __name__ == "__main__":
	main()
