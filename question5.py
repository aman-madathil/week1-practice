seats = ["Available", "Booked", "Available", "Available", "Booked", "Available", "Booked", "Available"]
print("Seat 1: ",seats[0])
print("Seat 2: ",seats[1])
print("Seat 3: ",seats[2])
print("Seat 4: ",seats[3])
print("Seat 5: ",seats[4])
print("Seat 6: ",seats[5])
print("Seat 7: ",seats[6])
print("Seat 8: ",seats[7])
seat_no = int(input("Enter a Seat Number: "))
if seat_no < 1 or seat_no > 8:
    print("Invalid Seat")
elif seats[seat_no - 1] == "Available":
    print("Seat is Available")
    seats[seat_no - 1] = "Booked"
    print("Seat is Booked Successfully")
elif seats[seat_no - 1] == "Booked":
    print("Seat is Already Booked")
print("Booked Seats: ", seats.count("Booked"))
print("Available Seats: ",seats.count("Available"))
print("Seat 1: ",seats[0])
print("Seat 2: ",seats[1])
print("Seat 3: ",seats[2])
print("Seat 4: ",seats[3])
print("Seat 5: ",seats[4])
print("Seat 6: ",seats[5])
print("Seat 7: ",seats[6])
print("Seat 8: ",seats[7])