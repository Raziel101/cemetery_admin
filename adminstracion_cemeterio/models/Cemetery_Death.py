# -*- coding: utf-8 -*-
from odoo import models, fields

class CemeteryDeath(models.Model):
    _name = 'cemetery.death'
    _description = 'Fallecido'

    name = fields.Char(string="Nomber y Apellido")
    muerte = fields.Date(string="Fecha de Fallecimiento")
    observaciones = fields.Char(string="Observaciones")

    representante_id = fields.Many2one('cemetery.representative', string="Representante")

    parcel_ids = fields.Many2many(
        'cemetery.parcel',
        'cemetery_death_parcel_rel',
        'death_id',
        'parcel_id',
        string="Parcela"
    )

    parentesco_fallecido = fields.Selection([
        ('padre', 'Padre'),
        ('madre', 'Madre'),
        ('abuelo', 'Abuelo'),
        ('abuela', 'Abuela'),
        ('padrastro', 'Padrastro'),
        ('madrastra', 'Madrastra'),
        ('hijo', 'Hijo'),
        ('hija', 'Hija'),
        ('hijo politico', 'Hijo Politico'),
        ('sobrino politico', 'Sobrino Politico'),
        ('conyuge', 'Conyuge'),
        ('esposa', 'Esposa'),
        ('esposo', 'Esposo'),
        ('concubina', 'Concubina'),
        ('concubino', 'Concubino'),
        ('cuñado', 'Cuñado'),
        ('cuñada', 'Cuñada'),
        ('hermano', 'Hermano'),
        ('hermana', 'Hermana'),
        ('nieto', 'Nieto'),
        ('nieta', 'Nieta'),
        ('bisnieto', 'Bisnieto'),
        ('bisnieta', 'Bisnieta'),
        ('vecino', 'Vecino'),
        ('vecina', 'Vecina'),
        ('encargado hogar', 'Encargado Hogar'),
        ('otra', 'Otra')
    ], string='Parentesco Fallecido')

    empresa = fields.Selection([
        ('barbieri', 'Barbieri'),
        ('colombo', 'Colombo'),
        ('monti', 'Monti'),
        ('brarda', 'Brarda'),
        ('otra', 'Otra'),
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