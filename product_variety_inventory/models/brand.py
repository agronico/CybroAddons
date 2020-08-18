# -*- coding: utf-8 -*-
###################################################################################
#
#    Cybrosys Technologies Pvt. Ltd.
#
#    Copyright (C) 2019-TODAY Cybrosys Technologies(<https://www.cybrosys.com>).
#    This program is free software: you can modify
#    it under the terms of the GNU Affero General Public License (AGPL) as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
###################################################################################

from odoo import models,fields,api


class ProductVariety(models.Model):
    _inherit = 'product.template'

    variety_id = fields.Many2one('product.variety',string='Variety')


class VarietyProduct(models.Model):
    _name = 'product.variety'


    name= fields.Char(String="Name")
    variety_image = fields.Binary()
    member_ids = fields.One2many('product.template', 'variety_id')
    product_count = fields.Char(String='Product Count', compute='get_count_products', store=True)

    @api.depends('member_ids')
    def get_count_products(self):
        self.product_count = len(self.member_ids)


class VarietyReportStock(models.Model):
    _inherit = 'stock.quant'

    variety_id  = fields.Many2one(related='product_id.variety_id',
        string='Variety', store=True, readonly=True)


