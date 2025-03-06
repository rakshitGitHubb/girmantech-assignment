import frappe
import json

@frappe.whitelist(allow_guest=True)
def get_user_data(search_term=None):
    frappe.response["Access-Control-Allow-Origin"] = "*"
    file_path = frappe.get_app_path('gt_assignment', 'userdata', 'users.json')
    with open(file_path, 'r') as file:
        users = json.load(file)
    if search_term:
        search_term = search_term.lower().strip()
        users = [
            user for user in users
            if search_term in user.get('first_name', '').lower() or
               search_term in user.get('last_name', '').lower()
        ]
    return users
