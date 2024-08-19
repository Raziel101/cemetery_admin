# -*- coding: utf-8 -*-
from odoo import models, fields

class CemeteryDeath(models.Model):
    _name = 'cemetery.death'
    _description = 'Fallecido'

    nombre = fields.Char(String="Nomber y Apellido")
    muerte = fields.Date(String="Fecha de Fallecimiento")

    representante_id = fields.Many2one('cemetery.representative', string="Representante")

    parentesco_fallecido = fields.Selection([
        ('padre', 'Padre'),
        ('madre', 'Madre'),
    ], string='Parentesco Fallecido')

    Empresa = fields.Selection([
        ('Barbieri', 'barbieri'),
        ('Colombo', 'Colombo'),
    ], string='Empresa')



