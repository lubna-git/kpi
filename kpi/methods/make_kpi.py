import frappe


def make_kpi(doc, method):

    if doc.status == "Completed":

        # Getting the employee name from the Employee table.
        employee = frappe.db.get_value(
            "Employee", {"user_id": doc.completed_by}, ["name"], as_dict=1
        )

        # Creating a new KPI Evaluation document and setting the values of the fields.
        new_kpi_instance = frappe.new_doc("KPI Evaluation")
        new_kpi_instance.user = doc.completed_by
        new_kpi_instance.employee = employee.name
        new_kpi_instance.task = doc.name
        new_kpi_instance.task_subject = doc.subject
        new_kpi_instance.expected_time = doc.expected_time

        # Checking if the KPI Evaluation document already exists
        # If it does not exist, then it will insert the new KPI Evaluation document.
        if not frappe.db.exists(
            "KPI Evaluation", {"employee": employee.name, "task_subject": doc.subject}
        ):
            new_kpi_instance.insert()
