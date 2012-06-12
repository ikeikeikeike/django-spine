from spine.management.commands.generate import scaffold
from .base import TestSpineBase


class TestSpineScaffold(TestSpineBase):

    def test_exit(self):
        command = scaffold.Command()
        self.assertRaises(
            SystemExit,
            command.execute,
            "ExceptionTest",
            stdout=self.stdout,
            stderr=self.stderr
        )



# vim: set et fenc=utf-8 ft=python ff=unix sts=4 sw=4 ts=4 :
