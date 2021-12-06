from odoo import models,fields,api
import logging

_logger = logging.getLogger(__name__)


class SaleOrderDiscount(models.TransientModel):
    _name = "sale.order.discount.wizard"
    _description = "Update tags"


    discount = fields.Selection([('10','10%'),('20','20%'),('50','50%'),('70','70%'),('75','75%')])
    discount_amount = fields.Float(string="Discount")



    def action_update_discount(self):
        active_ids = self.env.context.get('active_ids')
        active_records = self.env['sale.order'].browse(active_ids)
        for disc in active_records: 
            if self.discount == '10':
                discount_amount = disc.amount_total * 0.10
                disc.amount_total = disc.amount_total - discount_amount
            elif  self.discount == '20': 
                discount_amount = disc.amount_total * 0.20
                disc.amount_total = disc.amount_total - discount_amount
            elif  self.discount == '50': 
                discount_amount = disc.amount_total * 0.50
                disc.amount_total = disc.amount_total - discount_amount
            elif  self.discount == '70': 
                discount_amount = disc.amount_total * 0.70
                disc.amount_total = disc.amount_total - discount_amount
            else:
                discount_amount = disc.amount_total * 0.75
                disc.amount_total = disc.amount_total - discount_amount

                
            result = disc.write({
                'amount_total': disc.amount_total,
                'discount_amount': discount_amount
            })
            _logger.info(f'\n AMountTotal:{disc.amount_total} \n')         
            _logger.info(f'\n TYPE:{type(self.discount)} \n')         
            _logger.info(f'\n Disocunt:{discount_amount} \n')         
            _logger.info(f'\n ACTIVE RECORDS:{active_records} \n')         
            _logger.info(f'\n DISCOUNT:{self.discount_amount} \n')         
       