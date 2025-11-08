def AddEvent():
    data = {
        "title": input("Enter event title: "),
        "date": input("Enter event date (DD-MM-YY): "),
        "time": input("Enter event time (HH:MM): or leave blank for all-day event "),
        "description": input("Enter event description: ")
    }
    import JsonManagement as jm
    jm.Add(data)