# -*- coding: utf-8; -*-

import json
from unittest import TestCase
from unittest.mock import MagicMock

from wuttjamaican.conf import WuttaConfig

from pyramid import testing

from wuttaweb import subscribers
from wuttaweb import helpers


class TestNewRequest(TestCase):

    def setUp(self):
        self.config = WuttaConfig()

    def make_request(self):
        request = testing.DummyRequest()
        request.registry.settings = {'wutta_config': self.config}
        return request

    def test_wutta_config(self):
        request = self.make_request()
        event = MagicMock(request=request)

        # request gets a new attr
        self.assertFalse(hasattr(request, 'wutta_config'))
        subscribers.new_request(event)
        self.assertTrue(hasattr(request, 'wutta_config'))
        self.assertIs(request.wutta_config, self.config)

    def test_use_oruga_default(self):
        request = self.make_request()
        event = MagicMock(request=request)

        # request gets a new attr, false by default
        self.assertFalse(hasattr(request, 'use_oruga'))
        subscribers.new_request(event)
        self.assertFalse(request.use_oruga)

    def test_use_oruga_custom(self):
        self.config.setdefault('wuttaweb.oruga_detector.spec', 'tests.test_subscribers:custom_oruga_detector')
        request = self.make_request()
        event = MagicMock(request=request)

        # request gets a new attr, which should be true
        self.assertFalse(hasattr(request, 'use_oruga'))
        subscribers.new_request(event)
        self.assertTrue(request.use_oruga)


def custom_oruga_detector(request):
    return True


class TestBeforeRender(TestCase):

    def setUp(self):
        self.config = WuttaConfig()

    def make_request(self):
        request = testing.DummyRequest()
        request.registry.settings = {'wutta_config': self.config}
        request.wutta_config = self.config
        return request

    def test_basic(self):
        request = self.make_request()
        event = {'request': request}

        # event dict will get populated with more context
        subscribers.before_render(event)

        self.assertIn('config', event)
        self.assertIs(event['config'], self.config)

        self.assertIn('app', event)
        self.assertIs(event['app'], self.config.get_app())

        self.assertIn('h', event)
        self.assertIs(event['h'], helpers)

        self.assertIn('url', event)
        # TODO: not sure how to test this?
        # self.assertIs(event['url'], request.route_url)

        self.assertIn('json', event)
        self.assertIs(event['json'], json)


class TestIncludeMe(TestCase):

    def test_basic(self):
        with testing.testConfig() as pyramid_config:

            # just ensure no error happens when included..
            pyramid_config.include('wuttaweb.subscribers')
