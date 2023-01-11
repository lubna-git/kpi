import frappe


def make_kpi(doc, method):
    if doc.status == "Completed":

        # Getting the employee name from the Employee table.
        # employee = frappe.db.get_value(
        #     "Employee", {"user_id": doc.completed_by}, ["name"], as_dict=1
        # )
        
        # Creating a new KPI Evaluation document.
        frappe.new_doc(
            "KPI Evaluation",
            {
                "user": doc.completed_by,
                # "employee": employee,
                "task": doc.name,
                "task_subject": doc.subject,
            },
        ).insert()

