# Copyright (c) 2023, Lubna Hameed and contributors
# For license information, please see license.txt

from frappe import _, msgprint, throw
from frappe.model.document import Document

class KPIEvaluation(Document):
	def before_save(self):
		for i in self.kpi:
			if i.evaluation > i.score:
				throw(_("Evaluation Can't Be Larger Than Score"))