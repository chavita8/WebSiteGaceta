from odoo import http
from odoo.http import request

class NormaController(http.Controller):
    
    @http.route('/normas', type='http', auth='public', website=True)
    def list_normas(self, **kwargs):
        search_query = kwargs.get('search_query', '')
        normas = request.env['norma.management'].search([('nro_norma', 'ilike', f"%{search_query}%")])
        return request.render('normas_module.normas_list', {'normas': normas, 'search_query': search_query})

    @http.route('/normas/create', type='http', auth='public', website=True, methods=['POST'], csrf=True)
    def create_norma(self, **kwargs):
        request.env['norma.management'].create({
            'id_norma': kwargs.get('id_norma'),
            'nro_norma': kwargs.get('nro_norma'),
            'edicion': kwargs.get('edicion'),
            'tipo': kwargs.get('tipo'),
            'fecha': kwargs.get('fecha'),
            'resumen': kwargs.get('resumen'),
            'text': kwargs.get('text'),
            'archivo_pdf': kwargs.get('archivo_pdf'),
            'archivo_doc': kwargs.get('archivo_doc'),
        })
        return request.redirect('/normas')