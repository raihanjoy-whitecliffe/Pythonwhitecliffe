#importing all functions
from req_func import add_requisition, requisition_approval, display_requisitions
date, requisition_id, staff_id, staff_name, total2 = add_requisition()
print("----------------------------")
req_status, approval_ref = requisition_approval(requisition_id, staff_id, total2)
print("----------------------------")
display_requisitions(date, requisition_id, staff_id, staff_name, total2, req_status, approval_ref)