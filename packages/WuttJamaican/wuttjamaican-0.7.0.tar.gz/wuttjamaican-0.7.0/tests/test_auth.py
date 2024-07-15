# -*- coding: utf-8; -*-

from unittest import TestCase

from wuttjamaican import auth as mod
from wuttjamaican.conf import WuttaConfig


class TestAuthHandler(TestCase):

    def setUp(self):
        self.config = WuttaConfig()
        self.app = self.config.get_app()

    def test_basic(self):
        handler = mod.AuthHandler(self.config)
        self.assertIs(handler.app, self.app)
