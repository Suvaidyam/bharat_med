
from frappe import _
from frappe.utils import cint

# import frappe
from frappe.model.document import Document
import json
import frappe
from frappe import _
import base64
from frappe.utils.file_manager import save_file
from frappe.utils import today
from frappe.utils import now_datetime

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
def save_base64_image(dt,docname, base64_string, filename):
    # Remove the data:image/png;base64, or similar prefix if present
    if ',' in base64_string:
        base64_string = base64_string.split(',')[1]

    # Decode base64 string
    file_content = base64.b64decode(base64_string)
    # Save file using Frappe's file manager
    saved_file = save_file(
        fname=filename,
        content=file_content,
        dt=dt,       # e.g. "Employee", "Item", etc.
        dn=docname,
        decode=False             # Already decoded
    )

    return saved_file.file_url

    
@frappe.whitelist(allow_guest=True)
def register_patient(first_name, middle_name, last_name, date_of_birth, email, gender,
                     marital_status, address, city, state, zip_code, phone_number,
                     alternative_phone, contact_name, relationship, emergency_phone,
                     emergency_email, profile_photo=None):

    try:
        # Step 1: Create patient without photo
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
            "emergency_email": emergency_email
        })
        patient.insert(ignore_permissions=True)
        
        # Step 2: Save image after insert
        if profile_photo and ',' in profile_photo:
            base64_data = profile_photo.split(',')[1]
            file_content = base64.b64decode(base64_data)
            saved_file = save_file(
                fname=f"{first_name}_{last_name}_profile.png",
                content=file_content,
                dt="Patient",
                dn=patient.name,
                decode=False
            )
            # Attach the image URL
            patient.profile_photo = saved_file.file_url
            patient.save(ignore_permissions=True)

        frappe.db.commit()
        return {"message": "Patient registered successfully", "patient": patient.name}

    except Exception as e:
        frappe.log_error(frappe.get_traceback(), "Patient Registration Failed")
        return {"error": str(e)}
