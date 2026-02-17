def convert_temperature(value: float , unit : str) -> float | str:
    return round((value*9/5)+32,1) if unit.upper()=='C' else \
           round((value-32)*5/9,1) if unit.upper()=='F' else "Invalid Unit"
print(convert_temperature(float(input()), input()))
