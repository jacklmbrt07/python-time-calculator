def add_time(start, duration):
    start_list = start.split(" ")
    start_list[0] = start_list[0].split(":")
    
    start_dict = {
        "hours":  int(start_list[0][0]) if (start_list[1] == 'AM') else int(start_list[0][0]) + 12, 
        "minutes": int(start_list[0][1]), 
        "meridiem": start_list[1], 
    }




    return start_dict

# notes psuedo code
# 1) convert start time into 24 hour time, edge cases 12:00 AM = 00:00. 
# 2) convert start and duration into seconds
# 3) add start and duration together
# 4) convert final time into 24 hour time
# 5) convert into 12 hour time and return, and number of days ahead
#       5a) 1 day ahead: "(next day)"
#       5b) >1 day ahead: "(x days later)"
#  6) return day of the week later with conditional arg using modulos