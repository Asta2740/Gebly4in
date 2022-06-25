from odoo import fields, models, api
import undetected_chromedriver as uc
from selenium.webdriver.chrome.options import Options
from dataclasses import dataclass

from odoo.http import request


@dataclass
class Product:
    price: str = None
    size1: str = None
    size2: str = None
    size3: str = None
    size4: str = None
    size5: str = None
    size6: str = None
    counterT: str = None

def product_update(Url):
    counter = 0
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    driver = uc.Chrome(options=options)
    driver.get(Url)
    try:
        price = driver.find_element_by_xpath(
            '/html/body/div[1]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[1]/div[2]/div/div/span').text
    except:
        price = driver.find_element_by_xpath(
            '/html/body/div[1]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[1]/div[3]/div/div/span').text
    try:
        counter = counter + 1

        check_if_sold_out = driver.find_element_by_xpath(
            '/html/body/div[1]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/div/div[1]/div[2]/div[1]/span/div').get_attribute(
            "class")
        if 'radio_soldout' in check_if_sold_out:
            size1 = 'Nothing'

        else:

            size1 = driver.find_element_by_xpath(
                '/html/body/div[1]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/div/div[1]/div[2]/div[1]/span/div/div').text

            if 'XS - L' in size1:
                check_if_sold_out = driver.find_element_by_xpath(
                    '/html/body/div[1]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/div/div[1]/div[2]/div[2]/span/div').get_attribute(
                    "class")
                if 'radio_soldout' in check_if_sold_out:
                    size1 = 'Nothing'
                else:
                    size1 = driver.find_element_by_xpath(
                        '/html/body/div[1]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/div/div[1]/div[2]/div[2]/span/div/div').text

    except:
        size1 = 'Nothing'
        counter = counter - 1

    # if 'Nothing' in size1:
    #     size2 = 'Nothing'
    #     size3 = 'Nothing'
    #     size4 = 'Nothing'
    #     size5 = 'Nothing'
    #     size6 = 'Nothing'
    # else:
    try:
        counter = counter + 1
        check_if_sold_out = driver.find_element_by_xpath(
            '/html/body/div[1]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/div/div[1]/div[2]/div[2]/span/div').get_attribute(
            "class")
        if 'radio_soldout' in check_if_sold_out:
            size2 = 'Nothing'

        else:

            size2 = driver.find_element_by_xpath(
                '/html/body/div[1]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/div/div[1]/div[2]/div[2]/span/div/div').text
            if size1 in size2 and size1 != 'L' and size2 != 'XL' and size1 != 'XL' and size2 != 'XXL':
                check_if_sold_out = driver.find_element_by_xpath(
                    '/html/body/div[1]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/div/div[1]/div[2]/div[3]/span/div').get_attribute(
                    "class")
                if 'radio_soldout' in check_if_sold_out:
                    size2 = 'Nothing'
                else:
                    size2 = driver.find_element_by_xpath(
                        '/html/body/div[1]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/div/div[1]/div[2]/div[3]/span/div/div').text
    except:
        size2 = 'Nothing'
        counter = counter - 1

    try:
        counter = counter + 1
        check_if_sold_out = driver.find_element_by_xpath(
            '/html/body/div[1]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/div/div[1]/div[2]/div[3]/span/div').get_attribute(
            "class")
        if 'radio_soldout' in check_if_sold_out:
            size3 = 'Nothing'

        else:
            size3 = driver.find_element_by_xpath(
                '/html/body/div[1]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/div/div[1]/div[2]/div[3]/span/div/div').text
            if size2 in size3 and size2 != 'L' and size3 != 'XL' and size2 != 'XL' and size3 != 'XXL':
                check_if_sold_out = driver.find_element_by_xpath(
                    '/html/body/div[1]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/div/div[1]/div[2]/div[4]/span/div').get_attribute(
                    "class")
                if 'radio_soldout' in check_if_sold_out:
                    size3 = 'Nothing'

                else:
                    size3 = driver.find_element_by_xpath(
                        '/html/body/div[1]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/div/div[1]/div[2]/div[4]/span/div/div').text
    except:
        size3 = 'Nothing'
        counter = counter - 1

    try:
        counter = counter + 1
        check_if_sold_out = driver.find_element_by_xpath(
            '/html/body/div[1]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/div/div[1]/div[2]/div[4]/span/div').get_attribute(
            "class")
        if 'radio_soldout' in check_if_sold_out:
            size4 = 'Nothing'

        else:
            size4 = driver.find_element_by_xpath(
                '/html/body/div[1]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/div/div[1]/div[2]/div[4]/span/div/div').text
            if size3 in size4 and size3 != 'L' and size4 != 'XL':
                check_if_sold_out = driver.find_element_by_xpath(
                    '/html/body/div[1]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/div/div[1]/div[2]/div[5]/span/div').get_attribute(
                    "class")
                if 'radio_soldout' in check_if_sold_out:
                    size4 = 'Nothing'

                else:
                    size4 = driver.find_element_by_xpath(
                        '/html/body/div[1]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/div/div[1]/div[2]/div[5]/span/div/div').text
    except:
        counter = counter - 1
        size4 = 'Nothing'

    try:
        counter = counter + 1
        check_if_sold_out = driver.find_element_by_xpath(
            '/html/body/div[1]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/div/div[1]/div[2]/div[5]/span/div').get_attribute(
            "class")
        if 'radio_soldout' in check_if_sold_out:
            size5 = 'Nothing'

        else:
            size5 = driver.find_element_by_xpath(
                '/html/body/div[1]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/div/div[1]/div[2]/div[5]/span/div/div').text
            if size4 in size5 and size4 != 'L' and size5 != 'XL' and size4 != 'XL' and size5 != 'XXL':
                check_if_sold_out = driver.find_element_by_xpath(
                    '/html/body/div[1]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/div/div[1]/div[2]/div[6]/span/div').get_attribute(
                    "class")
                if 'radio_soldout' in check_if_sold_out:
                    size5 = 'Nothing'

                else:
                    size5 = driver.find_element_by_xpath(
                        '/html/body/div[1]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/div/div[1]/div[2]/div[6]/span/div/div').text
    except:
        counter = counter - 1
        size5 = 'Nothing'

    try:
        counter = counter + 1
        check_if_sold_out = driver.find_element_by_xpath(
            '/html/body/div[1]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/div/div[1]/div[2]/div[6]/span/div').get_attribute(
            "class")
        if 'radio_soldout' in check_if_sold_out:
            size6 = 'Nothing'

        else:
            size6 = driver.find_element_by_xpath(
                '/html/body/div[1]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/div/div[1]/div[2]/div[6]/span/div/div').text
            if size5 in size6 and size5 != 'L' and size6 != 'XL' and size5 != 'XL' and size6 != 'XXL':
                check_if_sold_out = driver.find_element_by_xpath(
                    '/html/body/div[1]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/div/div[1]/div[2]/div[7]/span/div').get_attribute(
                    "class")
                if 'radio_soldout' in check_if_sold_out:
                    size6 = 'Nothing'

                else:
                    size6 = driver.find_element_by_xpath(
                        '/html/body/div[1]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/div/div[1]/div[2]/div[7]/span/div/div').text
    except:
        counter = counter - 1
        size6 = 'Nothing'
    counterT = str(counter)

    driver.quit()

    return Product(price=price, size1=size1, size2=size2, size3=size3,
                   size4=size4, size5=size5, size6=size6, counterT=counter)
