def add_time(start, duration):
    start_list = start.split(" ")
    start_list[0] = start_list[0].split(":")
    
    duration_list = duration.split(":")
    
    
    start_time = {
        "hours":  int(start_list[0][0]),
        "minutes": int(start_list[0][1]), 
        "meridiem": start_list[1], 
        "duration_hours": int(duration_list[0]),
        "duration_minutes": int(duration_list[1]),
    }
    
# 1) convert start time into 24 hour time, edge cases 12:00 AM = 00:00. 
    if start_time["meridiem"] == 'PM' and not start_time["hours"] == 12:
        start_time["hours"] = start_time["hours"] + 12
    if start_time["hours"] == 12 and start_time["meridiem"] == 'AM':
        start_time["hours"] = 0
        
# 2) convert start and duration into minutes
    start_minutes = (start_time["hours"] * 60) + start_time["minutes"]
    duration_minutes = (start_time["duration_hours"] * 60) + start_time["duration_minutes"]

# 3) add start and duration together
    final_time_minutes = start_minutes + duration_minutes
    
# 4) convert final time into 24 hour time
    final_time_str = {
        "hours": (final_time_minutes / 60) % 24, 
        "minutes": final_time_minutes % 60,
        "meridiem": ""
    }
    
    if final_time_str["hours"] == 0:
        final_time_str["hours"] = 12
        final_time_str["meridiem"] = 'AM'
    elif final_time_str["hours"] > 0 and final_time_str["hours"] < 12:
        final_time_str["meridiem"] = 'AM'
    elif final_time_str["hours"] >= 12:
        final_time_str["meridiem"] = 'PM'
        
    if final_time_str["hours"] < 10:
        final_time_str["hours"] = "0{}".format(str(final_time_str["hours"]))
    else:
        final_time_str["hours"] = str(final_time_str["hours"])
        
    if final_time_str["minutes"] < 10:
        final_time_str["minutes"] = "0{}".format(str(final_time_str["minutes"]))
    else:
        final_time_str["minutes"] = str(final_time_str["minutes"])
        
    answer = "{hr}:{min} {mer}".format(hr = final_time_str["hours"], min = final_time_str["minutes"], mer = final_time_str["meridiem"])
            
    return answer

# notes psuedo code
# 5) convert into 12 hour time and return, and number of days ahead
#       5a) 1 day ahead: "(next day)"
#       5b) >1 day ahead: "(x days later)"
#  6) return day of the week later with conditional arg using modulos