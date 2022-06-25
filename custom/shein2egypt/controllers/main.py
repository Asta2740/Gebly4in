import base64
import urllib
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from dataclasses import dataclass
from odoo import http
from odoo.http import request
import time


import math
from tkinter import *
import tkinter as tk
from tkinter import ttk


# https://www.odoo.com/documentation/master/developer/reference/backend/http.html

class RealTimeCurrencyConverter():
    def __init__(self, url):
        self.data = requests.get(url).json()
        self.currencies = self.data['rates']

    def convert(self, from_currency, to_currency, amount):
        initial_amount = amount
        # first convert it into USD if it is not in USD.
        # because our base currency is USD
        if from_currency != 'USD':
            amount = amount / self.currencies[from_currency]

            # limiting the precision to 4 decimal places
        amount = round(amount * self.currencies[to_currency], 4)
        return amount


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
    size7: str = None
    size8: str = None
    size9: str = None
    size10: str = None
    size11: str = None
    size12: str = None
    size13: str = None
    size14: str = None
    size15: str = None
    size16: str = None
    size17: str = None
    size18: str = None
    counterT: str = None


def Define_sizes(counter, productS1, productS2, productS3, productS4, productS5, productS6,
                 productS7, productS8, productS9, productS10, productS11, productS12,
                 productS13, productS14, productS15, productS16, productS17, productS18,
                 _product):

    if counter:
        Attribute = request.env['product.attribute'].sudo().search([('name', '=', 'Size')])
        sizesList = [productS1, productS2, productS3, productS4,
                     productS5, productS6,
                     productS7, productS8, productS9, productS10, productS11, productS12,
                     productS13, productS14, productS15, productS16, productS17, productS18,
                     ]
        _product = _product
        # for rotation in sizesList:
        #     if 'Nothing' in sizesList:
        #         sizesList.remove('Nothing')

        Sizing_format = set_avilable_sizes(sizesList)

        Write_sizes(Sizing_format, Attribute, _product)


def set_avilable_sizes(sizesList):
    print(sizesList)
    sizesList2 = []
    for x in sizesList:
        val = request.env['product.attribute.value'].sudo().search([('name', '=', x,)])

        if val:
            sizesList2.append(val)

    return sizesList2


def check_avilable_sizes(productS1, productS2, productS3, productS4, productS5, productS6,
                         productS7, productS8, productS9, productS10, productS11, productS12,
                         productS13, productS14, productS15, productS16, productS17, productS18,
                         ):
    Attribute = request.env['product.attribute'].sudo().search([('name', '=', 'Size')])
    sizesList = [productS1, productS2, productS3, productS4,
                 productS5, productS6,
                 productS7, productS8, productS9, productS10, productS11, productS12,
                 productS13, productS14, productS15, productS16, productS17, productS18,
                 ]
    for rotation in sizesList:
        if 'Nothing' in sizesList:
            sizesList.remove('Nothing')

    for x in sizesList:
        if 'Nothing' in x or '-' in x:
            continue
        else:
            val = request.env['product.attribute.value'].sudo().search([('name', '=', x,)])
            if not val:
                request.env['product.attribute.value'].sudo().create({'name': x,
                                                                      'attribute_id': Attribute.id})


