from odoo import models, fields,api
class EstatePropertyType(models.Model):
    _name = "th.estate.property.type"
    _rec_name = 'property_type'
    _description = "many type of estate"
    property_type = fields.Char(string='property type')
    _sql_constraints = [
        ('check_duplicates', 'unique(property_type)', ' ko dc trung property')
    ]
    property_ids = fields.One2many('th.estate.property', 'property_type_id')
    _order = 'sequence,property_type'
    sequence = fields.Integer('sequence', default=1, help='asdasd')
    # property_type = fields.Char(required=True)
    # type_id = fields.One2many(comodel_name='th.estate.property',inverse_name='property_type_id')
    # offer_ids = fields.One2many('th.estate.property.offer', 'property_type_id')
    # offer_count = fields.Integer( string="Offers")

    # compute = '_compute_offer_count'
    # def action_test_offer(self):
    #     for record in self.env['th.estate.property.offer'].search([('property_ids', '=', self.property_ids)]):
    #         for record in self:
    #             print("afnsjfs")
    #     return True

    # @api.depends('offer_ids')
    # def _compute_offer_count(self):
    #     for record in self.env['th.estate.property.offer'].search([('property_ids','=', self.property_ids.id)]):
    #         self.offer_count = len(self.offer_ids.id)
    #     return True
