name = {"oche": "king", "ojima": "glory", "oha": "blessing"}
print(name)
print(name["oche"])
print(name["oha"])
for key in name:
    print(f"{key}: {name[key]}")

profile = {"name": "Deborah", "goal": "become an AI engineer", "days_learning": 10}
print(profile)
print(profile["name"])
profile["days_learning"] = 15
profile["current_skill"] = "Python"
print(profile)
for key in profile:
    print(f"{key}:{profile[key]}")
    .