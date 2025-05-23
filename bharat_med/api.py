
import frappe
from frappe import _

# @frappe.whitelist(allow_guest=True)
# def register_user(first_name, email, mobile, password, confirm_password, role):
#     print("Registering user with details??????????????????????????????????????????????:", first_name, email, mobile, password, confirm_password, role)
#     # Create user document
#     user = frappe.get_doc({
#         "doctype": "SVA User",
#         "first_name": first_name,
#         "email": email,
#         "mobile_number": mobile,
#         "password": password,
#         "confirm_password": confirm_password,
#         # "role_profile": role
#     })
    
#     user.insert(ignore_permissions=True,ignore_mandatory=True)
#     frappe.db.commit()
    
#     return {"message": "User registered successfully"}


import frappe
from frappe import _

# @frappe.whitelist(allow_guest=True)
# def register_user(first_name, email, mobile, password, confirm_password, role):
#     try:
#         print("Registering user with details:", first_name, email, mobile, password, confirm_password, role)

#         # Create user document
#         user = frappe.get_doc({
#             "doctype": "SVA User",
#             "first_name": first_name,
#             "email": email,
#             "mobile_number": mobile,
#             "password": password,
#             "confirm_password": confirm_password,
#             # "role_profile": role
#         })
        
#         user.insert(ignore_permissions=True, ignore_mandatory=True)
#         frappe.db.commit()

#         return {"message": "User registered successfully"}
    
#     except Exception as e:
#         frappe.log_error(frappe.get_traceback(), "User Registration Failed")
#         return {"error": "Failed to register user", "details": str(e)}


import frappe
from frappe import _

@frappe.whitelist(allow_guest=True)
def register_user(first_name, email, mobile, password, confirm_password,role_profile):
    try:
        if password != confirm_password:
            return {"error": "Passwords do not match."}

        user = frappe.get_doc({
            "doctype": "SVA User",
            "first_name": first_name,
            "email": email,
            "mobile_number": mobile,
            "password": password,
            "confirm_password": confirm_password,
            "role_profile": role_profile
        })

        user.insert(ignore_permissions=True, ignore_mandatory=True)
        frappe.db.commit()

        return {"message": "User registered successfully"}

    except Exception as e:
        frappe.log_error(frappe.get_traceback(), "User Registration Failed")
        return {"error": str(e)}

