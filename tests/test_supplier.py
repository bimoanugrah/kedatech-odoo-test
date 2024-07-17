from odoo.tests import common
from odoo import exceptions


class TestSupplier(common.TransactionCase):

    def setUp(self):
        super(TestSupplier, self).setUp()
        self.Supplier = self.env['supplier']

    def test_create_supplier(self):
        supplier = self.Supplier.create({
            'name': 'PT.baru'
        })
        self.assertEqual(supplier.name, 'PT.baru')
        print('Test create_supplier passed')

    def test_get_suppliers(self):
        supplier1 = self.Supplier.create({'name': 'Supplier 1'})
        supplier2 = self.Supplier.create({'name': 'Supplier 2'})

        suppliers = self.Supplier.search([])
        self.assertIn(supplier1, suppliers)
        self.assertIn(supplier2, suppliers)
        print('Test get_suppliers passed')

    def test_get_supplier(self):
        supplier = self.Supplier.create({'name': 'PT. Single'})
        retrieved_supplier = self.Supplier.browse(supplier.id)

        self.assertEqual(supplier, retrieved_supplier)
        print('Test get_supplier passed')

    def test_update_supplier(self):
        supplier = self.Supplier.create({'name': 'PT. OldName'})
        supplier.write({'name': 'PT. NewName'})

        updated_supplier = self.Supplier.browse(supplier.id)
        self.assertEqual(updated_supplier.name, 'PT. NewName')
        print('Test update_supplier passed')

    def test_delete_supplier(self):
        supplier = self.Supplier.create({'name': 'PT. ToDelete'})
        supplier_id = supplier.id
        supplier.unlink()

        deleted_supplier = self.Supplier.browse(supplier_id)
        self.assertFalse(deleted_supplier.exists())
        print('Test delete_supplier passed')
