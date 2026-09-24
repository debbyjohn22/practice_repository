def greet(person):
    print(f"Hello, {person}!")

greet("Deborah")
greet("sam")

def multiply(a, b):
    return a * b

total = multiply(4, 6)
print(total)

print()
 #Write print_all(items), looping through a list and printing each item with a - in front.
#Call it with your real ai_tools list.
#You already have count_letters, a version of the counting function. Also write count_items(items) 
# that counts how many items are in the list (not their letters), using the same total-and-loop pattern,
#  and call it with ai_tools.

def count_letters(items):
    total = 0
    for item in items:
        total = total + len(item)
    return total
provision = ["biscuit", "snacks", "yogurt"]
result = count_letters(provision)
print(result)

for itemss in provision:
      print("-" + itemss)

    
print()
    
def count_items(items):
    total = 0
    for item in items:
        total = total + 1
    return total

result = count_items(provision)
print(result)