from odoo import fields,models


class EstateModels(models.Model):
    _name = "estate.property"
    _description = 'day la estate property'
    name = fields.Char(default='Nhap vao day')
    description = fields.Text(required=True)
    postcode = fields.Char(required=True)
    date_availability= fields.Date("Last Seen", default=lambda self: fields.Date.today())
    expected_price = fields.Float()
    selling_price= fields.Float(default=20000.3333,readonly=True,required=False)
    bedrooms=fields.Integer(default=2)
    living_area=fields.Integer()
    facades=fields.Integer()
    garage=fields.Boolean(required=False)
    garden=fields.Boolean(default=True)
    garden_area = fields.Integer()
    garden_orientation= fields.Selection(
        string='Garden Orientation',
        selection=[('north','North'),('south','South'),('east','East'),('west','West')]
    )
    active=fields.Boolean()
    status=fields.Selection(
        string='Statuss',
        selection=[('new','New'),('offer received','Offer received'),('offer accepted','Offer accepted'),('sold','Sold'),('canceled','Canceled')]
    )

