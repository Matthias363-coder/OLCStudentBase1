# Task 5.1
def calculate_minutes(time):
    hour = time[:2]
    min = time[3:]

    hour_num = int(hour)
    min_num = int(min)

    total_minutes = hour_num * 60 + min_num

    return total_minutes

print(calculate_minutes("00:30"))
print(calculate_minutes("23:59"))

# Task 5.2
def calculate_wage(clock_in, clock_out):
    clock_in_mins = calculate_minutes(clock_in)
    clock_out_mins = calculate_minutes(clock_out)
    time_in_mins = clock_out_mins - clock_in_mins
    hour_worked = time_in_mins // 60

    if hour_worked <= 8:
        money = hour_worked * 20
    else:
        normal_pay = 8 * 20
        OT = hour_worked - 8
        OT_pay = OT * 30
        money = normal_pay + OT_pay

    return money
    
print(calculate_wage("00:00", "08:00"))
print(calculate_wage("00:00", "10:00"))

# Task 5.3
while True:
    while True:
        validate_clock_in_time = input("Enter time in the HH:MM format: ")
        hour = validate_clock_in_time[:2]
        minute = validate_clock_in_time[3:]
        if hour >= 00 and hour <= 23:
            print("Valid hour")
            break
        else:
            print("Invalid hour")
    while True:
        validate_clock_in_time = input("Enter time in the HH:MM format: ")
        if minutes >= 00 and minutes <= 59:
            print("Valid minute")
            break
        else:
            print("Invalid minute")
    while True:
        validate_clock_in_time = input("Enter time in the HH:MM format:")
        if len(validate_clock_in_time) != 5 and validate_clock_in_time[3] != ":":
            print("Invalid format")
        else:
            print("Valid format")
            break
    while True:
        validate_clock_out_time = input("Enter time in the HH:MM format: ")
        hours = validate_clock_out_time[:2]
        minutes = validate_clock_out_time[3:]
        if hours >= 00 and hours <= 23:
            print("Valid hour")
            break
        else:
            print("Invalid hour")
    while True:
        validate_clock_out_time = input("Enter time in the HH:MM format: ")
        if minutes >= 00 and minutes <= 59:
            print("Valid minute")
            break
        else:
            print("Invalid minute")
    while True:
        validate_clock_out_time = input("Enter time in the HH:MM format: ")
        if len(validate_clock_out_time) != 5 and validate_clock_out_time[3] != ":":
            print("Invalid format")
        else:
            print("Valid format")
            break

        hours_difference = validate_clock_out_time - validate_clock_in_time
        if hours_difference > 0:
            print("Valid Time")
            break
        else:
            print("Invalid time")




