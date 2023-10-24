from odoo import models, fields,api
from odoo.exceptions import AccessDenied, ValidationError


class EstateProperty(models.Model):
    _name = 'th.estate.property'
    _description = 'hello ae'
    # _order = 'id desc'

    name = fields.Char()
    description = fields.Text(required=True)
    postcode = fields.Char()
    date_availability = fields.Date('last seen', default=lambda self: fields.Date.today())
    expected_price = fields.Float()
    selling_price = fields.Float()
    bedroom = fields.Integer(default=2)
    living_area = fields.Integer(default=10)
    facades =   fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer(default=4)
    garden_orientation = fields.Selection(
        selection=[('north', 'North'), ('south', 'South'), ('east', 'East'), ('west', 'West')]
    )
    _sql_constraints = [
        ('check_price', 'check(expected_price>=0)', 'giá cả thì ko dc âm'),
        ('selling_price', 'check(selling_price>=0)', 'giá cả thì ko dc âm')
    ]
    active = fields.Boolean(default=True)
    state = fields.Selection(
        default='new', required=True, readonly=False,
        selection=[('new', 'New'), ('offer received', 'Offer Received'), ('offer accepted', 'Offer Accepted'),
                   ('sold', 'Sold'), ('canceled', 'Canceled')]
    )
<<<<<<< Updated upstream

  adasdasddfdaksao;iflhs;ufasf
=======
# Many2one
    property_id = fields.Many2one('res.users')
    property_type_id = fields.Many2one('th.estate.property.type', string='Property Type')
    type_seller = fields.Many2one('res.users', string='Seller', index=True, tracking=True, default=lambda self: self.env.user)
    type_buyer = fields.Char(readonly=True)
    # type_seller = fields.Char('Buyer', related='property_type_id.seller')
# many2many
    tag_ids = fields.Many2many('th.estate.property.tag', string="Tags")
# one2many
    offer_ids = fields.One2many('th.estate.property.offer', 'property_id')
    total_area = fields.Float(compute='_compute_total_area')
    best_price = fields.Float(compute='_max_price', string='Best Offer')

    @api.depends('living_area', 'garden_area')
    def _compute_total_area(self):
        for record in self:
            record.total_area = record.living_area + record.garden_area
            print(type(record.living_area), type(record.garden_area))

    @api.depends('offer_ids.price')
    def _max_price(self):
        for record in self:
            if record.offer_ids:
                record.best_price = max(record.mapped('offer_ids.price'))
            else:
                record.best_price = False

    @api.onchange('garden')
    def _onchange_garden(self):
        if self.garden:
            self.garden_area = 10
            self.garden_orientation = 'north'
        else:
            self.garden_area = False
            self.garden_orientation = False

    def action_sold(self):
        if self.state == 'canceled':
            raise AccessDenied("canceled can not sell")
        else:
            self.state = 'sold'
        return True

    def action_canceled(self):
        if self.state == 'sold':
            raise AccessDenied("can not canceled")
        else:
            self.state = 'canceled'
            self.best_price = False
        return True

    # def unlink(self):
    #     for record in self:
    #         super(EstateProperty, self).unlink()

    def unlink(self):
        if self.state in ('new', 'canceled'):
            raise AccessDenied('ko dc xoa')
        return super(EstateProperty, self).unlink()

    @api.model
    def create(self,vals_list):
        return super(EstateProperty, self).create(vals_list)

    def read(self,vals_list):
        result = super().read(vals_list)
        for record in self:
            if record.offer_ids.property_id:
                record.state = 'offer received'
            return result




>>>>>>> Stashed changes
