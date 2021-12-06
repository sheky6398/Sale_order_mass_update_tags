{
    'name': "Sale Order Mass Update Tags",
    'author': 'Bharat Yadav',
    'version': '1.0.3',
    'summary': 'User Can Update the tags by one button',
    'depends':['sale'],
    'data': [
      'security/ir.model.access.csv',
      'views/sale_order_inherited.xml',
      'views/sale_order_discount.xml',
      'wizard/sale_order_update_tag_wizard.xml',
      'wizard/sale_order_update_terms_wizard.xml',
      'wizard/sale_order_discount_wizard.xml',
    ]

}