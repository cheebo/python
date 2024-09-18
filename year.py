def check_year(year: int) -> bool:
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False


def year(year: int):
    if check_year(year):
        print("Високосный год")
    else:
        print("Обычный год")

year(2024)
year(2013)