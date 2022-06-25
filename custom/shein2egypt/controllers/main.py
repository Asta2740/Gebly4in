import base64
import urllib
import requests
import undetected_chromedriver as uc
from selenium.webdriver.chrome.options import Options
from dataclasses import dataclass
from odoo import http
from odoo.http import request
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver


# https://www.odoo.com/documentation/master/developer/reference/backend/http.html

@dataclass
class Product:
    name: str = None
    color: str = None
    price: str = None
    link: str = None
    image: str = None
    is_featured: bool = False
    size1: str = None
    size2: str = None
    size3: str = None
    size4: str = None
    size5: str = None
    size6: str = None
    counterT: str = None


def put_sizes(counter, productS1, productS2, productS3, productS4, productS5, productS6, _product):
    if counter:
        WhichSize: str = None
        Attribute = request.env['product.attribute'].sudo().search([('name', '=', 'Size')])
        sizezList = [productS1, productS2, productS3, productS4,
                     productS5, productS6, ]
        for qqq in sizezList:
            if 'Nothing' in sizezList:
                sizezList.remove('Nothing')

        sizezList_odoo = sizezList
        sizezList_odoo.extend(('1', '2', '3', '4', '5', '6'))
        print(sizezList_odoo)
        print(sizezList)

        try:
            for x in sizezList:

                val = request.env['product.attribute.value'].sudo().search([('name', '=', x,)])

                if sizezList_odoo[0] == x:
                    size_1 = val
                    if size_1:
                        WhichSize = "F1"

                if sizezList_odoo[1] == x:
                    size_2 = val
                    if size_2:
                        WhichSize = "F2"

                if sizezList_odoo[2] == x:
                    size_3 = val
                    if size_3:
                        WhichSize = "F3"

                if sizezList_odoo[3] == x:
                    size_4 = val
                    if size_4:
                        WhichSize = "F4"

                if sizezList_odoo[4] == x:
                    size_5 = val
                    if size_5:
                        WhichSize = "F5"

                if sizezList_odoo[5] == x:
                    size_6 = val
                    if size_6:
                        WhichSize = "F6"


        except:
            No_attribute = 0

        try:
            if size_1 and "F1" in WhichSize:
                ptal = request.env['product.template.attribute.line'].sudo().create({
                    'attribute_id': Attribute.id if Attribute else False,
                    'product_tmpl_id': _product.id,
                    'value_ids': [(6, 0, [size_1.id])],
                })
                _product.sudo().write({'attribute_line_ids': [(6, 0, [ptal.id])]})

        except:
            pass
        try:
            if size_2 and "F2" in WhichSize:
                ptal = request.env['product.template.attribute.line'].sudo().create({
                    'attribute_id': Attribute.id if Attribute else False,
                    'product_tmpl_id': _product.id,
                    'value_ids': [(6, 0, [size_1.id, size_2.id])],
                })
                _product.sudo().write({'attribute_line_ids': [(6, 0, [ptal.id])]})
        except:
            pass
        try:
            if size_3 and "F3" in WhichSize:
                ptal = request.env['product.template.attribute.line'].sudo().create({
                    'attribute_id': Attribute.id if Attribute else False,
                    'product_tmpl_id': _product.id,
                    'value_ids': [(6, 0, [size_1.id, size_2.id, size_3.id])],
                })
                _product.sudo().write({'attribute_line_ids': [(6, 0, [ptal.id])]})
        except:
            pass
        try:
            if size_4 and "F4" in WhichSize:
                ptal = request.env['product.template.attribute.line'].sudo().create({
                    'attribute_id': Attribute.id if Attribute else False,
                    'product_tmpl_id': _product.id,
                    'value_ids': [(6, 0, [size_1.id, size_2.id, size_3.id, size_4.id])],
                })
                _product.sudo().write({'attribute_line_ids': [(6, 0, [ptal.id])]})

        except:
            pass
        try:
            if size_5 and "F5" in WhichSize:
                ptal = request.env['product.template.attribute.line'].sudo().create({
                    'attribute_id': Attribute.id if Attribute else False,
                    'product_tmpl_id': _product.id,
                    'value_ids': [(6, 0, [size_1.id, size_2.id, size_3.id, size_4.id, size_5.id])],
                })
                _product.sudo().write({'attribute_line_ids': [(6, 0, [ptal.id])]})
        except:
            pass
        try:

            if size_6 and "F6" in WhichSize:
                ptal = request.env['product.template.attribute.line'].sudo().create({
                    'attribute_id': Attribute.id if Attribute else False,
                    'product_tmpl_id': _product.id,
                    'value_ids': [
                        (6, 0, [size_1.id, size_2.id, size_3.id, size_4.id, size_5.id, size_6.id])],
                })
                _product.sudo().write({'attribute_line_ids': [(6, 0, [ptal.id])]})
        except:
            pass


