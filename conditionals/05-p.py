#Movie ticket pricing based on age {$12 for adults (above 18) $8 for child(under 18)
# #2$ discount on Wednesday to everyone
# Define ticket prices
adult_price = 12
child_price = 8
wednesday_discount = 2

# Get user inputs
age = int(input("Enter your age: "))
day_of_week = input("Enter the day of the week: ").strip().lower()

# Determine ticket price based on age
if age >= 18:
    ticket_price = adult_price
else:
    ticket_price = child_price

# Apply Wednesday discount if applicable
if day_of_week == "wednesday":
    ticket_price -= wednesday_discount

print(f"Your ticket price is: ${ticket_price}")

