def time_ward(elapsed, elapsed_format, location_source):
    # location source:
    # - f: faerun
    # - h: hollowbold
    #
    # CONVERSION
    # Faerun | Hollowbold
    # 1 sec  = 30 seconds
    # 1 min  = 30 minutes
    # 1 day  = 30 days

    time_ward_multiplier = 30
    return_string = "Time Elapsed=:\n"
    
    if location_source == "h":
        if elapsed_format == "s":
            elapsed_seconds = float(elapsed) * 30
        if elapsed_format == "m":
            elapsed_seconds = float(elapsed) * 60 * 30
        if elapsed_format == "h":
            elapsed_seconds = float(elapsed) * 60 * 60 * 30
        if elapsed_format == "d":
            elapsed_seconds = float(elapsed) * 60 * 60 * 24 * 30
        # seconds
        return_string += f" - {elapsed_seconds} seconds\n"
        # minutes
        return_string += f" - {elapsed_seconds/60} minutes\n"
        # hours
        return_string += f" - {elapsed_seconds/60/60} hours\n"
        # days
        return_string += f" - {elapsed_seconds/60/60/24} days\n"
        # months
        return_string += f" - {elapsed_seconds/60/60/24/30} months\n"
    return return_string

my_elapsed = input("Elapsed in Hollowbold? ")
my_elapsed_format = input("(S)econds, (M)inutes, (H)ours, or (D)ays? ")
print(time_ward (my_elapsed, my_elapsed_format, "h"))