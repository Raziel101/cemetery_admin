# -*- coding: utf-8 -*-
from odoo import models, fields


class CemeteryParcel(models.Model):
    _name = 'cemetery.parcel'
    _description = 'Parcela del Cementerio'

    toggle_option = fields.Selection([
        ('nicho', 'Nicho'),
        ('boveda', 'Boveda')
    ], string='Seleccionar Opción', required=True, default='nicho')

    #Nicho
    galeria = fields.Integer(string='Galería')
    fila = fields.Integer(string='Fila')
    nicho = fields.Integer(string='Nicho')

    #Bobeda
    lote = fields.Integer(string="Lote")
    manzana = fields.Integer(string='Manzana')
    solar = fields.Integer(string='Solar')

    representante_id = fields.Many2one('cemetery.representative', string="Representante")

    contract_years = fields.Selection([(str(i), str(i)) for i in range(1, 100)], string='Años Contratados')
    contract_start_date = fields.Date(string='Fecha de Arrendamiento')
    contract_end_date = fields.Date(string='Fecha de Vencimiento')
