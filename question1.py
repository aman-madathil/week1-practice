parking_hours = int(input("Enter the number of parking hours: "))
if parking_hours <= 2:
    parking_charge = parking_hours * 30
elif parking_hours > 2 and parking_hours <= 5:
    parking_charge = parking_hours * 25
elif parking_hours > 5:
    parking_charge = parking_hours * 20
else:
    print("Invalid Input")
if parking_charge > 150:
    service_fee = 20
else:
    service_fee = 0
parking_charge += service_fee
print("Parking Charge: ",parking_charge)
print("Service Charge: ",service_fee)
print("Final amount: ",service_fee + parking_charge)
