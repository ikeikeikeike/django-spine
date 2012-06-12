from spine.management.commands.generate import controller
from .base import TestSpineBase


class TestSpineController(TestSpineBase):

    def test_exit(self):
        command = controller.Command()
        self.assertRaises(
            SystemExit,
            command.execute,
            "ExceptionTest",
            stdout=self.stdout,
            stderr=self.stderr
        )


# vim: set et fenc=utf-8 ft=python ff=unix sts=4 sw=4 ts=4 :
