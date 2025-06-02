
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
    
    # Patient
@frappe.whitelist(allow_guest=True)
def register_patient(first_name, middle_name, last_name,date_of_birth, email,gender,marital_status,address,city,state,zip_code,phone_number,alternative_phone,contact_name,relationship,emergency_phone,emergency_email,profile_photo):
    try:
        patient = frappe.get_doc({
            "doctype": "Patient",
            "first_name": first_name,
            "middle_name": middle_name,
            "last_name": last_name,
            "date_of_birth": date_of_birth,
            "email": email,
            "gender": gender,
            "marital_status": marital_status,
            "address": address,
            "city": city,
            "state": state,
            "zip_code": zip_code,
            "phone_number": phone_number,
            "alternative_phone": alternative_phone,
            "contact_name": contact_name,
            "relationship": relationship,
            "emergency_phone": emergency_phone,
            "emergency_email": emergency_email,
            "profile_photo": profile_photo
        })

        patient.insert(ignore_permissions=True, ignore_mandatory=True)
        frappe.db.commit()

        return {"message": "Patient registered successfully"}

    except Exception as e:
        frappe.log_error(frappe.get_traceback(), "Patient Registration Failed")
        return {"error": str(e)}
    