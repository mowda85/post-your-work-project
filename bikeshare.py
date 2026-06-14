import time
import pandas as pd
 
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
 
MONTHS = ['january', 'february', 'march', 'april', 'may', 'june']
DAYS = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
 
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
        city = input(
            "\nWhich city would you like to explore?\n"
            "  Options: Chicago, New York City, Washington\n"
            "> "
        ).strip().lower()
        if city in CITY_DATA:
            break
        print(f"  x '{city}' is not a valid city. Please try again.")
 
    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        filter_type = input(
            "\nWould you like to filter the data by month, day, both, or not at all?\n"
            "  Options: month, day, both, none\n"
            "> "
        ).strip().lower()
        if filter_type in ('month', 'day', 'both', 'none'):
            break
        print(f"  x '{filter_type}' is not a valid option. Please enter month, day, both, or none.")
 
    month = 'all'
    if filter_type in ('month', 'both'):
        while True:
            month = input(
                "\nWhich month? January, February, March, April, May, or June?\n"
                "> "
            ).strip().lower()
            if month in MONTHS:
                break
            print(f"  x '{month}' is not a valid month. Please choose from January-June.")
 
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = 'all'
    if filter_type in ('day', 'both'):
        while True:
            day = input(
                "\nWhich day of the week?\n"
                "  Options: Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday\n"
                "> "
            ).strip().lower()
            if day in DAYS:
                break
            print(f"  x '{day}' is not a valid day. Please enter a full day name.")
 
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
    bike_df = pd.read_csv(CITY_DATA[city])
 
    # Convert Start Time to datetime
    bike_df['Start Time'] = pd.to_datetime(bike_df['Start Time'])
 
    # Extract helper columns
    bike_df['month'] = bike_df['Start Time'].dt.month
    bike_df['day_of_week'] = bike_df['Start Time'].dt.dayofweek
    bike_df['hour'] = bike_df['Start Time'].dt.hour
 
    # Apply month filter
    if month != 'all':
        month_index = MONTHS.index(month) + 1
        df = df[df['month'] == month_index]
 
    # Apply day filter
    if day != 'all':
        day_index = DAYS.index(day)
        df = df[df['day_of_week'] == day_index]
 
    return bike_df
 
 
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
 
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
 
    # TO DO: display the most common month
    common_month_num = df['month'].mode()[0]
    common_month = MONTHS[common_month_num - 1].title()
    print(f"  Most Common Month     : {common_month}")
 
    # TO DO: display the most common day of week
    common_day_num = df['day_of_week'].mode()[0]
    common_day = DAYS[common_day_num].title()
    print(f"  Most Common Day       : {common_day}")
 
    # TO DO: display the most common start hour
    common_hour = df['hour'].mode()[0]
    period = 'AM' if common_hour < 12 else 'PM'
    display_hour = common_hour if common_hour in (0, 12) else common_hour % 12
    if display_hour == 0:
        display_hour = 12
    print(f"  Most Common Start Hour: {display_hour}:00 {period} (hour {common_hour})")
 
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
 
 
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
 
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
 
    # TO DO: display most commonly used start station
    common_start = df['Start Station'].mode()[0]
    print(f"  Most Common Start Station : {common_start}")
 
    # TO DO: display most commonly used end station
    common_end = df['End Station'].mode()[0]
    print(f"  Most Common End Station   : {common_end}")
 
    # TO DO: display most frequent combination of start station and end station trip
    df['trip'] = df['Start Station'] + '  ->  ' + df['End Station']
    common_trip = df['trip'].mode()[0]
    print(f"  Most Common Trip          : {common_trip}")
 
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
 
 
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
 
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
 
    # TO DO: display total travel time
    total_seconds = df['Trip Duration'].sum()
 
    # TO DO: display mean travel time
    mean_seconds = df['Trip Duration'].mean()
 
    def format_duration(seconds):
        """Convert seconds into a human-readable days/hours/minutes/seconds string."""
        seconds = int(seconds)
        days, remainder = divmod(seconds, 86400)
        hours, remainder = divmod(remainder, 3600)
        minutes, secs = divmod(remainder, 60)
        parts = []
        if days:
            parts.append(f"{days}d")
        if hours:
            parts.append(f"{hours}h")
        if minutes:
            parts.append(f"{minutes}m")
        parts.append(f"{secs}s")
        return ' '.join(parts)
 
    print(f"  Total Travel Time  : {format_duration(total_seconds)}  ({total_seconds:,} seconds)")
    print(f"  Average Travel Time: {format_duration(mean_seconds)}  ({mean_seconds:,.1f} seconds)")
 
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
 
 
def user_stats(df):
    """Displays statistics on bikeshare users."""
 
    print('\nCalculating User Stats...\n')
    start_time = time.time()
 
    # TO DO: Display counts of user types
    print("  User Types:")
    user_type_counts = df['User Type'].value_counts()
    for user_type, count in user_type_counts.items():
        print(f"    {user_type}: {count:,}")
 
    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        print("\n  Gender:")
        gender_counts = df['Gender'].value_counts()
        for gender, count in gender_counts.items():
            print(f"    {gender}: {count:,}")
        missing_gender = df['Gender'].isna().sum()
        if missing_gender > 0:
            print(f"    (Not provided: {missing_gender:,})")
    else:
        print("\n  Gender: Data not available for this city.")
 
    # TO DO: Display earliest, most recent, and most common year of birth (Only Chicago and NYC)
    if 'Birth Year' in df.columns:
        earliest = int(df['Birth Year'].min())
        most_recent = int(df['Birth Year'].max())
        most_common = int(df['Birth Year'].mode()[0])
        print(f"\n  Birth Year:")
        print(f"    Earliest   : {earliest}")
        print(f"    Most Recent: {most_recent}")
        print(f"    Most Common: {most_common}")
    else:
        print("\n  Birth Year: Data not available for this city.")
 
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
 
 
def display_raw_data(df):
    """
    Prompts the user whether they want to see raw data, then displays
    5 rows at a time until the user says 'no' or all rows are shown.
    """
    row_index = 0
    total_rows = len(df)
 
    while row_index < total_rows:
        show = input('\nWould you like to see 5 rows of raw data? Enter yes or no.\n').strip().lower()
        if show == 'yes':
            print(df.iloc[row_index: row_index + 5].to_string())
            row_index += 5
        elif show == 'no':
            break
        else:
            print("Please enter 'yes' or 'no'.")
 
 
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
 
        if df.empty:
            print('\nNo data found for the selected filters. Please try different options.')
        else:
            time_stats(df)
            station_stats(df)
            trip_duration_stats(df)
            user_stats(df)
            display_raw_data(df)
 
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
 
 
if __name__ == "__main__":
    main()