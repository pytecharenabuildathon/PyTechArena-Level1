#precise tip calculation                                                                                                                                     
def calculate_total_bill(amount : float , tip_percent : int) -> float:
    return round(float(amount) * (1 + float(tip_percent)/100), 2)
amount = input("Enter bill amount: ")
tip_percent = input("Enter tip percentage: ")
print(calculate_total_bill(amount, tip_percent))
