def get_ticket_price(age: int , is_student : bool) -> int:
    return 8 if age < 12 else 10 if age >= 65 else (12 if is_student else 15)
age = int(input())
is_student = input().lower() == "true"
print(get_ticket_price(age, is_student))
