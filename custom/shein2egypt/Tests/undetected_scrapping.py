# import undetected_chromedriver as uc

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
