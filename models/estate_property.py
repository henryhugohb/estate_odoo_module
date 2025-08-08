from odoo import fields, models

class TestModel(models.Model):
    _name = "Test H name Model"
    _description = "Test H description Model"

    name = fields.Char('H Name', required=True, translate=True)
    active = fields.Boolean('H Active', default=True)
    description = fields.Text('H Description')
    date_availability = fields.Date('H Avalilability Date')
    expected_price = fields.Float('H Price expected')
    bedrooms = fields.Integer('H Bedrooms', required=True)
    garden_orientation = fields.Selection(
        string = 'H Orientation',
        selection = [('nort', 'H Nort'),('south', 'H South'), ('east', 'H East'), ('west', 'H West')],
        help = "Select Orientation"
    )