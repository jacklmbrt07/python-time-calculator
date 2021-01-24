def add_time(start, duration):
    start_list = start.split(" ")
    start_list[0] = start_list[0].split(":")
    
    start_dict = {
        "hours":  int(start_list[0][0]) if (start_list[1] == 'AM') else int(start_list[0][0]) + 12, 
        "minutes": int(start_list[0][1]), 
        "meridiem": start_list[1], 
    }




    return start_dict