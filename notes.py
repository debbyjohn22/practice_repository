with open("notes.txt", "w") as file:
    file.write("Day 1: learned variables\n")
    file.write("Day 2: learned loops\n")
    file.write("Day 3: learned functions\n")


with open("notes.txt", "r") as file:
    content = file.read()
print(content)

with open("notes.txt", "a") as file:
    file.write("Day 4: learned files\n")

with open("notes.txt", "r") as file:
    content = file.read()
print(content)