def Write_sizes(sizes_id_separte_odoo_form, Attribute, _product, ):
    # check is it copying or new item
    if all([isinstance(item, int) for item in sizes_id_separte_odoo_form]):
        # copy
        sizes_id_int_form = sizes_id_separte_odoo_form
    else:
        # new
        sizes_id_separte_odoo_form = sizes_id_separte_odoo_form
        print(sizes_id_separte_odoo_form)

        sizes_id_int_form = []

        for adding_ids in sizes_id_separte_odoo_form:
            x = adding_ids.id
            if x:
                sizes_id_int_form.append(adding_ids.id)
        print(sizes_id_int_form)

    Sizing_format = request.env['product.template.attribute.line'].sudo().create({
        'attribute_id': Attribute.id if Attribute else False,
        'product_tmpl_id': _product.id,
        'value_ids': [(6, 0, sizes_id_int_form)],
    })
    _product.sudo().write({'attribute_line_ids': [(6, 0, [Sizing_format.id])]})


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


    except:
        size1 = 'Nothing'
        counter = counter - 1

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


    except:
        counter = counter - 1
        size6 = 'Nothing'
    counterT = str(counter)

    try:
        counter = counter + 1
        check_if_sold_out = driver.find_element_by_xpath(
            '/html/body/div[1]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/div/div[1]/div[2]/div[7]/span/div').get_attribute(
            "class")
        if 'radio_soldout' in check_if_sold_out:
            size7 = 'Nothing'

        else:
            size7 = driver.find_element_by_xpath(
                '/html/body/div[1]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/div/div[1]/div[2]/div[7]/span/div/div').text


    except:
        counter = counter - 1
        size7 = 'Nothing'
    counterT = str(counter)
    try:
        counter = counter + 1
        check_if_sold_out = driver.find_element_by_xpath(
            '/html/body/div[1]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/div/div[1]/div[2]/div[8]/span/div').get_attribute(
            "class")
        if 'radio_soldout' in check_if_sold_out:
            size8 = 'Nothing'

        else:
            size8 = driver.find_element_by_xpath(
                '/html/body/div[1]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/div/div[1]/div[2]/div[8]/span/div/div').text


    except:
        counter = counter - 1
        size8 = 'Nothing'
    counterT = str(counter)
    try:
        counter = counter + 1
        check_if_sold_out = driver.find_element_by_xpath(
            '/html/body/div[1]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/div/div[1]/div[2]/div[9]/span/div').get_attribute(
            "class")
        if 'radio_soldout' in check_if_sold_out:
            size9 = 'Nothing'

        else:
            size9 = driver.find_element_by_xpath(
                '/html/body/div[1]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/div/div[1]/div[2]/div[9]/span/div/div').text


    except:
        counter = counter - 1
        size9 = 'Nothing'
    counterT = str(counter)
    try:
        counter = counter + 1
        check_if_sold_out = driver.find_element_by_xpath(
            '/html/body/div[1]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/div/div[1]/div[2]/div[10]/span/div').get_attribute(
            "class")
        if 'radio_soldout' in check_if_sold_out:
            size10 = 'Nothing'

        else:
            size10 = driver.find_element_by_xpath(
                '/html/body/div[1]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/div/div[1]/div[2]/div[10]/span/div/div').text


    except:
        counter = counter - 1
        size10 = 'Nothing'
    counterT = str(counter)
    try:
        counter = counter + 1
        check_if_sold_out = driver.find_element_by_xpath(
            '/html/body/div[1]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/div/div[1]/div[2]/div[11]/span/div').get_attribute(
            "class")
        if 'radio_soldout' in check_if_sold_out:
            size11 = 'Nothing'

        else:
            size11 = driver.find_element_by_xpath(
                '/html/body/div[1]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/div/div[1]/div[2]/div[11]/span/div/div').text


    except:
        counter = counter - 1
        size11 = 'Nothing'
    counterT = str(counter)
    try:
        counter = counter + 1
        check_if_sold_out = driver.find_element_by_xpath(
            '/html/body/div[1]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/div/div[1]/div[2]/div[12]/span/div').get_attribute(
            "class")
        if 'radio_soldout' in check_if_sold_out:
            size12 = 'Nothing'

        else:
            size12 = driver.find_element_by_xpath(
                '/html/body/div[1]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/div/div[1]/div[2]/div[12]/span/div/div').text


    except:
        counter = counter - 1
        size12 = 'Nothing'
    counterT = str(counter)
    try:
        counter = counter + 1
        check_if_sold_out = driver.find_element_by_xpath(
            '/html/body/div[1]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/div/div[1]/div[2]/div[13]/span/div').get_attribute(
            "class")
        if 'radio_soldout' in check_if_sold_out:
            size13 = 'Nothing'

        else:
            size13 = driver.find_element_by_xpath(
                '/html/body/div[1]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/div/div[1]/div[2]/div[13]/span/div/div').text


    except:
        counter = counter - 1
        size13 = 'Nothing'
    counterT = str(counter)
    try:
        counter = counter + 1
        check_if_sold_out = driver.find_element_by_xpath(
            '/html/body/div[1]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/div/div[1]/div[2]/div[14]/span/div').get_attribute(
            "class")
        if 'radio_soldout' in check_if_sold_out:
            size14 = 'Nothing'

        else:
            size14 = driver.find_element_by_xpath(
                '/html/body/div[1]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/div/div[1]/div[2]/div[14]/span/div/div').text


    except:
        counter = counter - 1
        size14 = 'Nothing'
    counterT = str(counter)
    try:
        counter = counter + 1
        check_if_sold_out = driver.find_element_by_xpath(
            '/html/body/div[1]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/div/div[1]/div[2]/div[15]/span/div').get_attribute(
            "class")
        if 'radio_soldout' in check_if_sold_out:
            size15 = 'Nothing'

        else:
            size15 = driver.find_element_by_xpath(
                '/html/body/div[1]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/div/div[1]/div[2]/div[15]/span/div/div').text


    except:
        counter = counter - 1
        size15 = 'Nothing'
    counterT = str(counter)
    try:
        counter = counter + 1
        check_if_sold_out = driver.find_element_by_xpath(
            '/html/body/div[1]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/div/div[1]/div[2]/div[16]/span/div').get_attribute(
            "class")
        if 'radio_soldout' in check_if_sold_out:
            size16 = 'Nothing'

        else:
            size16 = driver.find_element_by_xpath(
                '/html/body/div[1]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/div/div[1]/div[2]/div[16]/span/div/div').text


    except:
        counter = counter - 1
        size16 = 'Nothing'
    counterT = str(counter)
    try:
        counter = counter + 1
        check_if_sold_out = driver.find_element_by_xpath(
            '/html/body/div[1]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/div/div[1]/div[2]/div[17]/span/div').get_attribute(
            "class")
        if 'radio_soldout' in check_if_sold_out:
            size17 = 'Nothing'

        else:
            size17 = driver.find_element_by_xpath(
                '/html/body/div[1]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/div/div[1]/div[2]/div[17]/span/div/div').text


    except:
        counter = counter - 1
        size17 = 'Nothing'
    counterT = str(counter)
    try:
        counter = counter + 1
        check_if_sold_out = driver.find_element_by_xpath(
            '/html/body/div[1]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/div/div[1]/div[2]/div[18]/span/div').get_attribute(
            "class")
        if 'radio_soldout' in check_if_sold_out:
            size18 = 'Nothing'

        else:
            size18 = driver.find_element_by_xpath(
                '/html/body/div[1]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/div/div[1]/div[2]/div[18]/span/div/div').text

    except:
        counter = counter - 1
        size18 = 'Nothing'
    counterT = str(counter)

    driver.quit()
    print(image)
    return Product(name=name, price=price, color=color,
                   link=link, image=image, size1=size1,
                   size2=size2, size3=size3,
                   size4=size4, size5=size5, size6=size6,
                   size7=size7, size8=size8, size9=size9,
                   size10=size10, size11=size11, size12=size12,
                   size13=size13, size14=size14, size15=size15,
                   size16=size16, size17=size17, size18=size18,
                   counterT=counter)


