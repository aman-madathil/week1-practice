customer_name = str(input("Customer Name: "))
age = int(input("Age: "))
number_of_tickets = int(input("Number Of Tickets: "))
if age < 12:
    ticket_price = 120 * number_of_tickets
elif age >= 12 and age <= 59:
    ticket_price = 200 * number_of_tickets
elif age >= 60:
    ticket_price = 150 * number_of_tickets
if number_of_tickets >= 5:
    discount = ticket_price / 100 * 10
else:
    discount = 0
total_ticket_price = ticket_price - discount
print("Ticket Price: ",ticket_price)
print("Discount: ",discount)
print("Total Ticket Price: ",total_ticket_price)
