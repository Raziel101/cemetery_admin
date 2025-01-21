# -*- coding: utf-8 -*-

from odoo import models, fields

class CemeteryRepresentavie(models.Model):
    _name = 'cemetery.representative'
    _description = 'Representante '

    # Datos Personales
    name = fields.Char(string='Nombre y Apellido', required=True)
    domicilio = fields.Char(string='Domicilio', required=True)
    fecha_nacimiento = fields.Date(string='Fecha de Nacimiento', required=True)
    telefono = fields.Char(string='Teléfono')
    correo_electronico = fields.Char(string='Correo Electrónico')
    dni = fields.Char(string='DNI', required=True)

    death_ids = fields.One2many('cemetery.death', 'representante_id', string='Fallecidos')
    parcel_ids = fields.One2many('cemetery.parcel', 'representante_id', string='Parcelas')