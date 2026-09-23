ai_tools = ["python", "Variables",  "Data types"]
ai_tools.append("working program")
print(ai_tools)
print(ai_tools[0])
print(len(ai_tools))
print(ai_tools[3])
for i in ai_tools:
    print(i)

for tool in ai_tools:
    if tool == "cooking":
        print(f"{tool} is your first language!")
    else:
        print(f"Also learning {tool}")