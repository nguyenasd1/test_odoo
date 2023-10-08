from odoo import models, fields


class EstateProperty(models.Model):
    _name = 'th.estate.property'
    _description = 'hello ae'

    name = fields.Char()
    description = fields.Text(required=True)
    postcode = fields.Char()
    date_availability = fields.Date('last seen',default= lambda self:fields.Date.today())
    expected_price = fields.Float()
    selling_price = fields.Float()
    bedroom = fields.Integer(default=2)
    living_area = fields.Integer(default=12312313)
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection(
        selection=[('north', 'North'), ('south', 'South'), ('east', 'East'), ('west', 'West')]
    )
    active = fields.Boolean(default=True)
    state = fields.Selection(
        default='new', required=True, readonly=False,
        selection=[('new', 'New'), ('offer received', 'Offer Received'), ('offer accepted', 'Offer Accepted'), ('sold', 'Sold'), ('canceled', 'Canceled')]
    )





asdasddasd
