class Vehicle:
    def __init__(self, vehicle_id, brand, model, rental_price_per_day):
        self.vehicle_id = vehicle_id
        self.brand = brand
        self.model = model
        self.rental_price_per_day = rental_price_per_day
        self.is_available = True

    def display_info(self):
        print(f"ID: {self.vehicle_id}, Brand: {self.brand}, Model: {self.model}, Price/Day: {self.rental_price_per_day}, Available: {self.is_available}")

    def rent(self):
        if self.is_available:
            self.is_available = False
            return True
        return False

    def return_vehicle(self):
        self.is_available = True

    def calculate_rental_cost(self, days):
        return self.rental_price_per_day * days