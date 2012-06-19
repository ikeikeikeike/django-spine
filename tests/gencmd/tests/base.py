import os
import shutil
from StringIO import StringIO
from django.test import TestCase
from spine.management.commands.generate import new


class TestSpineBase(TestCase):

    def setUp(self):
        """ ignore output buffer """
        self.stdout = StringIO()
        self.stderr = StringIO()
        self.new_command = new.Command()
        app_dir = __import__(self.new_command.usercommand)
        self.app_dir = app_dir.__path__[0]

    def tearDown(self):
        """ ignore output buffer """
        self.stdout.close()
        self.stderr.close()

    def new_setUp(self):
        """   """
        os.mkdir(os.path.join(self.app_dir, "static"))
        os.mkdir(os.path.join(self.app_dir, "static", "js"))

        self.assertRaises(
            (SystemExit, ValueError),
            self.new_command.execute,
            "gencmd",
#            stdout=self.stdout,
#            stderr=self.stderr
        )

    def new_tearDown(self):
        try:
            shutil.rmtree(os.path.join(self.app_dir, "static"))
        except OSError:
            pass


# vim: set et fenc= ft=python ff=unix sts=4 sw=4 ts=4 :
