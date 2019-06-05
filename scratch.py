for week in range(0, how_many_weeks_to_check):
    start_date = current_time + datetime.timedelta(days=week*7) + datetime.timedelta(days=weeks_from_now_to_look*7)
    end_date = start_date + datetime.timedelta(days=nights_stay)
    print(start_date.strftime("%a %b %d %Y") + ' to ' + end_date.strftime("%a %b %d %Y"))
    