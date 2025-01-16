from datetime import datetime, timedelta

gmt_time = datetime.utcnow()

offset = float(input("Enter the time zone offset in hours from GMT: "))

local_time = gmt_time + timedelta(hours=offset)

print("The current time in the specified time zone is:", local_time.strftime('%Y-%m-%d %H:%M:%S'))