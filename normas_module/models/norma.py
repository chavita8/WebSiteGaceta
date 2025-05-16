from odoo import models, fields

class Norma(models.Model):
    _name = 'norma.management'
    _description = 'Gestión de Normas'

    id_norma = fields.Integer(string='ID Norma', required=True)
    nro_norma = fields.Char(string='Número de Norma', required=True)
    edicion = fields.Char(string='Edición', required=True)
    tipo = fields.Char(string='Tipo', required=True)
    fecha = fields.Date(string='Fecha', required=True)
    resumen = fields.Text(string='Resumen', required=True)
    text = fields.Text(string='Texto', required=False)
    archivo_pdf = fields.Binary(string='Archivo PDF')
    archivo_doc = fields.Binary(string='Archivo DOC')