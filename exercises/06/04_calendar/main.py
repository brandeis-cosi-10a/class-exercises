def print_cal(num_weeks, days_per_week):
    day_num = 1
    for i in range(num_weeks):
        for d in range(days_per_week):
            print(str(day_num).zfill(3), end=' ')
            day_num += 1
        print()

print_cal(8, 11)