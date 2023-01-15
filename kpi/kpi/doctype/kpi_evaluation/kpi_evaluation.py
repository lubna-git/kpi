# Copyright (c) 2023, Lubna Hameed and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class KPIEvaluation(Document):
	def on_save(self):
		frappe.msgprint('this event work')
