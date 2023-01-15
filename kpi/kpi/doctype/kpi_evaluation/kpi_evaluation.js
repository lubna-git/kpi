// Copyright (c) 2023, Lubna Hameed and contributors
// For license information, please see license.txt

frappe.ui.form.on('KPI Evaluation', {
	// on change the value of employee field name
	employee: function (frm) {
		// filleter the task field name value depended on user field name
		cur_frm.set_query("task", function () {
			return {
				"filters": {
					"completed_by": frm.doc.user
				}
			}
		})
	},

	/* Adding the kpi template to the kpi evaluation form. */
	kpi_template: async function (frm) {
		// check if kpi_template field is not empty or null
		if (frm.doc.kpi_template && frm.doc.kpi_template != "") {
			// get the KPI Template document
			let doc = await frappe.db.get_doc("KPI Template", frm.doc.kpi_template)
			// loop through kpi list and add them as child to the current form
			doc.kpi.forEach(function (x) { cur_frm.add_child("kpi", { kpi: x.kpi, description: x.description, score: x.score }) });
			// refresh the form to display the added kpi
			frm.refresh()
		} else {
			// clear child table rows when kpi_template field is cleared
			cur_frm.doc.kpi = []
			frm.refresh()
		}
	},
});