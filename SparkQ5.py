def calculate(expression: str) -> float:
    expression += "+"
    total = last = num = 0
    sign = "+"
    for ch in expression:
        if ch.isdigit():
            num = num * 10 + int(ch)
        elif ch in "+-*/":
            if sign == "+": total, last = total + last, num
            elif sign == "-": total, last = total + last, -num
            elif sign == "*": last *= num
            else: last /= num
            num, sign = 0, ch
    result = round(total + last, 2)
    return float(f"{result:.2f}".rstrip('0').rstrip('.') if '.' in f"{result:.2f}" else result)
print("Result =", calculate(input("Enter expression: ")))
