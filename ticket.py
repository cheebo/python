def is_lucky_ticket(number: int) -> bool:
    left = 0
    right = 0
    for i in range(6):
        if i < 3:
            right += number // 10 ** i % 10
        else:
            left += number // 10 ** i % 10
    return left == right


def ticket(number: int):
    if is_lucky_ticket(number):
        print("Счастливый билет")
    else:
        print("Несчастливый билет")


ticket(123456)
ticket(123321)