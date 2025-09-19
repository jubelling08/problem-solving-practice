# Total Expenses for the Event
 
# The prime functionality of an Event Management System is budgeting. An Event Management System should estimate the total expenses incurred by an event and the percentage rate of each of the expenses involved in planning and executing an event. Nikhil, the founder of "Pine Tree" wanted to include this functionality in his company’s Amphi Event Management System and requested your help in writing a program for the same.

# The program should get the branding expenses, travel expenses, food expenses and logistics expenses as input from the user and calculate the total expenses for an event and the percentage rate of each of these expenses.

# Input Format:
# First input is a int value that corresponds to the branding expenses.
# Second input is a int value that corresponds to the travel expenses.
# Third input is a int value that corresponds to the food expenses.
# Fourth input is a int value that corresponds to the logistics expenses.

# Output Format:
# First line of the output should display the float value that corresponds to the total expenses for the Event.
# Next four lines should display the percentage rate of each of the expenses.
# Refer sample input and output for formatting specifications.
# [All text in bold corresponds to input and rest corresponds to output.]

# Sample Input and Output:
# Enter branding expenses
# 20000
# Enter travel expenses
# 40000
# Enter food expenses
# 15000
# Enter logistics expenses
# 25000
# Total expenses : Rs.100000.00
# Branding expenses percentage : 20.00%
# Travel expenses percentage : 40.00%
# Food expenses percentage : 15.00%
# Logistics expenses percentage : 25.00% 

branding=float(int(input("Enter branding expenses")))
travel=float(int(input("Enter travel expenses")))
food=float(int(input("Enter food expenses")))
logistics=float(int(input("Enter logistics expenses")))
print(f"Total expenses: Rs. {branding+travel+food+logistics:.2f}")
total=(branding+travel+food+logistics)
branding_per=branding/total*100
travel_per=travel/total*100
food_per=food/total*100
logistics_per=logistics/total*100
branding expenses percentage : {branding_per:.2f}%\nTravel expenses percentage : {travel_per:.2f}%\nFood expenses percentage : {food_per:.2f}%\nLogistics expenses percentage : {logistics_per:.2f}%")print(f"Branding expenses percentage : )
