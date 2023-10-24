from odoo import models, fields
from odoo.exceptions import AccessDenied

class Employee(models.Model):
    _inherit = "hr.employee"

    employee_code = fields.Integer(string="Mã Nhân Viên")

    def action_check_manager(self):
        if self.parent_id:
            raise AccessDenied("ok Manager")
        else:
            raise AccessDenied("ko co Manager???")
        # heheheeheheh1
# áadasdasdad

