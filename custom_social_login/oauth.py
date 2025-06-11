import frappe
from frappe.integrations.doctype.social_login_key.social_login_key import get_info_via_oauth

@frappe.whitelist(allow_guest=True)
def login_via_google_custom(code, state=None):
    login_manager = get_info_via_oauth("Google", code=code)
    frappe.local.login_manager = login_manager
    frappe.local.login_manager.post_login()

    redirect_url = "/"
    if state:
        result = frappe.get_all("Social Login Redirect Config", filters={"app_name": state}, fields=["redirect_url"])
        if result:
            redirect_url = result[0]["redirect_url"]

    frappe.local.response["type"] = "redirect"
    frappe.local.response["location"] = redirect_url
