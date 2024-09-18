def check_year(year: int) -> bool:
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False

if check_year(2000):
    print("високосный год")
else:
    print("не високосный год")