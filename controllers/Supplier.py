from odoo import http
from odoo.http import request
import json

class SupplierController(http.Controller):
    @http.route('/api/supplier', type='http', auth='public', methods=['GET'], csrf=False)
    def get_suppliers(self):
        suppliers = request.env['supplier'].search([])
        supplier_list = []

        for supplier in suppliers:
            supplier_list.append({
                'id': supplier.id,
                'name': supplier.name,
            })

        data = {
            'status': 200,
            'message': 'success',
            'response': supplier_list
        }

        # Mengembalikan respons JSON
        return request.make_response(
            json.dumps(data),
            headers={'Content-Type': 'application/json'}
        )

    @http.route('/api/supplier/<int:supplier_id>', type='http', auth='public', methods=['GET'], csrf=False)
    def get_supplier(self, supplier_id):
        supplier = request.env['supplier'].browse(supplier_id)
        if not supplier.exists():
            return json.dumps({'error': 'Supplier not found'})

        data = {
            'status': 200,
            'message': 'success',
            'response': {
                'id': supplier.id,
                'name': supplier.name,
            }
        }

        # Mengembalikan respons JSON
        return request.make_response(
            json.dumps(data),
            headers={'Content-Type': 'application/json'}
        )

    @http.route('/api/supplier', type='http', auth='public', methods=['POST'], csrf=False)
    def create_supplier(self, **kwargs):
        name = kwargs.get('name')

        if not name:
            data = {
                'status': 400,
                'message': 'name field is required',
                'response': {}
            }
            return request.make_response(
                json.dumps(data),
                headers={'Content-Type': 'application/json'}
            )

        # Membuat supplier baru
        supplier = request.env['supplier'].create({
            'name': name,
        })
        data = {
            'status': 200,
            'message': 'success',
            'response': {
                'id': supplier.id,
                'name': supplier.name,
            }
        }

        # Mengembalikan respons JSON
        return request.make_response(
            json.dumps(data),
            headers={'Content-Type': 'application/json'}
        )

    @http.route('/api/supplier/<int:supplier_id>', type='http', auth='public', methods=['PUT'], csrf=False)
    def update_supplier(self, supplier_id, **kwargs):
        supplier = request.env['supplier'].browse(supplier_id)
        if not supplier.exists():
            data = {
                'status': 404,
                'message': 'Supplier not found',
                'response': {}
            }
            return request.make_response(
                json.dumps(data),
                headers={'Content-Type': 'application/json'}
            )

        name = kwargs.get('name')
        if not name:
            data = {
                'status': 400,
                'message': 'name field is required',
                'response': {}
            }
            return request.make_response(
                json.dumps(data),
                headers={'Content-Type': 'application/json'}
            )

        supplier.write({
            'name': name,
        })
        data = {
            'status': 200,
            'message': 'success',
            'response': {
                'id': supplier.id,
                'name': supplier.name,
            }
        }

        # Mengembalikan respons JSON
        return request.make_response(
            json.dumps(data),
            headers={'Content-Type': 'application/json'}
        )

    @http.route('/api/supplier/<int:supplier_id>', type='http', auth='public', methods=['DELETE'], csrf=False)
    def delete_supplier(self, supplier_id):
        supplier = request.env['supplier'].browse(supplier_id)
        if not supplier.exists():
            data = {
                'status': 404,
                'message': 'Supplier not found',
                'response': {}
            }
            return request.make_response(
                json.dumps(data),
                headers={'Content-Type': 'application/json'}
            )

        supplier.unlink()
        data = {
            'status': 200,
            'message': 'Supplier deleted successfully',
            'response': {
                'id': supplier_id
            }
        }

        return request.make_response(
            json.dumps(data),
            headers={'Content-Type': 'application/json'}
        )
