from odoo import fields, models, api


class RecentInquiry(models.Model):
    _name = "recent.inquiry"
    _description = "inquiry templet"

    name = fields.Char(string="scrapper name",
                       required=True)  # you will see scrapper name in gui as label name , if you dont give any name it will be name
    responsible_id = fields.Char(string="Responsible")
    sales_price = fields.Float(string="Sales Price")
    cost = fields.Float(string="Cost")
    note = fields.Text(string="Description")
    Test = fields.Float(String="counter")
