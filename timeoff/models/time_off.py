from odoo import models, fields
from odoo.exceptions import AccessDenied


class TimeOff(models.Model):
    _inherit = "hr.leave"

    def action_approve(self):
        result = super(TimeOff, self).action_approve()
        if not self.name:
            raise AccessDenied("nghỉ ko lí do???!!")
        else:
            return result




