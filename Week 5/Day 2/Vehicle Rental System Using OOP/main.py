from vehicle import Vehicle
from car import Car
from bike import Bike
from customer import Customer
from rental_service import RentalService
def main():
    service = RentalService()

    # Sample Vehicles
    bike = Bike("B101", "Honda", "CG125", 1000, "125cc", "Standard")
    car = Car("C201", "Toyota", "Corolla", 4000, 4, "Petrol")
    ac_car = Car("C301", "Honda", "Civic", 6000, 4, "Petrol")

    service.add_vehicle(bike)
    service.add_vehicle(car)
    service.add_vehicle(ac_car)

    # Sample Customer
    customer = Customer("CU1", "Ali")
    service.register_customer(customer)

    while True:
        print("\n===== Vehicle Rental System =====")
        print("1. Show available vehicles")
        print("2. Rent a vehicle")
        print("3. Return a vehicle")
        print("4. View Rented Vehicle")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            service.show_available_vehicles()

        elif choice == "2":
            vid = input("Enter Vehicle ID: ")
            days = int(input("Enter number of days: "))
            service.rent_vehicle("CU1", vid, days)

        elif choice == "3":
            service.return_vehicle("CU1")
            
        elif choice == "4":
            customer.view_rented_vehicle()

        elif choice == "5":
            print("Exiting...")
            break

        else:
            print("Invalid choice")
main()