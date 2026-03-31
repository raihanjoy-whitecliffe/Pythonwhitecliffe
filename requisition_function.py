def add_requisition():
    #using counter for unique staff id
    counter=1
    requisition_id=counter+1000
    print("Enter your information:")
    date = input("Date: ")
    staff_id = input("Staff ID: ")
    staff_name = input("Staff Name: ")
    print("Requisition ID:", requisition_id)

    #totaling and listing items
    items = []
    more_item=''
    total = 0
    print("Add items: ")
    item_name = input("Item Name: ")
    item_price = input("Item Price ($): ")
    more_item = input("Add another item (yes/no): ").lower()
    if more_item == 'yes':
        item_name = input("Item Name: ")
        item_price = float(input("Item Price ($): "))
        more_item = input("Add another item (yes/no): ")
        items.append([item_name, item_price])
        total+=item_price