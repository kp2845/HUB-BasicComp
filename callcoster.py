call_day = input("Enter the day the call starter at: ")
call_time = int(input("Enter the time the call started at (hhmm): "))
call_duration = int(input("Enter the duration of the call (in minutes): "))
if call_day == "Sat" or call_day == "Sun":
    call_cost = .15 * call_duration
elif call_day == "Mon" or call_day == "Tue" or call_day == "Wed" or call_day == "Thu" or call_day == "Fri":
    if 800 <= call_time <= 1800:
        call_cost = .40 * call_duration
    else:
        call_cost = .25 * call_duration
print("This call will cost ${:0.2f}".format(call_cost))
