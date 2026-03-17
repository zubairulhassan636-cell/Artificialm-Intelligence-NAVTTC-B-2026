class RentalService:
    def __init__(self):
        self.vehicles = []
        self.customers = []

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)

    def register_customer(self, customer):
        self.customers.append(customer)

    def show_available_vehicles(self):
        print("\nAvailable Vehicles:")
        for v in self.vehicles:
            if v.is_available:
                v.display_info()

    def find_vehicle(self, vehicle_id):
        for v in self.vehicles:
            if v.vehicle_id == vehicle_id:
                return v
        return None

    def find_customer(self, customer_id):
        for c in self.customers:
            if c.customer_id == customer_id:
                return c
        return None

    def rent_vehicle(self, customer_id, vehicle_id, days):
        customer = self.find_customer(customer_id)
        vehicle = self.find_vehicle(vehicle_id)

        if not customer or not vehicle:
            print("Invalid customer or vehicle")
            return

        if vehicle.rent():
            customer.rent_vehicle(vehicle)
            cost = vehicle.calculate_rental_cost(days)
            print(f"Vehicle rented successfully! Total cost: {cost} PKR")
        else:
            print("Vehicle not available")

    def return_vehicle(self, customer_id):
        customer = self.find_customer(customer_id)

        if customer and customer.rented_vehicle:
            vehicle = customer.rented_vehicle
            vehicle.return_vehicle()
            customer.return_vehicle()
            print("Vehicle returned successfully")
        else:
            print("No vehicle to return")