{
    'name': 'Adminstracion Cementerio',
    'version': '1.0',
    'summary': 'Gestión de Parcelas del Cementerio 1.0',
    'author': 'Palmerola',
    'category': 'Management',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/cemetery_views.xml',
    ],
    'installable': True,
    'application': True,
}