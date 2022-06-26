# Gebly4in Website
Web scrapper module

## About
- After we got acquainted with our project and its components and we knew the problems that would face us, analyzed and divided them, we touched on the use of analysis and design programs and algorithms to implement our project, which in turn formed a website as follows:

When you start entering the page, the login form appears in front of us, you type in the first text your account and directly below it you write your password, and there is a small line before the accept button, there is an account creation if this is your first time, and you can create it from a Google account.

After logging in, the main page appears in front of us that contains the following:
Products with their abstract details, either on the right of the page shows the categories of products, and on top of it shows a web scraper.
As for the products, we can click on them to know more and more details and a set of icons appears, such as, add to cart, add to whishlist.
The web scraper is the one who puts the link of the product we want from shein, which is not on our website.
After we have added the products to the shopping cart, we move to it to see what we have added, and if we want to modify it, such as reducing the quantity or increasing it and knowing the total prices and so on, the checkout button appears, in which we enter the payment information such as address, phone number, name, e-mail and how The payment that appears in two ways, namely, fewery payment or Voafone cash, and then communication is done via WhatsApp, and after that, the site automatically checks the data and creates the invoice and sends it to the reseller, who in turn approves it to be sent when to the buyer.
## technical requirments
 ## HardWare
 - Computer ( windows / mac )
 - OS ( linux / windows )
 - Can be Hosted On Cloud
 - Accessing can be done through mobile or Personal Computer with an internet Connection (if it's Hosted and Online)
 ## SoftWare
 - for Developing you will need to configure the odoo Server into your IDE of Choice ( We Recommend PyCharm)
 - hosting can be done to Odoo SH, Saas, or keep it on your server.
 - Installation:
   - Selenium
     - elenium Python bindings provides a simple API to write functional/acceptance tests using Selenium WebDriver. Through Selenium Python API you can access all functionalities of Selenium WebDriver in an intuitive way.
Selenium Python bindings provide a convenient API to access Selenium WebDrivers like Firefox, Ie, Chrome, Remote etc. The current supported Python versions are 3.5 and above.

   ```
   pip install selenium
   ```
   - webdrivermanager
     - Python module to facilitate downloading and deploying WebDriver binaries. The classes in this module can be used to automatically search for and download the latest version (or a specific version) of a WebDriver binary and then extract it and place it by copying or symlinking it to the location where Selenium or other tools should be able to find it then.
    ```
    pip install webdrivermanager
    ```
   - dataclasses
     - This is an implementation of PEP 557, Data Classes. It is a backport for Python 3.6. Because dataclasses will be included in Python 3.7, any discussion of dataclass features should occur on the python-dev mailing list at https://mail.python.org/mailman/listinfo/python-dev. At this point this repo should only be used for historical purposes (it’s where the original dataclasses discussions took place) and for discussion of the actual backport to Python 3.6.
See https://www.python.org/dev/peps/pep-0557/ for the details of how Data Classes work.
    ```
    pip install dataclasses
    ```
## Introduction
 Here is an overview about the module folders and the purpose of each one;
 -  **Custom** {Adding your custom Add-ons(modules)}
      - `shein2egypt`  First moudle made to integrate with the framework

  -  **shein2egypt** {module Folder}
      - `__init__.py`  contains import instructions for various Python files in the module.
      - `__manifest__.py`  -	Serves to declare a python package as an Odoo module and to specify module metadata , contains a single Python dictionary, where each key specifies module meta data.

  - **controllers** {Handle requests from web browsers}
      - `__init__.py`  contains import instructions for various Python files in the module.
      - `BackEndInhertence.py`  -	inherting and existing module and overriding its functions and componenets (adding filters)
      - `main.py`  - handels requests from the web scrapper page

 - **i18n** {generate localized UTF-8 reports (Translations)}
      - `ar_001.po` - translations of the page module componenets 
 
 - **models** {Business objects are declared as Python classes extending Model which integrates them into the automated persistence system}
      - `products.py` - integrating new attributes and functions to the existing fields and model
      

 - **security** {To manage users and configure  security access rights}
      - `__init__.py`  contains import instructions for various Python files in the module.
      - `ir.model.access.csv`  -	declaring the rights to groups

 - **Static** {Images, CSS or JavaScript files used by the web interface or website}

 - **Tests** {Dump Folder for storing testing data}
 
 - **Views** {Definition of business objects UI display}
      - `__init__.py`  contains import instructions for various Python files in the module.
      - `Menu_bars.xml`  -	Adding menus to header of page template
      - `products.xml`  -	Addings UI to the product views
      - `template.xml`  -	Web Scrapper page
 

  ![project folders](https://user-images.githubusercontent.com/105456248/175781841-d8715faa-1c14-41b9-95f2-3f2c0102c740.PNG)




## Api
-We made an api to convert the image from the webp to a  jnp to be able to decode it and add to the code

```
import os
import urllib.request
from werkzeug.utils import secure_filename
from PIL import Image
from secrets import token_urlsafe


app = Flask(__name__)

app.secret_key = "A8I1slA8MGqsmYhaQLosme2OsYnzAQHJ"

UPLOAD_FOLDER = '/home/Angelo666/app/static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def main():
    return 'Homepage'

@app.route('/upload', methods=['POST'])
def upload_file():
    # check if the post request has the file part
    if 'files[]' not in request.files:
        resp = jsonify({'message' : 'No file part in the request'})
        resp.status_code = 400
        return resp

    files = request.files.getlist('files[]')

    errors = {}
    success = False
    file_id = ''

    for file in files:
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            name = generate_random()
            while name in os.listdir(UPLOAD_FOLDER):
                name = generate_random()
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], name))
            success = True
            file_id = name
        else:
            errors[file.filename] = 'File type is not allowed'

    if success and errors:
        errors['message'] = 'File(s) successfully uploaded'
        resp = jsonify(errors)
        resp.status_code = 500
        return resp
    if success:
        return file_id
    else:
        resp = jsonify(errors)
        resp.status_code = 500
        return resp

@app.route('/img/<img>/')
def get_file(img):
    if img in os.listdir(UPLOAD_FOLDER):
        im = Image.open(os.path.join(app.config['UPLOAD_FOLDER'], img))
        rgb_im = im.convert('RGB')
        rgb_im.save(os.path.join(app.config['UPLOAD_FOLDER'], 'colors.jpg'))
        os.remove(os.path.join(app.config['UPLOAD_FOLDER'], img))
        return send_file(os.path.join(app.config['UPLOAD_FOLDER'], 'colors.jpg'), mimetype='image/gif')
    resp = jsonify({'message' : 'File not found'})
    resp.status_code = 400
    return resp


def generate_random():
    return token_urlsafe(32)


if __name__ == '__main__':
    app.run()
    ```

