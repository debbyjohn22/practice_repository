print("printing current and provious number  sum in a range(10)")
provious_num = 0
#loop form 0 to 9

for i in range(10):
    x_sum = provious_num + i
    print(f"current Number {i} provious Number {provious_num} sum: {x_sum}")
    #update previous_num for the next loop
    
    previous_num = i
