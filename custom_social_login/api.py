import frappe

@frappe.whitelist(allow_guest=True)
def get_redirect_url(app_name):
    doc = frappe.get_all("Social Login Redirect Config", filters={"app_name": app_name}, fields=["redirect_url"])
    if doc:
        return doc[0]["redirect_url"]
    return "/"
