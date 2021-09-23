from odoo import models, api


class ResPartner(models.Model):
    _inherit = "res.partner"

    @api.model
    def disable_invoice_automatic(self):
        workflow_id = self.env["sale.workflow.process"].search(
            [("name", "=", "Automatic")]
        )
        if workflow_id:
            workflow_id.write(
                {
                    "validate_picking": False,
                    "create_invoice": False,
                    "validate_invoice": False,
                }
            )

    def write(self, vals):
        result = super(ResPartner, self).write(vals)
        for rec in self:
            stock_location = (
                self.env["stock.location"].sudo().search([("partner_id", "=", rec.id)])
            )
            for e in stock_location:
                e.write({"partner_id": rec.id})
        return result

    @api.model
    def create(self, vals_list):
        if "fax" in vals_list.keys():
            vals_list.pop("fax")
        return super(ResPartner, self).create(vals_list)
