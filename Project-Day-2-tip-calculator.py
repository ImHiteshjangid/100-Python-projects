#If the bill was $150.00, split between 5 people, with 12% tip.

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

# Tip_Calculator
#Write your code below this line 👇

print("Welcome to the tip calculator")
Total_bill = input("What Was the total bill ?\n ₹")
tip_percentage = input(
    "what percentage of tip would you like to give ?\n 10, 12 or 15 ?\n")
total_bill_with_tip = float(
    Total_bill) + float(Total_bill) * (float(tip_percentage) / 100)
print(f"The total bill with tip is ₹{total_bill_with_tip}")
people = input("How many people to split the bill ?\n")
bill_per_person = (total_bill_with_tip / int(people))
print("Each person should pay: ₹", ('%.2f' % bill_per_person))