def get_raw_price(string):
    new_str = ''
    for each in string:
        if each in "1234567890.,":
            new_str += each
    if ',' in new_str:
        new_str = new_str.replace(',', '.')

    if '€' in string:
        url = 'https://api.exchangerate-api.com/v4/latest/EUR'
        converter = RealTimeCurrencyConverter(url)
        price = math.ceil(converter.convert('EUR', 'EGP', float(new_str)))
    elif "$" in string:
        url = 'https://api.exchangerate-api.com/v4/latest/USD'
        converter = RealTimeCurrencyConverter(url)
        price = math.ceil(converter.convert('USD', 'EGP', float(new_str)))
    else:
        url = 'https://api.exchangerate-api.com/v4/latest/SAR'
        converter = RealTimeCurrencyConverter(url)
        price = math.ceil(converter.convert('SAR', 'EGP', float(new_str)))

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

            #Get Url
            Link_of_product = kw["Url"]

            # checking if its shein url only or not and not a homepage
            if 'https' in Link_of_product and 'shein' in Link_of_product and ".html" in Link_of_product:

                # check for parent products in database
                checkLink = request.env['product.template'].search([('product_description', 'like', Link_of_product[11:120]),
                     ('description', '=', '<p>first item</p>')])
                print(checkLink)

                if checkLink:

                    checkLink.sudo().write({'Counter': checkLink.Counter + 1})
                    if checkLink.Counter > 10:
                        category_implementation = request.env['product.public.category'].sudo().search(
                            [('id', '=', '8',)])
                        category_implementation2 = request.env['product.public.category'].sudo().search(
                            [('id', '=', '16',)])

                        checkLink.sudo().write({'public_categ_ids': [
                            (6, 0, [category_implementation.id, category_implementation2.id])]})

                    name_C = checkLink.name
                    Description_C = checkLink.product_description
                    price_C = checkLink.list_price
                    image_C = checkLink.image_1920
                    Cost_C = checkLink.standard_price
                    # put child category
                    category_implementation = request.env['product.public.category'].sudo().search(
                        [('id', '=', '14',)])

                    C_product = request.env['product.template'].sudo().create({'name': name_C,
                                                                               'list_price': price_C,
                                                                               'standard_price':Cost_C,
                                                                               'product_description': Description_C,
                                                                               'is_published': True,
                                                                               'image_1920': image_C,
                                                                               'public_categ_ids': [
                                                                                   (6, 0, [category_implementation.id])]
                                                                               })

                    copy_attributes = request.env['product.template.attribute.line'].sudo().search(
                        [('id', '=', checkLink.attribute_line_ids.id)])

                    Sizes_C = copy_attributes.value_ids

                    Write_sizes(Sizes_C.ids, Attribute, C_product)

                    return request.redirect("/shop/category/personal-shop-15")
                # Copying ends here and it endsss in 0.5 - 2 seconds

                else:
                    # if we dont have it in parents products
                    start = time.time()

                    product = get_product(Link_of_product)

                    code = upload_image(product.image)
                    # translation didnt work here so we added by id
                    # not name since it was translated inside so it couldn't find the name

                    category_implementation = request.env['product.public.category'].sudo().search(
                        [('id', '=', '8',)])

                    product_name = put_colour_in_name(product.name, product.color)
                    Cost = get_raw_price(product.price)
                    selling_price = math.ceil(Cost*(1+0.20)) #20% profit


                    _product = request.env['product.template'].sudo().create({'name': product_name,
                                                                              'list_price':selling_price,
                                                                              'standard_price':Cost,
                                                                              'product_description': product.link,
                                                                              'is_published': True,
                                                                              'image_1920': base64.b64encode(
                                                                                  get_img(code)),
                                                                              'public_categ_ids': [
                                                                                  (6, 0, [category_implementation.id])],
                                                                              'description': 'first item',
                                                                              'Counter': 1,

                                                                              })
                    S2 = _product.name
                    S2 = S2[S2.find(" co"):]
                    S1 = _product.product_description
                    S1 = S1[21:S1.find("-p-")]
                    if 'color' in S2:
                        English_name = S1 + S2
                    else:
                        English_name = S1
                    _product.sudo().write({'name': English_name})
                    print(_product.id)

                    counter = int(product.counterT)

                    check_avilable_sizes(product.size1, product.size2, product.size3, product.size4, product.size5,
                                         product.size6,
                                         product.size7, product.size8, product.size9, product.size10, product.size11,
                                         product.size12,
                                         product.size13, product.size14, product.size15, product.size16, product.size17,
                                         product.size18, )

                    Define_sizes(counter, product.size1, product.size2, product.size3, product.size4, product.size5,
                                 product.size6,
                                 product.size7, product.size8, product.size9, product.size10, product.size11,
                                 product.size12,
                                 product.size13, product.size14, product.size15, product.size16, product.size17,
                                 product.size18,
                                 _product)

                    end = time.time()
                    print(f"image loading Not in database {end - start}")

                    return request.redirect("/shop/category/personal-shop-15")

            else:

                return request.redirect("/Shein2egypt")

        return request.render('shein2egypt.Shein_page')
