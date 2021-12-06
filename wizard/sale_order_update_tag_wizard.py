from odoo import models,fields,api
import logging

_logger = logging.getLogger(__name__)

class SaleOrder(models.TransientModel):
    _name = "sale.order.update.tag.wizard"
    _description = "Update tags"



    tag_ids = fields.Many2many('crm.tag', string='Tags')


    def action_update_tags(self):
        active_ids = self.env.context.get('active_ids')
        active_records = self.env['sale.order'].browse(active_ids)
        _logger.info(f'\n Context={self.env.context}\n')
        for record in active_records:
            result = record.write({
                'tag_ids': [(6, 0, self.tag_ids.ids)]
            })
            _logger.info(f'\n Result:{result} \n')