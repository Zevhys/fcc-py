def add_time(start, duration, day_of_week=None):
    days_of_the_week_index = {
        "monday": 0,
        "tuesday": 1,
        "wednesday": 2,
        "thursday": 3,
        "friday": 4,
        "saturday": 5,
        "sunday": 6,
    }

    days_of_the_week_array = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday",
    ]

    duration_tuple = duration.partition(":")
    duration_hours = int(duration_tuple[0])
    duration_minutes = int(duration_tuple[2])
    start_tuple = start.partition(":")
    start_minutes_tuple = start_tuple[2].partition(" ")
    start_hours = int(start_tuple[0])
    start_minutes = int(start_minutes_tuple[0])
    am_or_pm = start_minutes_tuple[2]
    total_start_hours = start_hours

    if am_or_pm == "PM" and start_hours != 12:
        total_start_hours += 12
    elif am_or_pm == "AM" and start_hours == 12:
        total_start_hours = 0

    total_start_minutes = total_start_hours * 60 + start_minutes
    total_duration_minutes = duration_hours * 60 + duration_minutes
    total_end_minutes = total_start_minutes + total_duration_minutes
    amount_of_days = total_end_minutes // (24 * 60)
    remaining_minutes = total_end_minutes % (24 * 60)
    end_hours = remaining_minutes // 60
    end_minutes = remaining_minutes % 60

    if end_hours == 0:
        display_hours = 12
        final_am_pm = "AM"
    elif end_hours < 12:
        display_hours = end_hours
        final_am_pm = "AM"
    elif end_hours == 12:
        display_hours = 12
        final_am_pm = "PM"
    else:
        display_hours = end_hours - 12
        final_am_pm = "PM"

    returnTime = f"{display_hours}:{end_minutes:02d} {final_am_pm}"

    if day_of_week:
        day_of_week = day_of_week.lower()
        index = (days_of_the_week_index[day_of_week] + amount_of_days) % 7
        new_day = days_of_the_week_array[index]
        returnTime += f", {new_day}"

    if amount_of_days == 1:
        return returnTime + " (next day)"
    elif amount_of_days > 1:
        return returnTime + f" ({amount_of_days} days later)"

    return returnTime


print(add_time("3:00 PM", "6:10"))
