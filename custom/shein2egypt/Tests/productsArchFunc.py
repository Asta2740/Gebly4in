# def Archived_update(self):
#     intId = self.ids
#     'description', '=', '<p>first item</p>'
#
#     category_implementation = request.env['product.public.category'].sudo().search(
#         [('id', '=', '8',)])
#
#     Products_List = request.env['product.template']
#     for count in intId:
#         counter = request.env['product.template'].sudo().search([("id", "=", count)])
#         Products_List = Products_List + counter
#
#     RR = request.env['product.template'].sudo().search(
#         [('description', '=', '<p>first item</p>')])
#     Products_List = RR
#
#     for x in Products_List:
#         x.sudo().write({'public_categ_ids': [(6, 0, [category_implementation.id])]})