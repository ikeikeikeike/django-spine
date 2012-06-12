from StringIO import StringIO
from django.test import TestCase


class TestSpineBase(TestCase):

    def setUp(self):
        """ ignore output buffer """
        self.stdout = StringIO()
        self.stderr = StringIO()

    def tearDown(self):
        """ ignore output buffer """
        self.stdout.close()
        self.stderr.close()


# vim: set et fenc= ft=python ff=unix sts=4 sw=4 ts=4 :
