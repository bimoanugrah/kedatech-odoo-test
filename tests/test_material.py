from odoo.tests import common
from odoo import exceptions

class TestMaterial(common.TransactionCase):

    def setUp(self):
        super(TestMaterial, self).setUp()
        self.Material = self.env['material']

    def test_create_material(self):
        material = self.Material.create({
            'material_code': 'M001',
            'material_name': 'Material 1',
            'material_type': 'Type A',
            'material_buy_price': 150.0,
            'related_supplier': 'Supplier A',
        })
        self.assertEqual(material.material_name, 'Material 1')
        print('Test create_material passed')

    def test_get_materials(self):
        material1 = self.Material.create({
            'material_code': 'M001',
            'material_name': 'Material 1',
            'material_type': 'Type A',
            'material_buy_price': 150.0,
            'related_supplier': 'Supplier A',
        })
        material2 = self.Material.create({
            'material_code': 'M002',
            'material_name': 'Material 2',
            'material_type': 'Type B',
            'material_buy_price': 200.0,
            'related_supplier': 'Supplier B',
        })

        materials = self.Material.search([])
        self.assertIn(material1, materials)
        self.assertIn(material2, materials)
        print('Test get_materials passed')

    def test_get_material(self):
        material = self.Material.create({
            'material_code': 'M001',
            'material_name': 'Material 1',
            'material_type': 'Type A',
            'material_buy_price': 150.0,
            'related_supplier': 'Supplier A',
        })
        retrieved_material = self.Material.browse(material.id)

        self.assertEqual(material, retrieved_material)
        print('Test get_material passed')

    def test_update_material(self):
        material = self.Material.create({
            'material_code': 'M001',
            'material_name': 'Material 1',
            'material_type': 'Type A',
            'material_buy_price': 150.0,
            'related_supplier': 'Supplier A',
        })
        material.write({
            'material_name': 'Updated Material 1',
        })

        updated_material = self.Material.browse(material.id)
        self.assertEqual(updated_material.material_name, 'Updated Material 1')
        print('Test update_material passed')

    def test_delete_material(self):
        material = self.Material.create({
            'material_code': 'M001',
            'material_name': 'Material 1',
            'material_type': 'Type A',
            'material_buy_price': 150.0,
            'related_supplier': 'Supplier A',
        })
        material_id = material.id
        material.unlink()

        deleted_material = self.Material.browse(material_id)
        self.assertFalse(deleted_material.exists())
        print('Test delete_material passed')
