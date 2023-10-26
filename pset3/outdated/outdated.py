months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
while True:
    date = input("date: ").strip()
    try:
        month, day, year = date.split("/")
        if int(month) > 0 and int(month) < 13 and int(day) > 0 and int(day) < 32:
            break
    except:
        try:
            month, day, year = date.split()
            if month.title() in months and day.isdigit() is False:
                month, day = months.index(month.title()) + 1, day.replace(',', '')
            if int(month) > 0 and int(month) < 13 and int(day) > 0 and int(day) < 32:
                break
        except:
            pass

print(f"{year}-{int(month):02}-{int(day):02}")
