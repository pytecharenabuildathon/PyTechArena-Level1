def average_passing_grades (grades: list[int]) -> float:
    s = c = 0
    for g in grades:
        if g >= 50:
            s += g;
            c += 1
    return s/c if c else 0.0
grades = list(map(int, input().split()))
print(average_passing_grades(grades))
