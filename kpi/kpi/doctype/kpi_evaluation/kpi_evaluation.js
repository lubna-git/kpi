// Copyright (c) 2023, Lubna Hameed and contributors
// For license information, please see license.txt

frappe.ui.form.on('KPI Evaluation', {
	// on change the value of employee field name
		employee: function(frm) {
			// fillter the task field name value depened on user field name
			cur_frm.set_query("task", function(){
				return {
					"filters": {
						"completed_by":frm.doc.user
					} 
				}
			})},
	// on change the value of KPI Template field name
	kpi_template: async function(frm) {	
		// get kpi list with choose kpi template
			let doc = await frappe.db.get_doc("KPI Template",frm.doc.kpi_template)
			doc.kpi.forEach(function(x){cur_frm.add_child("kpi",{kpi:x.kpi,description:x.description,score:x.score})});
			frm.refresh()
		},  
	});
	