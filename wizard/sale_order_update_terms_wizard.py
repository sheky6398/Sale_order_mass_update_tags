from odoo import models,fields,api
import logging

_logger = logging.getLogger(__name__)

class UpdateTermsCondition(models.TransientModel):
    _name = "sale.order.update.terms.wizard"
    _description = "Update tags"


    note = fields.Text(string="Terms and Conditions")


    def action_update_terms(self):
        active_ids = self.env.context.get('active_ids')
        active_records = self.env['sale.order'].browse(active_ids)
        _logger.info(f'\n Context={self.env.context}\n')
        for record in active_records:
            result = record.write({
                'note': self.note
            })
            _logger.info(f'\n Result:{result} \n')