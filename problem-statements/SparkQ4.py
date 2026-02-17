def get_ticket_price(age: int, is_student: bool) -> int:
    if age < 12:
        return 8
    elif age >= 65:
        return 10
    elif is_student:
        return 12
    else:
        return 15
age = int(input())
is_student = input().lower() == "true"
print(get_ticket_price(age, is_student))
