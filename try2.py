import tkinter as tk
from tkinter import messagebox

#dictionary
items = {}
counter = 1
#Requisition Approval Function
def requisition_approval(requisition_id, staff_id, total2):
    req_status = "Pending"
    approval_reference = ""

    # approved if under $500
    if total2 < 500:
        req_status = "Approved"
        # generating approval ref num
        approval_reference = staff_id + str(requisition_id)[-3:]
    else:
        req_status = "Pending"

    return req_status, approval_reference


#Display Requisitions Function
def display_requisitions(date, req_id, s_id, s_name, total, status, approval_reference):
    result_text = (
        f"Printing Requisitions:\n"
        f"Date: {date}\n"
        f"Requisition ID: {req_id}\n"
        f"Staff ID: {s_id}\n"
        f"Staff Name: {s_name}\n"
        f"Total: ${total}\n"
        f"Status: {status}\n"
        f"Approval Reference Number: {approval_reference}"
    )
    result_label.config(text=result_text, justify="left")


#Tkinter Event Functions
def OnClick_AddItem():
    item_name = item_textbox.get()
    item_price = price_textbox.get()

    if item_name == "" or item_price == "":
        messagebox.showwarning("Warning", "Please enter both item and price")
    else:
        # Directly storing without numeric check
        items[item_name] = float(item_price)
        item_textbox.delete(0, tk.END)
        price_textbox.delete(0, tk.END)
        status_update_label.config(text=f"Added: {item_name}")


def OnClick_Submit():
    date = date_textbox.get()
    staff_id = id_textbox.get()
    staff_name = name_textbox.get()

    if date == "" or staff_id == "" or staff_name == "":
        messagebox.showwarning("Warning", "Missing Staff Information")
    else:
        if items == {}:
            messagebox.showwarning("Warning", "No items added")
        else:
            #generates the requisition ID
            requisition_id = counter + 10000

            #Calculate Total
            total = 0
            for key in items:
                total = total + items[key]
            total2 = total

            #Printing Approval Status
            status, ref = requisition_approval(requisition_id, staff_id, total2)

            #outputs the whole result
            display_requisitions(date, requisition_id, staff_id, staff_name, total2, status, ref)

def OnClick_Total():
    # Adding up all the prices in the dictionary
    total = sum(items.values())
    status_update_label.config(text=f"Current Total: ${total:.2f}")

def OnClick_Check():
    # Use sum() to get the actual dollar amount, not the count
    total_price = sum(items.values())

    if total_price > 0:
        if total_price < 500:
            status_update_label.config(text=f"Total: ${total_price:.2f} - Approved")
        else:
            status_update_label.config(text=f"Total: ${total_price:.2f} - Pending")
    else:
        status_update_label.config(text="Please Add Item For Status")

#Outlook of the UI
root = tk.Tk()
root.title("Requisition System")
root.geometry("400x900")

tk.Label(root, text="Requisition System", font=('Arial', 18, 'bold')).pack(pady=10)

# Staff Inputs
tk.Label(root, text="Date").pack()
date_textbox = tk.Entry(root)
date_textbox.pack()

tk.Label(root, text="Staff ID").pack()
id_textbox = tk.Entry(root)
id_textbox.pack()

tk.Label(root, text="Staff Name").pack()
name_textbox = tk.Entry(root)
name_textbox.pack()

# Item Inputs
tk.Label(root, text="--- Items ---", font=('Arial', 12, 'bold')).pack(pady=15)
tk.Label(root, text="Item Name").pack()
item_textbox = tk.Entry(root)
item_textbox.pack()

tk.Label(root, text="Price").pack()
price_textbox = tk.Entry(root)
price_textbox.pack()

status_update_label = tk.Label(root, text="", fg="green")
status_update_label.pack()

# Buttons for adding item, checking total & approval status before printing, and Printing Requisition
add_button = tk.Button(root, text="Add Item", command=OnClick_AddItem)
add_button.pack(pady=5)

check_total= tk.Button(root, text="Check Approval", command=OnClick_Check)
check_total.pack(pady=5)

check_button = tk.Button(root, text="Check Total", command=OnClick_Total)
check_button.pack(pady=5)

submit_button = tk.Button(root, text="Submit Requisition", command=OnClick_Submit)
submit_button.pack(pady=15)

# Output Label
result_label = tk.Label(root, text="Requisition Results", bg="lightgrey", width=40, height=10)
result_label.pack(pady=10)

root.mainloop()