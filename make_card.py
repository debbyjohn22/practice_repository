name = "Deborah"
goal = "to be come an AI ENGINEER"
current_skill = "software"
days_learning = 5
daily_challenges = 3
print(name)
print(goal)
print(current_skill)
print(days_learning)
print(daily_challenges)

print()
name = "deborah".title() 
goal = "learn programming"
days_learning = 4
daily_challenges = 6
print(f"I am {name}, and I am here to {goal}")
print(f"This is my day {days_learning} of learning the {daily_challenges} challenges")


print()
name = "Deborah"
goal = "AI ENGINEER"
days_learning = 10
daily_challenges = 6
total_challenges = days_learning * daily_challenges
print(f"{total_challenges}")

print()

days_learning = 2
daily_challenges = 6
total_challenges = days_learning * daily_challenges
if total_challenges >= 30:
    print("great work,keep going!")
else:
    print("small step still count.")    

print()
name = "Deborah" 
goal = "to become a software engineer"
total_challenges = "24"
page = f"""
<h1>Hello from {name}</h1>
<p>My goal is {goal}.</p>
<p>My total_challenges is {total_challenges}.</p>
"""
print(page)