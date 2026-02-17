def generate_threes(start: int, end: int) -> list[int]:
    return list(range(start, end, 3)) if start < end else []
start = int(input("Enter start value: "))
end = int(input("Enter end value: "))
print(generate_threes(start, end))
