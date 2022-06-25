{
    'name': 'WebScrapper',
    'version': '1.0',
    'author': 'Team 4',
    'summary': 'Links to products',
    'sequence': 10,
    'sequence': '1',
    'description': "we will begin our journy now",
    'category': 'Sales/Sales',
    'website': '',
    'depends': ['product', 'website', 'website_sale'],
    'data': [
        'security/ir.model.access.csv',
        'views/template.xml',
        'views/products.xml',
        'security/security.xml',
        'views/Menu_bars.xml',

    ],
    'assets': {
        'web.assets_frontend': [
            'shein2egypt/static/scss/shein2egypt.css',

        ],
    },

    'installable': True,
    'application': True,
}
# a short idea of what is the module about