def get_product(url):
    counter = 0
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    driver.get(url)
    name = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[1]/h1').text
    try:
        price = driver.find_element_by_xpath(
            '/html/body/div[1]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[1]/div[2]/div/div/span').text
    except:
        price = driver.find_element_by_xpath(
            '/html/body/div[1]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[1]/div[3]/div/div/span').text
    try:
        color = driver.find_element_by_xpath(
            '/html/body/div[1]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/div[1]/div[1]/span/span').text
    except:
        color = 'Fixed'
    link = url
    try:
        image = driver.find_element_by_xpath(
            '/html/body/div[1]/div[1]/div/div[1]/div/div[2]/div[1]/div[1]/div[2]/div/div[1]/div[2]/img').get_attribute(
            'src')
    except:
        image = driver.find_element_by_xpath(
            '/html/body/div[1]/div[1]/div/div[1]/div/div[2]/div[1]/div[1]/div[1]/div/div[1]/div[1]/img[1]').get_attribute(
            'src')
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
    print(image)
    return Product(name=name, price=price, color=color, link=link, image=image, size1=size1, size2=size2, size3=size3,
                   size4=size4, size5=size5, size6=size6, counterT=counter)


# def get_product(url):
#     counter = 0
#
#     options = Options()
#     # options.add_argument('--headless')
#     options.add_argument('--disable-gpu')
#     driver = uc.Chrome(options=options)
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
#             if 'XS - L' in size1:
#                 check_if_sold_out = driver.find_element_by_xpath(
#                     '/html/body/div[1]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/div/div[1]/div[2]/div[2]/span/div').get_attribute(
#                     "class")
#                 if 'radio_soldout' in check_if_sold_out:
#                     size1 = 'Nothing'
#                 else:
#                     size1 = driver.find_element_by_xpath(
#                         '/html/body/div[1]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/div/div[1]/div[2]/div[2]/span/div/div').text
#
#     except:
#         size1 = 'Nothing'
#         counter = counter - 1
#
#     # if 'Nothing' in size1:
#     #     size2 = 'Nothing'
#     #     size3 = 'Nothing'
#     #     size4 = 'Nothing'
#     #     size5 = 'Nothing'
#     #     size6 = 'Nothing'
#     # else:
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
#             if size1 in size2 and size1 != 'L' and size2 != 'XL':
#                 check_if_sold_out = driver.find_element_by_xpath(
#                     '/html/body/div[1]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/div/div[1]/div[2]/div[3]/span/div').get_attribute(
#                     "class")
#                 if 'radio_soldout' in check_if_sold_out:
#                     size2 = 'Nothing'
#                 else:
#                     size2 = driver.find_element_by_xpath(
#                         '/html/body/div[1]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/div/div[1]/div[2]/div[3]/span/div/div').text
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
#             if size2 in size3 and size2 != 'L' and size3 != 'XL':
#                 check_if_sold_out = driver.find_element_by_xpath(
#                     '/html/body/div[1]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/div/div[1]/div[2]/div[4]/span/div').get_attribute(
#                     "class")
#                 if 'radio_soldout' in check_if_sold_out:
#                     size3 = 'Nothing'
#
#                 else:
#                     size3 = driver.find_element_by_xpath(
#                         '/html/body/div[1]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/div/div[1]/div[2]/div[4]/span/div/div').text
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
#             if size3 in size4 and size3 != 'L' and size4 != 'XL':
#                 check_if_sold_out = driver.find_element_by_xpath(
#                     '/html/body/div[1]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/div/div[1]/div[2]/div[5]/span/div').get_attribute(
#                     "class")
#                 if 'radio_soldout' in check_if_sold_out:
#                     size4 = 'Nothing'
#
#                 else:
#                     size4 = driver.find_element_by_xpath(
#                         '/html/body/div[1]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/div/div[1]/div[2]/div[5]/span/div/div').text
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
#             if size4 in size5 and size4 != 'L' and size5 != 'XL':
#                 check_if_sold_out = driver.find_element_by_xpath(
#                     '/html/body/div[1]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/div/div[1]/div[2]/div[6]/span/div').get_attribute(
#                     "class")
#                 if 'radio_soldout' in check_if_sold_out:
#                     size5 = 'Nothing'
#
#                 else:
#                     size5 = driver.find_element_by_xpath(
#                         '/html/body/div[1]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/div/div[1]/div[2]/div[6]/span/div/div').text
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
#             if size5 in size6 and size5 != 'L' and size6 != 'XL':
#                 check_if_sold_out = driver.find_element_by_xpath(
#                     '/html/body/div[1]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/div/div[1]/div[2]/div[7]/span/div').get_attribute(
#                     "class")
#                 if 'radio_soldout' in check_if_sold_out:
#                     size6 = 'Nothing'
#
#                 else:
#                     size6 = driver.find_element_by_xpath(
#                         '/html/body/div[1]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/div/div[1]/div[2]/div[7]/span/div/div').text
#     except:
#         counter = counter - 1
#         size6 = 'Nothing'
#     counterT = str(counter)
#
#     driver.quit()
#     print(image)
#     return Product(name=name, price=price, color=color, link=link, image=image, size1=size1, size2=size2, size3=size3,
#                    size4=size4, size5=size5, size6=size6, counterT=counter)


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


