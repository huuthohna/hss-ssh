{
    'name': 'Nippon Purchase - Landed Cost Extend',
    'summary': '',
    'version': '1.0',
    'category': 'Purchase',
    'description': """
    Make a new flow of purchase cost distribution.\n
    - When make a Purchase Order, we have a checkbox to force waiting to
     enter landed cost for this Purchase Order
    - If you check Landed Cost box on PO form, the Incoming Shipment
    that create by the Purchase Order will be Waiting for Landed Cost state
    - In Purchase Cost Distribution form, we import Incoming Shipment in Waiting for
    Landed Cost state and calculate landed cost for the Incoming Shipments.
    - When you receipt Products by the Incoming Shipments, system will be calculate landed cost
    for you and update cost into product form
    """,
    'author': "HanelSoft ERP",
    'website': 'http://www.hanelsoft.vn/',
    'depends': ['purchase_landed_cost_posting_entries'],
    'data': ['views/views.xml',
             'views/res_partner_view.xml',
             'wizard/reposting_view.xml'],
    'price': 79.50,
    'currency': 'EUR',
    'installable': True,
    'auto_install': False,
    'application': False,
}
