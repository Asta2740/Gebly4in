# class RealTimeCurrencyConverter():
#     def __init__(self, url):
#         self.data = requests.get(url).json()
#         self.currencies = self.data['rates']
#
#     def convert(self, from_currency, to_currency, amount):
#         initial_amount = amount
#         # first convert it into USD if it is not in USD.
#         # because our base currency is USD
#         if from_currency != 'USD':
#             amount = amount / self.currencies[from_currency]
#
#             # limiting the precision to 4 decimal places
#         amount = round(amount * self.currencies[to_currency], 4)
#         return amount
#
#
# @dataclass
# class Product:
#     name: str = None
#     color: str = None
#     price: str = None
#     link: str = None
#     image: str = None
#     is_featured: bool = False
#     size1: str = None
#     size2: str = None
#     size3: str = None
#     size4: str = None
#     size5: str = None
#     size6: str = None
#     size7: str = None
#     size8: str = None
#     size9: str = None
#     size10: str = None
#     size11: str = None
#     size12: str = None
#     size13: str = None
#     size14: str = None
#     size15: str = None
#     size16: str = None
#     size17: str = None
#     size18: str = None
#     counterT: str = None
#
#
# def Define_sizes(counter, productS1, productS2, productS3, productS4, productS5, productS6,
#                  productS7, productS8, productS9, productS10, productS11, productS12,
#                  productS13, productS14, productS15, productS16, productS17, productS18,
#                  _product):
#     if counter:
#         Attribute = request.env['product.attribute'].sudo().search([('name', '=', 'Size')])
#         sizesList = [productS1, productS2, productS3, productS4,
#                      productS5, productS6,
#                      productS7, productS8, productS9, productS10, productS11, productS12,
#                      productS13, productS14, productS15, productS16, productS17, productS18,
#                      ]
#         _product = _product
#         # for rotation in sizesList:
#         #     if 'Nothing' in sizesList:
#         #         sizesList.remove('Nothing')
#
#         sizing = set_avilable_sizes(sizesList)
#
#         Write_sizes(sizing, Attribute, _product)
#
#
# def set_avilable_sizes(sizesList):
#     print(sizesList)
#     sizesList2 = []
#     for x in sizesList:
#         val = request.env['product.attribute.value'].sudo().search([('name', '=', x,)])
#
#         if val:
#             sizesList2.append(val)
#
#     return sizesList2
#
#
# def check_avilable_sizes(productS1, productS2, productS3, productS4, productS5, productS6,
#                          productS7, productS8, productS9, productS10, productS11, productS12,
#                          productS13, productS14, productS15, productS16, productS17, productS18,
#                          ):
#     Attribute = request.env['product.attribute'].sudo().search([('name', '=', 'Size')])
#     sizesList = [productS1, productS2, productS3, productS4,
#                  productS5, productS6,
#                  productS7, productS8, productS9, productS10, productS11, productS12,
#                  productS13, productS14, productS15, productS16, productS17, productS18,
#                  ]
#     for rotation in sizesList:
#         if 'Nothing' in sizesList:
#             sizesList.remove('Nothing')
#
#     for x in sizesList:
#         if 'Nothing' in x or '-' in x:
#             continue
#         else:
#             val = request.env['product.attribute.value'].sudo().search([('name', '=', x,)])
#             if not val:
#                 request.env['product.attribute.value'].sudo().create({'name': x,
#                                                                       'attribute_id': Attribute.id})
#
#
# def Write_sizes(sizes_id_separte_odoo_form, Attribute, _product, ):
#     # check is it copying or new item
#     if all([isinstance(item, int) for item in sizes_id_separte_odoo_form]):
#         # copy
#         sizes_id_int_form = sizes_id_separte_odoo_form
#     else:
#         # new
#         sizes_id_separte_odoo_form = sizes_id_separte_odoo_form
#         print(sizes_id_separte_odoo_form)
#
#         sizes_id_int_form = []
#
#         for adding_ids in sizes_id_separte_odoo_form:
#             x = adding_ids.id
#             if x:
#                 sizes_id_int_form.append(adding_ids.id)
#         print(sizes_id_int_form)
#
#     ptal = request.env['product.template.attribute.line'].sudo().create({
#         'attribute_id': Attribute.id if Attribute else False,
#         'product_tmpl_id': _product.id,
#         'value_ids': [(6, 0, sizes_id_int_form)],
#     })
#     _product.sudo().write({'attribute_line_ids': [(6, 0, [ptal.id])]})
#
#
# def get_product(url):
#     counter = 0
#     options = Options()
#     options.add_argument('--headless')
#     options.add_argument('--disable-gpu')
#     driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
#     driver.get(url)
#     name = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[1]/h1').text
#     try:
#         price = driver.find_element_by_xpath(
#             '/html/body/div[1]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[1]/div[2]/div/div/span').text
#     except:
#         price = driver.find_element_by_xpath(
#             '/html/body/div[1]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[1]/div[3]/div/div/span').text
#     try:
#         color = driver.find_element_by_xpath(
#             '/html/body/div[1]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/div[1]/div[1]/span/span').text
#     except:
#         color = 'Fixed'
#     link = url
#     try:
#         image = driver.find_element_by_xpath(
#             '/html/body/div[1]/div[1]/div/div[1]/div/div[2]/div[1]/div[1]/div[2]/div/div[1]/div[2]/img').get_attribute(
#             'src')
#     except:
#         image = driver.find_element_by_xpath(
#             '/html/body/div[1]/div[1]/div/div[1]/div/div[2]/div[1]/div[1]/div[1]/div/div[1]/div[1]/img[1]').get_attribute(
#             'src')
#     try:
#         counter = counter + 1
#
#         check_if_sold_out = driver.find_element_by_xpath(
#             '/html/body/div[1]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/div/div[1]/div[2]/div[1]/span/div').get_attribute(
#             "class")
#         if 'radio_soldout' in check_if_sold_out:
#             size1 = 'Nothing'
#
#         else:
#
#             size1 = driver.find_element_by_xpath(
#                 '/html/body/div[1]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/div/div[1]/div[2]/div[1]/span/div/div').text
#
#             # if 'XS - L' in size1:
#             #     check_if_sold_out = driver.find_element_by_xpath(
#             #         '/html/body/div[1]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/div/div[1]/div[2]/div[2]/span/div').get_attribute(
#             #         "class")
#             #     if 'radio_soldout' in check_if_sold_out:
#             #         size1 = 'Nothing'
#             #     else:
#             #         size1 = driver.find_element_by_xpath(
#             #             '/html/body/div[1]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/div/div[1]/div[2]/div[2]/span/div/div').text
#
#     except:
#         size1 = 'Nothing'
#         counter = counter - 1
#
#     try:
#         counter = counter + 1
#         check_if_sold_out = driver.find_element_by_xpath(
#             '/html/body/div[1]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/div/div[1]/div[2]/div[2]/span/div').get_attribute(
#             "class")
#         if 'radio_soldout' in check_if_sold_out:
#             size2 = 'Nothing'
#
#         else:
#
#             size2 = driver.find_element_by_xpath(
#                 '/html/body/div[1]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/div/div[1]/div[2]/div[2]/span/div/div').text
#             # if size1 in size2 and size1 != 'L' and size2 != 'XL' and size1 != 'XL' and size2 != 'XXL':
#             #     check_if_sold_out = driver.find_element_by_xpath(
#             #         '/html/body/div[1]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/div/div[1]/div[2]/div[3]/span/div').get_attribute(
#             #         "class")
#             #     if 'radio_soldout' in check_if_sold_out:
#             #         size2 = 'Nothing'
#             #     else:
#             #         size2 = driver.find_element_by_xpath(
#             #             '/html/body/div[1]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/div/div[1]/div[2]/div[3]/span/div/div').text
#     except:
#         size2 = 'Nothing'
#         counter = counter - 1
#
#     try:
#         counter = counter + 1
#         check_if_sold_out = driver.find_element_by_xpath(
#             '/html/body/div[1]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/div/div[1]/div[2]/div[3]/span/div').get_attribute(
#             "class")
#         if 'radio_soldout' in check_if_sold_out:
#             size3 = 'Nothing'
#
#         else:
#             size3 = driver.find_element_by_xpath(
#                 '/html/body/div[1]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/div/div[1]/div[2]/div[3]/span/div/div').text
#             # if size2 in size3 and size2 != 'L' and size3 != 'XL' and size2 != 'XL' and size3 != 'XXL':
#             #     check_if_sold_out = driver.find_element_by_xpath(
#             #         '/html/body/div[1]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/div/div[1]/div[2]/div[4]/span/div').get_attribute(
#             #         "class")
#             #     if 'radio_soldout' in check_if_sold_out:
#             #         size3 = 'Nothing'
#             #
#             #     else:
#             #         size3 = driver.find_element_by_xpath(
#             #             '/html/body/div[1]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/div/div[1]/div[2]/div[4]/span/div/div').text
#     except:
#         size3 = 'Nothing'
#         counter = counter - 1
#
#     try:
#         counter = counter + 1
#         check_if_sold_out = driver.find_element_by_xpath(
#             '/html/body/div[1]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/div/div[1]/div[2]/div[4]/span/div').get_attribute(
#             "class")
#         if 'radio_soldout' in check_if_sold_out:
#             size4 = 'Nothing'
#
#         else:
#             size4 = driver.find_element_by_xpath(
#                 '/html/body/div[1]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/div/div[1]/div[2]/div[4]/span/div/div').text
#             # if size3 in size4 and size3 != 'L' and size4 != 'XL':
#             #     check_if_sold_out = driver.find_element_by_xpath(
#             #         '/html/body/div[1]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/div/div[1]/div[2]/div[5]/span/div').get_attribute(
#             #         "class")
#             #     if 'radio_soldout' in check_if_sold_out:
#             #         size4 = 'Nothing'
#             #
#             #     else:
#             #         size4 = driver.find_element_by_xpath(
#             #             '/html/body/div[1]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/div/div[1]/div[2]/div[5]/span/div/div').text
#     except:
#         counter = counter - 1
#         size4 = 'Nothing'
#
#     try:
#         counter = counter + 1
#         check_if_sold_out = driver.find_element_by_xpath(
#             '/html/body/div[1]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/div/div[1]/div[2]/div[5]/span/div').get_attribute(
#             "class")
#         if 'radio_soldout' in check_if_sold_out:
#             size5 = 'Nothing'
#
#         else:
#             size5 = driver.find_element_by_xpath(
#                 '/html/body/div[1]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/div/div[1]/div[2]/div[5]/span/div/div').text
#             # if size4 in size5 and size4 != 'L' and size5 != 'XL' and size4 != 'XL' and size5 != 'XXL':
#             #     check_if_sold_out = driver.find_element_by_xpath(
#             #         '/html/body/div[1]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/div/div[1]/div[2]/div[6]/span/div').get_attribute(
#             #         "class")
#             #     if 'radio_soldout' in check_if_sold_out:
#             #         size5 = 'Nothing'
#             #
#             #     else:
#             #         size5 = driver.find_element_by_xpath(
#             #             '/html/body/div[1]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/div/div[1]/div[2]/div[6]/span/div/div').text
#     except:
#         counter = counter - 1
#         size5 = 'Nothing'
#
#     try:
#         counter = counter + 1
#         check_if_sold_out = driver.find_element_by_xpath(
#             '/html/body/div[1]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/div/div[1]/div[2]/div[6]/span/div').get_attribute(
#             "class")
#         if 'radio_soldout' in check_if_sold_out:
#             size6 = 'Nothing'
#
#         else:
#             size6 = driver.find_element_by_xpath(
#                 '/html/body/div[1]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/div/div[1]/div[2]/div[6]/span/div/div').text
#             # if size5 in size6 and size5 != 'L' and size6 != 'XL' and size5 != 'XL' and size6 != 'XXL':
#             #     check_if_sold_out = driver.find_element_by_xpath(
#             #         '/html/body/div[1]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/div/div[1]/div[2]/div[7]/span/div').get_attribute(
#             #         "class")
#             #     if 'radio_soldout' in check_if_sold_out:
#             #         size6 = 'Nothing'
#             #
#             #     else:
#             #         size6 = driver.find_element_by_xpath(
#             #             '/html/body/div[1]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/div/div[1]/div[2]/div[7]/span/div/div').text
#
#     except:
#         counter = counter - 1
#         size6 = 'Nothing'
#     counterT = str(counter)
#
#     try:
#         counter = counter + 1
#         check_if_sold_out = driver.find_element_by_xpath(
#             '/html/body/div[1]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/div/div[1]/div[2]/div[7]/span/div').get_attribute(
#             "class")
#         if 'radio_soldout' in check_if_sold_out:
#             size7 = 'Nothing'
#
#         else:
#             size7 = driver.find_element_by_xpath(
#                 '/html/body/div[1]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/div/div[1]/div[2]/div[7]/span/div/div').text
#             # if size5 in size6 and size5 != 'L' and size6 != 'XL' and size5 != 'XL' and size6 != 'XXL':
#             #     check_if_sold_out = driver.find_element_by_xpath(
#             #         '/html/body/div[1]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/div/div[1]/div[2]/div[7]/span/div').get_attribute(
#             #         "class")
#             #     if 'radio_soldout' in check_if_sold_out:
#             #         size6 = 'Nothing'
#             #
#             #     else:
#             #         size6 = driver.find_element_by_xpath(
#             #             '/html/body/div[1]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/div/div[1]/div[2]/div[7]/span/div/div').text
#
#     except:
#         counter = counter - 1
#         size7 = 'Nothing'
#     counterT = str(counter)
#     try:
#         counter = counter + 1
#         check_if_sold_out = driver.find_element_by_xpath(
#             '/html/body/div[1]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/div/div[1]/div[2]/div[8]/span/div').get_attribute(
#             "class")
#         if 'radio_soldout' in check_if_sold_out:
#             size8 = 'Nothing'
#
#         else:
#             size8 = driver.find_element_by_xpath(
#                 '/html/body/div[1]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/div/div[1]/div[2]/div[8]/span/div/div').text
#             # if size5 in size6 and size5 != 'L' and size6 != 'XL' and size5 != 'XL' and size6 != 'XXL':
#             #     check_if_sold_out = driver.find_element_by_xpath(
#             #         '/html/body/div[1]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/div/div[1]/div[2]/div[7]/span/div').get_attribute(
#             #         "class")
#             #     if 'radio_soldout' in check_if_sold_out:
#             #         size6 = 'Nothing'
#             #
#             #     else:
#             #         size6 = driver.find_element_by_xpath(
#             #             '/html/body/div[1]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/div/div[1]/div[2]/div[7]/span/div/div').text
#
#     except:
#         counter = counter - 1
#         size8 = 'Nothing'
#     counterT = str(counter)
#     try:
#         counter = counter + 1
#         check_if_sold_out = driver.find_element_by_xpath(
#             '/html/body/div[1]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/div/div[1]/div[2]/div[9]/span/div').get_attribute(
#             "class")
#         if 'radio_soldout' in check_if_sold_out:
#             size9 = 'Nothing'
#
#         else:
#             size9 = driver.find_element_by_xpath(
#                 '/html/body/div[1]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/div/div[1]/div[2]/div[9]/span/div/div').text
#             # if size5 in size6 and size5 != 'L' and size6 != 'XL' and size5 != 'XL' and size6 != 'XXL':
#             #     check_if_sold_out = driver.find_element_by_xpath(
#             #         '/html/body/div[1]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/div/div[1]/div[2]/div[7]/span/div').get_attribute(
#             #         "class")
#             #     if 'radio_soldout' in check_if_sold_out:
#             #         size6 = 'Nothing'
#             #
#             #     else:
#             #         size6 = driver.find_element_by_xpath(
#             #             '/html/body/div[1]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/div/div[1]/div[2]/div[7]/span/div/div').text
#
#     except:
#         counter = counter - 1
#         size9 = 'Nothing'
#     counterT = str(counter)
#     try:
#         counter = counter + 1
#         check_if_sold_out = driver.find_element_by_xpath(
#             '/html/body/div[1]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/div/div[1]/div[2]/div[10]/span/div').get_attribute(
#             "class")
#         if 'radio_soldout' in check_if_sold_out:
#             size10 = 'Nothing'
#
#         else:
#             size10 = driver.find_element_by_xpath(
#                 '/html/body/div[1]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/div/div[1]/div[2]/div[10]/span/div/div').text
#             # if size5 in size6 and size5 != 'L' and size6 != 'XL' and size5 != 'XL' and size6 != 'XXL':
#             #     check_if_sold_out = driver.find_element_by_xpath(
#             #         '/html/body/div[1]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/div/div[1]/div[2]/div[7]/span/div').get_attribute(
#             #         "class")
#             #     if 'radio_soldout' in check_if_sold_out:
#             #         size6 = 'Nothing'
#             #
#             #     else:
#             #         size6 = driver.find_element_by_xpath(
#             #             '/html/body/div[1]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/div/div[1]/div[2]/div[7]/span/div/div').text
#
#     except:
#         counter = counter - 1
#         size10 = 'Nothing'
#     counterT = str(counter)
#     try:
#         counter = counter + 1
#         check_if_sold_out = driver.find_element_by_xpath(
#             '/html/body/div[1]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/div/div[1]/div[2]/div[11]/span/div').get_attribute(
#             "class")
#         if 'radio_soldout' in check_if_sold_out:
#             size11 = 'Nothing'
#
#         else:
#             size11 = driver.find_element_by_xpath(
#                 '/html/body/div[1]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/div/div[1]/div[2]/div[11]/span/div/div').text
#             # if size5 in size6 and size5 != 'L' and size6 != 'XL' and size5 != 'XL' and size6 != 'XXL':
#             #     check_if_sold_out = driver.find_element_by_xpath(
#             #         '/html/body/div[1]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/div/div[1]/div[2]/div[7]/span/div').get_attribute(
#             #         "class")
#             #     if 'radio_soldout' in check_if_sold_out:
#             #         size6 = 'Nothing'
#             #
#             #     else:
#             #         size6 = driver.find_element_by_xpath(
#             #             '/html/body/div[1]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/div/div[1]/div[2]/div[7]/span/div/div').text
#
#     except:
#         counter = counter - 1
#         size11 = 'Nothing'
#     counterT = str(counter)
#     try:
#         counter = counter + 1
#         check_if_sold_out = driver.find_element_by_xpath(
#             '/html/body/div[1]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/div/div[1]/div[2]/div[12]/span/div').get_attribute(
#             "class")
#         if 'radio_soldout' in check_if_sold_out:
#             size12 = 'Nothing'
#
#         else:
#             size12 = driver.find_element_by_xpath(
#                 '/html/body/div[1]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/div/div[1]/div[2]/div[12]/span/div/div').text
#             # if size5 in size6 and size5 != 'L' and size6 != 'XL' and size5 != 'XL' and size6 != 'XXL':
#             #     check_if_sold_out = driver.find_element_by_xpath(
#             #         '/html/body/div[1]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/div/div[1]/div[2]/div[7]/span/div').get_attribute(
#             #         "class")
#             #     if 'radio_soldout' in check_if_sold_out:
#             #         size6 = 'Nothing'
#             #
#             #     else:
#             #         size6 = driver.find_element_by_xpath(
#             #             '/html/body/div[1]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/div/div[1]/div[2]/div[7]/span/div/div').text
#
#     except:
#         counter = counter - 1
#         size12 = 'Nothing'
#     counterT = str(counter)
#     try:
#         counter = counter + 1
#         check_if_sold_out = driver.find_element_by_xpath(
#             '/html/body/div[1]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/div/div[1]/div[2]/div[13]/span/div').get_attribute(
#             "class")
#         if 'radio_soldout' in check_if_sold_out:
#             size13 = 'Nothing'
#
#         else:
#             size13 = driver.find_element_by_xpath(
#                 '/html/body/div[1]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/div/div[1]/div[2]/div[13]/span/div/div').text
#             # if size5 in size6 and size5 != 'L' and size6 != 'XL' and size5 != 'XL' and size6 != 'XXL':
#             #     check_if_sold_out = driver.find_element_by_xpath(
#             #         '/html/body/div[1]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/div/div[1]/div[2]/div[7]/span/div').get_attribute(
#             #         "class")
#             #     if 'radio_soldout' in check_if_sold_out:
#             #         size6 = 'Nothing'
#             #
#             #     else:
#             #         size6 = driver.find_element_by_xpath(
#             #             '/html/body/div[1]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/div/div[1]/div[2]/div[7]/span/div/div').text
#
#     except:
#         counter = counter - 1
#         size13 = 'Nothing'
#     counterT = str(counter)
#     try:
#         counter = counter + 1
#         check_if_sold_out = driver.find_element_by_xpath(
#             '/html/body/div[1]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/div/div[1]/div[2]/div[14]/span/div').get_attribute(
#             "class")
#         if 'radio_soldout' in check_if_sold_out:
#             size14 = 'Nothing'
#
#         else:
#             size14 = driver.find_element_by_xpath(
#                 '/html/body/div[1]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/div/div[1]/div[2]/div[14]/span/div/div').text
#             # if size5 in size6 and size5 != 'L' and size6 != 'XL' and size5 != 'XL' and size6 != 'XXL':
#             #     check_if_sold_out = driver.find_element_by_xpath(
#             #         '/html/body/div[1]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/div/div[1]/div[2]/div[7]/span/div').get_attribute(
#             #         "class")
#             #     if 'radio_soldout' in check_if_sold_out:
#             #         size6 = 'Nothing'
#             #
#             #     else:
#             #         size6 = driver.find_element_by_xpath(
#             #             '/html/body/div[1]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/div/div[1]/div[2]/div[7]/span/div/div').text
#
#     except:
#         counter = counter - 1
#         size14 = 'Nothing'
#     counterT = str(counter)
#     try:
#         counter = counter + 1
#         check_if_sold_out = driver.find_element_by_xpath(
#             '/html/body/div[1]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/div/div[1]/div[2]/div[15]/span/div').get_attribute(
#             "class")
#         if 'radio_soldout' in check_if_sold_out:
#             size15 = 'Nothing'
#
#         else:
#             size15 = driver.find_element_by_xpath(
#                 '/html/body/div[1]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/div/div[1]/div[2]/div[15]/span/div/div').text
#             # if size5 in size6 and size5 != 'L' and size6 != 'XL' and size5 != 'XL' and size6 != 'XXL':
#             #     check_if_sold_out = driver.find_element_by_xpath(
#             #         '/html/body/div[1]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/div/div[1]/div[2]/div[7]/span/div').get_attribute(
#             #         "class")
#             #     if 'radio_soldout' in check_if_sold_out:
#             #         size6 = 'Nothing'
#             #
#             #     else:
#             #         size6 = driver.find_element_by_xpath(
#             #             '/html/body/div[1]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/div/div[1]/div[2]/div[7]/span/div/div').text
#
#     except:
#         counter = counter - 1
#         size15 = 'Nothing'
#     counterT = str(counter)
#     try:
#         counter = counter + 1
#         check_if_sold_out = driver.find_element_by_xpath(
#             '/html/body/div[1]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/div/div[1]/div[2]/div[16]/span/div').get_attribute(
#             "class")
#         if 'radio_soldout' in check_if_sold_out:
#             size16 = 'Nothing'
#
#         else:
#             size16 = driver.find_element_by_xpath(
#                 '/html/body/div[1]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/div/div[1]/div[2]/div[16]/span/div/div').text
#             # if size5 in size6 and size5 != 'L' and size6 != 'XL' and size5 != 'XL' and size6 != 'XXL':
#             #     check_if_sold_out = driver.find_element_by_xpath(
#             #         '/html/body/div[1]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/div/div[1]/div[2]/div[7]/span/div').get_attribute(
#             #         "class")
#             #     if 'radio_soldout' in check_if_sold_out:
#             #         size6 = 'Nothing'
#             #
#             #     else:
#             #         size6 = driver.find_element_by_xpath(
#             #             '/html/body/div[1]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/div/div[1]/div[2]/div[7]/span/div/div').text
#
#     except:
#         counter = counter - 1
#         size16 = 'Nothing'
#     counterT = str(counter)
#     try:
#         counter = counter + 1
#         check_if_sold_out = driver.find_element_by_xpath(
#             '/html/body/div[1]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/div/div[1]/div[2]/div[17]/span/div').get_attribute(
#             "class")
#         if 'radio_soldout' in check_if_sold_out:
#             size17 = 'Nothing'
#
#         else:
#             size17 = driver.find_element_by_xpath(
#                 '/html/body/div[1]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/div/div[1]/div[2]/div[17]/span/div/div').text
#             # if size5 in size6 and size5 != 'L' and size6 != 'XL' and size5 != 'XL' and size6 != 'XXL':
#             #     check_if_sold_out = driver.find_element_by_xpath(
#             #         '/html/body/div[1]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/div/div[1]/div[2]/div[7]/span/div').get_attribute(
#             #         "class")
#             #     if 'radio_soldout' in check_if_sold_out:
#             #         size6 = 'Nothing'
#             #
#             #     else:
#             #         size6 = driver.find_element_by_xpath(
#             #             '/html/body/div[1]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/div/div[1]/div[2]/div[7]/span/div/div').text
#
#     except:
#         counter = counter - 1
#         size17 = 'Nothing'
#     counterT = str(counter)
#     try:
#         counter = counter + 1
#         check_if_sold_out = driver.find_element_by_xpath(
#             '/html/body/div[1]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/div/div[1]/div[2]/div[18]/span/div').get_attribute(
#             "class")
#         if 'radio_soldout' in check_if_sold_out:
#             size18 = 'Nothing'
#
#         else:
#             size18 = driver.find_element_by_xpath(
#                 '/html/body/div[1]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/div/div[1]/div[2]/div[18]/span/div/div').text
#             # if size5 in size6 and size5 != 'L' and size6 != 'XL' and size5 != 'XL' and size6 != 'XXL':
#             #     check_if_sold_out = driver.find_element_by_xpath(
#             #         '/html/body/div[1]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/div/div[1]/div[2]/div[7]/span/div').get_attribute(
#             #         "class")
#             #     if 'radio_soldout' in check_if_sold_out:
#             #         size6 = 'Nothing'
#             #
#             #     else:
#             #         size6 = driver.find_element_by_xpath(
#             #             '/html/body/div[1]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/div/div[1]/div[2]/div[7]/span/div/div').text
#
#     except:
#         counter = counter - 1
#         size18 = 'Nothing'
#     counterT = str(counter)
#
#     driver.quit()
#     print(image)
#     return Product(name=name, price=price, color=color, link=link, image=image, size1=size1, size2=size2, size3=size3,
#                    size4=size4, size5=size5, size6=size6,
#                    size7=size7, size8=size8, size9=size9,
#                    size10=size10, size11=size11, size12=size12,
#                    size13=size13, size14=size14, size15=size15,
#                    size16=size16, size17=size17, size18=size18,
#                    counterT=counter)
