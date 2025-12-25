import tkinter as tk
from tkinter import messagebox
from model import Vehicle
from services import ParkingLotService

def gui(service: ParkingLotService):
    root = tk.Tk()
    root.title("Parking Lot Management Portal")
    root.geometry("700x600")
    root.resizable(False, False)
    
    title_label = tk.Label(root, text="WELCOME TO THE PORTAL", 
                          font=("Arial", 16, "bold"))
    title_label.pack(pady=10)
    
    status_frame = tk.Frame(root)
    status_frame.pack(pady=5)
    status_label = tk.Label(status_frame, text="Available: 20/20", 
                           font=("Arial", 14, "bold"), bg="green", fg="white",
                           padx=20, pady=8, relief="raised", bd=2)
    status_label.pack()
    
    slots_frame = tk.LabelFrame(root, text="Occupied Slots", font=("Arial", 10, "bold"))
    slots_frame.pack(pady=10, padx=20, fill="x")
    slots_listbox = tk.Listbox(slots_frame, height=6, font=("Arial", 10))
    slots_listbox.pack(pady=5, padx=5, fill="both", expand=True)
    
    plate_entry = None
    ticket_entry = None
    type_var = None
    
    park_frame = tk.LabelFrame(root, text="Park Vehicle", font=("Arial", 10, "bold"))
    park_frame.pack(pady=10, padx=20, fill="x")
    
    tk.Label(park_frame, text="Num Plate:", font=("Arial", 10)).grid(row=0, column=0, pady=5, sticky="e")
    plate_entry = tk.Entry(park_frame, width=15, font=("Arial", 10), relief="solid", bd=1)
    plate_entry.grid(row=0, column=1, pady=5, padx=(5,15))
    
    tk.Label(park_frame, text="Type:", font=("Arial", 10)).grid(row=0, column=2, pady=5, sticky="e")
    type_var = tk.StringVar(value="4_wheeler")
    type_combo = tk.OptionMenu(park_frame, type_var, "2_wheeler", "4_wheeler")
    type_combo.grid(row=0, column=3, pady=5, padx=(0,10))
    
    unpark_frame = tk.LabelFrame(root, text="Unpark Vehicle", font=("Arial", 10, "bold"))
    unpark_frame.pack(pady=10, padx=20, fill="x")
    
    tk.Label(unpark_frame, text="Ticket ID:", font=("Arial", 10)).grid(row=0, column=0, pady=5, sticky="e")
    ticket_entry = tk.Entry(unpark_frame, width=10, font=("Arial", 10), relief="solid", bd=1)
    ticket_entry.grid(row=0, column=1, pady=5, padx=(5,15))
    
    def park():
        num_plate = plate_entry.get().strip()
        if not num_plate:
            messagebox.showerror("Error", "Num Plate required!")
            return
        
        vehicle = Vehicle(num_plate=num_plate, vehicle_type=type_var.get())
        ticket = service.park_vehicle(vehicle)
        
        if ticket:
            messagebox.showinfo("" ,f"Ticket ID: {ticket.ticket_id}\nSlot: {ticket.slot_id}")
        else:
            messagebox.showwarning("Full", "No slots available!")
        
        plate_entry.delete(0, tk.END)
        update_display()
    
    def unpark():
        try:
            ticket_id = int(ticket_entry.get().strip())
            ticket = service.unpark_vehicle(ticket_id)
            
            if ticket:
                messagebox.showinfo("", f"Plate: {ticket.num_plate}\nSlot: {ticket.slot_id}\nFee: Rs{ticket.fee:.1f}")
            else:
                messagebox.showerror("Error", "Invalid ticket ID!")
        except ValueError:
            messagebox.showerror("Error", "Enter valid ticket ID number!")
        
        ticket_entry.delete(0, tk.END)
        update_display()
    
    park_btn = tk.Button(park_frame, text="PARK", command=park, 
                        bg="green", fg="white", font=("Arial", 11, "bold"),
                        width=12, height=2, relief="raised", bd=3)
    park_btn.grid(row=0, column=4, pady=5, padx=5)
    
    unpark_btn = tk.Button(unpark_frame, text="UNPARK", command=unpark,
                          bg="red", fg="white", font=("Arial", 11, "bold"),
                          width=12, height=2, relief="raised", bd=3)
    unpark_btn.grid(row=0, column=2, pady=5, padx=5)
    
    def update_display():
        avail = service.state.available_slots_count()
        status_label.config(text=f"Available: {avail}/20")
        
        slots_listbox.delete(0, tk.END)
        occupied = service.occupied_slots()
        for slot in occupied:
            slots_listbox.insert(tk.END, f"Slot {slot.slot_id}: {slot.num_plate}")
        
        root.after(2000, update_display)
    
    update_display()
    root.mainloop()
