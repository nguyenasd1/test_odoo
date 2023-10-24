from odoo import models, fields


class MyPet(models.Model):
    _name = 'th.my.pet'
    _description = 'this is pet pet'

    name = fields.Char('Pet Name', required=True)
    nickname = fields.Char('Nickname')
    description = fields.Text('Pet Description')
    age = fields.Integer('Pet Age', default=1)
    weight = fields.Float('Weight (kg)')
