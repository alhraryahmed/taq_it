import frappe
from frappe.model.document import Document
from frappe.utils import cint

class exam_group_date(Document):

    @frappe.whitelist()
    def get_preachers(self):

        limit = cint(self.count_to_exam or 0)

        preachers = frappe.get_all(
            "waed_info",
            filters={"workflow_state": "Scheduling an appointment"},
            fields=["name", "namee", "phoone", "office", "place"],
            limit=limit if limit > 0 else None
        )

        self.set("waed_info_to_exam", [])

        for p in preachers:
            self.append("waed_info_to_exam", {
                "waed_info": p.name,
                "full_name": p.namee,
                "phone": p.phoone,
				"office": p.office,
				"address": p.place
            })

        self.count_waes_exam = len(preachers)

        return preachers