kilometers_run = 14
total_time_seconds = (45 * 60) + 30
miles_per_kilometer = 1 / 1.6

average_speed_kph = (kilometers_run / total_time_seconds) * 3600
average_speed_mph = average_speed_kph * miles_per_kilometer

print('Average speed:', average_speed_mph, 'miles per hour')
