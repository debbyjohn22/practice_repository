def flow (num1, num2):
    if num1 * num2 <= 1000:
        return num1 * num2
    else:
        return num1 + num2
print(flow(20,  30))
print(flow(40, 30))
