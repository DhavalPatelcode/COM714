import tkinter as tk
import matplotlib.pyplot as plt

class Trip:
    def __init__(self, name, start_date, duration, contact_info):
        self.name = name
        self.start_date = start_date
        self.duration = duration
        self.contact_info = contact_info
        # Add more attributes as needed

    def update_trip(self, **kwargs):
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)
            else:
                raise AttributeError(f"'{type(self).__name__}' object has no attribute '{key}'")

    def delete_trip(self):
        print(f"Trip '{self.name}' has been deleted.")

class Traveller:
    def __init__(self, name, address, date_of_birth, emergency_contact):
        self.name = name
        self.address = address
        self.date_of_birth = date_of_birth
        self.emergency_contact = emergency_contact
        # Add more attributes as needed

    def update_traveller(self, **kwargs):
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)
            else:
                raise AttributeError(f"'{type(self).__name__}' object has no attribute '{key}'")

    def delete_traveller(self):
        print(f"Traveller '{self.name}' has been deleted.")

class TripLeg:
    def __init__(self, start_location, destination, transport_provider, mode_of_transport, cost):
        self.start_location = start_location
        self.destination = destination
        self.transport_provider = transport_provider
        self.mode_of_transport = mode_of_transport
        self.cost = cost
        # Add more attributes as needed

    def update_trip_leg(self, **kwargs):
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)
            else:
                raise AttributeError(f"'{type(self).__name__}' object has no attribute '{key}'")

    def delete_trip_leg(self):
        print(f"Trip leg from {self.start_location} to {self.destination} has been deleted.")

class TripCoordinator:
    def __init__(self, name, contact_info):
        self.name = name
        self.contact_info = contact_info
        # Add more attributes as needed

    def update_trip_coordinator(self, **kwargs):
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)
            else:
                raise AttributeError(f"'{type(self).__name__}' object has no attribute '{key}'")

    def delete_trip_coordinator(self):
        print(f"Trip Coordinator '{self.name}' has been deleted.")
    

class TripManager:
    def __init__(self):
        self.trips = []  # Initialize list to store trips

    def generate_trip_duration_report(self):
        trip_names = []
        trip_durations = []

        for trip in self.trips:
            trip_names.append(trip.name)
            trip_durations.append(int(trip.duration))  # Assuming duration is in integer format

        plt.figure(figsize=(10, 6))
        plt.bar(trip_names, trip_durations, color='skyblue')
        plt.xlabel('Trip Name')
        plt.ylabel('Duration (days)')
        plt.title('Trip Duration Report')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.savefig('trip_duration_report.png')  # Save the report as an image
        plt.close()  # Close the plot to release memory


class TravelManagementApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Travel Management System")
        self.geometry("800x600")
        self.trips = []  # List to store created trips
        self.travellers = []  # List to store created travellers
        self.trip_legs = []  # List to store created trip legs
        self.trip_coordinators = []  # List to store created trip coordinators
        self.trip_manager = TripManager()  # Initialize TripManager
        self.selected_trip_id = None

        # Initialize GUI components
        self.create_widgets()

    def create_widgets(self):
        # Create Buttons for Trip, Traveller, Trip Leg, Trip Coordinator, and Trip Manager Functions
        self.btn_trip = tk.Button(self, text="Trip", command=self.show_trip_form)
        self.btn_traveller = tk.Button(self, text="Traveller", command=self.show_traveller_form)
        self.btn_trip_leg = tk.Button(self, text="Trip Leg", command=self.show_trip_leg_form)
        self.btn_trip_coordinator = tk.Button(self, text="Trip Coordinator", command=self.show_trip_coordinator_form)
        self.btn_generate_report = tk.Button(self, text="Generate Trip Duration Report", command=self.generate_trip_duration_report)


        # Layout Buttons using grid manager
        self.btn_trip.grid(row=0, column=0, padx=10, pady=10)
        self.btn_traveller.grid(row=0, column=1, padx=10, pady=10)
        self.btn_trip_leg.grid(row=0, column=2, padx=10, pady=10)
        self.btn_trip_coordinator.grid(row=0, column=3, padx=10, pady=10)
        self.btn_generate_report.grid(row=1, column=0, columnspan=4, padx=10, pady=10)

    def generate_trip_duration_report(self):
        # Call TripManager's method to generate trip duration report
        self.trip_manager.generate_trip_duration_report()
        print("Trip duration report generated successfully.")

    def generate_invoice(self):
        # Call TripManager's generate_invoice method with selected trip ID
        if self.selected_trip_id:
            self.trip_manager.generate_invoice(self.selected_trip_id, self)

    def display_invoice(self, invoice_text):
        # Create Text widget to display invoice
        self.invoice_text = tk.Text(self, height=10, width=50)
        self.invoice_text.grid(row=2, column=0, columnspan=4, padx=10, pady=10)
        # Display invoice text in the Text widget
        self.invoice_text.delete(1.0, tk.END)  # Clear previous content
        self.invoice_text.insert(tk.END, invoice_text)

    def clear_widgets(self):
        # Destroy all widgets
        for widget in self.winfo_children():
            widget.destroy()

    def show_trip_form(self):
        # Destroy existing widgets and show trip form
        self.clear_widgets()
        self.create_trip_form()

    def show_traveller_form(self):
        # Destroy existing widgets and show traveller form
        self.clear_widgets()
        self.create_traveller_form()


    def show_trip_leg_form(self):
        # Destroy existing widgets and show trip leg form
        self.clear_widgets()
        self.create_trip_leg_form()

    def show_trip_coordinator_form(self):
        # Destroy existing widgets and show trip coordinator form
        self.clear_widgets()
        self.create_trip_coordinator_form()

    def clear_widgets(self):
        # Destroy all widgets
        for widget in self.winfo_children():
            widget.destroy()

    def create_trip_form(self):
        # Create Labels
        self.lbl_name = tk.Label(self, text="Trip Name:")
        self.lbl_start_date = tk.Label(self, text="Start Date:")
        self.lbl_duration = tk.Label(self, text="Duration:")
        self.lbl_contact_info = tk.Label(self, text="Contact Information:")

        # Create Entry fields
        self.entry_name = tk.Entry(self)
        self.entry_start_date = tk.Entry(self)
        self.entry_duration = tk.Entry(self)
        self.entry_contact_info = tk.Entry(self)

        # Create Buttons
        self.btn_create_trip = tk.Button(self, text="Create Trip", command=self.create_trip)
        self.btn_update_trip = tk.Button(self, text="Update Trip", command=self.update_trip)
        self.btn_delete_trip = tk.Button(self, text="Delete Trip", command=self.delete_trip)

        # Create Trip Listbox
        self.trip_listbox = tk.Listbox(self)
        self.trip_listbox.bind("<<ListboxSelect>>", self.on_trip_select)

        # Layout GUI components using grid manager
        self.lbl_name.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.entry_name.grid(row=1, column=1, padx=10, pady=5)
        self.lbl_start_date.grid(row=2, column=0, padx=10, pady=5, sticky="w")
        self.entry_start_date.grid(row=2, column=1, padx=10, pady=5)
        self.lbl_duration.grid(row=3, column=0, padx=10, pady=5, sticky="w")
        self.entry_duration.grid(row=3, column=1, padx=10, pady=5)
        self.lbl_contact_info.grid(row=4, column=0, padx=10, pady=5, sticky="w")
        self.entry_contact_info.grid(row=4, column=1, padx=10, pady=5)
        self.btn_create_trip.grid(row=5, column=0, padx=10, pady=10)
        self.btn_update_trip.grid(row=5, column=1, padx=10, pady=10)
        self.btn_delete_trip.grid(row=5, column=2, padx=10, pady=10)
        self.trip_listbox.grid(row=6, columnspan=3, padx=10, pady=10)

    def create_traveller_form(self):
        # Create Labels
        self.lbl_name = tk.Label(self, text="Name:")
        self.lbl_address = tk.Label(self, text="Address:")
        self.lbl_date_of_birth = tk.Label(self, text="Date of Birth:")
        self.lbl_emergency_contact = tk.Label(self, text="Emergency Contact:")

        # Create Entry fields
        self.entry_name = tk.Entry(self)
        self.entry_address = tk.Entry(self)
        self.entry_date_of_birth = tk.Entry(self)
        self.entry_emergency_contact = tk.Entry(self)

        # Create Buttons
        self.btn_create_traveller = tk.Button(self, text="Create Traveller", command=self.create_traveller)
        self.btn_update_traveller = tk.Button(self, text="Update Traveller", command=self.update_traveller)
        self.btn_delete_traveller = tk.Button(self, text="Delete Traveller", command=self.delete_traveller)

        # Create Traveller Listbox
        self.traveller_listbox = tk.Listbox(self)
        self.traveller_listbox.bind("<<ListboxSelect>>", self.on_traveller_select)

        # Layout GUI components using grid manager
        self.lbl_name.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.entry_name.grid(row=1, column=1, padx=10, pady=5)
        self.lbl_address.grid(row=2, column=0, padx=10, pady=5, sticky="w")
        self.entry_address.grid(row=2, column=1, padx=10, pady=5)
        self.lbl_date_of_birth.grid(row=3, column=0, padx=10, pady=5, sticky="w")
        self.entry_date_of_birth.grid(row=3, column=1, padx=10, pady=5)
        self.lbl_emergency_contact.grid(row=4, column=0, padx=10, pady=5, sticky="w")
        self.entry_emergency_contact.grid(row=4, column=1, padx=10, pady=5)
        self.btn_create_traveller.grid(row=5, column=0, padx=10, pady=10)
        self.btn_update_traveller.grid(row=5, column=1, padx=10, pady=10)
        self.btn_delete_traveller.grid(row=5, column=2, padx=10, pady=10)
        self.traveller_listbox.grid(row=6, columnspan=3, padx=10, pady=10)

    def create_trip_leg_form(self):
        # Create Labels
        self.lbl_start_location = tk.Label(self, text="Start Location:")
        self.lbl_destination = tk.Label(self, text="Destination:")
        self.lbl_transport_provider = tk.Label(self, text="Transport Provider:")
        self.lbl_mode_of_transport = tk.Label(self, text="Mode of Transport:")
        self.lbl_cost = tk.Label(self, text="Cost:")

        # Create Entry fields
        self.entry_start_location = tk.Entry(self)
        self.entry_destination = tk.Entry(self)
        self.entry_transport_provider = tk.Entry(self)
        self.entry_mode_of_transport = tk.Entry(self)
        self.entry_cost = tk.Entry(self)

        # Create Buttons
        self.btn_create_trip_leg = tk.Button(self, text="Create Trip Leg", command=self.create_trip_leg)
        self.btn_update_trip_leg = tk.Button(self, text="Update Trip Leg", command=self.update_trip_leg)
        self.btn_delete_trip_leg = tk.Button(self, text="Delete Trip Leg", command=self.delete_trip_leg)

        # Create Trip Leg Listbox
        self.trip_leg_listbox = tk.Listbox(self)
        self.trip_leg_listbox.bind("<<ListboxSelect>>", self.on_trip_leg_select)

        # Layout GUI components using grid manager
        self.lbl_start_location.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.entry_start_location.grid(row=1, column=1, padx=10, pady=5)
        self.lbl_destination.grid(row=2, column=0, padx=10, pady=5, sticky="w")
        self.entry_destination.grid(row=2, column=1, padx=10, pady=5)
        self.lbl_transport_provider.grid(row=3, column=0, padx=10, pady=5, sticky="w")
        self.entry_transport_provider.grid(row=3, column=1, padx=10, pady=5)
        self.lbl_mode_of_transport.grid(row=4, column=0, padx=10, pady=5, sticky="w")
        self.entry_mode_of_transport.grid(row=4, column=1, padx=10, pady=5)
        self.lbl_cost.grid(row=5, column=0, padx=10, pady=5, sticky="w")
        self.entry_cost.grid(row=5, column=1, padx=10, pady=5)
        self.btn_create_trip_leg.grid(row=6, column=0, padx=10, pady=10)
        self.btn_update_trip_leg.grid(row=6, column=1, padx=10, pady=10)
        self.btn_delete_trip_leg.grid(row=6, column=2, padx=10, pady=10)
        self.trip_leg_listbox.grid(row=7, columnspan=3, padx=10, pady=10)


    def create_trip(self):
        # Get values from entry fields
        trip_name = self.entry_name.get()
        start_date = self.entry_start_date.get()
        duration = self.entry_duration.get()
        contact_info = self.entry_contact_info.get()

        # Create new trip
        new_trip = Trip(trip_name, start_date, duration, contact_info)
        self.trips.append(new_trip)

        # Update trip listbox
        self.update_trip_listbox()

    def update_trip(self):
        # Get selected trip index
        selected_index = self.trip_listbox.curselection()
        if selected_index:
            trip_index = selected_index[0]
            trip = self.trips[trip_index]

            # Get values from entry fields
            trip_name = self.entry_name.get()
            start_date = self.entry_start_date.get()
            duration = self.entry_duration.get()
            contact_info = self.entry_contact_info.get()

            # Update trip attributes
            trip.update_trip(name=trip_name, start_date=start_date, duration=duration, contact_info=contact_info)

            # Update trip listbox
            self.update_trip_listbox()

    def delete_trip(self):
        # Get selected trip index
        selected_index = self.trip_listbox.curselection()
        if selected_index:
            trip_index = selected_index[0]
            deleted_trip = self.trips.pop(trip_index)
            deleted_trip.delete_trip()

            # Update trip listbox
            self.update_trip_listbox()

    def on_trip_select(self, event):
        # Get selected trip index
        selected_index = self.trip_listbox.curselection()
        if selected_index:
            trip_index = selected_index[0]
            trip = self.trips[trip_index]

            # Update entry fields with selected trip details
            self.entry_name.delete(0, tk.END)
            self.entry_name.insert(tk.END, trip.name)
            self.entry_start_date.delete(0, tk.END)
            self.entry_start_date.insert(tk.END, trip.start_date)
            self.entry_duration.delete(0, tk.END)
            self.entry_duration.insert(tk.END, trip.duration)
            self.entry_contact_info.delete(0, tk.END)
            self.entry_contact_info.insert(tk.END, trip.contact_info)

    def update_trip_listbox(self):
        # Clear existing listbox items
        self.trip_listbox.delete(0, tk.END)

        # Add trip names to listbox
        for trip in self.trips:
            self.trip_listbox.insert(tk.END, trip.name)

    def create_traveller(self):
        # Get values from entry fields
        name = self.entry_name.get()
        address = self.entry_address.get()
        date_of_birth = self.entry_date_of_birth.get()
        emergency_contact = self.entry_emergency_contact.get()

        # Create new traveller
        new_traveller = Traveller(name, address, date_of_birth, emergency_contact)
        self.travellers.append(new_traveller)

        # Update traveller listbox
        self.update_traveller_listbox()

    def update_traveller(self):
        # Get selected traveller index
        selected_index = self.traveller_listbox.curselection()
        if selected_index:
            traveller_index = selected_index[0]
            traveller = self.travellers[traveller_index]

            # Get values from entry fields
            name = self.entry_name.get()
            address = self.entry_address.get()
            date_of_birth = self.entry_date_of_birth.get()
            emergency_contact = self.entry_emergency_contact.get()

            # Update traveller attributes
            traveller.update_traveller(name=name, address=address, date_of_birth=date_of_birth, emergency_contact=emergency_contact)

            # Update traveller listbox
            self.update_traveller_listbox()

    def delete_traveller(self):
        # Get selected traveller index
        selected_index = self.traveller_listbox.curselection()
        if selected_index:
            traveller_index = selected_index[0]
            deleted_traveller = self.travellers.pop(traveller_index)
            deleted_traveller.delete_traveller()

            # Update traveller listbox
            self.update_traveller_listbox()

    def on_traveller_select(self, event):
        # Get selected traveller index
        selected_index = self.traveller_listbox.curselection()
        if selected_index:
            traveller_index = selected_index[0]
            traveller = self.travellers[traveller_index]

            # Update entry fields with selected traveller details
            self.entry_name.delete(0, tk.END)
            self.entry_name.insert(tk.END, traveller.name)
            self.entry_address.delete(0, tk.END)
            self.entry_address.insert(tk.END, traveller.address)
            self.entry_date_of_birth.delete(0, tk.END)
            self.entry_date_of_birth.insert(tk.END, traveller.date_of_birth)
            self.entry_emergency_contact.delete(0, tk.END)
            self.entry_emergency_contact.insert(tk.END, traveller.emergency_contact)

    def update_traveller_listbox(self):
        # Clear existing listbox items
        self.traveller_listbox.delete(0, tk.END)

        # Add traveller names to listbox
        for traveller in self.travellers:
            self.traveller_listbox.insert(tk.END, traveller.name)

    def create_trip_leg(self):
        # Get values from entry fields
        start_location = self.entry_start_location.get()
        destination = self.entry_destination.get()
        transport_provider = self.entry_transport_provider.get()
        mode_of_transport = self.entry_mode_of_transport.get()
        cost = self.entry_cost.get()

        # Create new trip leg
        new_trip_leg = TripLeg(start_location, destination, transport_provider, mode_of_transport, cost)
        self.trip_legs.append(new_trip_leg)

        # Update trip leg listbox
        self.update_trip_leg_listbox()

    def update_trip_leg(self):
        # Get selected trip leg index
        selected_index = self.trip_leg_listbox.curselection()
        if selected_index:
            trip_leg_index = selected_index[0]
            trip_leg = self.trip_legs[trip_leg_index]

            # Get values from entry fields
            start_location = self.entry_start_location.get()
            destination = self.entry_destination.get()
            transport_provider = self.entry_transport_provider.get()
            mode_of_transport = self.entry_mode_of_transport.get()
            cost = self.entry_cost.get()

            # Update trip leg attributes
            trip_leg.start_location = start_location
            trip_leg.destination = destination
            trip_leg.transport_provider = transport_provider
            trip_leg.mode_of_transport = mode_of_transport
            trip_leg.cost = cost

            # Update trip leg listbox
            self.update_trip_leg_listbox()

    def delete_trip_leg(self):
        # Get selected trip leg index
        selected_index = self.trip_leg_listbox.curselection()
        if selected_index:
            trip_leg_index = selected_index[0]
            deleted_trip_leg = self.trip_legs.pop(trip_leg_index)

            # Update trip leg listbox
            self.update_trip_leg_listbox()

    def on_trip_leg_select(self, event):
        # Get selected trip leg index
        selected_index = self.trip_leg_listbox.curselection()
        if selected_index:
            trip_leg_index = selected_index[0]
            trip_leg = self.trip_legs[trip_leg_index]

            # Update entry fields with selected trip leg details
            self.entry_start_location.delete(0, tk.END)
            self.entry_start_location.insert(tk.END, trip_leg.start_location)
            self.entry_destination.delete(0, tk.END)
            self.entry_destination.insert(tk.END, trip_leg.destination)
            self.entry_transport_provider.delete(0, tk.END)
            self.entry_transport_provider.insert(tk.END, trip_leg.transport_provider)
            self.entry_mode_of_transport.delete(0, tk.END)
            self.entry_mode_of_transport.insert(tk.END, trip_leg.mode_of_transport)
            self.entry_cost.delete(0, tk.END)
            self.entry_cost.insert(tk.END, trip_leg.cost)

    def update_trip_leg_listbox(self):
        # Clear existing listbox items
        self.trip_leg_listbox.delete(0, tk.END)

        # Add trip leg details to listbox
        for trip_leg in self.trip_legs:
            self.trip_leg_listbox.insert(tk.END, f"From: {trip_leg.start_location} - To: {trip_leg.destination}")



    def create_trip_coordinator_form(self):
        # Create Labels
        self.lbl_name = tk.Label(self, text="Name:")
        self.lbl_contact_info = tk.Label(self, text="Contact Information:")

        # Create Entry fields
        self.entry_name = tk.Entry(self)
        self.entry_contact_info = tk.Entry(self)

        # Create Buttons
        self.btn_create_trip_coordinator = tk.Button(self, text="Create Trip Coordinator", command=self.create_trip_coordinator)
        self.btn_update_trip_coordinator = tk.Button(self, text="Update Trip Coordinator", command=self.update_trip_coordinator)
        self.btn_delete_trip_coordinator = tk.Button(self, text="Delete Trip Coordinator", command=self.delete_trip_coordinator)

        # Create Trip Coordinator Listbox
        self.trip_coordinator_listbox = tk.Listbox(self)
        self.trip_coordinator_listbox.bind("<<ListboxSelect>>", self.on_trip_coordinator_select)

        # Layout GUI components using grid manager
        self.lbl_name.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.entry_name.grid(row=1, column=1, padx=10, pady=5)
        self.lbl_contact_info.grid(row=2, column=0, padx=10, pady=5, sticky="w")
        self.entry_contact_info.grid(row=2, column=1, padx=10, pady=5)
        self.btn_create_trip_coordinator.grid(row=3, column=0, padx=10, pady=10)
        self.btn_update_trip_coordinator.grid(row=3, column=1, padx=10, pady=10)
        self.btn_delete_trip_coordinator.grid(row=3, column=2, padx=10, pady=10)
        self.trip_coordinator_listbox.grid(row=4, columnspan=3, padx=10, pady=10)

    def create_trip_coordinator(self):
        # Get values from entry fields
        name = self.entry_name.get()
        contact_info = self.entry_contact_info.get()

        # Create new trip coordinator
        new_trip_coordinator = TripCoordinator(name, contact_info)
        self.trip_coordinators.append(new_trip_coordinator)

        # Update trip coordinator listbox
        self.update_trip_coordinator_listbox()

    def update_trip_coordinator(self):
        # Get selected trip coordinator index
        selected_index = self.trip_coordinator_listbox.curselection()
        if selected_index:
            coordinator_index = selected_index[0]
            coordinator = self.trip_coordinators[coordinator_index]

            # Get values from entry fields
            name = self.entry_name.get()
            contact_info = self.entry_contact_info.get()

            # Update trip coordinator attributes
            coordinator.update_trip_coordinator(name=name, contact_info=contact_info)

            # Update trip coordinator listbox
            self.update_trip_coordinator_listbox()

    def delete_trip_coordinator(self):
        # Get selected trip coordinator index
        selected_index = self.trip_coordinator_listbox.curselection()
        if selected_index:
            coordinator_index = selected_index[0]
            deleted_coordinator = self.trip_coordinators.pop(coordinator_index)
            deleted_coordinator.delete_trip_coordinator()

            # Update trip coordinator listbox
            self.update_trip_coordinator_listbox()

    def on_trip_coordinator_select(self, event):
        # Get selected trip coordinator index
        selected_index = self.trip_coordinator_listbox.curselection()
        if selected_index:
            coordinator_index = selected_index[0]
            coordinator = self.trip_coordinators[coordinator_index]

            # Update entry fields with selected trip coordinator details
            self.entry_name.delete(0, tk.END)
            self.entry_name.insert(tk.END, coordinator.name)
            self.entry_contact_info.delete(0, tk.END)
            self.entry_contact_info.insert(tk.END, coordinator.contact_info)

    def update_trip_coordinator_listbox(self):
        # Clear existing listbox items
        self.trip_coordinator_listbox.delete(0, tk.END)

        # Add trip coordinator names to listbox
        for coordinator in self.trip_coordinators:
            self.trip_coordinator_listbox.insert(tk.END, coordinator.name)


if __name__ == "__main__":
    app = TravelManagementApp()
    app.mainloop()
