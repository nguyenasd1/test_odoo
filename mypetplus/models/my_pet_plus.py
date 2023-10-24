from odoo import models, fields


class MyPetPlus(models.Model):
    _inherit = "th.my.pet"

    year = fields.Char(default=2023, string="Years")
