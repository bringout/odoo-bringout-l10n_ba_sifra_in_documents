{
    'name': 'Šifra posebna kolona u dokumentima',
    'version': '16.0.2.0.5',
    'category': 'Extra Tools',
    'summary': 'Šifra (Code) kao posebna kolona u dokumentima.',
    'author': 'bring.out doo Sarajevo',
    'website': "https://www.bring.out.ba",
    'license': 'AGPL-3',
    'depends': ['base', 'order_line_sequences'],
    'data': [
        'views/sale_order_document_view.xml',
        'views/report_picking_view.xml',
        'views/report_purchaseorder_document_view.xml',
    ],
    'images': ['static/description/banner.png'],
    'installable': True,
    'auto_install': False,
    'application': False,
}
