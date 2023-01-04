// Copyright (c) 2023, Lubna Hameed and contributors
// For license information, please see license.txt

frappe.ui.form.on('KPI Evaluation', {
	// filter the task depande on Employee name
		employee: async function(frm) {
			let doc =await frappe.db.get_doc('Employee', frm.doc.employee)
			cur_frm.set_query("task", function(){
				return {
					"filters": {
						"completed_by":doc.user_id
					} 
				}
			})},
		// get tabel of kpi template auto
		
		kpi_template: async function(frm) {	
			let doc = await frappe.db.get_doc("KPI Template",frm.doc.kpi_template)
			doc.kpi.forEach(function(x){cur_frm.add_child("kpi",{kpi:x.kpi,description:x.description,score:x.score})});
			frm.refresh()
		},  
	});
	