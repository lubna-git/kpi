# Copyright (c) 2023, Lubna Hameed and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class KPIEvaluation(Document):
	def before_save(self):
		for i in self.kpi:
			if i.evaluation > i.score:
				frappe.throw("Evaluation Can't Be Larger Than Score")
