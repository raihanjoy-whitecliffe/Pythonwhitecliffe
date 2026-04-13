#defining function for adding requisition details
def add_requisition():
    # using counter for unique staff id
    counter = 1
    requisition_id = counter + 10000
    print("Enter your information: ")
    date = input("Date: ")
    staff_id = input("Staff ID: ")
    staff_name = input("Staff Name: ")
    print("Requisition ID: ", requisition_id)
    # totaling and listing items
    items = []
    more_item = ''
    total = 0
    print("Add items: ")
    item_name = input("Item Name: ")
    item_price = input("Item Price ($): ")
    total = total + int(item_price)
    total2 = total
    # more item request and accepts lower case and also converts capital letters to lowercase letters to avoid error
    more_item = input("Add another item (yes/no): ").lower()
    while more_item == 'yes':
        item_name = input("Item Name: ")
        item_price = float(input("Item Price ($): "))
        items.append([item_name, item_price])
        total2 += item_price
        more_item = input("Add another item (yes/no): ").lower()
    print("Total: $", total2)
    return date, requisition_id, staff_id, staff_name, total2


#defining function for requisition status
def requisition_approval(requisition_id, staff_id, total2):
    #initially status is pending
    req_status = "Pending"
#if statement is for checking range to approve
    if total2 < 500:
        req_status = "Approved"
        #takes last 3 characters from requisition id
        approval_reference = staff_id + str(requisition_id)[-3:]

        print("\nTotal: $", total2)
        print("Status:", req_status)
        print("Approval Reference Number:", approval_reference)
        return req_status, approval_reference
    else:
        print("Total: $", total2)
        print("Status:", req_status)
        return req_status, "Pending"
#defining function for Printing requisition
def display_requisitions(date, requisition_id, staff_id, staff_name, total2, req_status, approval_reference):
    print("Printing Requisitions")
    print("Date: ", date)
    print("Requisition ID: ", requisition_id)
    print("Staff ID: ", staff_id)
    print("Staff Name: ", staff_name)
    print("Total: $", total2)
    print("Status: ", req_status)
    print("Approval Reference: ", approval_reference)
    return date, requisition_id, staff_id, staff_name, total2, req_status, approval_reference