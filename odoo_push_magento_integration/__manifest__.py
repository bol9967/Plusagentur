# -*- coding: utf-8 -*-
{
    "name": "Odoo Magento2 Connector",
    "summary": """
       Odoo Magento2 Connector""",
    "description": """
       Odoo Magento2 Connector
    """,
    "author": "Magenest",
    "website": "https://store.magenest.com",
    "category": "Accounting/Accounting",
    "version": "14.0.1.0.0",
    "depends": [
        "base",
        "account",
        "sale",
        "sale_management",
        "product",
        "payment",
        "stock",
        "website_sale",
        "sale_automatic_workflow",
        "delivery",
    ],
    "images": ["static/description/images/Odoo---Magento2-2.png"],
    "data": [
        "security/ir.model.access.csv",
        "views/menu.xml",
        "views/config/magento_instance.xml",
        "views/dashboard/website.xml",
        "views/dashboard/store.xml",
        "views/dashboard/storeview.xml",
        "views/dashboard/dashboard_view.xml",
        "views/stock_location/stock_location_view.xml",
        "views/product/product_template_sync.xml",
        "data/disable_workflow.xml",
    ],
    "installable": True,
    "application": True,
    "auto_install": True,
    "license": "OPL-1",
}
