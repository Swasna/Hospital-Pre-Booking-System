import os

FILE_NAME = "bookings.txt"


def add_booking():
    name = input("Enter patient name: ")
    age = input("Enter patient age: ")
    department = input("Enter department: ")
    date = input("Enter appointment date (DD-MM-YYYY): ")

    with open(FILE_NAME, "a") as file:
        file.write(name + "," + age + "," + department + "," + date + "\n")

    print("\nBooking added successfully!")


def view_bookings():
    if not os.path.exists(FILE_NAME):
        print("\nNo bookings found!")
        return

    with open(FILE_NAME, "r") as file:
        bookings = file.readlines()

    if len(bookings) == 0:
        print("\nNo bookings found!")
    else:
        print("\n--- Patient Bookings ---")
        for booking in bookings:
            details = booking.strip().split(",")
            if len(details) == 4:
                print("Name:", details[0])
                print("Age:", details[1])
                print("Department:", details[2])
                print("Appointment Date:", details[3])
                print("------------------------")


def search_booking():
    search_name = input("Enter patient name to search: ")

    if not os.path.exists(FILE_NAME):
        print("\nNo bookings found!")
        return

    with open(FILE_NAME, "r") as file:
        bookings = file.readlines()

    found = False

    for booking in bookings:
        details = booking.strip().split(",")

        if len(details) == 4 and details[0].lower() == search_name.lower():
            print("\nBooking Found!")
            print("Name:", details[0])
            print("Age:", details[1])
            print("Department:", details[2])
            print("Appointment Date:", details[3])
            found = True

    if not found:
        print("\nBooking not found!")


def cancel_booking():
    cancel_name = input("Enter patient name to cancel booking: ")

    if not os.path.exists(FILE_NAME):
        print("\nNo bookings found!")
        return

    with open(FILE_NAME, "r") as file:
        bookings = file.readlines()

    updated_bookings = []
    found = False

    for booking in bookings:
        details = booking.strip().split(",")

        if len(details) == 4 and details[0].lower() == cancel_name.lower() and not found:
            found = True
        else:
            updated_bookings.append(booking)

    with open(FILE_NAME, "w") as file:
        file.writelines(updated_bookings)

    if found:
        print("\nBooking cancelled successfully!")
    else:
        print("\nBooking not found!")


while True:
    print("\n===== HOSPITAL PRE-BOOKING SYSTEM =====")
    print("1. Add Patient Booking")
    print("2. View All Bookings")
    print("3. Search Booking")
    print("4. Cancel Booking")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_booking()
    elif choice == "2":
        view_bookings()
    elif choice == "3":
        search_booking()
    elif choice == "4":
        cancel_booking()
    elif choice == "5":
        print("Thank you for using the Hospital Pre-Booking System!")
        break
    else:
        print("Invalid choice! Please try again.")

