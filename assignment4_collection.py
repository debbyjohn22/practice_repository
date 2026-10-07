programming_languages = ["Python", "Java", "Go", "C++", "html"]
programming_languages.append("SQL")
programming_languages.remove("Java")
programming_languages.sort()
database = ("PostgreSQL", "MongoDB", "Redis")

numbers = {1, 2, 2, 3, 3} 
print("Set:", numbers)  # {1, 2, 3, 4}
dev = {"name": "wealth", "role": "genius"}
dev["role"] = "AI Engineer"; dev["city"] = "Lagos"

print(programming_languages, database, numbers, dev,sep="\n" )