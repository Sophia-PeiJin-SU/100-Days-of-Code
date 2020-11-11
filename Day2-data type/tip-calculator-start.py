#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Round the result to 2 decimal places = 33.60

print("Welcome to the tip calculator!")
bill = input("What was the total bill? $")
tips = input("What percentage tip woul you like to give? 10, 12, or 15? ")
people = input("How many people to split the bill? ")

total_bill = float(bill) + float(bill) * int(tips) / 100
split_bill = round(total_bill / int(people), 2)

print(f"Each person should pay: ${split_bill}")