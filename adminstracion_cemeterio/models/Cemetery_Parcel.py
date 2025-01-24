# -*- coding: utf-8 -*-
from odoo import models, fields


class CemeteryParcel(models.Model):
    _name = 'cemetery.parcel'
    _description = 'Parcela del Cementerio'

    """toggle_option = fields.Selection([
        ('nicho', 'Nicho'),
        ('boveda', 'Boveda'),
        ('panteon', 'Panteon'),
        ('nichera', 'Nichera')
    ], string='Seleccionar Opción', required=True, default='nicho')"""

    panteon = fields.Boolean(string="Panteon")
    fosa = fields.Boolean(string="Fosa")
    nichera = fields.Boolean(string="Nichera")
    boveda = fields.Boolean(string="Boveda")


    #Nicho,Nichera y Panteon
    galeria = fields.Integer(string='Galería')
    fila = fields.Integer(string='Fila')
    nicho = fields.Integer(string='Nicho')

    #Bobeda
    lote = fields.Integer(string="Lote")
    manzana = fields.Integer(string='Manzana')
    solar = fields.Integer(string='Solar')

    representante_id = fields.Many2one('cemetery.representative', string="Representante")

    death_ids = fields.Many2many(
        'cemetery.death',
        'cemetery_death_parcel_rel',
        'parcel_id',
        'death_id',
        string="Fallecido"
    )

    sociedad_italiana = fields.Boolean(string="¿Es parte de la Sociedad Ialiana?", default=False)

    contract_years = fields.Selection([(str(i), str(i)) for i in range(1, 100)], string='Años Contratados')
    contract_start_date = fields.Date(string='Fecha de Arrendamiento')
    contract_end_date = fields.Date(string='Fecha de Vencimiento')