def get_raw_price(string):
    if '€' in string:
        convert_price = 19.10
    elif "$" in string:
        convert_price = 18.26
    else:
        convert_price = 4.87

    new_str = ''
    for each in string:
        if each in "1234567890.,":
            new_str += each
    if ',' in new_str:
        new_str = new_str.replace(',', '.')
    price = round(float(new_str) * convert_price)
    return price


class ProductsTemplate(models.Model):
    _inherit = "product.template"
    # so now we inherted the product table and giviin it a new filed
    product_description = fields.Char(string="product description")
    if_sales = fields.Boolean(string="Has Sale or not")

    Counter = fields.Char(string="Counter")

    # you will see scrapper name in gui as label name , if you dont give any name it will be name

    def Update_products(self):
        intId = self.ids

        RR = request.env['product.template']
        for count in intId:
            counter = request.env['product.template'].sudo().search([("id", "=", count)])
            RR = RR + counter

        print(RR)

        y = str

        for x in RR:
            if y == x.name:
                continue
            Products_idz = x.product_description
            print(x.name)
            if Products_idz:

                product = product_update(Products_idz)

                x.sudo().write({'list_price': get_raw_price(product.price)})
                name = x.name

                Updating_samexs = request.env['product.template'].sudo().search(
                    [('name', '=', name)])
                # good till here

                Attribute = request.env['product.attribute'].sudo().search([('name', '=', 'Size')])
                counter = int(product.counterT)
                WhichSize: str = None

                sizezList = [product.size1, product.size2, product.size3, product.size4, product.size5,
                             product.size6, ]
                for qqq in sizezList:
                    if 'Nothing' in sizezList:
                        sizezList.remove('Nothing')

                sizezList_odoo = sizezList
                sizezList_odoo.extend(('1', '2', '3', '4', '5', '6'))

                try:
                    print("First item")
                    for ll in sizezList:

                        val = request.env['product.attribute.value'].sudo().search([('name', '=', ll,)])

                        if sizezList_odoo[0] == ll:
                            size_1 = val
                            if size_1:
                                WhichSize = "F1"

                        if sizezList_odoo[1] == ll:
                            size_2 = val
                            if size_2:
                                WhichSize = "F2"

                        if sizezList_odoo[2] == ll:
                            size_3 = val
                            if size_3:
                                WhichSize = "F3"

                        if sizezList_odoo[3] == ll:
                            size_4 = val
                            if size_4:
                                WhichSize = "F4"

                        if sizezList_odoo[4] == ll:
                            size_5 = val
                            if size_5:
                                WhichSize = "F5"

                        if sizezList_odoo[5] == ll:
                            size_6 = val
                            if size_6:
                                WhichSize = "F6"


                except:
                    No_attribute = 0

                try:
                    if size_1 and "F1" in WhichSize:
                        ptal = request.env['product.template.attribute.line'].sudo().create({
                            'attribute_id': Attribute.id if Attribute else False,
                            'product_tmpl_id': x.id,
                            'value_ids': [(6, 0, [size_1.id])],
                        })
                        x.sudo().write({'attribute_line_ids': [(6, 0, [ptal.id])]})

                except:
                    pass
                try:
                    if size_2 and "F2" in WhichSize:
                        ptal = request.env['product.template.attribute.line'].sudo().create({
                            'attribute_id': Attribute.id if Attribute else False,
                            'product_tmpl_id': x.id,
                            'value_ids': [(6, 0, [size_1.id, size_2.id])],
                        })
                        x.sudo().write({'attribute_line_ids': [(6, 0, [ptal.id])]})
                except:
                    pass
                try:
                    if size_3 and "F3" in WhichSize:
                        ptal = request.env['product.template.attribute.line'].sudo().create({
                            'attribute_id': Attribute.id if Attribute else False,
                            'product_tmpl_id': x.id,
                            'value_ids': [(6, 0, [size_1.id, size_2.id, size_3.id])],
                        })
                        x.sudo().write({'attribute_line_ids': [(6, 0, [ptal.id])]})
                except:
                    pass
                try:
                    if size_4 and "F4" in WhichSize:
                        ptal = request.env['product.template.attribute.line'].sudo().create({
                            'attribute_id': Attribute.id if Attribute else False,
                            'product_tmpl_id': x.id,
                            'value_ids': [(6, 0, [size_1.id, size_2.id, size_3.id, size_4.id])],
                        })
                        x.sudo().write({'attribute_line_ids': [(6, 0, [ptal.id])]})

                except:
                    pass
                try:
                    if size_5 and "F5" in WhichSize:
                        ptal = request.env['product.template.attribute.line'].sudo().create({
                            'attribute_id': Attribute.id if Attribute else False,
                            'product_tmpl_id': x.id,
                            'value_ids': [
                                (6, 0, [size_1.id, size_2.id, size_3.id, size_4.id, size_5.id])],
                        })
                        x.sudo().write({'attribute_line_ids': [(6, 0, [ptal.id])]})
                except:
                    pass
                try:

                    if size_6 and "F6" in WhichSize:
                        ptal = request.env['product.template.attribute.line'].sudo().create({
                            'attribute_id': Attribute.id if Attribute else False,
                            'product_tmpl_id': x.id,
                            'value_ids': [
                                (6, 0,
                                 [size_1.id, size_2.id, size_3.id, size_4.id, size_5.id, size_6.id])],
                        })
                        x.sudo().write({'attribute_line_ids': [(6, 0, [ptal.id])]})
                except:
                    pass

                for xy in Updating_samexs:

                    xy.sudo().write({'list_price': get_raw_price(product.price)})

                    Attribute = request.env['product.attribute'].sudo().search([('name', '=', 'Size')])
                    counter = int(product.counterT)
                    WhichSize: str = None
                    sizezList = [product.size1, product.size2, product.size3, product.size4, product.size5,
                                 product.size6, ]
                    for qqq in sizezList:
                        if 'Nothing' in sizezList:
                            sizezList.remove('Nothing')

                    sizezList_odoo = sizezList
                    sizezList_odoo.extend(('1', '2', '3', '4', '5', '6'))

                    try:
                        for ll in sizezList:

                            val = request.env['product.attribute.value'].sudo().search([('name', '=', ll,)])

                            if sizezList_odoo[0] == ll:
                                size_1 = val
                                if size_1:
                                    WhichSize = "F1"

                            if sizezList_odoo[1] == ll:
                                size_2 = val
                                if size_2:
                                    WhichSize = "F2"

                            if sizezList_odoo[2] == ll:
                                size_3 = val
                                if size_3:
                                    WhichSize = "F3"

                            if sizezList_odoo[3] == ll:
                                size_4 = val
                                if size_4:
                                    WhichSize = "F4"

                            if sizezList_odoo[4] == ll:
                                size_5 = val
                                if size_5:
                                    WhichSize = "F5"

                            if sizezList_odoo[5] == ll:
                                size_6 = val
                                if size_6:
                                    WhichSize = "F6"


                    except:
                        No_attribute = 0
                    print(xy)
                    print(Attribute)
                    print(size_1, size_2, size_3, size_4)
                    print(WhichSize)
                    try:
                        if size_1 and "F1" in WhichSize:
                            ptal = request.env['product.template.attribute.line'].sudo().create({
                                'attribute_id': Attribute.id if Attribute else False,
                                'product_tmpl_id': xy.id,
                                'value_ids': [(6, 0, [size_1.id])],
                            })
                            xy.sudo().write({'attribute_line_ids': [(6, 0, [ptal.id])]})

                    except:
                        pass
                    try:
                        if size_2 and "F2" in WhichSize:
                            ptal = request.env['product.template.attribute.line'].sudo().create({
                                'attribute_id': Attribute.id if Attribute else False,
                                'product_tmpl_id': xy.id,
                                'value_ids': [(6, 0, [size_1.id, size_2.id])],
                            })
                            xy.sudo().write({'attribute_line_ids': [(6, 0, [ptal.id])]})
                    except:
                        pass
                    try:
                        if size_3 and "F3" in WhichSize:
                            ptal = request.env['product.template.attribute.line'].sudo().create({
                                'attribute_id': Attribute.id if Attribute else False,
                                'product_tmpl_id': xy.id,
                                'value_ids': [(6, 0, [size_1.id, size_2.id, size_3.id])],
                            })
                            xy.sudo().write({'attribute_line_ids': [(6, 0, [ptal.id])]})
                    except:
                        pass
                    try:
                        if size_4 and "F4" in WhichSize:
                            ptal = request.env['product.template.attribute.line'].sudo().create({
                                'attribute_id': Attribute.id if Attribute else False,
                                'product_tmpl_id': xy.id,
                                'value_ids': [(6, 0, [size_1.id, size_2.id, size_3.id, size_4.id])],
                            })
                            xy.sudo().write({'attribute_line_ids': [(6, 0, [ptal.id])]})

                    except:
                        pass
                    try:
                        if size_5 and "F5" in WhichSize:
                            ptal = request.env['product.template.attribute.line'].sudo().create({
                                'attribute_id': Attribute.id if Attribute else False,
                                'product_tmpl_id': xy.id,
                                'value_ids': [
                                    (6, 0, [size_1.id, size_2.id, size_3.id, size_4.id, size_5.id])],
                            })
                            xy.sudo().write({'attribute_line_ids': [(6, 0, [ptal.id])]})
                    except:
                        pass
                    try:

                        if size_6 and "F6" in WhichSize:
                            ptal = request.env['product.template.attribute.line'].sudo().create({
                                'attribute_id': Attribute.id if Attribute else False,
                                'product_tmpl_id': xy.id,
                                'value_ids': [
                                    (6, 0,
                                     [size_1.id, size_2.id, size_3.id, size_4.id, size_5.id, size_6.id])],
                            })
                            xy.sudo().write({'attribute_line_ids': [(6, 0, [ptal.id])]})
                    except:
                        pass
                y = x.name

        # request.redirect("/shop/category/update-12")
