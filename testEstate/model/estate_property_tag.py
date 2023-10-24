from odoo import fields, models
class EstatePropertyTag(models.Model):
    _name = 'th.estate.property.tag'
    _description = 'cac tag'
    name = fields.Char(required=True)
    _sql_constraints = [
        ('check_name', 'unique(name)',' ten ko dc trung')
    ]
    _order = 'name'
    colour = fields.Integer()

