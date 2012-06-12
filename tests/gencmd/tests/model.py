from spine.management.commands.generate import model
from .base import TestSpineBase


class TestSpineModel(TestSpineBase):

    def test_exit(self):
        command = model.Command()
        self.assertRaises(
            SystemExit,
            command.execute,
            "ExceptionTest",
            stdout=self.stdout,
            stderr=self.stderr
        )


# vim: set et fenc=utf-8 ft=python ff=unix sts=4 sw=4 ts=4 :
