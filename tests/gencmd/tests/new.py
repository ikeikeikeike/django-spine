import os
from spine.management.commands.generate import new
from .base import TestSpineBase


class TestSpineNew(TestSpineBase):

    def test_exit(self):
        """ exception test """
        command = new.Command()
        self.assertRaises(
            SystemExit,
            command.execute,
            "ExceptionTest",
#            stdout=self.stdout,
#            stderr=self.stderr
        )

    def test_new(self):
        self.new_setUp()
        self.new_tearDown()

# vim: set et fenc=utf-8 ft=python ff=unix sts=4 sw=4 ts=4 :
