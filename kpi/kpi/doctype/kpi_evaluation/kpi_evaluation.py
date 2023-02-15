# Copyright (c) 2023, Lubna Hameed and contributors
# For license information, please see license.txt

import frappe
from frappe import _, throw
from frappe.model.document import Document

class KPIEvaluation(Document):
	def before_save(self):
		"""
		If the KPI Settings is_evaluation_based is set to true, then throw an error if the evaluation is
		larger than the score
		"""
		if is_evaluation_based := frappe.db.get_single_value(
			'KPI Settings', 'is_evaluation_based'
		):
			for i in self.kpi:
				if i.evaluation > i.score:
					throw(_("Evaluation Can't Be Larger Than Score"))