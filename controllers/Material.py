from odoo import http
from odoo.http import request
import json

class MaterialController(http.Controller):
    @http.route('/api/materials', type='http', auth='public', methods=['GET'], csrf=False)
    def get_materials(self):
        materials = request.env['material'].search([])
        material_list = []
        for material in materials:
            material_list.append({
                'id': material.id,
                'material_code': material.material_code,
                'material_name': material.material_name,
                'material_type': material.material_type,
                'material_buy_price' : material.material_buy_price,
                'related_supplier': material.related_supplier.name,
            })
        data = {
            'status': 200,
            'message': 'success',
            'response': material_list
        }

        # Mengembalikan respons JSON
        return request.make_response(
            json.dumps(data),
            headers={'Content-Type': 'application/json'}
        )

    @http.route('/api/filter/materials', type='http', auth='public', methods=['GET'], csrf=False)
    def filter_materials(self, material_type=None):
        domain = []
        if material_type:
            domain = [('material_type', '=', material_type)]

        materials = request.env['material'].search(domain)
        material_list = []
        for material in materials:
            material_list.append({
                'id': material.id,
                'material_code': material.material_code,
                'material_name': material.material_name,
                'material_type': material.material_type,
                'material_buy_price': material.material_buy_price,
                'related_supplier': material.related_supplier.name if material.related_supplier else None,
            })

        if not material_list:
            data = {
                'status': 404,
                'message': 'not found',
                'response': material_list
            }

            # Mengembalikan respons JSON
            return request.make_response(
                json.dumps(data),
                headers={'Content-Type': 'application/json'}
            )

        data = {
            'status': 200,
            'message': 'success',
            'response': material_list
        }

        # Mengembalikan respons JSON
        return request.make_response(
            json.dumps(data),
            headers={'Content-Type': 'application/json'}
        )

    @http.route('/api/material/<int:material_id>', type='http', auth='public', methods=['GET'], csrf=False)
    def get_material(self, material_id):
        material = request.env['material'].browse(material_id)
        if not material.exists():
            return json.dumps({'error': 'Material not found'})

        # Mendapatkan informasi supplier
        if material.related_supplier:
            supplier_name = material.related_supplier.name
        else:
            supplier_name = None  # Atau sesuaikan dengan informasi yang tersedia

        if not material:
            data = {
                'status': 404,
                'message': 'not found',
                'response': material
            }

            # Mengembalikan respons JSON
            return request.make_response(
                json.dumps(data),
                headers={'Content-Type': 'application/json'}
            )

        data = {
            'status': 200,
            'message': 'success',
            'response': {
                'id': material.id,
                'material_name': material.material_name,
                'material_code': material.material_code,
                'material_type': material.material_type,
                'material_buy_price': material.material_buy_price,
                'related_supplier': supplier_name,  # Menggunakan nama supplier atau ID, bukan objek supplier langsung
            }
        }


        return request.make_response(
            json.dumps(data),
            headers={'Content-Type': 'application/json'}
        )

    @http.route('/api/material', type='http', auth='public', methods=['POST'], csrf=False)
    def create_material(self, **kwargs):
        material_buy_price = float(kwargs.get('material_buy_price', 0.0))
        material_code = kwargs.get('material_code')
        material_name = kwargs.get('material_name')
        material_type = kwargs.get('material_type')
        related_supplier = kwargs.get('related_supplier')

        # Validasi jika salah satu field tidak diisi
        if not material_code or not material_name or not material_type or not related_supplier:
            data = {
                'status': 400,
                'message': 'All fields (material_code, material_name, material_type, related_supplier) are required',
                'response': {}
            }
            return request.make_response(
                json.dumps(data),
                headers={'Content-Type': 'application/json'}
            )

        if material_buy_price < 100:
            return json.dumps({
                'status': 400,
                'message': 'material_buy_price must be at least 100',
                'response': {}
            })

        # Membuat material baru
        material = request.env['material'].create({
            'material_code': material_code,
            'material_name': material_name,
            'material_type': material_type,
            'material_buy_price': material_buy_price,
            'related_supplier': related_supplier,
        })

        # Menyiapkan respons sukses
        data = {
            'status': 200,
            'message': 'success',
            'response': {
                'id': material.id,
                'material_code': material_code,
                'material_name': material_name,
                'material_type': material_type,
                'material_buy_price': material_buy_price,
                'related_supplier': related_supplier,
            }
        }

        # Mengembalikan respons JSON
        return request.make_response(
            json.dumps(data),
            headers={'Content-Type': 'application/json'}
        )

    @http.route('/api/material/<int:material_id>', type='http', auth='public', methods=['PUT'], csrf=False)
    def update_material(self, material_id, **kwargs):
        material = request.env['material'].browse(material_id)

        if not material.exists():
            return json.dumps({'error': 'Material not found'})

        material_code = kwargs.get('material_code')
        material_name = kwargs.get('material_name')
        material_type = kwargs.get('material_type')
        material_buy_price = float(kwargs.get('material_buy_price', 0.0))
        related_supplier = kwargs.get('related_supplier')

        # Validasi jika salah satu field tidak diisi
        if not material_code or not material_name or not material_type or not related_supplier:
            data = {
                'status': 400,
                'message': 'All fields (material_code, material_name, material_type, related_supplier) are required',
                'response': {}
            }
            return request.make_response(
                json.dumps(data),
                headers={'Content-Type': 'application/json'}
            )

        if material_buy_price < 100:
            return json.dumps({
                'status': 400,
                'message': 'material_buy_price must be at least 100',
                'response': {}
            })

        # Update material
        material.write({
            'material_code': material_code,
            'material_name': material_name,
            'material_type': material_type,
            'material_buy_price': material_buy_price,
            'related_supplier': related_supplier,
        })

        # Menyiapkan respons sukses
        data = {
            'status': 200,
            'message': 'success',
            'response': {
                'id': material.id,
                'material_code': material_code,
                'material_name': material_name,
                'material_type': material_type,
                'material_buy_price': material_buy_price,
                'related_supplier': related_supplier,
            }
        }

        # Mengembalikan respons JSON
        return request.make_response(
            json.dumps(data),
            headers={'Content-Type': 'application/json'}
        )

    @http.route('/api/material/<int:material_id>', type='http', auth='public', methods=['DELETE'], csrf=False)
    def delete_material(self, material_id):
        material = request.env['material'].browse(material_id)
        if not material.exists():
            data = {
                'status': 404,
                'message': 'Material not found',
                'response': {}
            }
            return request.make_response(
                json.dumps(data),
                headers={'Content-Type': 'application/json'}
            )

        material.unlink()
        data = {
            'status': 200,
            'message': 'Material deleted successfully',
            'response': {
                'id': material_id
            }
        }

        return request.make_response(
            json.dumps(data),
            headers={'Content-Type': 'application/json'}
        )

