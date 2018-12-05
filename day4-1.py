class Log:
    def __init__(self, raw_data):
        self.raw_data = raw_data.strip()
        self.year, self.month, \
        self.day, self.hour, \
        self.minute, self.message = self.parse_raw_data(raw_data)
    
    def __str__(self):
        return self.raw_data

    def __repr__(self):
        return self.raw_data

    def __lt__(self, other):
        if self.year < other.year:
            return True
        elif self.year == other.year:
            if self.month < other.month:
                return True
            elif self.month == other.month:
                if self.day < other.day:
                    return True
                elif self.day == other.day:
                    if self.hour < other.hour:
                        return True
                    elif self.hour == other.hour:
                        if self.minute < other.minute:
                            return True
        return False

    def parse_raw_data(self, raw_data):
        # Get the message
        split_raw = raw_data.split('] ')
        message = split_raw[1]
        # Get the date data
        split_raw[0] = split_raw[0].replace('[', '')
        split_date_time = split_raw[0].split(' ')
        split_date = split_date_time[0].split('-')
        year = split_date[0]
        month = split_date[1]
        day = split_date[2]
        # Get the time data
        split_time = split_date_time[1].split(':')
        hour = split_time[0]
        minute = split_time[1]
        # Return data
        return (int(year), int(month), int(day), int(hour), int(minute), message)

def get_guard_number(message):
    """ Returns the number of the guard referenced in the message.
        Assumes that the guard number is in the message. """
    split_message = message.split(' ')
    return int(split_message[1].replace('#', ''))

def get_longest_sleeping_guard(logs):
    """ Given sorted logs, returns a tuple containing the guard who slept 
        the longest, how long they slept, and their sleep distribution. """
    # Calculate all guard sleep counts
    sleep_durations = {}
    sleep_distributions = {}
    current_guard = None
    sleep_start = None
    for log in logs:
        if 'Guard' in log.message:
            current_guard = get_guard_number(log.message)
            # Give guard a sleep distribution if they don't have one
            if current_guard not in sleep_distributions:
                sleep_distributions[current_guard] = {}
        elif 'falls asleep' in log.message:
            sleep_start = log.minute
        elif 'wakes up' in log.message:
            if current_guard in sleep_durations:
                sleep_durations[current_guard] = sleep_durations[current_guard] + (log.minute - sleep_start)
            else:
                sleep_durations[current_guard] = log.minute - sleep_start
            # Update sleep distributions
            for i in range(sleep_start, log.minute):
                if i in sleep_distributions[current_guard]:
                    sleep_distributions[current_guard][i] = sleep_distributions[current_guard][i] + 1
                else:
                    sleep_distributions[current_guard][i] = 1
    # Determine which guard slept the longest and how long
    longest = 0
    longest_guard = None
    for guard in sleep_durations:
        if sleep_durations[guard] > longest:
            longest = sleep_durations[guard]
            longest_guard = guard
    # Return the longest sleeping guard's data
    return (longest_guard, longest, sleep_distributions[longest_guard])

if __name__ == '__main__':
    # Read in the logs
    logs = []
    with open('day4.txt') as guard_log:
        for entry in guard_log:
            logs.append(Log(entry))
    # Sort the logs chronologically
    logs.sort()
    # Determine which guard slept the most
    guard, amount_slept, sleep_distribution = get_longest_sleeping_guard(logs)
    # Determine which minute that guard slept most
    most_slept_minute = -1
    most_slept_minutes = -1
    for minute in sleep_distribution:
        if sleep_distribution[minute] > most_slept_minutes:
            most_slept_minute = minute
            most_slept_minutes = sleep_distribution[minute]
    # Calculate answer
    print(guard * most_slept_minute)
