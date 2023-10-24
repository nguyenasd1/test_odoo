from odoo import fields, models, api
from datetime import date, timedelta, datetime
from odoo.exceptions import AccessDenied,ValidationError

class EstatePropertyOffer(models.Model):
    _name = 'th.estate.property.offer'
    _description = 'cac offer'
    _sql_constraints = [
        ('price', 'check(price>=0)', 'giá cả thì ko dc âm')
    ]
    _order = 'price desc'

    name_offer = fields.Char(string="Tên property")
    price = fields.Float()
    status = fields.Selection(
        selection=[('refused', 'Refused'), ('accept', 'Accept')], nocopy=True
    )
    partner_id = fields.Many2one('res.partner', string='Partner', required=True)
    property_id = fields.Many2one('th.estate.property', required=True)
    # property_type_id = fields.Many2one(related="property_id.property_type_id")
    validity = fields.Integer()
    date_deadline = fields.Date(compute='_compute_deadline', inverse='_inverse_deadline')

    @api.depends('validity', 'create_date')
    def _compute_deadline(self):
        for record in self:
            # today = date.today()
            if record.create_date:
                record.date_deadline = record.create_date + timedelta(days=record.validity)
            else:
                record.date_deadline = False

    def _inverse_deadline(self):
        for record in self:
            if record.create_date and record.date_deadline:
                record.validity = (record.date_deadline - record.create_date.date()).days
            else:
                record.validity = False

    def action_confirm_state(self):
        for record in self.env['th.estate.property.offer'].search([('status', '=', 'accept'), ('property_id', '=', self.property_id.id)]):
            if record:
                raise AccessDenied("can not have 2 accept")
        self.status = 'accept'
        a = self.price
        self.property_id.selling_price = a
        self.property_id.type_buyer = self.partner_id.name
        return True

    @api.constrains('price')
    def _check_price_90_percent(self):
        for record in self:
            if record.price < (record.property_id.expected_price*90)/100:
                raise ValidationError("offer ko dc thap hon 90 percent")

    def action_refuse_state(self):
        self.status = 'refused'
        self.property_id.selling_price = False
        # self.property_id.best_price = False
        return True


