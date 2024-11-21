import csv
with open('exercises/09/01_mta_ridership/mta_ridership.csv') as f:
    reader = csv.reader(f, delimiter=",")
    max_subway = 0
    max_subway_day = None
    subway_total = 0
    bus_ridership_higher = 0
    total_days = 0
    bus_rides_first_of_month = 0

    next(reader)
    for line in reader:
        date = line[0]
        subway_rides = int(line[1])
        bus_rides = int(line[3])

        total_days += 1
        subway_total += subway_rides
        if max_subway < subway_rides:
            max_subway = subway_rides
            max_subway_day = date
        if bus_rides > subway_rides:
            bus_ridership_higher += 1
        if(int(date.split('/')[1]) == 1):
            bus_rides_first_of_month += bus_rides

print(f"Total subway rides: {subway_total}")
print(f"Highest subway day: {max_subway_day}")
print(f"Bus ridership higher on {bus_ridership_higher / total_days * 100}% of days")
print(f"Bus rides on first of month: {bus_rides_first_of_month}")
