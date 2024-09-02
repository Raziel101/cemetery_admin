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

    empresa = fields.Selection([
        ('Barbieri', 'barbieri'),
        ('Colombo', 'Colombo'),
    ], string='Empresa')

    def name_get(self):
        result = []
        for record in self:
            name = "{} - {} - {} - {}".format(
                record.nombre or '',
                record.muerte or '',
                record.empresa or '',
                record.representante_id.name or ''
            )
            result.append((record.id, name))
        return result