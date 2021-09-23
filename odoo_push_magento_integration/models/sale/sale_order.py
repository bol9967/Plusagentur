from odoo import api, tools, models, fields


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"
    _description = "Sale Order Line"

    @api.model
    def create(self, vals_list):
        if vals_list.get("partner_id"):
            vals_list.pop("partner_id")
            vals_list["invoice_status"] = "no"
        if vals_list.get("odoo_partner_id"):
            vals_list["order_partner_id"] = vals_list.get("odoo_partner_id")
            vals_list.pop("odoo_partner_id")
        return super(SaleOrderLine, self).create(vals_list)


class SaleOrder(models.Model):
    _inherit = "sale.order"
    _description = "Sale Order"

    @api.model
    def create(self, vals_list):
        if vals_list.get("state") and vals_list.get("state") == "sale":
            vals_list["state"] = "draft"
            vals_list["invoice_status"] = "no"
            workflow_id = self.env["sale.workflow.process"].search(
                [("name", "=", "Automatic")]
            )
            if workflow_id:
                vals_list["workflow_process_id"] = workflow_id.id
        return super(SaleOrder, self).create(vals_list)
