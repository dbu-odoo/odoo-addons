# -*- coding: utf-8 -*-
{
    'name': 'PayuMoney Payment Acquirer',
    'category': 'Payment Acquirer',
    'summary': 'Payment Acquirer: PayuMoney Implementation',
    'description': """
    PayuMoney Payment Acquirer for India.

    PayUmoney payment gateway supports only INR currency.
    """,
    'author': 'Deep Bundela'
    "website": "",
    'depends': ['payment'],
    'data': [
        'views/payment_views.xml',
        'views/payment_payumoney_templates.xml',
        'data/payment_acquirer_data.xml',
    ],
    'license': 'AGPL-3',
}
