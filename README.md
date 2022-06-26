# Gebly4in Website
Web scrapper module

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
     - Selenium Python bindings provides a simple API to write functional/acceptance tests using Selenium WebDriver. Through Selenium Python API you can access all functionalities of Selenium WebDriver in an intuitive way.
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

