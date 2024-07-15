# -*- coding: utf-8; -*-

from unittest import TestCase

try:
    import sqlalchemy as sa
    from wuttjamaican.db.model import base as model
except ImportError:
    pass
else:

    class TestUUIDColumn(TestCase):

        def test_basic(self):
            column = model.uuid_column()
            self.assertIsInstance(column, sa.Column)
            self.assertIsInstance(column.type, sa.String)
            self.assertEqual(column.type.length, 32)

    class TestUUIDFKColumn(TestCase):

        def test_basic(self):
            column = model.uuid_column()
            self.assertIsInstance(column, sa.Column)
            self.assertIsInstance(column.type, sa.String)
            self.assertEqual(column.type.length, 32)

    class TestSetting(TestCase):

        def test_basic(self):
            setting = model.Setting()
            self.assertEqual(str(setting), "")
            setting.name = 'foo'
            self.assertEqual(str(setting), "foo")