def upload_image(link):
    if 'https:' in link:
        get = urllib.request.urlopen(link)
    else:
        get = urllib.request.urlopen(
            'https:' + str(link))

    img = get.read()
    files = {'files[]': ('image.png', img)}
    post = requests.post('https://angelo666.pythonanywhere.com/upload', files=files)
    return post.content.decode('utf-8')


def get_img(code):
    return requests.get(f'https://angelo666.pythonanywhere.com/img/{code}/').content


def put_colour_in_name(name, colour):
    if "Fixed" in colour:
        colour_name = name
    else:
        colour_name = name + " color:" + colour
    return colour_name


class shein2egypt(http.Controller):

    @http.route('/Shein2egypt', website=True, auth='user')
    def web_scrapper(self, **kw):
        if kw:
            Attribute = request.env['product.attribute'].sudo().search([('name', '=', 'Size')])

            # checking if its shein url only or not and not a homepage
            if 'https' in kw["Url"] and 'shein' in kw["Url"] and ".html" in kw["Url"]:
                start = time.time()

                Link_of_product = kw["Url"]

                checkLink = request.env['product.template'].search(
                    [('product_description', 'like', Link_of_product[11:120]),
                     ('description', '=', '<p>first item</p>')])
                print(type(checkLink))

                print(Link_of_product[12:110])

                # if there is a product with same link we remove it from category, so it doesn't show in
                # ALl search history part
                if checkLink:
                    copy_attributes = request.env['product.template.attribute.line'].sudo().search(
                        [('id', '=', checkLink.attribute_line_ids.id)])

                    tot = copy_attributes.value_ids
                    i = 0
                    for qq in tot.ids:

                        valC = request.env['product.attribute.value'].sudo().search([('id', '=', qq,)])
                        if i == 0:
                            size_1 = valC
                            if size_1:
                                WhichSize = "F1"

                        if i == 1:
                            size_2 = valC
                            if size_1:
                                WhichSize = "F2"

                        if i == 2:
                            size_3 = valC
                            if size_1:
                                WhichSize = "F3"

                        if i == 3:
                            size_4 = valC
                            if size_1:
                                WhichSize = "F4"

                        if i == 4:
                            size_5 = valC
                            if size_1:
                                WhichSize = "F5"

                        if i == 5:
                            size_6 = valC
                            if size_1:
                                WhichSize = "F6"

                        i += 1

                    _product = request.env['product.template'].sudo().create({'name': checkLink.name,
                                                                              'list_price': checkLink.list_price,
                                                                              'product_description': checkLink.product_description,
                                                                              'is_published': True,
                                                                              'image_1920': checkLink.image_1920,
                                                                              })
                    try:
                        if size_1 and "F1" in WhichSize:
                            ptal = request.env['product.template.attribute.line'].sudo().create({
                                'attribute_id': Attribute.id if Attribute else False,
                                'product_tmpl_id': _product.id,
                                'value_ids': [(6, 0, [size_1.id])],
                            })
                            _product.sudo().write({'attribute_line_ids': [(6, 0, [ptal.id])]})
                    except:
                        pass
                    try:
                        if size_2 and "F2" in WhichSize:
                            ptal = request.env['product.template.attribute.line'].sudo().create({
                                'attribute_id': Attribute.id if Attribute else False,
                                'product_tmpl_id': _product.id,
                                'value_ids': [(6, 0, [size_1.id, size_2.id])],
                            })
                            _product.sudo().write({'attribute_line_ids': [(6, 0, [ptal.id])]})
                    except:
                        pass
                    try:
                        if size_3 and "F3" in WhichSize:
                            ptal = request.env['product.template.attribute.line'].sudo().create({
                                'attribute_id': Attribute.id if Attribute else False,
                                'product_tmpl_id': _product.id,
                                'value_ids': [(6, 0, [size_1.id, size_2.id, size_3.id])],
                            })
                            _product.sudo().write({'attribute_line_ids': [(6, 0, [ptal.id])]})
                    except:
                        pass
                    try:
                        if size_4 and "F4" in WhichSize:
                            ptal = request.env['product.template.attribute.line'].sudo().create({
                                'attribute_id': Attribute.id if Attribute else False,
                                'product_tmpl_id': _product.id,
                                'value_ids': [(6, 0, [size_1.id, size_2.id, size_3.id, size_4.id])],
                            })
                            _product.sudo().write({'attribute_line_ids': [(6, 0, [ptal.id])]})
                    except:
                        pass
                    try:
                        if size_5 and "F5" in WhichSize:
                            ptal = request.env['product.template.attribute.line'].sudo().create({
                                'attribute_id': Attribute.id if Attribute else False,
                                'product_tmpl_id': _product.id,
                                'value_ids': [(6, 0, [size_1.id, size_2.id, size_3.id, size_4.id, size_5.id])],
                            })
                            _product.sudo().write({'attribute_line_ids': [(6, 0, [ptal.id])]})
                    except:
                        pass
                    try:

                        if size_6 and "F6" in WhichSize:
                            ptal = request.env['product.template.attribute.line'].sudo().create({
                                'attribute_id': Attribute.id if Attribute else False,
                                'product_tmpl_id': _product.id,
                                'value_ids': [
                                    (6, 0, [size_1.id, size_2.id, size_3.id, size_4.id, size_5.id, size_6.id])],
                            })
                            _product.sudo().write({'attribute_line_ids': [(6, 0, [ptal.id])]})
                    except:
                        pass

                    end = time.time()
                    print(f"copy database done {end - start}")
                    return request.redirect("/shop/category/your-search-history-8")
                # Copying ends here and it endsss in 2 secs :)

                else:
                    start = time.time()
                    product = get_product(kw["Url"])

                    code = upload_image(product.image)
                    # translation didnt work here so we added by id
                    # not name since it was translated inside so it couldn't find the name

                    x = request.env['product.public.category'].sudo().search(
                        [('id', '=', '8',)])

                    product_name = put_colour_in_name(product.name, product.color)

                    _product = request.env['product.template'].sudo().create({'name': product_name,
                                                                              'list_price': get_raw_price(
                                                                                  product.price),
                                                                              'product_description': product.link,
                                                                              'is_published': True,
                                                                              'image_1920': base64.b64encode(
                                                                                  get_img(code)),
                                                                              'public_categ_ids': [(6, 0, [x.id])],
                                                                              'description': 'first item',

                                                                              })
                    print(_product.id)

                    counter = int(product.counterT)

                    put_sizes(counter, product.size1, product.size2, product.size3, product.size4, product.size5,
                              product.size6, _product)

                    end = time.time()
                    print(f"image loading Not in database {end - start}")

                    return request.redirect("/shop/category/your-search-history-8")

            else:


                return request.redirect("/Shein2egypt")

        return request.render('shein2egypt.Shein_page')
