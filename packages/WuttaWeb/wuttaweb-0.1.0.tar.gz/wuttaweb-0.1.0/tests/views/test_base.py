# -*- coding: utf-8; -*-

from unittest import TestCase

from pyramid import testing

from wuttjamaican.conf import WuttaConfig
from wuttaweb.views import base


class TestView(TestCase):

    def test_basic(self):
        config = WuttaConfig()
        request = testing.DummyRequest()
        request.wutta_config = config

        view = base.View(request)
        self.assertIs(view.request, request)
        self.assertIs(view.config, config)
        self.assertIs(view.app, config.get_app())
